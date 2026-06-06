import urllib.request
import os
import json

d = 'frontend/static/toys_v4'
os.makedirs(d, exist_ok=True)

# 18 distinct, high-quality, professional toy photos from Unsplash
toy_mappings = {
    173: "1623694483110-3b036575187e",
    174: "1585366119957-8073e8b70ca3",
    175: "1510070112810-d4e9a46d9e91",
    176: "1611996575749-74d3c332aaee",
    178: "1611891487122-207579d67d98",
    180: "1596464673641-f67fceba9d9c",
    181: "1591994843349-f41270158f94",
    183: "1511884642898-4c92249e20b6",
    184: "1595152230353-8326e6d1e4e4",
    185: "1581235720704-06d31ceb3ebf",
    187: "1586522510164-9b24af1ddb06",
    188: "1559440666-3d2319f3957a",
    189: "1615486511484-92e172cc4fe0",
    190: "1594731802114-173873495079",
    191: "1581092160562-40aa08e78837",
    192: "1516280440614-37939bbacd81",
    193: "1594122611112-964673bc8a77",
    194: "1519892300165-cb5542fb47c7"
}

def download_images():
    for pid, photo_id in toy_mappings.items():
        fname = f"toy_{pid}_v4.png"
        fpath = os.path.join(d, fname)
        url = f"https://images.unsplash.com/photo-{photo_id}?q=80&w=1000&auto=format&fit=crop"
        
        try:
            print(f"Downloading Unsplash image for toy {pid}...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as res, open(fpath, 'wb') as f_out:
                f_out.write(res.read())
            print(f"Saved {fname}")
        except Exception as e:
            print(f"Failed {pid}: {e}")

def update_catalog():
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for p in data:
        if p.get('id') in toy_mappings:
            p['image'] = f"/static/toys_v4/toy_{p['id']}_v4.png"

    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("Catalog updated with local Unsplash paths.")

if __name__ == '__main__':
    download_images()
    update_catalog()
