import os
import re

INSTRUCTIONS_DIR = 'src/instructions'

# Mapping of text to Google Maps URLs
LOCATION_MAP = {
    "The Prince Park Tower Tokyo": "https://www.google.com/maps/search/?api=1&query=The+Prince+Park+Tower+Tokyo",
    "Hamamatsucho Station": "https://www.google.com/maps/search/?api=1&query=Hamamatsucho+Station",
    "Hamamatsuchō Station": "https://www.google.com/maps/search/?api=1&query=Hamamatsucho+Station",
    "Tokyo Tower": "https://www.google.com/maps/search/?api=1&query=Tokyo+Tower",
    "Zojoji Temple": "https://www.google.com/maps/search/?api=1&query=Zojoji+Temple",
    "Shiba Park": "https://www.google.com/maps/search/?api=1&query=Shiba+Park",
    "Akabanebashi Station": "https://www.google.com/maps/search/?api=1&query=Akabanebashi+Station",
    "Daimon Station": "https://www.google.com/maps/search/?api=1&query=Daimon+Station",
    "Akihabara Station": "https://www.google.com/maps/search/?api=1&query=Akihabara+Station",
    "Tokyo Station": "https://www.google.com/maps/search/?api=1&query=Tokyo+Station",
    "Kyoto Station": "https://www.google.com/maps/search/?api=1&query=Kyoto+Station",
    "Shinjuku Station": "https://www.google.com/maps/search/?api=1&query=Shinjuku+Station",
    "Shibuya Station": "https://www.google.com/maps/search/?api=1&query=Shibuya+Station",
    "Harajuku Station": "https://www.google.com/maps/search/?api=1&query=Harajuku+Station",
    "Roppongi Station": "https://www.google.com/maps/search/?api=1&query=Roppongi+Station",
    "Kamiyacho Station": "https://www.google.com/maps/search/?api=1&query=Kamiyacho+Station",
    "Azabudai Hills": "https://www.google.com/maps/search/?api=1&query=Azabudai+Hills",
    "Tsukiji Outer Market": "https://www.google.com/maps/search/?api=1&query=Tsukiji+Outer+Market",
    "Yayoi Kusama Museum": "https://www.google.com/maps/search/?api=1&query=Yayoi+Kusama+Museum",
    "Ushigome-yanagicho Station": "https://www.google.com/maps/search/?api=1&query=Ushigome-yanagicho+Station",
    "The Thousand Kyoto": "https://www.google.com/maps/search/?api=1&query=The+Thousand+Kyoto",
    "Fushimi-Momoyama Station": "https://www.google.com/maps/search/?api=1&query=Fushimi-Momoyama+Station",
    "Keio Plaza Hotel Tokyo": "https://www.google.com/maps/search/?api=1&query=Keio+Plaza+Hotel+Tokyo",
    "TeamLab Planets": "https://www.google.com/maps/search/?api=1&query=TeamLab+Planets+Tokyo",
    "Shibuya Scramble Square": "https://www.google.com/maps/search/?api=1&query=Shibuya+Scramble+Square",
    "Hachiko Exit": "https://www.google.com/maps/search/?api=1&query=Hachiko+Exit+Shibuya+Station",
    "Oji Inari-jinja Shrine": "https://www.google.com/maps/search/?api=1&query=Oji+Inari-jinja+Shrine",
    "Narita Airport": "https://www.google.com/maps/search/?api=1&query=Narita+Airport",
    "Haneda Airport": "https://www.google.com/maps/search/?api=1&query=Haneda+Airport",
    "NRT": "https://www.google.com/maps/search/?api=1&query=Narita+Airport",
    "HND": "https://www.google.com/maps/search/?api=1&query=Haneda+Airport",
    "7-Eleven": "https://www.google.com/maps/search/?api=1&query=7-Eleven+Japan",
    "Lawson": "https://www.google.com/maps/search/?api=1&query=Lawson+Japan",
    "FamilyMart": "https://www.google.com/maps/search/?api=1&query=FamilyMart+Japan",
    "Yamanote Line": "https://www.google.com/maps/search/?api=1&query=Yamanote+Line",
    "Oedo Line": "https://www.google.com/maps/search/?api=1&query=Oedo+Line",
    "Ginza": "https://www.google.com/maps/search/?api=1&query=Ginza+Tokyo",
    "Arashiyama": "https://www.google.com/maps/search/?api=1&query=Arashiyama+Kyoto",
    "Nishiki Market": "https://www.google.com/maps/search/?api=1&query=Nishiki+Market",
    "Gion": "https://www.google.com/maps/search/?api=1&query=Gion+Kyoto",
    "Yasaka Shrine": "https://www.google.com/maps/search/?api=1&query=Yasaka+Shrine",
    "Kaminarimon Gate": "https://www.google.com/maps/search/?api=1&query=Kaminarimon+Gate",
    "Nakamise Street": "https://www.google.com/maps/search/?api=1&query=Nakamise+Street",
    "Senso-ji": "https://www.google.com/maps/search/?api=1&query=Senso-ji+Temple",
    "Takeshita Street": "https://www.google.com/maps/search/?api=1&query=Takeshita+Street",
    "Omotesando": "https://www.google.com/maps/search/?api=1&query=Omotesando",
    "Cat Street": "https://www.google.com/maps/search/?api=1&query=Cat+Street+Harajuku",
    "Toyosu Station": "https://www.google.com/maps/search/?api=1&query=Toyosu+Station",
    "Tsukiji Station": "https://www.google.com/maps/search/?api=1&query=Tsukiji+Station",
    "Higashi-ginza Station": "https://www.google.com/maps/search/?api=1&query=Higashi-ginza+Station",
    "Asakusa Station": "https://www.google.com/maps/search/?api=1&query=Asakusa+Station",
    "Ueno Station": "https://www.google.com/maps/search/?api=1&query=Ueno+Station",
    "Oji Station": "https://www.google.com/maps/search/?api=1&query=Oji+Station",
}

# Sort keys by length (descending) to avoid partial replacements (e.g. replacing "Tokyo Station" inside "Tokyo Station Hotel")
SORTED_KEYS = sorted(LOCATION_MAP.keys(), key=len, reverse=True)

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content

    # 1. Update H1 style to be sticky
    # Look for existing h1 style in the style block
    h1_style_regex = r"(h1\s*\{[^}]*)\}"
    
    # We want to add sticky positioning to h1. 
    # Current style usually: h1 { border-bottom: 2px solid #eee; padding-bottom: 10px; }
    # New style: h1 { border-bottom: 2px solid #eee; padding-bottom: 10px; position: sticky; top: 0; background: white; z-index: 100; margin-top: 0; padding-top: 10px; }
    
    # Check if sticky is already there to avoid double addition
    if "position: sticky" not in content:
        replacement_style = r"\1; position: sticky; top: 0; background-color: white; z-index: 1000; padding-top: 10px; margin-top: 0; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }"
        content = re.sub(h1_style_regex, replacement_style, content)

    # 2. Linkify locations
    # We need to be careful not to replace text inside existing <a> tags.
    # We'll split the text by tags and only process outside tags.
    
    # Simple approach: Loop through keys. For each key, find it. If it's not inside an <a> tag, replace it.
    # A robust regex for "not inside <a> tag" is complex. 
    # Alternative: Use a placeholder for existing <a> tags, perform replacements, then restore.
    
    links = []
    def save_link(match):
        links.append(match.group(0))
        return f"__LINK_{len(links)-1}__"

    # Hide existing links
    content = re.sub(r'<a\s+[^>]*>.*?</a>', save_link, content, flags=re.DOTALL)

    for term in SORTED_KEYS:
        url = LOCATION_MAP[term]
        # Regex to match the term as a whole word (or at least bounded appropriately)
        # We use \b for word boundaries, but some terms might end with punctuation or start with it.
        # \b works well for English.
        pattern = r'\b' + re.escape(term) + r'\b'
        
        replacement = f'<a href="{url}" target="_blank" style="color: #007bff; text-decoration: none;">{term}</a>'
        
        content = re.sub(pattern, replacement, content)

    # Restore existing links
    def restore_link(match):
        idx = int(match.group(1))
        return links[idx]

    content = re.sub(r'__LINK_(\d+)__', restore_link, content)

    if content != original_content:
        print(f"Updating {filepath}")
        with open(filepath, 'w') as f:
            f.write(content)
    else:
        print(f"No changes for {filepath}")

def main():
    if not os.path.exists(INSTRUCTIONS_DIR):
        print(f"Directory {INSTRUCTIONS_DIR} not found.")
        return

    for filename in os.listdir(INSTRUCTIONS_DIR):
        if filename.endswith(".html"):
            filepath = os.path.join(INSTRUCTIONS_DIR, filename)
            process_file(filepath)

if __name__ == "__main__":
    main()
