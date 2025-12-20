import glob
import os

# Root files
root_files = glob.glob('src/*.html')

# Card files
card_files = glob.glob('src/cards/*.html')

def update_sidebar(path, is_root):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'currency.html' in content:
        print(f"Skipping {path} (already has link)")
        return
        
    # Target: Learn Words
    if is_root:
        target = '<li><a href="words.html">Learn Words</a></li>'
        insert = '                <li><a href="currency.html">Yen/Dollar</a></li>'
    else:
        target = '<li><a href="../words.html">Learn Words</a></li>'
        insert = '                <li><a href="../currency.html">Yen/Dollar</a></li>'
    
    if target in content:
        # Insert BEFORE target
        content = content.replace(target, insert + '\n' + target)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        # Fallback if Learn Words not found (some cards might not have it?)
        # Let's try Prince Park
        if is_root:
            target = '<li><a href="prince-park.html">Prince Park</a></li>'
            insert = '                <li><a href="currency.html">Yen/Dollar</a></li>'
        else:
            target = '<li><a href="../prince-park.html">Prince Park</a></li>'
            insert = '                <li><a href="../currency.html">Yen/Dollar</a></li>'
            
        if target in content:
             # Insert AFTER Prince Park if words.html not found
             content = content.replace(target, target + '\n' + insert)
             with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
             print(f"Updated {path} (fallback)")
        else:
             print(f"Warning: Target not found in {path}")

for f in root_files:
    if f.endswith('currency.html') or f.endswith('index.html'): 
        continue
    update_sidebar(f, True)

for f in card_files:
    update_sidebar(f, False)
