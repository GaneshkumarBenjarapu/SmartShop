import urllib.request
import urllib.parse
import json
import os

queries = {
    "foundation_maybelline.png": "sleek matte liquid foundation bottle on a clean elegant studio background professional lighting crisp details",
    "foundation_lakme.png": "luxurious flawless matte liquid foundation bottle with an elegant design placed on a minimalist premium studio background",
    "serum_loreal.png": "clear glass serum bottle with a dropper containing hyaluronic acid placed on a clean reflective studio surface with water droplets"
}

base_dir = r"c:\Users\DELL\OneDrive\Desktop\Product recommendation\frontend\static"

for filename, query in queries.items():
    encoded_query = urllib.parse.quote(query)
    url = f"https://lexica.art/api/v1/search?q={encoded_query}"
    filepath = os.path.join(base_dir, filename)
    
    try:
        print(f"Searching Lexica for {filename}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data['images']:
                image_url = data['images'][0]['src']
                print(f"Downloading image from {image_url}...")
                img_req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(img_req) as img_response, open(filepath, 'wb') as out_file:
                    out_file.write(img_response.read())
                print(f"Successfully saved {filename}")
            else:
                print(f"No results found for {filename}")
    except Exception as e:
        print(f"Failed for {filename}: {e}")
