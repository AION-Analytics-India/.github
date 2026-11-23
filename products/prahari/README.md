# AION Prahari · India

**An Android personal-data privacy and device-security assessment pilot.**

[Product page](https://aionanalytics.in/models/prahari) · [Comparison and sources](COMPARISON.md) · [Diagrams](../DIAGRAMS.md) · [Publication status](../PUBLICATION_MANIFEST.md) · [Sargas (LT / EN)](../sargas/README.md)

## What individuals can use it for

- Review registered accessibility services and device administrators, particularly unfamiliar services with powerful access.
- Enable the optional local DNS filter to refuse listed domains and review local **blocked requests**. Keep or selectively allow an individual domain.
- Investigate an Android diagnostic report with available known spyware/security indicators and identify which checks were not possible.
- Follow explanations to Android settings and decide whether to change access or uninstall an app.

**Important:** a service's registration does not establish abuse. The DNS block log does not identify the requesting app. A negative diagnostic cannot rule out spyware. The comprehensive per-app contacts, messages, microphone, camera, files and location permission inventory is not yet validated.

## Why India needs more specific public guidance

CERT-In documented a March 17, 2026 campaign distributing fake RTO/e-Challan Android APKs, including malicious apps impersonating government notices. The campaign targeted sensitive financial information. The advisory recommends avoiding untrusted APKs, reviewing powerful permissions and enabling Google Play Protect. **There is no evidence in this documentation that Prahari detects the named malware.**

[Read CERT-In advisory](https://www.cert-in.org.in/s2cMainServlet?CACODE=CICA-2026-3492&pageid=PUBADV01).

Example: someone receives a purported challan APK in a messaging app. The safe workflow is to verify the challan through the official government service, avoid installing the file, keep Android updated, and examine access settings. Prahari's existing observations can supplement that workflow, **not replace it**.

## Why institutions might evaluate it

A field team, bank, retailer or professional-services organisation may need consistent assessment of Android devices accessing work systems. The product currently shows a **synthetic** institutional location-integrity demonstration, not a deployed workforce-monitoring system. Any future organisation view must be scoped to necessary findings, with a lawful basis and safeguards for personal devices. No fleet dashboard, MDM integration or employee activity capture has been validated.

## Planned prices (checkout not enabled)

**Essential:** Free. **Personal:** ₹499/year, one Android device. **Family:** ₹999/year, up to three devices. The paid feature split and renewal model depend on real-phone validation, licensing and consumer terms. The current website accepts controlled pilot enquiries.

## Known constraints

Android's VPN permission is required for the optional filter; another VPN or specified Private DNS may block this mode. DNS-only blocking cannot inspect message contents or attribute a request to an app. Android does not allow ordinary apps to enforce root prevention. Detection sensitivity and false-positive rate against real spyware have not been measured.

[Compare with existing tools](COMPARISON.md) · [View diagrams](../DIAGRAMS.md) · [Request pilot](https://aionanalytics.in/models/prahari#pilot)
