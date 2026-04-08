# 🚨 Incident Report: Suspicious Onboarding Email Alert

## 📅 Date & Time
27 March 2026, 14:01 UTC

---

## 🔍 Alert Summary
An alert was triggered for a potentially suspicious email containing a link. The email was reviewed to determine whether it was malicious or part of legitimate business activity.

---

## 📧 Affected Entities
- **Sender:** onboarding@hrconnex.thm  
- **Recipient:** j.garcia@thetrydaily.thm  
- **URL:** https://hrconnex.thm/onboarding/15400654060/j.garcia  
- **Data Source:** Email  

---

## 🧠 Investigation Process
- Analyzed the sender email address for legitimacy  
- Reviewed the domain **hrconnex.thm**, which appears to be an internal HR system  
- Examined the email context and purpose (employee onboarding)  
- Verified that the URL structure matches typical onboarding workflows  
- Checked for common phishing indicators:
  - No spoofed domain  
  - No suspicious attachments  
  - No urgency or social engineering tactics  

---

## 🛠 Tools & Techniques Used
- Email analysis (TryHackMe simulation)  
- Domain and URL inspection  
- Phishing indicator assessment  

---

## ⚠️ Indicators of Compromise (IOCs)
**None identified**

---

## 🚨 Incident Classification
**False Positive**

### Reason:
- Email originates from a legitimate internal domain  
- Content aligns with standard HR onboarding procedures  
- No signs of phishing, spoofing, or malicious intent  
- Alert likely triggered due to link presence rather than actual threat  

---

## 🛡 Response Actions Taken
- Alert reviewed and validated as benign  
- No containment or remediation required  

---

## 🔧 Recommended Actions
- No immediate action required  
- Fine-tune email filtering rules to reduce similar false positives  
- Continue monitoring for abnormal email patterns  

---

## 📘 Key Takeaways
- Not all alerts indicate malicious activity  
- Understanding normal business processes is critical in SOC analysis  
- Proper classification helps reduce alert fatigue  

---

## 📌 Lab Source
TryHackMe (SOC Simulation)
