import glob
import os

# Root files
root_files = glob.glob('src/*.html')

# Card files
card_files = glob.glob('src/cards/*.html')

def update_sidebar(path, is_root):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'subway-tips.html' in content:
        print(f"Skipping {path} (already has link)")
        return
        
    # Target: Prince Park
    if is_root:
        target = '<li><a href="prince-park.html">Prince Park</a></li>'
        insert = '                <li><a href="subway-tips.html">Subway Tips</a></li>'
    else:
        target = '<li><a href="../prince-park.html">Prince Park</a></li>'
        insert = '                <li><a href="../subway-tips.html">Subway Tips</a></li>'
    
    if target in content:
        # Insert AFTER target
        content = content.replace(target, target + '\n' + insert)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Warning: Target not found in {path}")

for f in root_files:
    if f.endswith('subway-tips.html'): 
        continue
    update_sidebar(f, True)

for f in card_files:
    update_sidebar(f, False)
