[README.md](https://github.com/user-attachments/files/34366475/README.md)
# Cybersecurity Portfolio — Leonard Ndungu

Entry-level SOC Analyst portfolio showcasing hands-on work in SIEM log analysis, incident investigation, threat detection, network reconnaissance, packet analysis, and Python-based security automation.

> **Portfolio note:** Reports document lab exercises and simulated investigations unless explicitly stated otherwise. Testing was performed only in authorised lab environments.

## Featured projects

| Project | What it demonstrates | Report / source |
|---|---|---|
| Lazarus Group (Ronin) detection engineering | MITRE ATT&CK mapping, threat research, detection engineering | [Open report](02-THREAT-DETECTION-AND-INCIDENT-RESPONSE/Lazarus-Group-Ronin-Hack-Detection-Engineering.pdf) |
| SOAR-style IOC enrichment | Threat intelligence enrichment, risk scoring, Python automation | [Open report](03-SOAR-AND-SECURITY-AUTOMATION/IOC-Enrichment-and-Threat-Scoring-Report.pdf) · [Python tool](06-PYTHON-SECURITY-TOOLS/ioc_checker.py) |
| Phishing email analysis tool | Email parsing, header/domain analysis, IOC extraction | [Python source](06-PYTHON-SECURITY-TOOLS/phishing_email_analyser.py) · [SIEM report](02-THREAT-DETECTION-AND-INCIDENT-RESPONSE/Phishing-Email-Detection-Tool-SIEM-Report.pdf) |
| HTTP log analysis with Splunk | Web log investigation and suspicious activity analysis | [Open report](01-SIEM-AND-LOG-ANALYSIS/HTTP-Log-Analysis-Using-Splunk.pdf) |
| SSH log analysis with Splunk | Authentication log analysis and investigation | [Open report](01-SIEM-AND-LOG-ANALYSIS/SSH-Log-Analysis-Using-Splunk.pdf) |
| SMTP log analysis with Splunk | Email traffic and mail-server log analysis | [Open report](01-SIEM-AND-LOG-ANALYSIS/SMTP-Log-Analysis-Using-Splunk.pdf) |

## Project categories

### 1. SIEM and log analysis
- [HTTP log analysis using Splunk](01-SIEM-AND-LOG-ANALYSIS/HTTP-Log-Analysis-Using-Splunk.pdf)
- [SSH log analysis using Splunk](01-SIEM-AND-LOG-ANALYSIS/SSH-Log-Analysis-Using-Splunk.pdf)
- [SMTP log analysis using Splunk](01-SIEM-AND-LOG-ANALYSIS/SMTP-Log-Analysis-Using-Splunk.pdf)
- [DNS report recovery note](01-SIEM-AND-LOG-ANALYSIS/DNS-LOG-REPORT-RECOVERY-REQUIRED.md) — the uploaded PDF was corrupted (1 byte) and has been excluded.

### 2. Threat detection and incident response
- [Lazarus Group / Ronin detection engineering](02-THREAT-DETECTION-AND-INCIDENT-RESPONSE/Lazarus-Group-Ronin-Hack-Detection-Engineering.pdf)
- [Incident 01 — Blacklisted URL](02-THREAT-DETECTION-AND-INCIDENT-RESPONSE/Incident-01-Blacklisted-URL.md)
- [Incident 02 — Onboarding email false positive](02-THREAT-DETECTION-AND-INCIDENT-RESPONSE/Incident-02-Onboarding-Email-False-Positive.md)
- [Incident 03 — Microsoft typosquatting phishing](02-THREAT-DETECTION-AND-INCIDENT-RESPONSE/Incident-03-Microsoft-Typosquatting-Phishing.md)
- [Incident 04 — Onboarding email false positive](02-THREAT-DETECTION-AND-INCIDENT-RESPONSE/Incident-04-Onboarding-Email-False-Positive.md)
- [Incident 05 — Amazon delivery phishing](02-THREAT-DETECTION-AND-INCIDENT-RESPONSE/Incident-05-Amazon-Delivery-Phishing.md)
- [Phishing email detection SIEM report](02-THREAT-DETECTION-AND-INCIDENT-RESPONSE/Phishing-Email-Detection-Tool-SIEM-Report.pdf)

### 3. SOAR and security automation
- [IOC enrichment and threat scoring report](03-SOAR-AND-SECURITY-AUTOMATION/IOC-Enrichment-and-Threat-Scoring-Report.pdf)

### 4. Network reconnaissance — Nmap
- [Project 01 — Port scanning and service mapping](04-NETWORK-RECONNAISSANCE/Nmap-Project-01-Port-Scanning-and-Service-Mapping.md)
- [Project 02 report](04-NETWORK-RECONNAISSANCE/Nmap-Project-02-Report.pdf)
- [Project 03 report](04-NETWORK-RECONNAISSANCE/Nmap-Project-03-Report.pdf)
- [Project 04 report](04-NETWORK-RECONNAISSANCE/Nmap-Project-04-Report.pdf)

### 5. Network traffic analysis — Wireshark
- [Level 01 report](05-NETWORK-TRAFFIC-ANALYSIS/Wireshark-Level-01-Report.pdf)
- [Level 03 report](05-NETWORK-TRAFFIC-ANALYSIS/Wireshark-Level-03-Report.pdf)
- [Level 04 report](05-NETWORK-TRAFFIC-ANALYSIS/Wireshark-Level-04-Traffic-Analysis-Report.pdf)

### 6. Python security tools
- [IOC enrichment tool](06-PYTHON-SECURITY-TOOLS/ioc_checker.py)
- [Phishing email analyser](06-PYTHON-SECURITY-TOOLS/phishing_email_analyser.py)

## Skills demonstrated
- SIEM investigation and log analysis with Splunk
- Alert triage, phishing analysis, and incident documentation
- MITRE ATT&CK mapping and detection engineering
- IOC enrichment and threat intelligence workflows
- Network reconnaissance with Nmap and traffic analysis with Wireshark
- Python scripting and security automation

## Running the Python tools

Use Python 3. Install dependencies as needed (the phishing analyser uses third-party packages such as `requests` and `dnspython`). Never hard-code API credentials in source code. Configure credentials as environment variables before running `ioc_checker.py`:

- `ABUSEIPDB_API_KEY`
- `VIRUSTOTAL_API_KEY`
- `SHODAN_API_KEY`

The IOC tool uses these environment variables and does not contain embedded API keys. API keys that were previously committed to a public repository should be revoked and replaced immediately.

## Repository structure

```text
01-SIEM-AND-LOG-ANALYSIS/
02-THREAT-DETECTION-AND-INCIDENT-RESPONSE/
03-SOAR-AND-SECURITY-AUTOMATION/
04-NETWORK-RECONNAISSANCE/
05-NETWORK-TRAFFIC-ANALYSIS/
06-PYTHON-SECURITY-TOOLS/
```

---
**Contact:** See the profile linked to this GitHub account for professional contact details.
