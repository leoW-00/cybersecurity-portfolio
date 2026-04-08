# 🚨 Incident Report: Onboarding Email Alert (False Positive)

## 🧾 Incident Overview
An alert was triggered for a potentially suspicious inbound email containing an external link. Investigation confirmed that this was part of standard HR onboarding, not a malicious attempt.

---

## 📅 Date & Time
27 March 2026, 14:07 UTC

---

## 🎯 Alert Details
- **Alert Type:** Suspicious Email / Potential Phishing  
- **Severity:** Low  
- **Data Source:** Email Security System  

---

## 🌐 Affected Entities
- **Sender:** onboarding@hrconnex.thm  
- **Recipient:** j.garcia@thetrydaily.thm  
- **Subject:** Action Required: Finalize Your Onboarding Profile  
- **URL:** https://hrconnex.thm/onboarding/15400654060/j.garcia  
- **Direction:** Inbound  

---

## 🧠 Investigation & Analysis

### 1. Sender Verification
- Internal HR domain confirmed (hrconnex.thm)  
- No signs of spoofing or malicious activity  

### 2. URL Analysis
- Corporate onboarding link is consistent with standard workflows  
- No obfuscation or external redirect  

### 3. Email Content Review
- Content aligns with typical onboarding procedures  
- No attachments, no urgent threats, no social engineering detected  

### 4. Threat Assessment
- No indicators of compromise (IOCs) found  
- Likely a benign false positive due to presence of an external link  

---

## ⚠️ Indicators of Compromise (IOCs)
**None identified**

---

## 🧪 MITIGATION / RESPONSE ACTIONS
- Alert reviewed and confirmed benign  
- No containment or remediation required  

---

## 🚨 Incident Classification
**False Positive**

### 📝 Justification:
The email is a legitimate internal communication from HR. The alert was likely triggered because the email contains an external link, but all evidence shows normal business activity.  

---

## ⬆️ Escalation Decision
**No escalation required**

### Reason:
- No threat detected  
- Activity aligns with expected onboarding workflow  

---

## 🔧 Recommendations
- Consider adjusting email filtering rules to reduce false positives  
- Educate SOC analysts on normal HR processes to prevent unnecessary alerts  

---

## 📘 Lessons Learned
- False positives are common with automated email filters  
- Understanding internal processes prevents unnecessary escalations  
- Proper documentation helps maintain SOC efficiency  

---

## 📌 Lab Source
TryHackMe (SOC Simulation)
