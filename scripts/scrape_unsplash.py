import urllib.request
import re
import json

def get_html_images(query):
    req = urllib.request.Request(f'https://unsplash.com/s/photos/{query}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        urls = re.findall(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+\?crop=entropy&cs=tinysrgb&fit=max&fm=jpg[^\"\'\s]*', html)
        if not urls:
            urls = re.findall(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+', html)
        
        # Clean URLs to just the base photo ID to avoid duplicates from different query params
        base_urls = []
        for u in urls:
            m = re.search(r'(https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+)', u)
            if m:
                base_urls.append(m.group(1) + '?q=80&w=1000&auto=format&fit=crop')
                
        return list(set(base_urls))
    except Exception as e:
        print(e)
        return []

print('tshirt:', len(get_html_images('mens-tshirt')))
print('jeans:', len(get_html_images('mens-jeans')))
print('trousers:', len(get_html_images('mens-trousers')))
print('shirt:', len(get_html_images('mens-shirt')))

tshirt = get_html_images('mens-tshirt')
jeans = get_html_images('mens-jeans')
trousers = get_html_images('mens-trousers')
shirt = get_html_images('mens-shirt')

data = {'tshirt': tshirt, 'jeans': jeans, 'trousers': trousers, 'shirt': shirt}
with open('data/scraped_unsplash.json', 'w') as f:
    json.dump(data, f)
