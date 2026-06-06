import urllib.request
import os

d = 'frontend/static/toys_v5'
os.makedirs(d, exist_ok=True)

targets = [
    (173, 'Educational Wooden Alphabet Puzzle'),
    (174, 'Electronic Dancing Cactus with Recording'),
    (175, 'Reversible Octopus Soft Toy'),
    (176, '2-in-1 Magnetic Writing Board'),
    (177, 'Friction Powered Heavy Duty Truck Set'),
    (178, 'DIY Crystal Slime Making Kit'),
    (179, 'Miniature Kitchen Set with Accessories'),
    (180, 'Complete Doctor Play Set Suitcase'),
    (181, 'Handheld Water Ring Toss Toy'),
    (182, 'Pull-back Mini Racing Cars (Pack of 6)'),
    (183, 'Magical Water Drawing Painting Mat'),
    (184, 'Bubble Gun Blaster with Solution'),
    (185, 'Flying Sensor Induction Helicopter'),
    (186, 'Musical Toy Mobile Phone with Lights'),
    (187, 'Soft Plush Rabbit Toy (Meesho Edition)')
]

for pid, name in targets:
    fname = f"toy_{pid}_meesho_v2.png"
    fpath = os.path.join(d, fname)
    import urllib.parse
    prompt = f"Authentic mobile phone photo of {name} on a clean floor, bright indoor lighting, Meesho app product listing, realistic, simple, unedited"
    encoded_prompt = urllib.parse.quote(prompt)
    seed = pid * 12345
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=800&nologo=true&seed={seed}"
    
    try:
        import time
        time.sleep(15) # Safe sleep
        print(f"Downloading Meesho image for {name}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as res, open(fpath, 'wb') as f_out:
            f_out.write(res.read())
        print(f"Saved {fname}")
    except Exception as e:
        print(f"Failed {name}: {e}")
