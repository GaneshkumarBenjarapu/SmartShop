import json
import urllib.request
import os

image_map = {
    60: "https://images.unsplash.com/photo-1581655353564-df123a1eb820?q=80&w=1000&auto=format&fit=crop", 
    61: "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=1000&auto=format&fit=crop", 
    62: "https://images.unsplash.com/photo-1596755094514-f8b1e4c70fba?q=80&w=1000&auto=format&fit=crop", 
    63: "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?q=80&w=1000&auto=format&fit=crop", 
    143: "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=1000&auto=format&fit=crop", 
    144: "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?q=80&w=1000&auto=format&fit=crop", 
    145: "https://images.unsplash.com/photo-1602810318383-e386cc2a3ce3?q=80&w=1000&auto=format&fit=crop", 
    146: "https://images.unsplash.com/photo-1604176354204-9268738cb284?q=80&w=1000&auto=format&fit=crop", 
    147: "https://images.unsplash.com/photo-1576566588028-4147f3842f27?q=80&w=1000&auto=format&fit=crop", 
    148: "https://images.unsplash.com/photo-1555689502-c4b22d76c56f?q=80&w=1000&auto=format&fit=crop", 
    149: "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?q=80&w=1000&auto=format&fit=crop", 
    150: "https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?q=80&w=1000&auto=format&fit=crop", 
    151: "https://images.unsplash.com/photo-1510312480391-768ad8b857dc?q=80&w=1000&auto=format&fit=crop", 
    152: "https://images.unsplash.com/photo-1582552938357-32b906df40cb?q=80&w=1000&auto=format&fit=crop", 
    153: "https://images.unsplash.com/photo-1503342394128-c104d54dba01?q=80&w=1000&auto=format&fit=crop", 
    154: "https://images.unsplash.com/photo-1588359348347-9bc6cbbb689e?q=80&w=1000&auto=format&fit=crop", 
    155: "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?q=80&w=1000&auto=format&fit=crop", 
    156: "https://images.unsplash.com/photo-1559582798-678dfc71caf8?q=80&w=1000&auto=format&fit=crop", 
    157: "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?q=80&w=1000&auto=format&fit=crop", 
    9004: "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=1000&auto=format&fit=crop", 
    9005: "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?q=80&w=1000&auto=format&fit=crop" 
}

def download_and_update_catalog():
    os.makedirs('frontend/static/men_unique', exist_ok=True)
    
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    count = 0
    for p in data:
        if p.get('category', '').lower() == 'men fashion' and p.get('id') in image_map:
            url = image_map[p['id']]
            filename = f"men_unique_{p['id']}.jpg"
            filepath = os.path.join('frontend', 'static', 'men_unique', filename)
            
            print(f"Downloading {filename}...")
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=15) as res, open(filepath, 'wb') as f_out:
                    f_out.write(res.read())
                
                # Update the URL to local path
                p['image'] = f'/static/men_unique/{filename}'
                count += 1
            except Exception as e:
                print(f"Failed {p['id']}: {e}")

    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"Successfully downloaded and updated {count} local images.")

if __name__ == '__main__':
    download_and_update_catalog()
