# AION Prahari / Sargas: explanatory diagrams

**Conceptual documentation, not implementation proof.** Solid flows represent the workflows described on current public product pages. Dotted flows identify future designs that have **not** been verified in a production device/fleet.

## Individual device owner journey

~~~mermaid
flowchart TD
 A[Owner notices a concern] --> B{Which question?}
 B -->|Powerful access| C[Review reported accessibility and device admin registrations]
 B -->|Blocked destination| D[Inspect local DNS refusal history, if filter enabled]
 B -->|Possible infection| E[Run available known-indicator diagnostic]
 C --> F[Read observation, uncertainty and limits]
 D --> F
 E --> F
 F --> G[Owner chooses action in Android settings]
 G --> H[Keep Play Protect enabled; seek specialist help if needed]
~~~

## Layers and running modes

~~~mermaid
flowchart LR
 Owner[Android device owner] --> A[User-initiated privilege inspection]
 Owner --> B[Optional active DNS filter]
 Owner --> C[User-initiated diagnostic report]
 B --> D[Local blocked-domain history]
 A --> E[Owner-visible observations]
 C --> E
 D --> E
 E --> R[Guidance and chosen remediation]
 F[Future per-app sensitive permission inventory] -.-> E
~~~

## Institution and privacy boundary

~~~mermaid
flowchart TB
 subgraph Phone[Personal or organisation-owned device]
 A[Detailed local observations] --> B[Device owner sees findings]
 B --> C[Owner-controlled corrections]
 end
 subgraph Future[Not shipped: proposed institutional path]
 D[Minimised risk summary] --> E[Approved human reviewer]
 end
 B -.->|Requires lawful basis, policy and verified controls| D
 P[Personal messages, photos, contacts, browsing] -.->|No automatic export| E
~~~

## Reading a finding

~~~mermaid
flowchart TD
 A[Diagnostic check] --> B{Outcome}
 B -->|Indicator matched| C[Investigate; not a malware verdict]
 B -->|No indicator matched| D[Not detected by that check; not a guarantee]
 B -->|Not observable| E[Unknown, never treat as clean]
 C --> F[User or authorised specialist review]
 D --> F
 E --> F
~~~

**Accessibility note:** diagrams are accompanied by captions and text. The product does not prove which app exercised an Android permission, identify which app sent a refused DNS request, or guarantee all malware is detected.
