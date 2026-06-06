import urllib.request
import os

d = 'frontend/static/shoes'
os.makedirs(d, exist_ok=True)

targets = [
    ('nike_performance_shoes_21.png', 'nike,running,shoes'),
    ('red_tape_running_shoes_12.png', 'running,shoes'),
    ('skechers_go_walk_shoes.png', 'walking,shoes,comfortable'),
    ('red_tape_mens_walking_shoes.png', 'walking,shoes,mens')
]

for fname, keywords in targets:
    url = f'https://loremflickr.com/1000/1000/{keywords}/all'
    fpath = os.path.join(d, fname)
    try:
        print(f"Downloading {fname}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as res, open(fpath, 'wb') as f_out:
            f_out.write(res.read())
        print(f"Saved to {fpath}")
    except Exception as e:
        print(f"Failed {fname}: {e}")
