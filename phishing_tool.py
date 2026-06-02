import email
from email import policy
from email.parser import BytesParser
import dns.resolver
import requests
import re
import os
import json

VT_API_KEY = "YOUR_API_KEY"
SAMPLES_DIR = "samples/"
OUTPUT_FILE = "output.json"


def parse_email(file_path):
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    return {
        "from": msg.get("From"),
        "subject": msg.get("Subject"),
        "return_path": msg.get("Return-Path"),
        "headers": dict(msg.items()),
        "body": get_body(msg)
    }


def get_body(msg):
    try:
        return msg.get_body(preferencelist=('html', 'plain')).get_content()
    except:
        return ""


def extract_domain(email_field):
    if not email_field:
        return None
    match = re.search(r'@([a-zA-Z0-9.-]+)', email_field)
    return match.group(1).lower() if match else None


def extract_links(text):
    if not text:
        return []
    return re.findall(r'https?://[^\s"<>()]+', text)


def check_spf(domain):
    try:
        answers = dns.resolver.resolve(domain, "TXT")
        for r in answers:
            if "v=spf1" in r.to_text():
                return True
    except:
        pass
    return False


def check_dkim(headers):
    dkim_header = headers.get("DKIM-Signature")
    if not dkim_header:
        return False
    return "d=" in dkim_header


def check_domain_vt(domain):
    if not domain:
        return None

    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {"x-apikey": VT_API_KEY}

    try:
        res = requests.get(url, headers=headers)
        data = res.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]

        return {
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0)
        }
    except:
        return None


def is_lookalike_domain(domain):
    legit = "equitybank.co.ke"

    if not domain:
        return False

    if domain == legit:
        return False

    if "equitybank" in domain:
        return True

    return False


def analyze(parsed, spf, dkim, vt):
    from_domain = extract_domain(parsed["from"])
    return_domain = extract_domain(parsed["return_path"])
    links = extract_links(parsed["body"])

    score = 0
    flags = []

    if is_lookalike_domain(from_domain):
        score += 3
        flags.append("Lookalike domain")

    if from_domain and return_domain and from_domain != return_domain:
        score += 2
        flags.append("Domain mismatch")

    if not spf:
        score += 1
        flags.append("SPF fail")

    if not dkim:
        score += 1
        flags.append("DKIM missing")

    if vt and vt["malicious"] > 0:
        score += 3
        flags.append("Malicious domain (VT)")

    body = (parsed["body"] or "").lower()
    if any(x in body for x in ["equity", "verify", "login", "account"]):
        score += 2
        flags.append("Phishing language")

    for link in links:
        if "equitybank.co.ke" not in link:
            score += 2
            flags.append(f"Suspicious link: {link}")

    verdict = "CLEAN"
    if score >= 6:
        verdict = "MALICIOUS"
    elif score >= 3:
        verdict = "SUSPICIOUS"

    return {
        "score": score,
        "flags": flags,
        "verdict": verdict,
        "links": links
    }


def main():
    for file in os.listdir(SAMPLES_DIR):
        path = os.path.join(SAMPLES_DIR, file)

        print(f"\n--- Analyzing: {file} ---")

        parsed = parse_email(path)
        domain = extract_domain(parsed["from"])

        spf = check_spf(domain)
        dkim = check_dkim(parsed["headers"])
        vt = check_domain_vt(domain)

        result = analyze(parsed, spf, dkim, vt)

        print(f"From: {parsed['from']}")
        print(f"Subject: {parsed['subject']}")
        print(f"Result: {result}")

        # 🔥 SAVE TO JSON
        log_entry = {
            "file": file,
            "from": parsed["from"],
            "subject": parsed["subject"],
            "spf": spf,
            "dkim": dkim,
            "analysis": result
        }

        with open(OUTPUT_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")


if __name__ == "__main__":
    main()