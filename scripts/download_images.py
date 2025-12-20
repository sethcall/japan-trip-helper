import urllib.request
import re
import os

def download_image(url, filename):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
            print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def get_wikimedia_url(file_page_url):
    try:
        req = urllib.request.Request(file_page_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            text = response.read().decode('utf-8')
            match = re.search(r'class="fullMedia"><a href="//(upload\.wikimedia\.org/[^"]+)"', text)
            if match:
                return "https://" + match.group(1)
    except Exception as e:
        print(f"Error fetching page {file_page_url}: {e}")
    return None

targets = [
    ("zojoji-temple.jpg", "https://commons.wikimedia.org/wiki/File:Zojoji.jpg"),
    ("atago-shrine.jpg", "https://commons.wikimedia.org/wiki/File:Stairs_to_Atago_jinja_Tokyo.JPG"),
    ("uniqlo-tokyo.jpg", "https://commons.wikimedia.org/wiki/File:UNIQLO_Ginza_Store_2012.jpg"), 
    ("ginza-mitsukoshi.jpg", "https://commons.wikimedia.org/wiki/File:Ginza_Mitsukoshi.jpg"),
    ("marronnier-gate.jpg", "https://commons.wikimedia.org/wiki/File:Marronnier_Gate_Ginza_2.jpg"), 
    ("itoya-ginza.jpg", "https://commons.wikimedia.org/wiki/File:Ginza_Itoya_2015.jpg"),
    ("mont-blanc-cake.jpg", "https://commons.wikimedia.org/wiki/File:Mont_Blanc_aux_marrons.jpg")
]

output_dir = "src/assets/photos"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

direct_targets = [
    ("don-quijote-roppongi.jpg", "https://upload.wikimedia.org/wikipedia/commons/e/e7/Don_Quijote_Roppongi_Store_20060517.jpg")
]

for filename, page_url in targets:
    print(f"Processing {filename}...")
    img_url = get_wikimedia_url(page_url)
    if img_url:
        print(f"Found URL: {img_url}")
        download_image(img_url, os.path.join(output_dir, filename))
    else:
        print(f"Could not extract URL for {filename}")

for filename, url in direct_targets:
    download_image(url, os.path.join(output_dir, filename))