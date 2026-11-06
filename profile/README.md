# AION Analytics (India) — Official GitHub Organization

**Sovereign intelligence infrastructure for India's diversity.** AION Analytics Private Limited builds language- and jurisdiction-aware AI systems for markets, citizens and developers. This is the **official GitHub organization** for AION's open-source packages, public model documentation and research. [Company website](https://aionanalytics.in/) · [Identity and scope](https://aionanalytics.in/llms.txt)

**Canonical GitHub home:** [github.com/AION-Analytics-India](https://github.com/AION-Analytics-India). The separate [AION-Analytics user profile](https://github.com/AION-Analytics) is a secondary account, **not another official organization or product catalogue**. Use this organization for public releases, research and developer issues.

## Featured public repositories

These six projects represent AION's current public developer tools and product disclosures. **Use the source repositories below**, not the older documentation mirror or the secondary GitHub user account.

| Project | What visitors can use or inspect | Access |
| --- | --- | --- |
| **[Indian Market Calendar](https://github.com/AION-Analytics-India/aion-indian-market-calendar)** | NSE/BSE/MCX/CDS trading and settlement days, phases, expiries and holidays in Python | [MIT source](https://github.com/AION-Analytics-India/aion-indian-market-calendar) · [PyPI](https://pypi.org/project/aion-indian-market-calendar/) |
| **[Lithuanian Market Calendar](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar)** | Lithuanian statutory days, TARGET euro settlement and supported European trading sessions | [MIT source](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar) · [PyPI](https://pypi.org/project/aion-lithuanian-market-calendar/) |
| **[Indian Market Intelligence (IMI)](https://github.com/AION-Analytics-India/aion-indian-market-intelligence)** | Public integration, API contract and documentation for Indian financial-event sector impact | [Hosted API access](https://aionanalytics.in/apis) · [Model page](https://aionanalytics.in/models/indian-market-intelligence) |
| **[IMI MCP Server](https://github.com/AION-Analytics-India/aion-mcp-server)** | Open-source MCP wrapper to connect agents and compatible clients to the credentialed IMI API | [AGPL wrapper](https://github.com/AION-Analytics-India/aion-mcp-server) · [PyPI](https://pypi.org/project/aion-indian-market-intelligence-mcp/) |
| **[Veritas](https://github.com/AION-Analytics-India/aion-veritas)** | Pre-open index probability bands, published methodology and validation including misses | [Public receipts](https://aionanalytics.in/veritas/validation) · [7-day NIFTY trial and plans](https://aionanalytics.in/veritas) |
| **[Know Your Rights](https://github.com/AION-Analytics-India/know-your-rights)** | Multilingual Indian legal-information pilot client, API contract and limitations | [Pilot availability](https://aionanalytics.in/models/know-your-rights/demo) · [Public client](https://github.com/AION-Analytics-India/know-your-rights) |

For published evidence, see **[AION Research](https://github.com/AION-Analytics-India/aion-research)**. The **[market-calendar data repository](https://github.com/AION-Analytics-India/aion-market-calendar-data)** supports both calendars but is not a separate end-user package.

## Start here

**This is the maintained publishing organization.** Start from the code repository if you plan to inspect, fork or contribute; use the listed PyPI release to install. The older [calendar documentation mirror](https://github.com/AION-Analytics-India/aion-indian-market-calendar-docs) is not the source repository.

**Choose your route:** [Developers](https://aionanalytics.in/for-developers) · [Institutions](https://aionanalytics.in/for-institutions) · [Citizens](https://aionanalytics.in/for-citizens) · [Full product registry](https://aionanalytics.in/models)

- **Python developers:** inspect, fork or contribute to the [Indian Market Calendar (source)](https://github.com/AION-Analytics-India/aion-indian-market-calendar) or the [Lithuanian Market Calendar (source)](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar). Both are MIT licensed; core calendar use does not require an AION account or API key. [India on PyPI](https://pypi.org/project/aion-indian-market-calendar/) · [Lithuania on PyPI](https://pypi.org/project/aion-lithuanian-market-calendar/)
- **AI and API developers:** install the [IMI client](https://pypi.org/project/aion-indian-market-intelligence/) or [MCP server](https://pypi.org/project/aion-indian-market-intelligence-mcp/). Installation is separate from the proprietary hosted service: inference requires credentials and model-specific entitlements. [API catalogue and access](https://aionanalytics.in/apis)
- **Researchers:** read [AION Research](https://github.com/AION-Analytics-India/aion-research), the [canonical library](https://aionanalytics.in/research) and [public validation records](https://aionanalytics.in/veritas/validation). Published findings, citations and limitations do not grant access to proprietary implementations.

Install the calendars from their canonical [Indian](https://pypi.org/project/aion-indian-market-calendar/) and [Lithuanian](https://pypi.org/project/aion-lithuanian-market-calendar/) PyPI distributions:

```sh
pip install aion-indian-market-calendar aion-lithuanian-market-calendar
```

For example, compare settlement days using the documented [India](https://github.com/AION-Analytics-India/aion-indian-market-calendar) and [Lithuania](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar) interfaces:

```python
from aion_indian_market_calendar import is_settlement_day as india_settles
from aion_lithuanian_market_calendar import is_settlement_day as euro_settles

india_settles("2026-04-01")  # False
euro_settles("2026-04-03")  # False
```

Both packages automatically obtain published calendar-data updates through the shared [versioned, hash-verified manifest contract](https://github.com/AION-Analytics-India/aion-market-calendar-data). Supported online installations do not need a new PyPI release for each ordinary holiday or closure update. The normal refresh interval is daily; verified cached or bundled data provides fallback. Offline installations do not receive new data until a permitted refresh can succeed. [Indian behavior](https://github.com/AION-Analytics-India/aion-indian-market-calendar) · [Lithuanian behavior and offline option](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar)

Next: [developer documentation](https://aionanalytics.in/for-developers), [institutional enquiries](https://aionanalytics.in/for-institutions), or [citizen services](https://aionanalytics.in/for-citizens).

## Open-source tools

- **[Indian Market Calendar](https://github.com/AION-Analytics-India/aion-indian-market-calendar):** MIT-licensed calendar and session utilities for Indian markets, including settlement-day and expiry-date interfaces. [PyPI](https://pypi.org/project/aion-indian-market-calendar/)
- **[Lithuanian Market Calendar](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar):** MIT-licensed computed Lithuanian holidays, TARGET settlement-day utilities and exchange calendars using refreshed data. [PyPI](https://pypi.org/project/aion-lithuanian-market-calendar/)
- **[MCP Server](https://github.com/AION-Analytics-India/aion-mcp-server):** an AGPL-3.0-or-later-licensed wrapper for the hosted Indian Market Intelligence service. The wrapper license does not cover the proprietary inference service or confer API access. [License](https://github.com/AION-Analytics-India/aion-mcp-server/blob/main/LICENSE) · [Access and entitlements](https://aionanalytics.in/apis)

Recent calendar releases add practical interfaces for developers:

- **[India 1.7.1](https://pypi.org/project/aion-indian-market-calendar/1.7.1/):** trading versus settlement days, index-expiry and intraday phases, Muhurat sessions, plus commodity closing rules that distinguish US daylight-saving and standard-time seasons. MCX agricultural contracts require their own checks; published exchange notices remain authoritative. [Release details](https://github.com/AION-Analytics-India/aion-indian-market-calendar/blob/main/CHANGELOG.md)
- **[Lithuania 1.2.1](https://pypi.org/project/aion-lithuanian-market-calendar/1.2.1/):** Lithuanian statutory business days, TARGET euro settlement, market phases for supported EU venues, and timezone/daylight-saving utilities. Auction phases are not modelled; exchange-holiday updates remain distinct from statutory holiday calculations. [Release details](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar/blob/main/CHANGELOG.md)

## Hosted products

These services have separate access conditions. Public client code does not include their proprietary models or implementations. The [current product registry](https://aionanalytics.in/models) and [API catalogue](https://aionanalytics.in/apis) govern availability and plans.

- **[Indian Market Intelligence](https://aionanalytics.in/models/indian-market-intelligence):** financial headlines, circulars or notifications to structured sector-impact output. Hosted API with a credentialed free plan and paid plans; model-scoped quotas apply. [Access](https://aionanalytics.in/apis) · [Demo](https://aionanalytics.in/demo)
- **[Veritas](https://aionanalytics.in/models/veritas):** pre-open probability bands for NIFTY 50, BANK NIFTY and SENSEX, with public post-session receipts including misses. NIFTY 50 live access has a **free 7-day trial** (verified email and passkey, no card; 168 hours including non-trading days); continued or other-index access requires a subscription. Live bands are not public without an eligible key. A band is not a trade instruction. [Trial and subscriptions](https://aionanalytics.in/veritas) · [Public model card](https://github.com/AION-Analytics-India/aion-veritas) · [Validation](https://aionanalytics.in/veritas/validation)
- **[Sentinel](https://aionanalytics.in/models/sentinel):** public company filings to corporate-integrity screening results. Access is restricted; current sampling and institutional availability are stated in the [catalogue](https://aionanalytics.in/apis). A screening result does not establish fraud or a regulatory violation.
- **[Edge Engine](https://aionanalytics.in/models/edge-engine):** supported index-option market data to structured per-contract statistical output with an as-of time. Paid API access; supported indices and limitations are in the [catalogue](https://aionanalytics.in/apis).
- **[Signal Infrastructure](https://aionanalytics.in/models/signal-infrastructure):** white-label signal-generation infrastructure leased as an API to eligible SEBI-registered Research Analysts, Investment Advisers and brokers. Not available to retail customers; no signal family currently qualifies for promotion. Pricing by enquiry.
- **[AION Setu (Order Execution Agent)](https://aionanalytics.in/models/order-execution-agent):** execution events to a device-resident record for examining an automated order. Available through direct engagement on request, with no public download; it records orders and does not place them.
- **[Know Your Rights](https://aionanalytics.in/models/know-your-rights):** Indian-law questions to cited legal information in English, Hindi and Gujarati. Public text-only pilot, not legal advice; **new-question availability is governed by the live pilot page**, which currently displays a temporary pause. [Current pilot status](https://aionanalytics.in/models/know-your-rights/demo) · [Public client and documentation](https://github.com/AION-Analytics-India/know-your-rights)
- **[Lithuanian Tax Assistant](https://aionanalytics.in/lt-tax-demo.html):** entered Lithuanian income to tax calculations with cited legal provisions, in Lithuanian and English. Public pilot, not individualized tax advice.

## Research and citations

Published papers and notes are listed in [AION Research](https://github.com/AION-Analytics-India/aion-research) and the [canonical research library](https://aionanalytics.in/research). Cite each publication using its existing identifier and observe its stated publication rights; public access is not a license to proprietary methodology.

Selected papers:

- *Signal Provenance, Part 2. The Structural Harvest* - [SSRN 7663940](https://ssrn.com/abstract=7663940) · [DOI](https://doi.org/10.2139/ssrn.7663940)
- *Contextual Intelligence: A Causal Layer for Country-Specific Decisions* - [SSRN 7596079](https://ssrn.com/abstract=7596079) · [DOI](https://doi.org/10.2139/ssrn.7596079)
- *The Signature Trap: Structural Gaps in Spyware Detection and the Limits of Indicator-Based Defense* - [SSRN 7503278](https://ssrn.com/abstract=7503278) · [DOI](https://doi.org/10.2139/ssrn.7503278)

Other existing papers: [The Uncodified Margin](https://doi.org/10.2139/ssrn.7235801), [Signal Provenance, Part 1](https://doi.org/10.2139/ssrn.7118421), [The Great Indian Illusion](https://doi.org/10.2139/ssrn.6973958), [Asymmetric Multipolarity](https://doi.org/10.2139/ssrn.6449739), and [Beyond the Mirror](https://doi.org/10.2139/ssrn.5232429).

[SSRN author page](https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=7415772) · [ORCID](https://orcid.org/0009-0000-7501-9230) · [Public validation, including misses](https://aionanalytics.in/veritas/validation)

## Contribute or report a defect

- **Calendar correctness:** report a reproducible exchange/date discrepancy with a primary exchange notice and package version in the [India calendar issues](https://github.com/AION-Analytics-India/aion-indian-market-calendar/issues) or [Lithuania calendar issues](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar/issues). Source contributions follow each repository's `CONTRIBUTING.md`.
- **MCP developer integration:** test the [public wrapper](https://github.com/AION-Analytics-India/aion-mcp-server), file a focused [issue](https://github.com/AION-Analytics-India/aion-mcp-server/issues), or suggest an example that does not disclose tokens or proprietary inference logic.
- **Research corrections:** use the [research contribution process](https://github.com/AION-Analytics-India/aion-research/blob/main/CONTRIBUTING.md) with a cited publication and reproducible evidence.

If a public tool is useful in your workflow, starring its **source repository** helps other developers discover that specific package; it does not affect AION access or support priority.

## Support and corrections

Report package defects and documentation mistakes through the relevant repository's issues and contribution guidance. Research corrections belong with the cited publication and its [contribution process](https://github.com/AION-Analytics-India/aion-research/blob/main/CONTRIBUTING.md). For API, account or entitlement help, use [AION's support contacts](https://aionanalytics.in/contact).

Do not post vulnerabilities, credentials or private data in public issues or Discussions. Follow the affected repository's published security policy where one is provided.

## Company and legal notices

AION Analytics Private Limited (India), founded by Lokesh Gupta, is an independent India-based AI systems and software company. It is not affiliated with Aion Analytics LLC (United States), AION Labs (Israel), or Polymathic's AION astronomy project. [Identity and disambiguation](https://aionanalytics.in/llms.txt)

Information, not advice. AION Analytics is not registered with SEBI as a Research Analyst or Investment Adviser. Product outputs are not instructions to buy or sell. [Terms](https://aionanalytics.in/legal/terms) · [Privacy](https://aionanalytics.in/legal/privacy)

Three provisional patent applications are publicly disclosed: IN202621086466 (signal provenance / Order Execution Agent), and IN202621118523 and IN202621119269 (Indian Market Intelligence). Proprietary implementations remain confidential. [Current product disclosures](https://aionanalytics.in/models)

[Website](https://aionanalytics.in/) · [LinkedIn](https://www.linkedin.com/company/aion-analytics-india/) · [Hugging Face](https://huggingface.co/aion-analytics-india) · [Google Scholar](https://scholar.google.com/citations?user=QuCFm9YAAAAJ) · [X](https://x.com/aion_analytics_) · [YouTube](https://www.youtube.com/@aionanalytics) · [Instagram](https://www.instagram.com/aion_analytics/) · [Threads](https://www.threads.com/%40aion_analytics) · [Telegram](https://t.me/+VXWCiDgZjBI3ZjA1) · [Discord](https://discord.gg/Dk9Pjc9cVa)

## Hiring

The current [Sales Architect opportunity](https://aionanalytics.in/careers) covers B2B and B2C sales, is remote within India, and uses a three-part challenge instead of a conventional CV or cover letter. Refer to the live careers page for current requirements, the application form and the published contact route.
