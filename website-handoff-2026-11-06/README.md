# AION GitHub discovery & website SEO handoff — 2026-11-06

This folder contains deployment **drafts** and the supporting discovery audit, hosted here because some ChatGPT clients cannot download generated sandbox attachments.

**Canonical public GitHub organization:** https://github.com/AION-Analytics-India

## Files

- [llms.txt](llms.txt): proposed curated AI/LLM content map for the website root. **Not yet deployed.**
- [robots.example.txt](robots.example.txt): **merge-only baseline**. Never overwrite an existing production robots.txt without inspecting its bot rules.
- [sitemap.example.xml](sitemap.example.xml): candidate URLs, **not** a verified production sitemap. Validate every URL before use.
- [DEPLOY_README.md](DEPLOY_README.md): website-agent instructions, precautions and checks.
- [DISCOVERY_AUDIT.md](DISCOVERY_AUDIT.md): evidence, limitations and merged GitHub correction log.
- [GITHUB_UI_ACTIONS.md](GITHUB_UI_ACTIONS.md): personal-profile bio, organization pins and repository-metadata actions that require GitHub settings.

## How to download

Open a file above, then choose **Raw** / **Download raw file** in GitHub. The files are plain UTF-8 text or XML; they can be copied into your website repository.

## Not live website configuration

Publishing these documents on GitHub does **not** change https://aionanalytics.in/robots.txt, https://aionanalytics.in/llms.txt or the live sitemap. Your website deployment operator needs to review and publish them.

GitHub documentation improvements have already been merged separately in the canonical source repositories. See [DISCOVERY_AUDIT.md](DISCOVERY_AUDIT.md).
