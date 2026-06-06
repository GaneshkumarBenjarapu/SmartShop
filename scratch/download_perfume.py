import urllib.request
import os

img_url = "https://images.unsplash.com/photo-1615484477778-ca3b77940c25?q=80&w=1000"
local_path = r"c:\Users\DELL\OneDrive\Desktop\Product recommendation\frontend\static\perfume_luxury.png"

try:
    print(f"Downloading {img_url}...")
    req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, timeout=15) as response, open(local_path, 'wb') as out_file:
        out_file.write(response.read())
    print(f"Successfully saved to {local_path}")
except Exception as e:
    print(f"Failed to download: {e}")
