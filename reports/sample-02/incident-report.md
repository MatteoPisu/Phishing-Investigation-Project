# Incident Report: Sample 02 - Crypto-Drainer / Web3 Phishing

## 1. Incident Overview
* **Sample ID:** Sample 02
* **Threat Type:** Web3 Phishing / Crypto-Drainer
* **Impersonated Brand:** MetaMask
* **Detection Status:** Bypassed standard spam filters due to abused third-party bulk-mailing infrastructure; passed SPF and DKIM authentication.

---

## 2. Executive Summary
Sample 03 represents an advanced phishing vector targeting cryptocurrency holders. Rather than forging headers directly, the threat actor abused a legitimate third-party mass-marketing and newsletter platform (`anpdm.com`) to dispatch a fraudulent security alert. The email leverages severe urgency and fear tactics, claiming a user's wallet is blocked due to Ethereum network updates, and directs the victim to a malicious redirection link designed to harvest wallet credentials or private keys.

---

## 3. Email Header & Authentication Analysis
* **From Display Name:** `"MetaMask"`
* **Envelope Sender:** `3fd.c.1838003603.J151697800-32676051@innfactorholdningkommunal.anpdm.com`
* **Authentication Results:** 
  * **SPF:** `pass` (authorized via Apsis MTA)
  * **DKIM:** `pass` (`header.d=anpdm.com`)
  * **DMARC:** `none`
* **Analyst Note on Authentication:** While technical checks passed successfully, a deep-dive header review reveals a stark brand mismatch. The email claims to originate from MetaMask, but the structural infrastructure belongs to an unrelated Swedish municipal union (`kommunal.se`) and a commercial email service provider (Apsis). This proves that **passing email authentication does not guarantee legitimacy**.

---

## 4. Indicators of Compromise (IOCs)
* **Sender IP Address:** `91.227.208.158` (Apsis MTA / `rs-158.mta.anpdm.com`)
  * *Threat Intelligence Note:* Evaluates as clean or neutral on reputation databases like AbuseIPDB because it belongs to a legitimate commercial mail server. This highlights how actors abuse trusted infrastructure to evade IP-based blocking.
* **Phishing / Redirect Domain:** `one-lnk.com`
  * *Associated Payload URL:* Found embedded in the "Press here to Upgrade" button, routing victims through tracking/redirect links to a malicious Web3 wallet-drainer landing page.

---

## 5. MITRE ATT&CK Mapping
* **T1566.002 (Phishing: Spearphishing Link):** Delivering a malicious redirect URL within the email body.
* **T1583.001 (Acquire Infrastructure: Domains / Mail Relays):** Abusing existing third-party marketing platforms to distribute fraudulent content with high deliverability.
* **T1589.002 (Gather Victim Identity Information: Email Addresses):** Leveraging subscriber/mailing distribution lists for targeted asset theft.

---

## 6. Remediation & Recommendations
1. **URL Filtering:** Ensure network-level blocks are active for identified redirect domains (`one-lnk.com`).
2. **User Education:** Train employees and users to recognize that legitimate cryptocurrency platforms never request manual wallet updates via email links or threaten permanent loss of funds under tight deadlines.
3. **Advanced Email Security:** Implement behavioral and contextual email analysis tools that flag brand-to-domain discrepancies, even when baseline SPF/DKIM checks pass.
