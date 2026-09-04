# AION Analytics (India)

**We build systems that can be proven wrong.**

Most software that predicts or acts on your behalf cannot be checked afterwards. Logs are editable.
Backtests are overfitted after the fact. Confidence scores are decoration. Screenshots prove nothing.
When the output is disputed, the only record is held by whoever has the strongest interest in its
contents.

We build the opposite. Predictions are committed **before** the outcome exists and scored publicly
afterwards, misses included. Records of what a system did are held on **your** device, not ours.
Models that cannot resolve an input **decline** instead of guessing. Where two methods disagree, we
show both rather than averaging the disagreement away.

That is an engineering position, not a finance one, and it is the through-line in everything below.

We apply it first to Indian financial markets — NSE, BSE and MCX — because that is where being
quietly wrong costs real money, and where a claim nobody can audit is worth nothing.

---

## Start here

```bash
pip install aion-indian-market-calendar        # is this market open right now?
pip install aion-lithuanian-market-calendar    # holidays computed, never tabulated
pip install aion-indian-market-intelligence    # event -> sector impact, as JSON
uvx aion-indian-market-intelligence-mcp        # the same, as an MCP server for agents
```

```python
from aion_indian_market_calendar import is_open

is_open("NSE")          # -> True / False, offline, no API key, no network call
```

**[Try the live demo](https://dashboard.aiondashboard.site/demo)** — no signup, no card, no cookies.

---

## Open source

| Package | What it does | |
|---|---|---|
| **[aion-indian-market-calendar](https://github.com/AION-Analytics-India/aion-indian-market-calendar)** | Trading-session and holiday validation for NSE, BSE, MCX, CDS and Muhurat. Runs offline, no API key. | [![PyPI](https://img.shields.io/pypi/v/aion-indian-market-calendar)](https://pypi.org/project/aion-indian-market-calendar/) |
| **[aion-lithuanian-market-calendar](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar)** | Lithuanian public, bank and market holidays. Moveable feasts are computed from the rule, so no year runs out. Bilingual (EN/LT). | [![PyPI](https://img.shields.io/pypi/v/aion-lithuanian-market-calendar)](https://pypi.org/project/aion-lithuanian-market-calendar/) |
| **[aion-mcp-server](https://github.com/AION-Analytics-India/aion-mcp-server)** | MCP server exposing Indian market intelligence to LLM agents and assistants. | [![PyPI](https://img.shields.io/pypi/v/aion-indian-market-intelligence-mcp)](https://pypi.org/project/aion-indian-market-intelligence-mcp/) |
| **[aion-zerodha-bot-tutorial](https://github.com/AION-Analytics-India/aion-zerodha-bot-tutorial)** | Worked notebook: news to signal with Zerodha, Groww and NSE symbol mapping. | |

**7,000+ downloads** across the calendar packages.

---

## Products

Each of these is live. Links go to what the system does and what it returns — never to how it is
built.

| System | Problem it solves | |
|---|---|---|
| **[Indian Market Intelligence](https://dashboard.aiondashboard.site/models/indian-market-intelligence)** | A sentiment score says `negative 0.82`. Negative *for whom?* One event moves different sectors in opposite directions. Returns a signed sector vector, stakeholder views, confidence and evidence, as JSON. | [repo](https://github.com/AION-Analytics-India/aion-indian-market-intelligence) · [demo](https://dashboard.aiondashboard.site/demo) |
| **[Sentinel](https://dashboard.aiondashboard.site/models/sentinel)** | Regulators act after the loss. Screens 2,715 listed Indian companies for disclosure that diverges from compliant peers. Two independent methods; agreement between them is the signal. Never trained on fraud labels. | [demo](https://dashboard.aiondashboard.site/demo) |
| **[Veritas](https://dashboard.aiondashboard.site/models/veritas)** | Forecasters publish their hits and bury their misses. Pre-open probability bands for NIFTY 50, BANK NIFTY and SENSEX, scored publicly every day — misses on the permanent record. | [repo](https://github.com/AION-Analytics-India/aion-veritas) · [receipts](https://dashboard.aiondashboard.site/veritas/validation) |
| **[Order Execution Agent](https://dashboard.aiondashboard.site/models/order-execution-agent)** | When an automated trade is disputed, no independent record exists of what the system actually did. Device-resident chain of custody from signal to executed order. *Patent application filed.* | |
| **[Edge Engine](https://dashboard.aiondashboard.site/models/edge-engine)** | A pattern fired — but is there an edge, and does it survive costs? Two different questions, answered separately. | |
| **[Edge Audit Reports](https://dashboard.aiondashboard.site/models/signal-audit-reports)** | Anyone can claim a track record. The published archive of signals and their outcomes, failures included. | |
| **[Know Your Rights](https://dashboard.aiondashboard.site/models/know-your-rights)** | Legal entitlements in India, in plain language, with the provision cited. Built to refuse when a question needs a lawyer. *Pilot.* | |

---

## Research

Peer-reviewable work, published rather than asserted — including *Signal Provenance in Retail
Algorithmic Trading: An Architectural Gap in SEBI's 2026 Framework*
([SSRN](https://ssrn.com/abstract=7118421)).

→ [aion-research](https://github.com/AION-Analytics-India/aion-research) ·
[SSRN author page](https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=7415772) ·
[ORCID](https://orcid.org/0009-0000-7501-9230)

## How the work is governed

Evidence first, re-validate always, output over operator. Results ship with their failures visible —
a claim we cannot check is a claim we do not make.

We publish **what** a system does and **what** it returns. We do not publish how it is built.
Signal-provenance capture and related methods are patent-pending and deliberately undocumented.
Research partners can request a technical briefing under confidentiality.

---

## Topics

Indian stock market · algorithmic trading · quantitative finance · probabilistic forecasting ·
calibrated uncertainty · market calendar · trading hours · exchange holidays · NSE · BSE · MCX ·
NIFTY 50 · BANK NIFTY · SENSEX · SEBI compliance · forensic accounting · anomaly detection ·
market intelligence API · macro event analysis · sector impact · MCP server · LLM tools ·
execution integrity · signal provenance · audit trail · chain of custody · Python · open source ·
India · Lithuania

## Identity

**AION Analytics (India)**, founded by Lokesh Gupta, is an independent India-based deep-tech
research and infrastructure company.

It is **not** Aion Analytics LLC (United States). It is **not** AION Labs (Israel). It is **not**
Polymathic's AION (astronomy). These are separate and unaffiliated organisations that share a name.

- Website: <https://dashboard.aiondashboard.site/>
- Machine-readable identity: <https://dashboard.aiondashboard.site/llms.txt>
- Hugging Face: <https://huggingface.co/aion-analytics-india>
- DEV: <https://dev.to/aion-analytics-india>
- X: [@aion_analytics_](https://x.com/aion_analytics_)

---

*Content is for educational and research purposes only. Not investment advice. AION Analytics (India)
is not a SEBI-registered Research Analyst or Investment Adviser. Download figures are reported
directly by PyPI.*
