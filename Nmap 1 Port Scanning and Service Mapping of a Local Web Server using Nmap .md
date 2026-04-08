# 🔍 Network Reconnaissance and Service Enumeration Using Nmap




## 📌 Objective

The objective of this project was to simulate a real-world network reconnaissance scenario by identifying open ports, running services, and potential attack surfaces on a target system using Nmap.

---

## 🖥️ Lab Environment

* Attacker Machine: Ubuntu Linux (VirtualBox)
* Target Machine: Localhost (Python HTTP Server)
* Network Type: Host-only / NAT
* Tools Used: Nmap, Python3 (http.server)

---

## ⚙️ Methodology

### 🔹 Phase 1: Setup

Installed Nmap and verified installation:

```bash
nmap --version
```

Started HTTP server:

```bash
python3 -m http.server 80
```

---

### 🔹 Phase 2: Host Discovery

```bash
nmap -sn 127.0.0.1
```

Explanation:
Confirmed that the target system is live and reachable.

---

### 🔹 Phase 3: Port Scanning

```bash
nmap 127.0.0.1
nmap -p 1-1000 127.0.0.1
nmap -p- 127.0.0.1
```

Explanation:
Default scan checks common ports.
Full scan checks all 65535 ports.
This helps identify hidden or uncommon services.

---

### 🔹 Phase 4: Service Enumeration

```bash
nmap -sV 127.0.0.1
```

Explanation:
Detected running services and identified their versions.

---

### 🔹 Phase 5: Output & Reporting

```bash
nmap -oN scan.txt 127.0.0.1
nmap -oX scan.xml 127.0.0.1
nmap -oG scan.grep 127.0.0.1
```

Explanation:
-oN: Human-readable output
-oX: XML format for automation and tools
-oG: Grepable format for parsing

---

## 📊 Analysis

The scan revealed that port 80 was open, indicating a web service running on the target system. This represents a potential attack surface, as web servers are common entry points for attackers if misconfigured or unpatched.

---

## ⚠️ Security Implications

* Open ports increase attack surface
* Service versions allow vulnerability matching
* Full scans reveal hidden services attackers may exploit

---

## 🛡️ Recommendations

* Close unnecessary ports
* Use firewalls (e.g., UFW)
* Perform regular vulnerability scanning
* Keep services updated and patched
* Monitor logs using SIEM tools

---

## ✅ Conclusion

This project demonstrated how Nmap can be used to identify open ports and services on a target system. The findings highlight the importance of minimizing exposed services and continuously monitoring network activity to reduce potential attack vectors.

---

## 🎯 MITRE ATT&CK Mapping

Technique: T1046 – Network Service Discovery

---

## 🧠 Attacker Mindset

An attacker could use this information to identify vulnerable services and attempt exploitation.




