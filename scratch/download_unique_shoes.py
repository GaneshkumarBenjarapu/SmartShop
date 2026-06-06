import urllib.request
import urllib.parse
import os

d = 'frontend/static/shoes'
os.makedirs(d, exist_ok=True)

targets = [
    (114, "Skechers Walking Sneakers 52"),
    (113, "Skechers Casual Kicks 70"),
    (112, "Skechers Athletic Footwear 58"),
    (111, "Nike Running Shoes 97"),
    (109, "Nike Performance Shoes 21"),
    (107, "Red Tape Running Shoes 12"),
    (46, "Skechers Go Walk Shoes"),
    (45, "Red Tape Men's Walking Shoes")
]

for pid, name in targets:
    fname = name.lower().replace(' ', '_').replace("'", "") + ".png"
    fpath = os.path.join(d, fname)
    
    # Using Pollinations for unique AI generation based on name
    prompt = f"Professional studio product photography of {name}, white background, high resolution, detailed texture, realistic"
    encoded_prompt = urllib.parse.quote(prompt)
    # Using unique seed to force different images
    seed = pid * 12345 
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1000&height=1000&nologo=true&seed={seed}"
    
    try:
        print(f"Downloading unique image for {name}...")
        import time
        time.sleep(15) # 15 seconds is very safe
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as res, open(fpath, 'wb') as f_out:
            f_out.write(res.read())
        print(f"Saved to {fpath}")
    except Exception as e:
        print(f"Failed {name}: {e}")
