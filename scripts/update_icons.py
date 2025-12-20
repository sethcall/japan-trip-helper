import glob
import os

# Root files
root_files = glob.glob('src/*.html')

# Card files
card_files = glob.glob('src/cards/*.html')

def update_icon(path, is_root):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    old_icon_root = 'link rel="apple-touch-icon" href="assets/cards/keio-plaza-hotel.png"'
    new_icon_root = 'link rel="apple-touch-icon" href="assets/infographics/app-icon.jpg"'
    
    old_icon_card = 'link rel="apple-touch-icon" href="../assets/cards/keio-plaza-hotel.png"'
    new_icon_card = 'link rel="apple-touch-icon" href="../assets/infographics/app-icon.jpg"'

    if is_root:
        if old_icon_root in content:
            content = content.replace(old_icon_root, new_icon_root)
        else:
            print(f"Old icon not found in root file: {path}")
            return
    else:
        if old_icon_card in content:
            content = content.replace(old_icon_card, new_icon_card)
        else:
            print(f"Old icon not found in card file: {path}")
            return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated icon in {path}")

for f in root_files:
    update_icon(f, True)

for f in card_files:
    update_icon(f, False)
