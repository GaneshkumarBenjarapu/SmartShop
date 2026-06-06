import urllib.request
import urllib.parse
import os
import time
import random

prompts = {
    "foundation_lakme.png": "A luxurious, high-end product photography shot of a flawless matte liquid foundation bottle with an elegant design, placed on a minimalist premium studio background. Soft studio lighting, sharp focus on the bottle, luxury cosmetics aesthetic.",
    "serum_loreal.png": "A stunning, high-quality product photography shot of a clear glass serum bottle with a dropper containing hyaluronic acid. Placed on a clean, reflective studio surface with water droplets to emphasize hydration. Premium lighting, luxury skincare aesthetic."
}

base_dir = r"c:\Users\DELL\OneDrive\Desktop\Product recommendation\frontend\static"

for filename, prompt in prompts.items():
    seed = random.randint(1, 1000000)
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1000&height=1000&nologo=true&seed={seed}"
    filepath = os.path.join(base_dir, filename)
    
    success = False
    for attempt in range(3):
        try:
            print(f"Generating and downloading {filename} (Attempt {attempt+1})...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=60) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Successfully saved {filename}")
            success = True
            break
        except Exception as e:
            print(f"Failed to generate {filename}: {e}")
            time.sleep(5)
    
    if success:
        time.sleep(3)
