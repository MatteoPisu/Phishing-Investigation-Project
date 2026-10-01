# Phishing Investigation Project

A collection of simulated and real-world phishing analysis write-ups, email header investigations, and threat indicator tracking.

## Overview
This repository contains documentation and technical analysis for various email-based threats. Each case study breaks down:
* **Email Headers & Routing:** Identifying spoofed sender addresses, non-matching Return-Paths, and authentication failures (SPF, DKIM, DMARC).
* **Threat Indicators:** Spotting social engineering lures, obfuscated redirect links, and spam evasion techniques.
* **Remediation & Action Plan:** Recommended defensive measures, IP/domain blocklists, and user awareness strategies.

## Directory Structure
* `reports/` - Detailed Markdown reports for individual phishing investigations (e.g., brand impersonation, credential harvesting).
* `samples/` - Raw `.eml` files and sanitized email samples analyzed in the reports.
* `scripts/` - Python automation script for parsing `.eml` files and quickly checking SPF, DKIM, and DMARC statuses.
## Automation
After working through these email samples, I decided to try and build a python script that automates email header verification.
Here is what it does:
* **Interactive File Input:** Prompts you to input the local filepath to a raw `.eml` sample to begin parsing immediately.
* **Streamlined Triage:** Quickly extracts sender details and checks for **SPF**, **DKIM**, and **DMARC** statuses.
* **Efficiency Boost:** Eliminates the need for manual DNS lookups, speeding up the initial phase of email header analysis.

