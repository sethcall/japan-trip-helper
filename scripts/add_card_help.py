import os
import re

CARDS_DIR = 'src/cards'
HELP_TEXT = '<p style="text-align: center; color: #666; font-style: italic; margin-top: -10px; margin-bottom: 20px; font-size: 0.9em;">Use this to show to a taxi driver or friendly person to get directions or driven somewhere.</p>'

def process_card(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    if HELP_TEXT in content:
        return

    # More robust replacement
    pattern = r'(</div>\s+<div style="text-align: center; margin-bottom: 20px;">)'
    replacement = r'</div>\n                    ' + HELP_TEXT + r'\n                    <div style="text-align: center; margin-bottom: 20px;">'
    
    new_content = re.sub(pattern, replacement, content, count=1)
    
    if new_content != content:
        print(f"Updating {filepath}")
        with open(filepath, 'w') as f:
            f.write(new_content)
    else:
        print(f"Failed to update {filepath}")

def main():
    for filename in os.listdir(CARDS_DIR):
        if filename.endswith(".html"):
            process_card(os.path.join(CARDS_DIR, filename))

if __name__ == "__main__":
    main()