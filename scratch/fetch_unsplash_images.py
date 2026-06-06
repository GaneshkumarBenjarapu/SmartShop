import urllib.request
import re

queries = {
    "maybelline": "https://unsplash.com/s/photos/liquid-foundation-makeup",
    "lakme": "https://unsplash.com/s/photos/foundation-makeup-bottle",
    "loreal": "https://unsplash.com/s/photos/face-serum-dropper"
}

for name, url in queries.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            # Look for image URLs
            matches = re.findall(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+\?[\w\=\&\-]+', html)
            if matches:
                print(f"{name}: {matches[0]}")
            else:
                print(f"{name}: No matches found")
    except Exception as e:
        print(f"{name}: Failed - {e}")
