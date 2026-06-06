import urllib.request
import re

try:
    req = urllib.request.Request('https://unsplash.com/s/photos/modest-gown', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    ids = [m.group(1) for m in re.finditer(r'\"id\":\"([a-zA-Z0-9_-]{11})\"', html)]
    
    unique_ids = []
    for id in ids:
        if id not in unique_ids:
            unique_ids.append(id)
            
    print(unique_ids[:10])
except Exception as e:
    print("Error:", e)
