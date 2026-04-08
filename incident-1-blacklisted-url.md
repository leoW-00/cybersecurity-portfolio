# 🚨 Incident Report: Access to Blacklisted URL

## 📅 Date & Time
27 March 2026, 14:05 UTC

---

## 🔍 Alert Summary
A user attempted to access a known blacklisted external URL. The request was successfully blocked by the firewall, preventing any outbound connection.

---

## 🌐 Affected Entities
- **Source IP:** 10.20.2.17  
- **Destination IP:** 67.199.248.11  
- **URL:** http://bit.ly/3sHkX3da12340  
- **Application:** Web Browsing  

---

## 🧠 Investigation Process
- Reviewed the alert triggered by the firewall for access to a blacklisted URL  
- Identified the use of a **URL shortener (bit.ly)**, commonly used to hide malicious destinations  
- Confirmed that the destination URL is flagged in threat intelligence feeds as suspicious/malicious  
- Verified that the firewall successfully **blocked the connection attempt**  
- Assessed the possibility of user exposure through phishing or malicious links  

---

## 🛠 Tools & Techniques Used
- SIEM alert monitoring (TryHackMe simulation)  
- Firewall log analysis  
- Threat intelligence awareness (blacklisted URLs, URL shorteners)  

---

## ⚠️ Indicators of Compromise (IOCs)
- Suspicious shortened URL: http://bit.ly/3sHkX3da12340  
- Destination IP: 67.199.248.11  

---

## 🚨 Incident Classification
**True Positive**

### Reason:
- The URL is confirmed as blacklisted  
- URL shortening service used to obscure destination  
- Matches common phishing/malware delivery techniques  

---

## ⬆️ Escalation Decision
**Yes — Escalated**

### Reason:
- Indicates potential phishing attempt or malicious user activity  
- User may have interacted with the link before it was blocked  
- Requires further endpoint and email investigation  

---

## 🛡 Response Actions Taken
- Firewall successfully blocked the request  
- Alert reviewed and confirmed as malicious  
- Incident escalated for further investigation  

---

## 🔧 Recommended Remediation
- Investigate the source host (10.20.2.17) for:
  - Malware infection  
  - Suspicious processes or downloads  
- Check email logs for phishing attempts targeting the user  
- Educate user on phishing awareness  
- Block or monitor related indicators across the network  

---

## 📘 Key Takeaways
- URL shorteners are commonly used to hide malicious links  
- Even blocked attempts can indicate deeper threats  
- Monitoring user behavior is critical in early threat detection  

---

## 📌 Lab Source
TryHackMe (SOC Simulation)
