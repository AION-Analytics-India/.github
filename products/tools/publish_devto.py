#!/usr/bin/env python3
"""Publish the reviewed AION DEV Community article only with explicit authenticated approval.

Run from the .github repository root:
  python3 products/tools/publish_devto.py                   # local validation only
  DEVTO_API_KEY=... DEVTO_ORGANIZATION_ID=... python3 products/tools/publish_devto.py --publish

Never commit tokens. This script does not alter the GitHub source article.
"""
import argparse
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API = "https://dev.to/api"
ARTICLE = Path(__file__).resolve().parents[1] / "DEVTO_DRAFT.md"


def parse_markdown(raw):
    parts = raw.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError("Missing YAML-style frontmatter")
    front = {}
    for line in parts[1].splitlines():
        if not line.strip():
            continue
        k, sep, v = line.partition(":")
        if not sep:
            raise ValueError(f"Invalid frontmatter line: {line}")
        front[k.strip()] = v.strip().strip('"')
    if front.get("published", "").lower() != "false":
        raise ValueError("The tracked article must remain explicitly unpublished")
    for key in ("title", "description", "canonical_url", "tags"):
        if not front.get(key):
            raise ValueError(f"Missing {key}")
    tags = [x.strip() for x in front["tags"].split(",") if x.strip()]
    if len(tags) > 4:
        raise ValueError("DEV.to permits at most four tags")
    body = parts[2].strip()
    body = body.replace("> **Publication status: DRAFT ONLY.** Do not flip \`published\` to \`true\` without evidence review and authenticated DEV Community publication. Avoid duplicate posting across AION's DEV accounts.\n\n", "")
    return front, body, tags


def request(url, key, method="GET", payload=None):
    headers = {"api-key": key, "Accept": "application/vnd.forem.api-v1+json",
               "User-Agent": "AION-Publication/1.0 (documentation-only; security claims reviewed)"}
    if payload is not None:
        headers["Content-Type"] = "application/json"
    req = Request(url, data=json.dumps(payload).encode("utf-8") if payload is not None else None,
                  headers=headers, method=method)
    try:
        with urlopen(req, timeout=25) as res:
            return json.loads(res.read().decode("utf-8"))
    except HTTPError as exc:
        raise RuntimeError(f"DEV API HTTP {exc.code}: {exc.read(700).decode('utf-8', 'replace')}") from exc
    except URLError as exc:
        raise RuntimeError(f"DEV API unavailable: {exc.reason}") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publish", action="store_true", help="Create a live DEV article; requires credentials")
    args = parser.parse_args()
    front, body, tags = parse_markdown(ARTICLE.read_text(encoding="utf-8"))
    obj = {"title": front["title"], "body_markdown": body,
           "published": args.publish, "description": front["description"],
           "canonical_url": front["canonical_url"], "tags": ", ".join(tags)}
    if not args.publish:
        print(json.dumps({"mode": "DRY_RUN_NO_API_CALL", "title": obj["title"],
                          "canonical_url": obj["canonical_url"], "tags": tags,
                          "body_characters": len(body)}, ensure_ascii=False, indent=2))
        return
    key = os.getenv("DEVTO_API_KEY", "").strip()
    org = os.getenv("DEVTO_ORGANIZATION_ID", "").strip()
    if not key or not org.isdigit():
        raise SystemExit("BLOCKED: set DEVTO_API_KEY and numeric DEVTO_ORGANIZATION_ID securely")
    org_id = int(org)
    own = request(API + "/articles/me/all?per_page=100", key)
    if not isinstance(own, list):
        raise RuntimeError("Unable to verify existing articles; refusing to risk a duplicate")
    if any(a.get("canonical_url") == obj["canonical_url"] or a.get("title") == obj["title"] for a in own):
        raise RuntimeError("Matching article already exists; use an explicit update, not a new post")
    obj["organization_id"] = org_id
    published = request(API + "/articles", key, method="POST", payload={"article": obj})
    if not published.get("published") or not published.get("url"):
        raise RuntimeError("API response did not confirm live publication")
    print(json.dumps({"status": "PUBLISHED", "url": published["url"], "id": published.get("id"),
                      "organization_id": org_id}, indent=2))


if __name__ == "__main__":
    main()
