import urllib.request
import urllib.parse
import re
import ssl
import json
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

queries = [
    "Samsung 28L Convection Microwave Oven",
    "Samsung 1.5 Ton 5 Star Inverter Split AC",
    "Samsung 6.5 kg Fully-Automatic Top Load",
    "LG 655 L Frost Free Side-by-Side Refrigerator",
    "LG 8 Kg 5 Star Front Load Washing Machine",
    "LG 1.5 Ton 5 Star AI DUAL Inverter AC",
    "LG 32 L Charcoal Convection Microwave",
    "LG 260 L 3 Star Frost Free Double Door",
    "Blue Star 1.5 Ton 3 Star Inverter Split AC",
    "Blue Star 1 Ton 4 Star Inverter Split AC",
    "Blue Star Water Purifier",
    "Blue Star 1.5 Ton Window AC",
    "Blue Star Portable Air Conditioner"
]

results = {}

for q in queries:
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(q)}&form=HDRSC2&first=1"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})
    try:
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        # Bing images often have m='{... "murl":"https://..." ...}'
        match = re.search(r'murl&quot;:&quot;(.*?)&quot;', html)
        if match:
            img_url = match.group(1)
            results[q] = img_url
            print(f"Found for {q}: {img_url}")
        else:
            match2 = re.search(r'm="([^"]*murl[^"]*)"', html)
            if match2:
                import html as h
                data = h.unescape(match2.group(1))
                m = re.search(r'"murl":"(.*?)"', data)
                if m:
                    img_url = m.group(1)
                    results[q] = img_url
                    print(f"Found for {q}: {img_url}")
            else:
                print(f"Not found for {q}")
    except Exception as e:
        print(f"Error {q}: {e}")
    time.sleep(1)

with open('scraped_images.json', 'w') as f:
    json.dump(results, f, indent=4)
