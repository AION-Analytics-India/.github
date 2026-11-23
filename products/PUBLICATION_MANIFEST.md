# Publication and claim-status register

**Review date:** 2026-11-23. **Current canonical documentation:** [GitHub organisation public mobile-privacy catalogue](https://github.com/AION-Analytics-India/.github/tree/main/products/). This is a documentation-only interim location, **not** either requested independent product repository. The private `AION-Analytics/sovereign-sentinel` repository has not been published.

## Live-publication receipts and verification levels

Verification labels:
- **Independent readback:** this register's maintainer retrieved the public surface or a relevant public file.
- **Agent receipt:** the website/publishing agent reported a successful deployment, commit or test, but that exact assertion was not independently reproduced here.
- **Pending:** the result was not demonstrated.

| Surface | Public URL | Status and evidence |
| --- | --- | --- |
| Prahari (India) | https://aionanalytics.in/models/prahari | **Independent readback 2026-11-23:** personal and institutional uses, India-specific CERT-In example, comparisons, proposed ₹499 / ₹999 plans and free pilot limitations |
| Sargas (Lithuanian) | https://aionanalytics.in/models/sargas | **Independent readback 2026-11-23:** Lithuanian content, explicit limitations, proposed €14.99 / €34.99 annual plans, no paid checkout |
| Sargas (English) | https://aionanalytics.in/models/sargas/en | **Independent readback 2026-11-23:** matching English pricing and release caveats |
| Sovereign Sentinel family | https://aionanalytics.in/models/sovereign-sentinel | **Independent readback 2026-11-23:** regional overview and links to both editions |
| Model registry | https://aionanalytics.in/models | **Independent readback 2026-11-23:** Prahari and Sargas discoverable in pilot section and menu |
| DEV Community | https://dev.to/aion-analytics-in/what-can-an-android-phone-tell-you-about-privacy-a-guide-for-phone-owners-and-institutions-39jl | **Independent readback 2026-11-23:** article published under AION Analytics (India), visible in organisation listing. **Agent receipt:** article ID `5097651`, full approved Markdown verified |
| Hugging Face documentation | https://huggingface.co/spaces/aion-analytics-india/README | **Independent readback 2026-11-23:** organisation card links to Prahari/Sargas docs; Prahari README and original publication manifest accessible; the file page displays revision `4fdc50c`. **Agent receipt:** full revision `4fdc50c44a5d`, all 10 files verified |
| GitLab documentation | https://gitlab.com/aion-analytics-india/mobile-privacy-security | **Agent receipt:** public project, 9 files, revision `9f369193ae09`; independent file readback unavailable through current web access |
| GitHub documentation | https://github.com/AION-Analytics-India/.github/tree/main/products | **Independently read and updated.** Active `main` is the living publication register, not the immutable original mirror snapshot |
| Dedicated Prahari repository | https://github.com/AION-Analytics-India/aion-prahari | **Pending:** separate repo not created through this GitHub connection |
| Dedicated Sargas repository | https://github.com/AION-Analytics-India/aion-sargas | **Pending:** separate repo not created through this GitHub connection |

The website agent reports **website commit** `5f4f3a7b789e442b354ae43073a8d844ae4cd0e3`, **deployment** `frontend_mobile_commercial_20261123_104011`, 26 live page/device checks and six deployment smoke tests. These exact internal build/test records were **not independently inspected** from this connector. Website, privacy, terms and refund routing were agent-reported as deployed.

## Current prices and release status

| Region | Essential (planned) | Personal / 1 Android device | Family / up to 3 Android devices | Active billing? |
| --- | --- | --- | --- | --- |
| India · Prahari | Free | ₹499/year | ₹999/year | **No** |
| Lithuania · Sargas | Free | €14.99/year | €34.99/year | **No** |

Institutional evaluation and licensing are separate and individually contracted. The first **100 admitted users shared across both editions** are promised free pilot access. Pilot enrolment is **not automatic** on opening an email draft; sent email, inbox delivery and admission remain unverified. The public pages do not collect payment details or promise automatic paid conversion.

## Claims supported and not supported

| Claim | Publication-safe treatment | Validation still needed |
| --- | --- | --- |
| Android privileged accessibility and device-administrator inspection | Development-build feature reported on product pages | Hardware and Android version coverage |
| Optional active DNS-domain filtering and local refusal history | Development-build capability; only refused domains visible | VPN coexistence, Private DNS, IPv6, reboot, performance and false blocks |
| Known spyware indicators / diagnostic scan | Descriptive evidence-limited inspection, **not** a malware-free guarantee | Confirmed real-spyware dataset, false positives and detection accuracy |
| Historical count comparisons and finding correlations | Development tests passed, **physical-phone validation outstanding** | End-to-end device testing with reproducible receipts |
| Sensitive contacts/SMS/location/microphone/camera/files permission inventory by app | **Not shipped in documented pilot** | Implement under Android visibility/policy restrictions and validate |
| DNS requester-to-app attribution | **Not supported** in existing refusal history | Do not claim until measured capability exists |
| Institutional location example | **Synthetic records** only | Consent/lawful basis, actual deployment and organisational data minimisation |
| Fleet dashboard, MDM, SSO, automated employee enforcement | **Not validated** | Separate enterprise design and customer acceptance |

## Release and cross-platform parity

- **Website:** user-facing source of product availability and prices.
- **GitHub:** living public documentation and evidence/status register; the earlier source document [DEVTO_DRAFT.md](DEVTO_DRAFT.md) is a **historical, unpublished draft**, not the expanded DEV article that was published.
- **Hugging Face / GitLab:** the agent mirrored the *original* GitHub documentation snapshot. Their retained original register can therefore accurately describe the **state before** cross-platform publication. Do not treat that snapshot's old "unpublished" lines as present-day status.
- **DEV:** a separately expanded article is live; its title and full text **differ from the earlier GitHub draft**. Do not claim byte-identical parity between them. [Published article](https://dev.to/aion-analytics-in/what-can-an-android-phone-tell-you-about-privacy-a-guide-for-phone-owners-and-institutions-39jl).
- A future mirror refresh should publish a dated sync receipt with commit SHA, path list and SHA-256 content matches; **semantic consistency is supported**, but byte-for-byte parity across all public platforms is **not independently demonstrated**.

## Remaining acceptance gates

1. Physical-phone testing of historical comparisons, diagnostics, VPN compatibility and network observations, with actual hardware / Android versions.
2. Per-app sensitive-permission inventory design, implementation and evidence. Do not imply permissions were *used* when only *granted*.
3. Native Lithuanian-language editorial sign-off.
4. Verify pilot inbox delivery, handling, confirmation and admission accounting; do not claim a queue or subscription from an email draft.
5. Paid release gates: malware-performance evidence, app distribution/store approval, licences, support, taxes, privacy terms, refunds, and a clear paid-vs-free feature split.
6. Separate public documentation repositories `aion-prahari` and `aion-sargas`, if still required. Keep proprietary Android code private unless explicitly approved.
7. Mirror publication of any revised canonical docs to Hugging Face and GitLab with independent revision-level readbacks.

**Security statement:** GitHub publication, agent smoke tests and a public article do not certify Android security efficacy or establish enterprise readiness.
