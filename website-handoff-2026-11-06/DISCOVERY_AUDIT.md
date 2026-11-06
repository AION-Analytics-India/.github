# AION GitHub discovery: evidence-led audit and change log
Date: 2026-11-06
Canonical GitHub: https://github.com/AION-Analytics-India
Secondary user account: https://github.com/AION-Analytics

## Verified public GitHub snapshot
Direct GitHub repository metadata read on 2026-11-06:
- aion-indian-market-intelligence: 24 stars, 1 fork.
- aion-research: 1 star, 0 forks.
- Nine other public organization repos: 0 stars, 0 forks.
- 11 public organization repos in total, plus 1 private. Personal account: 1 public repo plus 5 private.
- Most product repositories have topic tags already. Calendar source code and tests are public in maintained canonical repos.
- The legacy calendar-docs mirror and archived Zerodha tutorial create additional, lower-value entry points.

## Evidence-backed observations
1. The historical documentation mirror used a retired `dashboard.aiondashboard.site` URL and described older package versions.
2. The MCP README linked to an obsolete dashboard registration path, whereas current hosted API keys are issued from `/apis`.
2a. The live `/for-developers` page links the Indian calendar to PyPI and an explanatory comparison but not directly to its public source/issue repository, adding an unnecessary discovery step.
3. The organization profile was out of date on calendar package versions.
4. The website's `/llms.txt` contains 415 lines, including long keyword/topic inventories and repeated product narratives. It is not a replacement for a sitemap or search-engine indexing.
5. `/robots.txt` and `/sitemap.xml` were not retrievable through the browsing tool. Their HTTP status and contents remain **unverified**; DO NOT claim that they are missing, blocked or incorrectly configured without server-side checks.
6. PyPI confirms India 1.7.1 and Lithuania 1.2.1 as the releases published on 2026-11-02. Neither shows uploaded provenance attestations in the PyPI UI.
7. GitHub and PyPI can be indexed but no Search Console, actual conversion analytics or user research was supplied. We cannot infer one definitive cause of low stars from the numbers.

## Changes merged into default branch in this task
- Org profile: https://github.com/AION-Analytics-India/.github/pull/5 — source routing, current releases and contribution guidance.
- Indian Calendar: https://github.com/AION-Analytics-India/aion-indian-market-calendar/pull/6 — badges, reproducible example and source-first path.
- Lithuanian Calendar: https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar/pull/3 — source identity, 1.2.1 and runnable example.
- MCP: https://github.com/AION-Analytics-India/aion-mcp-server/pull/5 — fixed key-registration links and documented open-wrapper versus hosted engine access.
- Old calendar docs: https://github.com/AION-Analytics-India/aion-indian-market-calendar-docs/pull/2 — explicit historical mirror, canonical source and issue destination.

Previously merged in this conversation:
- Org identity: https://github.com/AION-Analytics-India/.github/pull/4
- Veritas website consistency: https://github.com/AION-Analytics-India/aion-veritas/pull/2
- Secondary user public README notice: https://github.com/AION-Analytics/awesome-mcp-servers/pull/1

All five new PRs were squash-merged successfully; default-branch re-fetch confirmed the expected new README content. Source code, permissions and visibility were not altered.

## Prioritized diagnosis (not asserted causality)
P0 — Eliminate retired-domain and wrong-signup links. DONE in the affected GitHub READMEs.
P0 — Drive readers to actual public source repo instead of documentation mirror. DONE in GitHub READMEs.
P1 — Link from website developer landing surfaces to canonical GitHub source, PyPI and issues. WEBSITE WORK.
P1 — Ensure public GitHub organization has six representative pins; retire distracting personal bio. GITHUB UI WORK.
P1 — Measure organic discoverability and click-through across Search Console, website outbound links, GitHub traffic and qualified PyPI installs. ANALYTICS WORK.
P2 — Provide clean issue templates, transparent CI/release provenance and well-scoped beginner-friendly examples. ENGINEERING/COMMUNITY WORK.
P2 — Publish factual technical comparisons and examples in relevant developer communities where permitted, without manufactured stars, fake social proof or unsolicited promotions.

## What stars/forks can and cannot tell us
- A star records a discretionary GitHub action, not an install, API call or active user.
- Forks are naturally less likely for read-only model cards, research archives or thin hosted-service wrappers than for reusable code.
- An absence of stars on new repositories is not proof that GitHub search or robots.txt is blocking them.
- A package can be used via PyPI without its consumer ever visiting GitHub. Separate package download counts from human visits and verified production use.
- Search indexing and public discoverability must be tested independently; llms.txt alone will not generate stars.