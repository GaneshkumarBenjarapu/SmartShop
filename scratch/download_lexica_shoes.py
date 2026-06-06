import urllib.request
import json
import os

d = 'frontend/static/shoes'
os.makedirs(d, exist_ok=True)

queries = [
    ("Red Tape Running Shoes 12", "red running shoe high quality"),
    ("Nike Performance Shoes 21", "blue athletic sneaker professional"),
    ("Skechers Athletic Footwear 58", "green sports shoe"),
    ("Skechers Casual Kicks 70", "yellow casual sneaker"),
    ("Skechers Walking Sneakers 52", "purple walking shoe"),
    ("Skechers Go Walk Shoes", "black sleek walking shoe"),
    ("Red Tape Men's Walking Shoes", "orange men sneaker"),
    ("Nike Running Shoes 97", "neon running shoe white background")
]

for name, q in queries:
    url = f"https://lexica.art/api/v1/search?q={urllib.parse.quote(q)}"
    fname = name.lower().replace(' ', '_').replace("'", "") + "_lex.png"
    fpath = os.path.join(d, fname)
    
    try:
        print(f"Searching Lexica for {name} ({q})...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as res:
            data = json.loads(res.read().decode())
            if data['images']:
                img_url = data['images'][0]['src']
                print(f"Downloading {img_url}...")
                img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(img_req, timeout=15) as img_res, open(fpath, 'wb') as f_out:
                    f_out.write(img_res.read())
                print(f"Saved {name} to {fname}")
            else:
                print(f"No results for {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")
