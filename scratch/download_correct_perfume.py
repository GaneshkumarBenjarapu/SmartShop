import urllib.request
import os

img_url = "https://images.unsplash.com/photo-1458538977777-0549b2370168?crop=entropy&cs=srgb&fm=jpg&ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzc4OTAxNjE5fA&ixlib=rb-4.1.0&q=85"
local_path = r"c:\Users\DELL\OneDrive\Desktop\Product recommendation\frontend\static\perfume_luxury.png"

try:
    print(f"Downloading correct perfume image from {img_url}...")
    req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as response, open(local_path, 'wb') as out_file:
        out_file.write(response.read())
    print("Download complete.")
except Exception as e:
    print(f"Failed to download image: {e}")
