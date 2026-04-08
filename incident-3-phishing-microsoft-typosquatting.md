# 🚨 Incident Report: Phishing Email – Suspicious Microsoft Login Alert

## 🧾 Incident Overview
An inbound email was flagged for containing a suspicious external link and potential phishing characteristics. The email impersonates Microsoft and attempts to trick the user into clicking a malicious link.

---

## 📅 Date & Time
27 March 2026, 17:09 UTC

---

## 🎯 Alert Details
- **Alert Type:** Phishing Email  
- **Severity:** Medium  
- **Data Source:** Email Security System  

---

## 🌐 Affected Entities
- **Sender:** no-reply@m1crosoftsupport.co  
- **Recipient:** c.allen@thetrydaily.thm  
- **Subject:** Unusual Sign-In Activity on Your Microsoft Account  
- **Malicious URL:** https://m1crosoftsupport.co/login  
- **Direction:** Inbound  

---

## 🧠 Investigation & Analysis

### 1. Sender Analysis
- The sender domain **m1crosoftsupport.co** is suspicious  
- Uses **typosquatting** (“m1crosoft” instead of “microsoft”)  
- Not an official Microsoft domain  

### 2. Email Content Review
- Claims “unusual sign-in attempt” to create urgency  
- Includes:
  - Location: Lagos, Nigeria  
  - IP Address: 102.89.222.143  
- Uses fear-based language to prompt immediate action  

### 3. URL Analysis
- Embedded link redirects to a fake login page  
- Domain is not owned by Microsoft  
- Likely intended to steal user credentials  

### 4. Threat Assessment
- Classic phishing attempt:
  - Impersonation of trusted brand  
  - Malicious external link  
  - Social engineering tactics  

---

## ⚠️ Indicators of Compromise (IOCs)
- **Malicious Domain:** m1crosoftsupport.co  
- **Phishing URL:** https://m1crosoftsupport.co/login  
- **Suspicious IP (claimed):** 102.89.222.143  

---

## 🧪 MITIGATION / RESPONSE ACTIONS
- Email identified and flagged as phishing  
- User advised not to click the link  
- Domain flagged for blocking/monitoring  
- Incident escalated for further review  

---

## 🚨 Incident Classification
**True Positive**

### 📝 Justification:
- Domain impersonation (typosquatting) detected  
- Presence of malicious phishing link  
- Social engineering techniques used  
- Not a legitimate Microsoft communication  

---

## ⬆️ Escalation Decision
**Escalated**

### Reason:
- High likelihood of credential harvesting  
- Potential risk to user accounts  
- Requires organization-wide awareness and blocking  

---

## 🔧 Recommended Remediation
- Block the domain **m1crosoftsupport.co** at firewall/email gateway  
- Educate user on phishing awareness  
- Scan affected endpoint for suspicious activity  
- Reset user credentials if interaction occurred  
- Monitor for similar phishing campaigns  

---

## 📘 Lessons Learned
- Typosquatting domains are common in phishing attacks  
- Urgency and fear are key social engineering tactics  
- Always verify sender domains before interacting with emails  

---

## 📌 Lab Source
TryHackMe (SOC Simulation)
