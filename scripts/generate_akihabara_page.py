import re
import os

def format_content(text):
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    return text

def markdown_to_html(md_text):
    html_lines = []
    in_list = False
    
    lines = md_text.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines, but close list if open
        if not line:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            continue
            
        # Skip image definitions at the end
        if line.startswith('[image'):
            continue

        # Headers
        if line.startswith('# '):
            content = format_content(line[2:])
            html_lines.append(f'<h1>{content}</h1>')
        elif line.startswith('## '):
            content = format_content(line[3:])
            html_lines.append(f'<h2>{content}</h2>')
        elif line.startswith('### '):
            content = format_content(line[4:])
            html_lines.append(f'<h3>{content}</h3>')
        elif line.startswith('#### '):
            content = format_content(line[5:])
            html_lines.append(f'<h4>{content}</h4>')
        
        # Reference Style Images ![][image1]
        elif line.startswith('![][image'):
            # Extract the image number
            match = re.search(r'image(\d+)', line)
            if match:
                img_num = match.group(1)
                src = f"assets/photos/akihabara/image{img_num}.png"
                html_lines.append(f'<img src="{src}" alt="Akihabara Image {img_num}" style="max-width:100%; height:auto; margin: 20px 0; display:block;">')
            else:
                html_lines.append(f'<p><em>Image placeholder: {line}</em></p>')

        # Lists
        elif line.startswith('* '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            content = line[2:]
            content = format_content(content)
            html_lines.append(f'<li>{content}</li>')
        
        # Standard Paragraphs
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            
            content = format_content(line)
            html_lines.append(f'<p>{content}</p>')
            
    if in_list:
        html_lines.append('</ul>')
        
    return '\n'.join(html_lines)

def generate_page():
    # 1. Suggestions Data
    suggestions = [
        {
            "type": "Breakfast/Brunch",
            "name": "The French Toast Factory",
            "link": "https://www.google.com/maps/search/?api=1&query=The+French+Toast+Factory+Yodobashi+Akiba",
            "desc": "Renowned for soufflé pancakes. Located on the 8th floor of Yodobashi Akiba. Opens at 11:00 AM."
        },
        {
            "type": "Breakfast/Brunch",
            "name": "Flying Scotsman",
            "link": "https://www.google.com/maps/search/?api=1&query=Flying+Scotsman+Akihabara",
            "desc": "Famous for thick, dense hotcakes. Opens 11:00 AM weekdays, 10:00 AM weekends."
        },
        {
            "type": "Early Morning",
            "name": "Coffee Renoir (Showa-dori Exit)",
            "link": "https://www.google.com/maps/search/?api=1&query=Coffee+Renoir+Akihabara+Showa-dori",
            "desc": "Traditional Japanese coffee house ('Kissaten') with comfortable velvet seats. Opens 7:30 AM."
        },
        {
            "type": "Early Morning",
            "name": "Beck's Coffee Shop",
            "link": "https://www.google.com/maps/search/?api=1&query=Beck's+Coffee+Shop+Akihabara+Electric+Town+Gate",
            "desc": "Quick, functional morning plates. Located at the Electric Town Gate. Opens 6:30 AM."
        },
        {
            "type": "Electronics",
            "name": "Yodobashi Akiba",
            "link": "https://www.google.com/maps/search/?api=1&query=Yodobashi+Camera+Multimedia+Akiba",
            "desc": "Massive 9-story electronics complex. A theme park for consumerism. Opens 9:30 AM."
        },
        {
            "type": "Electronics Components",
            "name": "Akihabara Radio Center",
            "link": "https://www.google.com/maps/search/?api=1&query=Akihabara+Radio+Center",
            "desc": "Two-story warren of tiny stalls selling electronic components. Authentic cyberpunk bazaar atmosphere."
        },
        {
            "type": "Anime/Figures",
            "name": "Radio Kaikan",
            "link": "https://www.google.com/maps/search/?api=1&query=Radio+Kaikan+Akihabara",
            "desc": "10-story tower serving as a 'Vertical High Street' for otaku culture. Figures, cards, models."
        },
        {
            "type": "Vintage/Rare",
            "name": "Mandarake Complex",
            "link": "https://www.google.com/maps/search/?api=1&query=Mandarake+Complex+Akihabara",
            "desc": "The gold standard for vintage and rare collectibles. 8 floors of manga, toys, and cells."
        },
        {
            "type": "Retro Games",
            "name": "Super Potato",
            "link": "https://www.google.com/maps/search/?api=1&query=Super+Potato+Akihabara",
            "desc": "Famous retro game store with a 5th-floor arcade. A nostalgia overload."
        },
        {
            "type": "Souvenirs/Night",
            "name": "Don Quijote Akihabara",
            "link": "https://www.google.com/maps/search/?api=1&query=Don+Quijote+Akihabara",
            "desc": "Open 24 hours. Mass-market souvenirs, KitKats, cosmetics. Houses the AKB48 Theater."
        }
    ]

    # 2. Read Background Content
    with open('akihabara_shopping.md', 'r') as f:
        md_content = f.read()
    
    background_html = markdown_to_html(md_content)

    # 3. HTML Template
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akihabara Shopping Guide - Japan Trip 2025</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .address-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 40px;
        }
        .address-table th, .address-table td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #eee;
            vertical-align: top;
        }
        .address-table th {
            background-color: #007bff; /* Blue for Akihabara */
            color: white;
            font-weight: bold;
            text-transform: uppercase;
            font-size: 0.9em;
        }
        .address-table tr:hover {
            background-color: #f9f9f9;
        }
        .location-name {
            font-weight: bold;
            font-size: 1.1em;
            color: #333;
            display: block;
            margin-bottom: 5px;
        }
        .location-type {
            font-size: 0.8em;
            color: #666;
            text-transform: uppercase;
            margin-right: 5px;
        }
        .map-link {
            display: inline-block;
            margin-top: 5px;
            color: #007bff;
            text-decoration: none;
            font-size: 0.9em;
        }
        .map-link:hover {
            text-decoration: underline;
        }
        .description-text {
            font-size: 0.95em;
            color: #555;
            line-height: 1.5;
        }
        .background-content {
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            margin-top: 40px;
        }
        .background-content h1, .background-content h2, .background-content h3 {
            color: #333;
            margin-top: 1.5em;
        }
        .background-content p {
            line-height: 1.6;
            color: #444;
            margin-bottom: 1em;
        }
        .background-content ul {
            padding-left: 20px;
            margin-bottom: 1em;
        }
        .background-content li {
            margin-bottom: 0.5em;
        }
        /* Make images in background content responsive */
        .background-content img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
    </style>
    <link rel="manifest" href="manifest.json">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <link rel="apple-touch-icon" href="assets/infographics/app-icon.jpg">
    <link rel="icon" type="image/jpeg" href="assets/infographics/app-icon.jpg">
</head>
<body>
    <div class="layout">
        <nav class="sidebar">
            <h2>Menu</h2>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="itinerary.html">Itinerary</a></li>
                <li><a href="sunday-schedule.html">Sunday Plan</a></li>
                <li><a href="ginza-shopping.html">Ginza Shopping</a></li>
                <li><a href="shibuya.html">Shibuya & Harajuku</a></li>
                <li><a href="akihabara.html" class="active">Akihabara Arcade</a></li>
                <li><a href="suggestions.html">Suggestions</a></li>
                <li><a href="tips.html">General Travel Tips</a></li>
                <li><a href="prince-park.html">Prince Park</a></li>
                <li><a href="subway-tips.html">Subway Tips</a></li>
                <li><a href="currency.html">Yen/Dollar</a></li>
                <li><a href="words.html">Learn Words</a></li>
                <li><a href="phrases.html">Learn Phrases</a></li>
                <li><a href="install.html">Install App</a></li>
                <li><a href="blog-2025-12-21.html">Blog: Dec 21, Sunday</a></li>
            </ul>
        </nav>
        <main class="content">
            <header>
                <h1>Akihabara Shopping Guide</h1>
            </header>

            <section>
                <h2>Quick Suggestions</h2>
                <p>Curated list of spots in Akihabara.</p>
                
                <table class="address-table">
                    <thead>
                        <tr>
                            <th style="width: 30%;">Location</th>
                            <th style="width: 70%;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
""".strip()
    
    # 4. Generate Table Rows
    table_rows = ""
    for item in suggestions:
        row = f"""
                        <tr>
                            <td>
                                <span class="location-type">{item["type"]}:</span>
                                <span class="location-name">{item["name"]}</span>
                                <a href="{item["link"]}" class="map-link" target="_blank">Google Maps</a>
                            </td>
                            <td class="description-text">
                                {item["desc"]}
                            </td>
                        </tr>
"""
        table_rows += row

    html_template += table_rows
    html_template += """
                    </tbody>
                </table>
            </section>

            <section class="background-content">
                <h2>Akihabara Shopping Background Reading</h2>
""".strip()
    html_template += background_html
    html_template += """
            </section>
        </main>
    </div>
    <script src="js/sw-register.js"></script>
</body>
</html>
""".strip()

    with open('src/akihabara.html', 'w') as f:
        f.write(html_template)
    
    print("Created src/akihabara.html")

if __name__ == "__main__":
    generate_page()
