import glob
import os

files = glob.glob('src/*.html') + glob.glob('src/cards/*.html') + glob.glob('scripts/*.py')

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'General Travel Tips' in content:
        new_content = content.replace('General Travel Tips', 'General Travel Tips')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
