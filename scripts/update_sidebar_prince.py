import glob
import os

# Root files
root_files = ['src/index.html', 'src/itinerary.html', 'src/suggestions.html', 'src/tips.html', 'src/words.html', 'src/phrases.html', 'src/install.html']

# Card files
card_files = glob.glob('src/cards/*.html')

root_target = '<li><a href="tips.html">Tips & Tricks</a></li>'
root_insert = '                <li><a href="prince-park.html">Prince Park</a></li>'

card_target = '<li><a href="../suggestions.html">Suggestions</a></li>'
card_insert = '                <li><a href="../prince-park.html">Prince Park</a></li>'

def update_file(path, is_root):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'prince-park.html' in content:
        print(f"Skipping {path} (already has link)")
        return
        
    target = root_target if is_root else card_target
    insert = root_insert if is_root else card_insert
    
    if target in content:
        content = content.replace(target, target + '\n' + insert)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Warning: Target not found in {path}")

for f in root_files:
    if os.path.exists(f):
        update_file(f, True)

for f in card_files:
    update_file(f, False)
