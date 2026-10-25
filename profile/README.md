# AION Analytics (India)

An AI systems and software company building domain-specific intelligence infrastructure.

Our public work serves markets, citizens and developers, with product availability described individually in the [current registry](https://aionanalytics.in/models). Start with the [developer guide](https://aionanalytics.in/for-developers), [citizen guide](https://aionanalytics.in/for-citizens) or [research library](https://aionanalytics.in/research).

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

We apply it first to Indian financial markets (NSE, BSE and MCX) because that is where being
quietly wrong costs real money, and where a claim nobody can audit is worth nothing.

> **We're hiring a communication architect.** No CVs: [the challenge is the
> application](https://aionanalytics.in/careers).

---

## Start here

```bash
pip install aion-indian-market-calendar        # open now? settlement day? next NIFTY expiry?
pip install aion-lithuanian-market-calendar    # holidays, TARGET settlement, 19 EU venues
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
import os
os.environ["AION_IN_CALENDAR_OFFLINE"] = "1"  # use bundled data without refresh

from aion_indian_market_calendar import is_market_open, get_expiry_day, get_market_phase

is_market_open("NSE")           # -> True / False for the current time, no API key
get_market_phase(market="NSE")  # -> "PRE_OPEN", "CONTINUOUS", "CLOSING_AUCTION", ...
get_expiry_day("BANKNIFTY")     # -> next monthly expiry, moved earlier if it falls on a holiday
```

**[Try the live demo](https://aionanalytics.in/demo)**: a free demo key, issued on the page against your email. No card, no cookies.

Not a trader? **[Know Your Rights](https://aionanalytics.in/models/know-your-rights/demo)** answers questions about Indian law in English, Hindi or Gujarati, and cites the section it came from. It is in pilot, and a rating on a *wrong* answer helps us more than a rating on a right one.

## What you can ask us about

- *Is NSE, BSE or MCX open right now, and which days in 2026 are stock market holidays?* [aion-indian-market-calendar](https://aionanalytics.in/open-source/indian-market-calendar)
- *When does the next NIFTY, BANKNIFTY or SENSEX contract expire, and does NSE Clearing settle today?* [aion-indian-market-calendar](https://aionanalytics.in/open-source/indian-market-calendar), from the exchange circulars it cites
- *Which sectors does this Indian news headline, RBI or SEBI circular affect, and in which direction?* An alternative to a news sentiment score: [Indian Market Intelligence](https://aionanalytics.in/models/indian-market-intelligence)
- *What range is NIFTY 50 likely to trade within in the first 15 minutes, and how often was that band wrong?* [Veritas](https://aionanalytics.in/veritas) and its [validation record](https://aionanalytics.in/veritas/validation)
- *Which listed Indian companies' filings look least like their peers'?* A forensic-accounting screen for red flags, not a finding of fraud: [Sentinel](https://aionanalytics.in/models/sentinel)
- *What does Indian law say about my situation with the police, a landlord, an employer or a hospital?* Free legal information in English, Hindi or Gujarati, citing the section: [Know Your Rights](https://aionanalytics.in/models/know-your-rights/demo)
- *How much Lithuanian income tax (GPM) might apply to my income?* [Lithuanian Tax Assistant](https://aionanalytics.in/lt-tax-demo.html), in Lithuanian and English
- *Lithuanian public holidays, business days or the Nasdaq Vilnius calendar in Python?* [aion-lithuanian-market-calendar](https://aionanalytics.in/open-source/lithuanian-market-calendar)
- *Does TARGET settle euro payments today, even though it is a Lithuanian holiday?* [aion-lithuanian-market-calendar](https://aionanalytics.in/open-source/lithuanian-market-calendar)

---

## Open source

| Package | What it does | |
|---|---|---|
| **[aion-indian-market-calendar](https://github.com/AION-Analytics-India/aion-indian-market-calendar)** | Trading-session and holiday validation for NSE, BSE, MCX, CDS and Muhurat. From 1.6.0: NSE Clearing settlement days, intraday phases (pre-open, continuous, closing auction, post-close) and derivative expiry dates from the NSE and BSE circulars. Runs offline, no API key. | [![PyPI](https://img.shields.io/pypi/v/aion-indian-market-calendar)](https://pypi.org/project/aion-indian-market-calendar/) |
| **[aion-lithuanian-market-calendar](https://github.com/AION-Analytics-India/aion-lithuanian-market-calendar)** | Lithuanian public, bank and market holidays. Moveable feasts are computed from the rule, so no year runs out. From 1.1.0: TARGET settlement days, which differ from Lithuanian holidays in both directions, and the trading phase for 19 EU venues. Bilingual (EN/LT). | [![PyPI](https://img.shields.io/pypi/v/aion-lithuanian-market-calendar)](https://pypi.org/project/aion-lithuanian-market-calendar/) |
| **[aion-mcp-server](https://github.com/AION-Analytics-India/aion-mcp-server)** | MCP server exposing Indian market intelligence to LLM agents and assistants. | [![PyPI](https://img.shields.io/pypi/v/aion-indian-market-intelligence-mcp)](https://pypi.org/project/aion-indian-market-intelligence-mcp/) |

Package download events are not unique developers or successful installations.

---

## Products

Availability differs by product. Check the [current product registry](https://aionanalytics.in/models) for deployed services, pilots and direct-engagement offerings.

| System | Problem it solves | |
|---|---|---|
| **[Indian Market Intelligence](https://aionanalytics.in/models/indian-market-intelligence)** | A sentiment score says `negative 0.82`. Negative *for whom?* One event moves different sectors in opposite directions. Returns a signed sector vector, stakeholder views, confidence and evidence, as JSON. | [repo](https://github.com/AION-Analytics-India/aion-indian-market-intelligence) · [demo](https://aionanalytics.in/demo) |
| **[Sentinel](https://aionanalytics.in/models/sentinel)** | Regulators act after the loss. A forensic-accounting screen of listed Indian companies (2,753 in the snapshot of 17 October 2026) for filings that diverge from peers with clean records. Two independent methods; the classifier is trained on enforcement actions, and agreement between the two is the signal. A reason to read further, not a finding of fraud. | [demo](https://aionanalytics.in/demo) |
| **[Veritas](https://aionanalytics.in/models/veritas)** | Forecasters publish their hits and bury their misses. Pre-open probability bands for NIFTY 50, BANK NIFTY and SENSEX, scored publicly every day, misses on the permanent record. | [repo](https://github.com/AION-Analytics-India/aion-veritas) · [receipts](https://aionanalytics.in/veritas/validation) |
| **[Order Execution Agent](https://aionanalytics.in/models/order-execution-agent)** | When an automated trade is disputed, no independent record exists of what the system actually did. Device-resident chain of custody from signal to executed order. *Patent application filed.* | |
| **[Edge Engine](https://aionanalytics.in/models/edge-engine)** | A pattern fired, but is there an edge, and does it survive costs? Two different questions, answered separately. | |
| **[Edge Audit Reports](https://aionanalytics.in/veritas/validation)** | Anyone can claim a track record. The published archive of signals and their outcomes, failures included. | |
| **[Know Your Rights](https://aionanalytics.in/models/know-your-rights)** | Most people meet the law at the worst possible moment, and the answer they need is public but unreadable. Ask in English, Hindi or Gujarati about police, tenancy, consumer, employment, healthcare, banking or family matters, and get a plain answer that names the provision it came from. Refuses when the corpus cannot answer, rather than guessing. Text only for now; voice follows later. *Pilot, open.* | [repo](https://github.com/AION-Analytics-India/know-your-rights) · [try it](https://aionanalytics.in/models/know-your-rights/demo) |
| **[Lithuanian Tax Assistant](https://aionanalytics.in/lt-tax-demo.html)** | Lithuanian personal income tax (GPM) for 2026, in Lithuanian and English. Every line of the result names the GPMĮ article it rests on, and the calculation runs in your browser. Reports the law; not tax advice. *Pilot, open.* | [try it](https://aionanalytics.in/lt-tax-demo.html) |

---

## Follow the work

Both channels carry output, not announcements.

| | |
|---|---|
| **[Telegram](https://t.me/+VXWCiDgZjBI3ZjA1)** | Central and constitutional changes to Indian law, found each morning from India Code and the Press Information Bureau, with the source linked. |
| **[Discord](https://discord.gg/Dk9Pjc9cVa)** | The same, one thread per change, plus the daily Veritas validation record, hits and misses both. |

A legal notice says *that* the law moved and links the source. It does not say
what the law now says: nobody has reviewed it at that point, and publishing an
interpretation ahead of a human reading the provision is the failure the whole
project is built to avoid.

---

## We're hiring: Communication Architect

**We don't read CVs. We read code.**

The technical work here is solid. The gap is communication: very few people outside the field know
this work exists, and even fewer can explain it clearly. We need someone who can sit with the actual
code and models, understand what they do and why they matter, and then produce content that makes a
developer, a trader, or a curious founder say: *"I didn't know this was possible."*

This is not a social media management role. It is a thinking role that sometimes outputs social media.

**There is no form to fill before you do the work. The challenge *is* the application.** Read the
repositories on this page (the model card, the package README, what the code actually does), then
write one piece that explains a single AION product to someone who has never heard of us. Under
~500 words, in whatever format you choose. That is the only CV we read.

We publish exactly what we weight, because transparency about evaluation criteria is part of how
AION works: **technical understanding** highest, then **strategic thinking**, then **communication
clarity**. Showing how you would automate your own work is a bonus signal, not a requirement.

A generic cover letter is an instant pass. A thoughtful piece of work is an invitation to a
conversation.

Remote. Output-based. The first engagement is a **paid trial** based on the challenge submission:
if the work is strong, the conversation continues from there. We especially welcome applicants from
underrepresented backgrounds; the challenge is the same for everyone, and the only thing we evaluate
is the work.

**→ [Read the full challenge and submit](https://aionanalytics.in/careers)**

---

## Research

Peer-reviewable work, published rather than asserted:

- *Contextual Intelligence: A Causal Layer for Country-Specific Decisions* ([SSRN](https://ssrn.com/abstract=7596079)), the architecture behind AION Indian Market Intelligence.
- *The Signature Trap: Structural Gaps in Spyware Detection and the Limits of Indicator-Based Defense* ([SSRN](https://ssrn.com/abstract=7503278))
- *The Uncodified Margin: Human Relational Intelligence as a Structural Complement to Algorithmic Systems in Five Emerging Markets* ([SSRN](https://ssrn.com/abstract=7235801))
- *Signal Provenance in Retail Algorithmic Trading: An Architectural Gap in SEBI's 2026 Framework and Its General Form* ([SSRN](https://ssrn.com/abstract=7118421))
- *The Great Indian Illusion: Unpacking the Gap Between Growth Statistics and Citizen Well-Being* ([SSRN](https://ssrn.com/abstract=6973958))
- *Asymmetric Multipolarity: Financial, Industrial, Resource, and Strategic Power in the Post-Unipolar Global Order* ([SSRN](https://ssrn.com/abstract=6449739))
- *Beyond the Mirror: Systemic Vulnerabilities in LLM Safeguards Exposed Through Intentional Conditioning* ([SSRN](https://ssrn.com/abstract=5232429))

→ [aion-research](https://github.com/AION-Analytics-India/aion-research) ·
[SSRN author page](https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=7415772) ·
[ORCID](https://orcid.org/0009-0000-7501-9230)

## How the work is governed

Evidence first, re-validate always, output over operator. Results ship with their failures visible:
a claim we cannot check is a claim we do not make.

We publish **what** a system does and **what** it returns. We do not publish how it is built.
Three provisional patent applications are filed (IN202621086466, signal-provenance capture; IN202621118523, AION Indian Market Intelligence governance loop; IN202621119269, AION Indian Market Intelligence classification engine). The methods are deliberately undocumented.
Research partners can request a technical briefing under confidentiality.

---

## Topics

Indian stock market · algorithmic trading · quantitative finance · probabilistic forecasting ·
calibrated uncertainty · market calendar · trading hours · exchange holidays · NSE · BSE · MCX ·
NIFTY 50 · BANK NIFTY · SENSEX · SEBI compliance · forensic accounting · anomaly detection ·
market intelligence API · macro event analysis · sector impact · MCP server · LLM tools ·
execution integrity · signal provenance · audit trail · chain of custody · Python · open source ·
NSE holidays 2026 · stock market holidays India · is NSE open today · news sentiment API India ·
financial news analysis · RBI policy impact · pre-open session · NIFTY opening range ·
red flags in annual reports · corporate governance · free legal information India · Hindi · Gujarati ·
Lithuanian income tax calculator · GPM skaičiuoklė · Lithuanian public holidays · business days ·
Nasdaq Vilnius · India · Lithuania

## Identity

**AION Analytics (India)**, founded by Lokesh Gupta, is an independent India-based deep-tech
research and infrastructure company.

It is **not** Aion Analytics LLC (United States). It is **not** AION Labs (Israel). It is **not**
Polymathic's AION (astronomy). These are separate and unaffiliated organisations that share a name.

- Website: <https://aionanalytics.in/>
- LinkedIn: <https://www.linkedin.com/company/aion-analytics-india/>
- Machine-readable identity: <https://aionanalytics.in/llms.txt>
- Hugging Face: <https://huggingface.co/aion-analytics-india>
- X: [@aion_analytics_](https://x.com/aion_analytics_)
- YouTube: <https://www.youtube.com/@aionanalytics>
- Telegram: <https://t.me/+VXWCiDgZjBI3ZjA1>
- Discord: <https://discord.gg/Dk9Pjc9cVa>
- Instagram: <https://www.instagram.com/aion_analytics/>
- Threads: <https://www.threads.com/@aion_analytics>

---

*Content is for educational and research purposes only. Not investment advice. AION Analytics (India)
is not a SEBI-registered Research Analyst or Investment Adviser. Download figures are reported
directly by PyPI.*
