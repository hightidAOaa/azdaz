#!/usr/bin/env python3
import subprocess, json, time

# translation mapping
translation = {
    '0':'f','1':'e','2':'d','3':'c','4':'b','5':'a',
    '6':'9','7':'8','8':'7','9':'6',
    'a':'5','b':'4','c':'3','d':'2','e':'1','f':'0'
}

def translate_preserve_5g(s):
    """Translate string but leave '_5G' untouched."""
    parts = s.split("_5G")
    translated = []
    for i, part in enumerate(parts):
        t = ''.join(translation.get(ch.lower(), ch) for ch in part)
        translated.append(t)
        if i != len(parts)-1:
            translated.append("_5G")
    return ''.join(translated)

def scan_once():
    """Run one wifi scan via Termux API."""
    try:
        output = subprocess.check_output(["termux-wifi-scaninfo"], text=True)
        return json.loads(output)
    except Exception:
        return []

def main():
    print("🔍 Scanning for Wi-Fi networks (30 seconds)...\n")
    seen = []
    info = {}
    start = time.time()

    while time.time() - start < 30:
        nets = scan_once()
        for n in nets:
            ssid = n.get("ssid", "")
            if ssid.startswith("fh_") and ssid not in seen:
                seen.append(ssid)
                info[ssid] = n
        time.sleep(4)  # wait a bit between scans

    if not seen:
        print("⚠️  No 'fh_' networks found.")
        return

    print(f"{'SSID':<35} {'Signal':>7}  {'Translated name'}")
    print("-"*70)
    for ssid in seen:
        strength = info.get(ssid, {}).get("level", "?")
        base = ssid[3:]  # drop the 'fh_'
        translated = translate_preserve_5g(base)
        print(f"{ssid:<35} {str(strength):>7}  wlan{translated}")

if __name__ == "__main__":
    main()
