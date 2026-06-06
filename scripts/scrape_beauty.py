import urllib.request
import urllib.parse
import re
import ssl
import json
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

queries = {
    "Lakme Absolute Foundation": "foundation_lakme.jpg",
    "Huda Beauty Nude Eyeshadow Palette": "palette_huda.jpg",
    "L'Oréal Paris Revitalift Serum": "serum_loreal.jpg",
    "MAC Matte Lipstick Ruby Woo": "lipstick_ruby.jpg",
    "Clinique Moisture Surge": "moisture_clinique.jpg",
    "Estee Lauder Night Repair": "night_repair.jpg",
    "Fenty Beauty Gloss Bomb": "gloss_fenty.jpg",
    "Anastasia Beverly Hills Brow Wiz": "brow_abh.jpg"
}

for q, filename in queries.items():
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(q + ' product isolated white background')}&form=HDRSC2&first=1"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})
    try:
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        img_url = None
        match = re.search(r'murl&quot;:&quot;(.*?)&quot;', html)
        if match:
            img_url = match.group(1)
        else:
            match2 = re.search(r'm="([^"]*murl[^"]*)"', html)
            if match2:
                import html as h
                data = h.unescape(match2.group(1))
                m = re.search(r'"murl":"(.*?)"', data)
                if m:
                    img_url = m.group(1)
        
        if img_url:
            print(f"Found {q} at {img_url}")
            try:
                img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                data = urllib.request.urlopen(img_req, context=ctx, timeout=10).read()
                with open(f"static/{filename}", "wb") as f:
                    f.write(data)
                print(f"-> Saved to static/{filename}")
            except Exception as e:
                print(f"Failed to download image for {q}: {e}")
        else:
            print(f"Not found for {q}")
    except Exception as e:
        print(f"Error {q}: {e}")
    time.sleep(1)
