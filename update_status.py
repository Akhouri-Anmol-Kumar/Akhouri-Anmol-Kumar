"""Reads the SAME number your website shows: downloads.json (API total across all repos + the 105 recovery offset),
written every 15 min by the website repo's workflow. Prints the total to stdout."""
import json, os, sys, time, urllib.request

URL = os.environ.get("DOWNLOADS_JSON_URL",
      "https://raw.githubusercontent.com/Akhouri-Anmol-Kumar/Akhouri-systems/main/downloads.json")

try:
    req = urllib.request.Request(f"{URL}?t={int(time.time())}", headers={"User-Agent": "akhouri-profile-bot", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=30) as r: data = json.load(r)
    total = int(data["total"])
    if total < 0: raise ValueError("negative total")
except Exception as e:
    print(f"FETCH FAILED: {e}", file=sys.stderr); sys.exit(1)

print(f"downloads.json -> total={total} updated={data.get('updated')}", file=sys.stderr)
print(total)
