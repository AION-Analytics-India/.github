# Website discovery handoff — AION Analytics
Date: 2026-11-06
Owner: website deployment agent

## Scope and safeguards
The ZIP contains *proposed website files*, not live website changes. ChatGPT GitHub access does not provide a repository for the aionanalytics.in production deployment. The existing website must be updated by its operator.

- DO NOT change DNS, hosting, account access, payment flows or application endpoints.
- DO NOT silently overwrite an existing robots.txt: this audit could not reliably retrieve the live robots.txt or sitemap.xml. A web-tool retrieval failure is not proof that either file is missing or blocked.
- Preserve all existing intentional `Disallow`, `Allow`, and crawler-specific rules in the live robots.txt. The included robots.txt is a minimal *baseline*, not an audited replacement.
- Robots directives do not authorize or prevent access to private endpoints. Enforce all access controls on the server.
- Do not add `Disallow: /` to the public search-bot rules. Do not blanket-block `/models/`, `/research/`, `/open-source/` or `/for-developers/`.
- Do not add `noindex` headers or meta tags to these public pages.
- No fabricated release counts, press coverage, community stars, product accuracy or research validation.

## Deploy llms.txt
1. Back up the current `/llms.txt` (it was 415 lines at audit time). If full context remains useful, publish the previous version at `/llms-full.txt` and add a genuine link to it from the new index after the URL exists.
2. Put the supplied `llms.txt` at the web root as UTF-8 text with HTTP 200 and `Content-Type: text/plain; charset=utf-8`.
3. Check that it has one H1 heading, the short identity blockquote, and links to the maintained **AION-Analytics-India** organization, two source calendar repositories, PyPI, API docs, research and legal notices.
4. Verify current access terms from the product registry on each deployment. The revised file distinguishes MIT Python calendars from credentialed IMI API access and the free seven-day NIFTY 50 trial.
5. Do not rely on llms.txt to improve Google ranking. It is a curated machine-readable context guide, not a supported general search ranking control.

## Merge robots.txt safely
1. Fetch the actual current file in the deployment environment and save a copy.
2. Keep the current bot-specific rules and existing restrictions unless independently justified.
3. Confirm public content remains crawlable by your intended search engines.
4. Add the *one* canonical line `Sitemap: https://aionanalytics.in/sitemap.xml` if missing and if that URL exists.
5. Serve `/robots.txt` from the domain root with HTTP 200, `Content-Type: text/plain`, no sign-in and no JS challenge.
6. Do not put private endpoint paths into the sitemap.

## Sitemap
`/sitemap.xml` was not accessible in the audit browsing tool; do not infer that it does not exist.
- Prefer the website's automatic sitemap generation. Use `sitemap.example.xml` only as a list of candidate public canonical pages.
- Include only indexable canonical URLs returning 200 with meaningful content. Check every candidate before deployment; remove redirects, 404s and noindex pages.
- Submit the live sitemap URL in Google Search Console and Bing Webmaster Tools.
- Update sitemap automatically as public research and product pages are added.
- No invented `lastmod`. Use precise content modification timestamps only when the build system knows them.
- XML MIME type: `application/xml` or `text/xml`, HTTP 200.

## Canonical linking and structured data
- **Priority:** `/for-developers` currently links the Indian calendar to PyPI and a comparison article, but offers no adjacent direct GitHub-source link. Add a visible `Source code / issues / contribute` link to `https://github.com/AION-Analytics-India/aion-indian-market-calendar` beside its install command. Preserve the Lithuanian calendar's existing direct GitHub link.
- Header/footer and `/for-developers` should link directly to the official GitHub organization and the *source* calendar repositories. Avoid linking first to the legacy documentation mirror.
- Use `rel="canonical"` on public website pages with the preferred `https://aionanalytics.in` host.
- Use consistent Organization schema `name: AION Analytics Private Limited`, `url: https://aionanalytics.in/`, `sameAs: [https://github.com/AION-Analytics-India, ...verified profiles]`. Do not invent contact, address or legal IDs.
- Open Graph and page titles should describe developer-specific tasks, not just the brand. Search-console query data should determine refinements.
- Ensure www and http variants redirect to the canonical https non-www host.

## Website content inconsistencies to correct
- The home page previously labelled NIFTY Veritas "free" without the 7-day trial restriction; `/veritas` gives the correct conditions.
- `/for-developers` claims "No equivalent package existed for either market" without a documented market-wide comparison; replace that superlative with verified scope and supported interfaces.
- The Indian calendar product page showed overgeneralized exchange closing times and "no network dependency"; current package handles different segments, seasonal commodity closes and a permitted hash-verified data refresh.
- The Lithuanian product page claimed the package "never needs updating". Statutory holidays are computed, but exchange-closure updates are maintained separately.
- The institutions page previously called the entity an LLP. Check and align with AION Analytics Private Limited.
- Make every website-to-GitHub link point to the maintained organization/source repository, not the historical mirror or secondary user account.
- Keep all privacy and legal claims synchronized with actual implementation and policy.

## Verification
From macOS Terminal in the project directory:
    bash check_public_discovery.sh

Success criteria:
- `/robots.txt`, `/llms.txt` and `/sitemap.xml` return 200 and are publicly readable.
- robots.txt advertises the **working** sitemap.
- sitemap URLs are genuinely public, canonical and return 200.
- No public source/download links use `dashboard.aiondashboard.site`.
- Public developer landing pages visibly link to `github.com/AION-Analytics-India`.
- The content says PyPI 1.7.1 / 1.2.1 (as of this audit), with updates driven by the actual PyPI releases.
- API key pages route via `/apis`, not the separate `/access/register` referral route.

## Monitoring: establish a baseline, then review after 14/30 days
- Search Console: indexed pages, impressions, click-throughs and queries for "NSE market calendar Python", "MCX trading session", "Lithuania business day Python", and "Indian market intelligence API".
- GitHub Insights: repository visitors, cloners, issues/PRs from outside contributors, stars and forks. Star counts alone are not conversion metrics.
- PyPI: qualified downloads, package versions and mirrored-download caveats.
- Website: aggregate page-level clickouts from `/for-developers` to the canonical GitHub and PyPI domains, without user fingerprinting.
- Compare the same window pre/post change; never attribute gains to llms.txt without evidence.