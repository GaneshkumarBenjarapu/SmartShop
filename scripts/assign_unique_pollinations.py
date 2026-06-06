import json
import urllib.parse
import os

def update_catalog():
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    count = 0
    for p in data:
        cat = p.get('category', '').lower()
        if cat == 'men fashion':
            prompt = f"Professional studio photography of Men fashion: {p['name']}, white background, high resolution, product shot"
            encoded_prompt = urllib.parse.quote(prompt)
            seed = sum(ord(c) for c in p['name']) # Deterministic seed based on name
            new_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=1000&nologo=true&seed={seed}"
            if p.get('image') != new_url:
                p['image'] = new_url
                count += 1
        elif cat == 'toys':
            prompt = f"Professional studio photography of Toy: {p['name']}, bright lighting, high resolution, product shot"
            encoded_prompt = urllib.parse.quote(prompt)
            seed = sum(ord(c) for c in p['name']) # Deterministic seed based on name
            new_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=1000&nologo=true&seed={seed}"
            if p.get('image') != new_url:
                p['image'] = new_url
                count += 1

    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"Updated {count} products in data/catalog.json")

if __name__ == '__main__':
    update_catalog()
