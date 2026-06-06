import urllib.request
import urllib.parse
import re
import ssl
import json
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open('catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

women_products = [p for p in catalog if p.get('category') == 'Women Fashion']
used_urls = set()

for p in women_products:
    query = p["name"] + " product isolated white background"
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(query)}&form=HDRSC2&first=1"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    img_url = None
    try:
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        murls = []
        for match in re.finditer(r'murl&quot;:&quot;(.*?)&quot;', html):
            murls.append(match.group(1))
        
        import html as h
        for match2 in re.finditer(r'm="([^"]*murl[^"]*)"', html):
            data = h.unescape(match2.group(1))
            m = re.search(r'"murl":"(.*?)"', data)
            if m:
                murls.append(m.group(1))
        
        # find first unique url
        for u in murls:
            if u not in used_urls:
                img_url = u
                used_urls.add(u)
                break
                
        if img_url:
            print(f"[{p['id']}] Found {p['name']} at {img_url}")
            img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                data = urllib.request.urlopen(img_req, context=ctx, timeout=5).read()
                filename = f"women_fashion_{p['id']}.jpg"
                with open(f"static/{filename}", "wb") as f:
                    f.write(data)
                
                # Update the original catalog dict directly
                p['image'] = f"/static/{filename}"
                print(f"-> Saved to static/{filename}")
            except Exception as e:
                print(f"Failed to download image for {p['name']}: {e}")
        else:
            print(f"Not found unique image for {p['name']}")
    except Exception as e:
        print(f"Error {p['name']}: {e}")
        
    time.sleep(1)

with open('catalog.json', 'w', encoding='utf-8') as f:
    json.dump(catalog, f, indent=4)

print("Women Fashion update complete.")
