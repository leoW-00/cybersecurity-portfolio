Cybersecurity Portfolio — Leonard Ndungu
Entry-level SOC Analyst portfolio showcasing hands-on work in SIEM log analysis, incident investigation, threat detection, network reconnaissance, packet analysis, and Python-based security automation.
> **Portfolio note:** Reports document lab exercises and simulated investigations unless explicitly stated otherwise. Testing was performed only in authorised lab environments.
Featured projects
Project	What it demonstrates	Report / source
Lazarus Group (Ronin) detection engineering	MITRE ATT&CK mapping, threat research, detection engineering	Open report
SOAR-style IOC enrichment	Threat intelligence enrichment, risk scoring, Python automation	Open report · Python tool
Phishing email analysis tool	Email parsing, header/domain analysis, IOC extraction	Python source · SIEM report
HTTP log analysis with Splunk	Web log investigation and suspicious activity analysis	Open report
SSH log analysis with Splunk	Authentication log analysis and investigation	Open report
SMTP log analysis with Splunk	Email traffic and mail-server log analysis	Open report
Project categories
1. SIEM and log analysis
HTTP log analysis using Splunk
SSH log analysis using Splunk
SMTP log analysis using Splunk
DNS report recovery note — the uploaded PDF was corrupted (1 byte) and has been excluded.
2. Threat detection and incident response
Lazarus Group / Ronin detection engineering
Incident 01 — Blacklisted URL
Incident 02 — Onboarding email false positive
Incident 03 — Microsoft typosquatting phishing
Incident 04 — Onboarding email false positive
Incident 05 — Amazon delivery phishing
Phishing email detection SIEM report
3. SOAR and security automation
IOC enrichment and threat scoring report
4. Network reconnaissance — Nmap
Project 01 — Port scanning and service mapping
Project 02 report
Project 03 report
Project 04 report
5. Network traffic analysis — Wireshark
Level 01 report
Level 03 report
Level 04 report
6. Python security tools
IOC enrichment tool
Phishing email analyser
Skills demonstrated
SIEM investigation and log analysis with Splunk
Alert triage, phishing analysis, and incident documentation
MITRE ATT&CK mapping and detection engineering
IOC enrichment and threat intelligence workflows
Network reconnaissance with Nmap and traffic analysis with Wireshark
Python scripting and security automation
Running the Python tools
Use Python 3. Install dependencies as needed (the phishing analyser uses third-party packages such as `requests` and `dnspython`). Never hard-code API credentials in source code. Configure credentials as environment variables before running `ioc_checker.py`:
`ABUSEIPDB_API_KEY`
`VIRUSTOTAL_API_KEY`
`SHODAN_API_KEY`
The IOC tool uses these environment variables and does not contain embedded API keys. API keys that were previously committed to a public repository should be revoked and replaced immediately.
Repository structure
```text
01-SIEM-AND-LOG-ANALYSIS/
02-THREAT-DETECTION-AND-INCIDENT-RESPONSE/
03-SOAR-AND-SECURITY-AUTOMATION/
04-NETWORK-RECONNAISSANCE/
05-NETWORK-TRAFFIC-ANALYSIS/
06-PYTHON-SECURITY-TOOLS/
```
---
Contact: See the profile linked to this GitHub account for professional contact details.
