import requests
import json
from datetime import datetime

# 🔑 PASTE YOUR API KEYS HERE
ABUSE_API = "503277fafe80243ab8fe6ca288b16734578ab88d76f16c33a260203833e23a01308f5e783ab04bc5"
VT_API = "88d4db69fc17aa7cd7fc10715a3f9a6f87ac51e0ef0966d20e90781ca4b504b7"
SHODAN_API = "SX1pjQwwM7DlmjK1O5hoVBFST1ssZgWA"

# 🎨 Simple colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def check_abuseipdb(ip):
    try:
        url = "https://api.abuseipdb.com/api/v2/check"
        headers = {"Key": ABUSE_API, "Accept": "application/json"}
        params = {"ipAddress": ip}
        r = requests.get(url, headers=headers, params=params).json()
        return r["data"]["abuseConfidenceScore"]
    except:
        return 0

def check_virustotal(ioc):
    try:
        # Try IP first
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ioc}"
        headers = {"x-apikey": VT_API}
        r = requests.get(url, headers=headers).json()
        stats = r["data"]["attributes"]["last_analysis_stats"]
        return stats["malicious"]
    except:
        return 0

def check_shodan(ip):
    try:
        url = f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API}"
        r = requests.get(url).json()
        return len(r.get("ports", []))
    except:
        return 0

def calculate_risk(abuse, vt, ports):
    score = (abuse * 0.5) + (vt * 10) + (ports * 2)

    # ✅ cap at 100
    score = min(score, 100)

    if score < 25:
        level = "LOW"
        color = GREEN
    elif score < 50:
        level = "MEDIUM"
        color = YELLOW
    elif score < 75:
        level = "HIGH"
        color = RED
    else:
        level = "EXTREME"
        color = RED

    return score, level, color

def save_report(data):
    filename = "ioc_report.json"
    with open(filename, "a") as f:
        f.write(json.dumps(data, indent=4))
        f.write("\n\n")

def main():
    ioc = input("Enter IP / Domain / Hash: ")

    print("\nChecking threat intelligence...\n")

    abuse = check_abuseipdb(ioc)
    vt = check_virustotal(ioc)
    ports = check_shodan(ioc)

    score, level, color = calculate_risk(abuse, vt, ports)

    report = {
        "IOC": ioc,
        "AbuseIPDB": abuse,
        "VirusTotal": vt,
        "Open Ports": ports,
        "Risk Score": score,
        "Risk Level": level,
        "Time": str(datetime.now())
    }

    print("===== REPORT =====")
    print(f"IOC: {ioc}")
    print(f"AbuseIPDB Score: {abuse}")
    print(f"VirusTotal Detections: {vt}")
    print(f"Open Ports: {ports}")

    print(f"\nFINAL RISK: {color}{level}{RESET} ({score}/100)")

    if level in ["HIGH", "EXTREME"]:
        print(f"{RED}⚠️ ACTION: Consider blocking this IOC{RESET}")

    # 💾 Save report
    save_report(report)

    print("\nReport saved to ioc_report.json")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
