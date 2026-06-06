import os
import json
import urllib.request
import time

missing_fallbacks = {
    'action figure': 'https://images.unsplash.com/photo-1558060370-d64111d52c14?q=80&w=1000',
    'block': 'https://images.unsplash.com/photo-1587654780291-39c9404d746b?q=80&w=1000',
    'board game': 'https://images.unsplash.com/photo-1558060370-d64111d52c14?q=80&w=1000',
    'puzzle': 'https://images.unsplash.com/photo-1558060370-d64111d52c14?q=80&w=1000'
}

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    if p.get('category', '').lower() == 'toys':
        pid = p['id']
        path = f'frontend/static/toy_real_{pid}.jpg'
        
        # If the file does not exist or was failed to download due to 429
        if not os.path.exists(path) or os.path.getsize(path) < 1000:
            print(f'Need to fix: {pid} ({p["name"]})')
            
            # Since Wiki 429'd us, we'll try again with a specific descriptive bot User-Agent as they asked format, and slow down.
            # However, I didn't store the original wikipedia URL in JSON! The JSON has `/static/toy_real...`.
            # So let's just download a new Unsplash image or use a fake one?
            
            # Actually, I can just use placeholder pics or use fake data again? No, they explicitly want them unique and relevant.
            # I will re-map them to known wiki thumbnails.
