# Android mobile-security comparison: evidence and boundaries

**Dated 23 November 2026.** This is a comparison of **documented capabilities**, not an independent efficacy ranking. AION's entries are based on current public pilot descriptions and reported development tests, not source-code audit or real-world spyware benchmarking.

| Question | Google Play Protect | Quick Heal Mobile Security | Sophos Intercept X Mobile | RethinkDNS + Firewall | AION Prahari / Sargas |
| --- | --- | --- | --- | --- | --- |
| Harmful app scanning | Yes, including install/periodic assessment [1] | Has mobile security scanning [3] | Mobile security scanning [4] | Not primary focus [5] | Known-indicator diagnostic; real spyware efficacy **not measured** [6] |
| Per-app sensitive permission overview | Android OS privacy controls; not compared as dedicated inventory [1] | Privacy Advisor [2] | Not assessed here | Not assessed here | **Incomplete**, reported review limited to powerful registrations [6] |
| Attribute a network request to a specific app | Not assessed here | Not assessed here | Not assessed here | Per-app connection logs [5] | **No**; refused DNS name alone cannot identify app [6] |
| Domain/network blocking | Not the product's documented primary role | Edition-dependent [3] | Network protection features; edition-dependent [4] | Yes, DNS/firewall [5] | Optional listed-domain DNS refusals; VPN/Private DNS limitations [6] |
| Accessibility / device-admin review | Android settings available | Advisor features [2] | Not assessed here | Not assessed here | Reported Android registrations review [6] |
| Compare privileged registrations over time | Not assessed here | Not assessed here | Not assessed here | Not assessed here | Development tests reported; real-phone acceptance **pending** [6] |
| Verified enterprise device management | Android Enterprise separate | Edition-dependent | Managed enterprise products exist [4] | Not assessed here | **Not verified**; institutional example uses synthetic records [6] |

“Not assessed here” **does not mean absent**. Marketing claims of technical superiority require same-device, same-threat test evidence and reproducible results; none is currently published. The reason to evaluate AION is the combination of owner-explainable evidence, local observation and region-specific guidance, **not** an asserted best-in-class detection score.

## References
1. [Google Play Protect](https://support.google.com/googleplay/answer/2812853?hl=en)
2. [Quick Heal Privacy Advisor](https://docs.quickheal.com/docs/quick-heal-mobile-security-24/features/privacy-protection/privacy-advisor/)
3. [Quick Heal Mobile Security documentation](https://docs.quickheal.com/)
4. [Sophos Intercept X for Mobile guide](https://support.home.sophos.com/hc/en-us/articles/360041259751-Sophos-Intercept-X-For-Mobile-Guide-for-Sophos-Home-customers)
5. [RethinkDNS Firewall](https://docs.rethinkdns.com/firewall/)
6. [AION Prahari product pilot](https://aionanalytics.in/models/prahari) and [Sargas LT](https://aionanalytics.in/models/sargas)
7. [Android VPN service](https://developer.android.com/reference/android/net/VpnService)
8. [Google Play app visibility policy](https://support.google.com/googleplay/android-developer/answer/10158779)

Sources are vendor/developer descriptions. This comparison is **not** a certification or measured malware detection test. Correct any mismatch using exact vendor documentation and date of inspection.
