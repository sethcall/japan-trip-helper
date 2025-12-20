import glob
import os

# Root files
root_files = glob.glob('src/*.html')

# Card files
card_files = glob.glob('src/cards/*.html')

def add_favicon(path, is_root):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'rel="icon"' in content:
        print(f"Favicon already exists in {path}")
        return

    icon_path = "assets/infographics/app-icon.jpg" if is_root else "../assets/infographics/app-icon.jpg"
    favicon_tag = f'    <link rel="icon" type="image/jpeg" href="{icon_path}">' 
    
    # Insert before </head>
    if '</head>' in content:
        content = content.replace('</head>', favicon_tag + '\n</head>')
    else:
        print(f"</head> not found in {path}")
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Added favicon to {path}")

for f in root_files:
    add_favicon(f, True)

for f in card_files:
    add_favicon(f, False)

