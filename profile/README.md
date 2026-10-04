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

> **We're hiring a communication architect.** No CVs — [the challenge is the
> application](https://aionanalytics.in/careers).

---

## Start here

```bash
pip install aion-indian-market-calendar        # is this market open right now?
pip install aion-lithuanian-market-calendar    # 19 EU venues, timezone-correct
pip install aion-indian-market-intelligence    # event -> sector impact, as JSON
uvx aion-indian-market-intelligence-mcp        # the same, as an MCP server for agents
```

**Install from PyPI, always.** We do not attach wheels to GitHub releases: PyPI
is the canonical source, a wheel in a repository invites installing from a path
nobody tests, and two ways to install is one more than anyone needs. Releases
here carry a changelog and a link, and that is all.

Both calendars send **no telemetry, no analytics and no identifiers**. Their
holiday data updates itself from
[aion-market-calendar-data](https://github.com/AION-Analytics-India/aion-market-calendar-data),
hash-verified, so a new closure never needs a release.

```python
from aion_indian_market_calendar import is_open

is_open("NSE")          # -> True / False, offline, no API key, no network call
```

**[Try the live demo](https://aionanalytics.in/demo)** — no signup, no card, no cookies.

Not a trader? **[Know Your Rights](https://aionanalytics.in/models/know-your-rights/demo)** answers questions about Indian law in English, Hindi or Gujarati, and cites the section it came from. It is in pilot, and a rating on a *wrong* answer helps us more than a rating on a right one.

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
| **[Indian Market Intelligence](https://aionanalytics.in/models/indian-market-intelligence)** | A sentiment score says `negative 0.82`. Negative *for whom?* One event moves different sectors in opposite directions. Returns a signed sector vector, stakeholder views, confidence and evidence, as JSON. | [repo](https://github.com/AION-Analytics-India/aion-indian-market-intelligence) · [demo](https://aionanalytics.in/demo) |
| **[Sentinel](https://aionanalytics.in/models/sentinel)** | Regulators act after the loss. Screens 2,715 listed Indian companies for disclosure that diverges from compliant peers. Two independent methods; agreement between them is the signal. Never trained on fraud labels. | [demo](https://aionanalytics.in/demo) |
| **[Veritas](https://aionanalytics.in/models/veritas)** | Forecasters publish their hits and bury their misses. Pre-open probability bands for NIFTY 50, BANK NIFTY and SENSEX, scored publicly every day — misses on the permanent record. | [repo](https://github.com/AION-Analytics-India/aion-veritas) · [receipts](https://aionanalytics.in/veritas/validation) |
| **[Order Execution Agent](https://aionanalytics.in/models/order-execution-agent)** | When an automated trade is disputed, no independent record exists of what the system actually did. Device-resident chain of custody from signal to executed order. *Patent application filed.* | |
| **[Edge Engine](https://aionanalytics.in/models/edge-engine)** | A pattern fired — but is there an edge, and does it survive costs? Two different questions, answered separately. | |
| **[Edge Audit Reports](https://aionanalytics.in/veritas/validation)** | Anyone can claim a track record. The published archive of signals and their outcomes, failures included. | |
| **[Know Your Rights](https://aionanalytics.in/models/know-your-rights)** | Most people meet the law at the worst possible moment, and the answer they need is public but unreadable. Ask in English, Hindi or Gujarati — by voice or typing, in your own script or Roman letters — and get a plain answer that names the provision it came from. Refuses when the corpus cannot answer, rather than guessing. *Pilot — open.* | [repo](https://github.com/AION-Analytics-India/know-your-rights) · [try it](https://aionanalytics.in/models/know-your-rights/demo) |

---

## Follow the work

Both channels carry output, not announcements.

| | |
|---|---|
| **[Telegram](https://t.me/AionAnalyticsIndia)** | Central and constitutional changes to Indian law, found each morning from India Code and the Press Information Bureau, with the source linked. |
| **[Discord](https://discord.gg/bCuH37bv)** | The same, one thread per change, plus the daily Veritas validation record — hits and misses both. |

A legal notice says *that* the law moved and links the source. It does not say
what the law now says: nobody has reviewed it at that point, and publishing an
interpretation ahead of a human reading the provision is the failure the whole
project is built to avoid.

---

## We're hiring — Communication Architect

**We don't read CVs. We read code.**

The technical work here is solid. The gap is communication: very few people outside the field know
this work exists, and even fewer can explain it clearly. We need someone who can sit with the actual
code and models, understand what they do and why they matter, and then produce content that makes a
developer, a trader, or a curious founder say: *"I didn't know this was possible."*

This is not a social media management role. It is a thinking role that sometimes outputs social media.

**There is no form to fill before you do the work. The challenge *is* the application.** Read the
repositories on this page — the model card, the package README, what the code actually does — then
write one piece that explains a single AION product to someone who has never heard of us. Under
~500 words, in whatever format you choose. That is the only CV we read.

We publish exactly what we weight, because transparency about evaluation criteria is part of how
AION works: **technical understanding** highest, then **strategic thinking**, then **communication
clarity**. Showing how you would automate your own work is a bonus signal, not a requirement.

A generic cover letter is an instant pass. A thoughtful piece of work is an invitation to a
conversation.

Remote. Output-based. The first engagement is a **paid trial** based on the challenge submission —
if the work is strong, the conversation continues from there. We especially welcome applicants from
underrepresented backgrounds; the challenge is the same for everyone, and the only thing we evaluate
is the work.

**→ [Read the full challenge and submit](https://aionanalytics.in/careers)**

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
Two provisional patent applications are filed (IN202621086466, signal-provenance capture; IN202621118523, AION Indian Market Intelligence). The methods are deliberately undocumented.
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

- Website: <https://aionanalytics.in/>
- Machine-readable identity: <https://aionanalytics.in/llms.txt>
- Hugging Face: <https://huggingface.co/aion-analytics-india>
- DEV: <https://dev.to/aion-analytics-india>
- X: [@aion_analytics_](https://x.com/aion_analytics_)

---

*Content is for educational and research purposes only. Not investment advice. AION Analytics (India)
is not a SEBI-registered Research Analyst or Investment Adviser. Download figures are reported
directly by PyPI.*
