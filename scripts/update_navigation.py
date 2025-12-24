import os
import glob
import re

def update_navigation():
    # Define the standard menu structure
    # {p} is a placeholder for the relative path prefix ("" or "../")
    menu_items = [
        ('index.html', 'Home'),
        ('itinerary.html', 'Itinerary'),
        ('ginza-shopping.html', 'Ginza Shopping'),
        ('shibuya.html', 'Shibuya & Harajuku'),
        ('akihabara.html', 'Akihabara Arcade'),
        ('suggestions.html', 'Suggestions'),
        ('tips.html', 'General Travel Tips'),
        ('prince-park.html', 'Prince Park'),
        ('subway-tips.html', 'Subway Tips'),
        ('currency.html', 'Yen/Dollar'),
        ('words.html', 'Learn Words'),
        ('phrases.html', 'Learn Phrases'),
        ('install.html', 'Install App'),
        ('monday-schedule.html', 'Monday Plan'),
        ('wednesday-schedule.html', 'Wednesday Plan'),
        ('sunday-schedule.html', 'Sunday Plan'),
        ('blog-2025-12-21.html', 'Blog: Dec 21, Sunday'),
    ]

    def build_menu_html(prefix, current_file_name):
        html = '            <ul>\n'
        for filename, label in menu_items:
            # Determine active class
            # For blog posts, we might want a generic check if we have multiple, but for now exact match
            # Also handle the fact that card pages don't have their own entry in the main menu usually,
            # but they share the same sidebar.
            
            # Check if this menu item corresponds to the current file
            is_active = (filename == current_file_name)
            
            class_attr = ' class="active"' if is_active else ''
            
            html += f'                <li><a href="{prefix}{filename}"{class_attr}>{label}</a></li>\n'
        html += '            </ul>'
        return html

    # Process all HTML files in src/
    root_files = glob.glob('src/*.html')
    for file_path in root_files:
        filename = os.path.basename(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find the ul inside nav class="sidebar"
        # We look for <nav class="sidebar"> ... <h2>Menu</h2>        <ul> ... </ul>
        pattern = re.compile(r'(<nav class="sidebar">.*?<h2>Menu</h2>\s*)(<ul>.*?</ul>)', re.DOTALL)
        
        match = pattern.search(content)
        if match:
            new_menu = build_menu_html("", filename)
            new_content = content[:match.start(2)] + new_menu + content[match.end(2):]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_path}")
        else:
            print(f"Warning: Could not find sidebar menu in {file_path}")

    # Process all HTML files in src/cards/
    card_files = glob.glob('src/cards/*.html')
    for file_path in card_files:
        filename = os.path.basename(file_path) # Card filename won't match main menu items usually
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        pattern = re.compile(r'(<nav class="sidebar">.*?<h2>Menu</h2>\s*)(<ul>.*?</ul>)', re.DOTALL)
        
        match = pattern.search(content)
        if match:
            new_menu = build_menu_html("../", filename)
            new_content = content[:match.start(2)] + new_menu + content[match.end(2):]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_path}")
        else:
            print(f"Warning: Could not find sidebar menu in {file_path}")

if __name__ == "__main__":
    update_navigation()
