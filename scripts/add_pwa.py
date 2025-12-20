import glob
import os

# Root files
root_files = ['src/index.html', 'src/itinerary.html', 'src/suggestions.html', 'src/tips.html', 'src/words.html', 'src/phrases.html']

# Card files
card_files = glob.glob('src/cards/*.html')

# Content to inject for ROOT
root_head = """    <link rel="manifest" href="manifest.json">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <link rel="apple-touch-icon" href="assets/cards/keio-plaza-hotel.png">
"""
root_sidebar = '                <li><a href="install.html">Install App</a></li>'
root_script = '    <script src="js/sw-register.js"></script>'

# Content to inject for CARDS
card_head = """    <link rel="manifest" href="../manifest.json">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <link rel="apple-touch-icon" href="../assets/cards/keio-plaza-hotel.png">
"""
# Card sidebar: append to list. Most cards end with suggestions.html.
card_sidebar_target = '<li><a href="../suggestions.html">Suggestions</a></li>'
card_sidebar_insert = '                <li><a href="../install.html">Install App</a></li>'
card_script = '    <script src="../js/sw-register.js"></script>'

def update_file(path, is_root):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already updated (check for manifest)
    if 'manifest.json' in content:
        print(f"Skipping {path} (already updated)")
        return
        
    # HEAD
    head_inject = root_head if is_root else card_head
    if '</head>' in content:
        content = content.replace('</head>', head_inject + '</head>')
    
    # SIDEBAR
    # For root files, look for Learn Phrases
    if is_root:
        target = '<li><a href="phrases.html">Learn Phrases</a></li>'
        insert = root_sidebar
        if target in content:
            content = content.replace(target, target + '\n' + insert)
        else:
            print(f"Warning: Sidebar target not found in {path}")
    else:
        # Cards
        target = card_sidebar_target
        insert = card_sidebar_insert
        if target in content:
            content = content.replace(target, target + '\n' + insert)
        else:
             print(f"Warning: Sidebar target not found in {path}")

    # SCRIPT
    script_inject = root_script if is_root else card_script
    if '</body>' in content:
        content = content.replace('</body>', script_inject + '\n</body>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")

for f in root_files:
    if os.path.exists(f):
        update_file(f, True)

for f in card_files:
    update_file(f, False)
