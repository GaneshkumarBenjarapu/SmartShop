import urllib.request
import os

d = 'frontend/static/shoes'
os.makedirs(d, exist_ok=True)

# 8 distinct, high-quality, professional shoe photos from Unsplash
targets = [
    ("Red Tape Running Shoes 12", "red_tape_running_v4.png", "1542291026-7eec264c27ff"), # Red Nike
    ("Nike Performance Shoes 21", "nike_performance_shoes_v4.png", "1551107696-a4b0c5a0d9a2"), # Blue Nike
    ("Skechers Athletic Footwear 58", "skechers_athletic_footwear_v4.png", "1606107557195-0e29a4b5b4aa"), # Green Nike
    ("Skechers Casual Kicks 70", "skechers_casual_kicks_v4.png", "1525966222134-fcfa99b8ae77"), # Yellow Vans
    ("Skechers Walking Sneakers 52", "skechers_walking_sneakers_v4.png", "1595950653106-6c9ebd614d3a"), # White/neon sneaker
    ("Skechers Go Walk Shoes", "skechers_go_walk_v4.png", "1460353581641-37baddab0fa2"), # White/red sneaker
    ("Red Tape Men's Walking Shoes", "red_tape_mens_walking_v4.png", "1560769629-975ec94e6a86"), # Grey sneaker
    ("Nike Running Shoes 97", "nike_running_shoes_97_v4.png", "1514989940723-e8e51635b782") # Grey running shoe
]

for name, fname, photo_id in targets:
    fpath = os.path.join(d, fname)
    url = f"https://images.unsplash.com/photo-{photo_id}?q=80&w=1000&auto=format&fit=crop"
    
    try:
        print(f"Downloading Unsplash image for {name}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as res, open(fpath, 'wb') as f_out:
            f_out.write(res.read())
        print(f"Saved {fname}")
    except Exception as e:
        print(f"Failed {name}: {e}")
