# AION Analytics (India)

Market-intelligence infrastructure, open-source developer utilities and published research from an AI systems and software company serving India and Lithuania. [About AION](https://aionanalytics.in/llms.txt)

## Start here

- **Python developers:** use the [Indian Market Calendar](https://github.com/AION-Analytics-India/aion-indian-market-calendar) or [Lithuanian Market Calendar](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar), without an account or API key.
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

- **[India 1.6.0](https://pypi.org/project/aion-indian-market-calendar/1.6.0/):** distinguish trading and settlement days, identify intraday market phases, query supported index-derivative expiry dates and inspect Muhurat sessions. Unsupported expiry inputs and dates beyond available settlement data raise errors. [Release details](https://github.com/AION-Analytics-India/aion-indian-market-calendar/blob/main/CHANGELOG.md)
- **[Lithuania 1.1.0](https://pypi.org/project/aion-lithuanian-market-calendar/1.1.0/):** check TARGET settlement days, find the next settlement day and query continuous/closed market phases. Lithuanian public holidays and euro settlement days are different calendars; auction phases are not modelled. [Release details](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar/blob/main/CHANGELOG.md)

## Hosted products

These services have separate access conditions. Public client code does not include their proprietary models or implementations. The [current product registry](https://aionanalytics.in/models) and [API catalogue](https://aionanalytics.in/apis) govern availability and plans.

- **[Indian Market Intelligence](https://aionanalytics.in/models/indian-market-intelligence):** financial headlines, circulars or notifications to structured sector-impact output. Hosted API with a credentialed free plan and paid plans; model-scoped quotas apply. [Access](https://aionanalytics.in/apis) · [Demo](https://aionanalytics.in/demo)
- **[Veritas](https://aionanalytics.in/models/veritas):** index-market context to pre-open probability bands, with outcomes and misses in the public record. The NIFTY 50 band is published free each trading morning; BANK NIFTY and SENSEX access is by subscription. A band is not a trade instruction. [Plans](https://aionanalytics.in/apis) · [Public model card](https://github.com/AION-Analytics-India/aion-veritas) · [Validation](https://aionanalytics.in/veritas/validation)
- **[Sentinel](https://aionanalytics.in/models/sentinel):** public company filings to corporate-integrity screening results. Access is restricted; current sampling and institutional availability are stated in the [catalogue](https://aionanalytics.in/apis). A screening result does not establish fraud or a regulatory violation.
- **[Edge Engine](https://aionanalytics.in/models/edge-engine):** supported index-option market data to structured per-contract statistical output with an as-of time. Paid API access; supported indices and limitations are in the [catalogue](https://aionanalytics.in/apis).
- **[AION Setu (Order Execution Agent)](https://aionanalytics.in/models/order-execution-agent):** execution events to a device-resident record for examining an automated order. Available through direct engagement on request, with no public download; it records orders and does not place them.
- **[Know Your Rights](https://aionanalytics.in/models/know-your-rights):** Indian-law questions to cited legal information in English, Hindi and Gujarati. Public text-only pilot; information rather than legal advice. [Pilot](https://aionanalytics.in/models/know-your-rights/demo) · [Public documentation](https://github.com/AION-Analytics-India/know-your-rights)
- **[Lithuanian Tax Assistant](https://aionanalytics.in/lt-tax-demo.html):** entered Lithuanian income to tax calculations with cited legal provisions, in Lithuanian and English. Public pilot, not individualized tax advice.

## Research and citations

Published papers and notes are listed in [AION Research](https://github.com/AION-Analytics-India/aion-research) and the [canonical research library](https://aionanalytics.in/research). Cite each publication using its existing identifier and observe its stated publication rights; public access is not a license to proprietary methodology.

Selected papers:

- *Signal Provenance, Part 2. The Structural Harvest* - [SSRN 7663940](https://ssrn.com/abstract=7663940) · [DOI](https://doi.org/10.2139/ssrn.7663940)
- *Contextual Intelligence: A Causal Layer for Country-Specific Decisions* - [SSRN 7596079](https://ssrn.com/abstract=7596079) · [DOI](https://doi.org/10.2139/ssrn.7596079)
- *The Signature Trap: Structural Gaps in Spyware Detection and the Limits of Indicator-Based Defense* - [SSRN 7503278](https://ssrn.com/abstract=7503278) · [DOI](https://doi.org/10.2139/ssrn.7503278)

Other existing papers: [The Uncodified Margin](https://doi.org/10.2139/ssrn.7235801), [Signal Provenance, Part 1](https://doi.org/10.2139/ssrn.7118421), [The Great Indian Illusion](https://doi.org/10.2139/ssrn.6973958), [Asymmetric Multipolarity](https://doi.org/10.2139/ssrn.6449739), and [Beyond the Mirror](https://doi.org/10.2139/ssrn.5232429).

[SSRN author page](https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=7415772) · [ORCID](https://orcid.org/0009-0000-7501-9230) · [Public validation, including misses](https://aionanalytics.in/veritas/validation)

## Support and corrections

Report package defects and documentation mistakes through the relevant repository's issues and contribution guidance. Research corrections belong with the cited publication and its [contribution process](https://github.com/AION-Analytics-India/aion-research/blob/main/CONTRIBUTING.md). For API, account or entitlement help, use [AION's support contacts](https://aionanalytics.in/contact).

Do not post vulnerabilities, credentials or private data in public issues or Discussions. Follow the affected repository's published security policy where one is provided.

## Company and legal notices

AION Analytics (India), founded by Lokesh Gupta, is an independent India-based AI systems and software company. It is not affiliated with Aion Analytics LLC (United States), AION Labs (Israel), or Polymathic's AION astronomy project. [Identity and disambiguation](https://aionanalytics.in/llms.txt)

Information, not advice. AION Analytics is not registered with SEBI as a Research Analyst or Investment Adviser. Product outputs are not instructions to buy or sell. [Terms](https://aionanalytics.in/terms) · [Privacy](https://aionanalytics.in/privacy)

Provisional patent filed. Proprietary implementations remain confidential. [Public product disclosures](https://aionanalytics.in/models)

[Website](https://aionanalytics.in/) · [LinkedIn](https://www.linkedin.com/company/aion-analytics-india/) · [Hugging Face](https://huggingface.co/aion-analytics-india) · [X](https://x.com/aion_analytics_) · [YouTube](https://www.youtube.com/@aionanalytics) · [Telegram](https://t.me/+VXWCiDgZjBI3ZjA1) · [Discord](https://discord.gg/Dk9Pjc9cVa)

## Hiring

The Communication Architect opportunity and its challenge are listed on the live [careers page](https://aionanalytics.in/careers). Read the current requirements there and submit through its form or published contact route.
