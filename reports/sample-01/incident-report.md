# Incident Report: Phishing Email Analysis (Sample 01)

## Incident Overview
- **Analysis Date:** November 2022 (sample email date)
- **Detection Vector:** Secure Email Gateway (SEG) automated filtering / Junk Mail placement
- **Attack Type:** Brand Impersonation & Credential Harvesting Pretext

--- MITRE ATT&CK Framework Mapping

| Tactic | ID | Technique | Description |
| :--- | :--- | :--- | :--- |
| **Initial Access** | **T1566.002** | Spearphishing Link | Sending emails with malicious links or call-to-action buttons (e.g., "Report The User") directing victims to external domains. |
| **Credential Access** | **T1589.001** | Gather Victim Identity Information: Credentials | Attempting to harvest corporate or personal authentication material through fake security warnings. |
| **Reconnaissance** | **T1598.003** | Phishing for Information | Using social engineering pretexts (fake geopolitical login alerts) to manipulate the user into compliance. |

---

## Technical Findings & Header Analysis

### 1. Authentication & Routing Anomalies
Analysis of the underlying SMTP `Received:` headers and authentication results revealed structural forgery:
* **SPF Result:** `None` (Sender IP `103.167.154.120` is unlisted in authorized sender policies).
* **DKIM Result:** `Fail` (Cryptographic signature verification failed due to missing or invalid public keys for domain `microsoft.com`).
* **DMARC Status:** `Fail` / `Action: Oreject` (The legitimate domain owner, Microsoft, enforces a strict `p=reject` DMARC policy, which triggered the mail filter to handle the unaligned message accordingly).

### 2. Social Engineering & Deceptive Elements
* **Header Discrepancy:** The `From` header was spoofed to mimic `Microsoft account team <no-reply@microsoft.com>`, whereas the `Reply-To` and action links redirected target interaction to an external, attacker-controlled domain (`usual-assist.com`).
* **Pretexting Strategy:** The message weaponized artificial urgency and fear by fabricating an unauthorized login event originating from Moscow, Russia, using Windows 10 / Firefox.
* **Evasion & Telemetry:** The payload included a hidden tracking pixel (`sefnet.net`) designed to confirm active email engagement, alongside HTML/CSS keyword stuffing intended to evade basic content filters.

---

## Indicators of Compromise (IOCs)
* **Sender IP:** `103.167.154.120`
* **Suspicious Reply-To Domain:** `usual-assist.com`
* **Tracking Pixel Domain:** `sefnet.net`

---

## Remediation & Hardening Recommendations
1. **Network & Gateway Blocking:** Blacklist the identified sender IP address and external domains (`usual-assist.com`, `sefnet.net`) at the Secure Email Gateway (SEG).
2. **Security Awareness Training:** Conduct targeted phishing simulations focusing on brand spoofing, urgent geographic-alert pretexts, and verifying discrepancies between `From` and `Reply-To` fields.
3. **Enterprise Policy Enforcement:** Ensure internal organization domains maintain strict DMARC enforcement policies (`p=reject`) to protect against brand impersonation.
