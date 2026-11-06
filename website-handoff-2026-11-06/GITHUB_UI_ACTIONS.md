# Remaining GitHub account-level actions — browser UI only

These controls are not exposed by the connected GitHub app's available write tools. All relevant README changes were applied separately via GitHub PRs.

## 1. Official organization: https://github.com/AION-Analytics-India
- Set website to `https://aionanalytics.in/`.
- Suggested short description: `Sovereign, jurisdiction-aware AI infrastructure. Open-source market calendars, Indian market intelligence, MCP tools and public research.`
- From the organization profile, choose `View as: Public`, then `Pin repositories` / `Customize pins`. Choose six public repos:
  1. aion-indian-market-calendar (maintained source, not the docs mirror)
  2. aion-lithuanian-market-calendar
  3. aion-indian-market-intelligence
  4. aion-mcp-server
  5. know-your-rights
  6. aion-research
- Do not pin the archived Zerodha tutorial, `.github`, or the historical `aion-indian-market-calendar-docs` mirror.
- Consider making a verified maintainer publicly visible if that is compatible with the organization's privacy and governance policy; this is optional.

## 2. Secondary user profile: https://github.com/AION-Analytics
- Replace the old "Soon to announce" bio/status with:
  `Secondary maintenance account for AION Analytics. Official repositories, releases and research: github.com/AION-Analytics-India`
- Point the profile website field to `https://github.com/AION-Analytics-India`.
- This user account already contains a public notice in `awesome-mcp-servers` linking the canonical organization.
- Do not delete the user account or private repositories: this may disrupt access, integrations and existing links.
- Optionally create the public profile README repository named `AION-Analytics/AION-Analytics` and repeat only the canonical redirect. Creating repositories is not supported by the connected actions.

## 3. Repository metadata
- `AION-Analytics-India/aion-lithuanian-market-calendar`: replace the description "never needs updating", which is too broad for separate exchange-holiday data.
  Suggested: `Lithuanian business holidays, TARGET settlement and European trading sessions. Python, MIT; validated exchange-data refresh.`
- `AION-Analytics-India/aion-market-calendar-data`: add a relevant homepage and 3–5 accurate topics such as `market-calendar`, `exchange-holidays`, `python`, `data-integrity`, `calendar-data`.
- Check Veritas homepage and metadata link to the currently supported `/veritas` or `/models/veritas`.
- Keep the canonical source repository descriptions precise, with no unverified superlatives.
- Repository topics are *already present* for most projects; do not blanket-add irrelevant keywords.

## 4. Supply-chain credibility
- Both current calendar releases on PyPI (India 1.7.1, Lithuania 1.2.1) showed "No provenance" in the PyPI release UI.
- Review release workflow and publisher configuration before any migration to PyPI Trusted Publishing / attestations. This is a release-pipeline action, NOT a README change.
- Do not publish a new package release solely to change GitHub discovery copy.