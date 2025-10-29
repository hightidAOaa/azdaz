import subprocess
import time
import json
import re

# Translation map based on your image
translation_map = {
    '0': 'f', '1': 'e', '2': 'd', '3': 'c', '4': 'b', '5': 'a',
    '6': '9', '7': '8', '8': '7', '9': '6',
    'a': '5', 'b': '4', 'c': '3', 'd': '2', 'e': '1', 'f': '0'
}

def translate_string(s):
    """Translate characters using the provided mapping, but skip '_5G'."""
    if "_5G" in s:
        prefix, suffix = s.split("_5G", 1)
        translated_prefix = ''.join(translation_map.get(ch, ch) for ch in prefix)
        return translated_prefix + "_5G" + suffix
    else:
        return ''.join(translation_map.get(ch, ch) for ch in s)

def scan_wifi():
    """Use termux-api to scan Wi-Fi networks."""
    try:
        result = subprocess.check_output(["termux-wifi-scaninfo"], text=True)
        return json.loads(result)
    except subprocess.CalledProcessError:
        return []
    except json.JSONDecodeError:
        return []

def main():
    print("📡 Scanning for Wi-Fi networks for 30 seconds...\n")
    found_ssids = []
    start_time = time.time()

    while time.time() - start_time < 30:
        networks = scan_wifi()
        for net in networks:
            ssid = net.get("ssid", "")
            if ssid and ssid.startswith("fh_") and ssid not in found_ssids:
                found_ssids.append(ssid)
        time.sleep(5)  # wait before rescanning

    print(f"\n✅ Found {len(found_ssids)} matching networks:\n")
    print(f"{'Original Name':<30} | {'Translated Name'}")
    print("-" * 60)

    for ssid in found_ssids:
        part = ssid[3:]  # Remove 'fh_'
        translated = translate_string(part)
        print(f"{ssid:<30} | wlan{translated}")

if __name__ == "__main__":
    main()
