import urllib.request, os

# URL of a high-quality Lakme foundation image (Unsplash example)
img_url = "https://images.unsplash.com/photo-1498579804530-03e226f9dbcb?auto=format&fit=crop&w=1000"
# Destination path
local_path = r"c:\\Users\\DELL\\OneDrive\\Desktop\\Product recommendation\\frontend\\static\\foundation_lakme.png"

try:
    print(f"Downloading Lakme foundation image from {img_url}...")
    req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as response, open(local_path, 'wb') as out_file:
        out_file.write(response.read())
    print("Download complete.")
except Exception as e:
    print(f"Failed to download image: {e}")
