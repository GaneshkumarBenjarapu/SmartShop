import urllib.request
import os

d = 'frontend/static/toys_v3'
os.makedirs(d, exist_ok=True)

targets = [
    (173, 'uno_v3.png', '1623694483110-3b036575187e'),
    (174, 'lego_box_v3.png', '1585366119957-8073e8b70ca3'),
    (175, 'jenga_v3.png', '1510070112810-d4e9a46d9e91'),
    (176, 'connect4_v3.png', '1611996575749-74d3c332aaee'),
    (177, 'operation_v3.png', '1616514122113-1763134e7040'),
    (178, 'guesswho_v3.png', '1611891487122-207579d67d98'),
    (179, 'trouble_v3.png', '1566579633-b43d3dfc7cce'),
    (180, 'playdoh_v3.png', '1596464673641-f67fceba9d9c'),
    (181, 'rubiks_v3.png', '1591994843349-f41270158f94'),
    (182, 'battleship_v3.png', '1605342080315-9c9860477e7d'),
    (183, 'twister_v3.png', '1511884642898-4c92249e20b6'),
    (184, 'nerf_v3.png', '1595152230353-8326e6d1e4e4'),
    (185, 'hotwheels_v3.png', '1581235720704-06d31ceb3ebf'),
    (186, 'lego_classic_v3.png', '1587654780288-6b280ce0eb82'),
    (187, 'magnatiles_v3.png', '1586522510164-9b24af1ddb06')
]

for pid, fname, photo_id in targets:
    fpath = os.path.join(d, fname)
    url = f"https://images.unsplash.com/photo-{photo_id}?q=80&w=1000&auto=format&fit=crop"
    
    try:
        print(f"Downloading high-quality image for toy {pid}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as res, open(fpath, 'wb') as f_out:
            f_out.write(res.read())
        print(f"Saved {fname}")
    except Exception as e:
        print(f"Failed {pid}: {e}")
