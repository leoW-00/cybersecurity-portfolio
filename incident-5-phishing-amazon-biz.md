# 🚨 Incident Report: Phishing Email – Amazon Package Scam

## 🧾 Incident Overview
An inbound email was flagged for containing a suspicious external link. The email impersonates Amazon delivery services and attempts to trick the recipient into clicking a malicious URL.

---

## 📅 Date & Time
27 March 2026, 17:06 UTC

---

## 🎯 Alert Details
- **Alert Type:** Phishing Email  
- **Severity:** Medium  
- **Data Source:** Email Security System  

---

## 🌐 Affected Entities
- **Sender:** urgents@amazon.biz  
- **Recipient:** h.harris@thetrydaily.thm  
- **Subject:** Your Amazon Package Couldn’t Be Delivered – Action Required  
- **Malicious URL:** http://bit.ly/3sHkX3da12340  
- **Direction:** Inbound  

---

## 🧠 Investigation & Analysis

### 1. Sender Analysis
- Sender domain `amazon.biz` is **not a legitimate Amazon domain**  
- Likely created to impersonate Amazon and bypass filters  

### 2. Email Content Review
- Claims “package couldn’t be delivered” to create urgency  
- Includes warning about returning the package within 48 hours  
- Encourages clicking a link to confirm shipping information  

### 3. URL Analysis
- Shortened URL (`bit.ly`) hides the final destination  
- Known tactic to deliver phishing/malware links  
- Checked in threat intel database → flagged as malicious  

### 4. Threat Assessment
- Classic phishing attempt using social engineering:  
  - Fear of lost package  
  - Urgency to click link  
- High likelihood of credential theft if link clicked  

---

## ⚠️ Indicators of Compromise (IOCs)
- **Malicious domain:** amazon.biz (spoofed)  
- **Phishing URL:** http://bit.ly/3sHkX3da12340  

---

## 🧪 MITIGATION / RESPONSE ACTIONS
- Email flagged and quarantined  
- User notified of phishing attempt  
- Malicious domain blocked at email gateway/firewall  
- Endpoint monitored for suspicious activity  

---

## 🚨 Incident Classification
**True Positive**

### 📝 Justification:
- Domain impersonation detected (amazon.biz vs amazon.com)  
- Shortened URL hides malicious destination  
- Social engineering and urgency tactics present  

---

## ⬆️ Escalation Decision
**Escalated**

### Reason:
- High risk of credential compromise  
- Requires organizational awareness and blocking  

---

## 🔧 Recommended Remediation
- Block the domain **amazon.biz** and related URLs  
- Train user on phishing awareness  
- Scan affected endpoints for suspicious activity  
- Monitor for similar phishing campaigns  

---

## 📘 Lessons Learned
- Shortened URLs are commonly used in phishing attacks  
- Social engineering exploits urgency and fear  
- SOC analysts must verify sender domains and URLs before interaction  

---

## 📌 Lab Source
TryHackMe (SOC Simulation)
