#!/usr/bin/env python3
import subprocess, json, time
import sys

# translation mapping
translation = {
    '0':'f','1':'e','2':'d','3':'c','4':'b','5':'a',
    '6':'9','7':'8','8':'7','9':'6',
    'a':'5','b':'4','c':'3','d':'2','e':'1','f':'0'
}

def translate_preserve_5g(s):
    parts = s.split("_5G")
    translated = []
    for i, part in enumerate(parts):
        t = ''.join(translation.get(ch.lower(), ch) for ch in part)
        translated.append(t)
        if i != len(parts)-1:
            translated.append("_5G")
    return ''.join(translated)

def scan_once():
    try:
        output = subprocess.check_output(["termux-wifi-scaninfo"], text=True)
        return json.loads(output)
    except Exception:
        return []

def print_table(seen, info):
    print(f"{'SSID':<35} {'Signal':>7}  {'Translated name'}")
    print("-"*70)
    for ssid in seen:
        strength = info.get(ssid, {}).get("level", "?")
        base = ssid[3:]
        translated = translate_preserve_5g(base)
        print(f"{ssid:<35} {str(strength):>7}  wlan{translated}")

def main():
    print("🔍 Scanning for Wi-Fi networks (30 seconds, updates every 5 seconds)...\n")
    seen = []
    info = {}
    start = time.time()
    printed_lines = 0

    while time.time() - start < 30:
        nets = scan_once()
        for n in nets:
            ssid = n.get("ssid", "")
            if ssid.startswith("fh_") and ssid not in seen:
                seen.append(ssid)
                info[ssid] = n

        if seen:
            # Move cursor up to overwrite previous table
            if printed_lines > 0:
                sys.stdout.write(f"\033[{printed_lines}A")
            print_table(seen, info)
            printed_lines = len(seen) + 2  # header + separator + rows
        else:
            print("⚠️ No 'fh_' networks found yet...")
            printed_lines = 1

        print("\n")  # space before next scan
        time.sleep(5)

if __name__ == "__main__":
    main()
