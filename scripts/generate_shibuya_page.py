import re
import os

def markdown_to_html(md_text):
    html_lines = []
    in_list = False
    
    lines = md_text.split('\n')
    
    for line in lines:
        line = line.strip()
        
        if not line:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            continue
            
        # Headers
        if line.startswith('# '):
            html_lines.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('#### '):
            html_lines.append(f'<h4>{line[5:]}</h4>')
        # Images
        elif line.startswith('!['):
            match = re.match(r'!\\\[(.*?)\]\((.*?)\)', line)
            if match:
                alt = match.group(1)
                src = match.group(2)
                html_lines.append(f'<img src="{src}" alt="{alt}" style="max-width:100%; height:auto; margin: 20px 0;">')
        # Lists
        elif line.startswith('* '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            content = line[2:]
            # Inline formatting for list items
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', content)
            html_lines.append(f'<li>{content}</li>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            
            # Paragraphs with inline formatting
            content = line
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', content)
            
            html_lines.append(f'<p>{content}</p>')
            
    if in_list:
        html_lines.append('</ul>')
        
    return '\n'.join(html_lines)

def generate_shibuya_page():
    # 1. Prepare Suggestions Data
    suggestions = [
        {
            "type": "Breakfast",
            "name": "Shinpachi Shokudō Shibuya Meijidōri",
            "link": "https://maps.app.goo.gl/1qpvovcGsqpuy49x5",
            "desc": "Charcoal-grilled fish set meals. Authentic, healthy, and reasonably priced. Opens at 7:00 AM.",
            "image": "assets/photos/shinpachi.png" # Assuming this path from md file
        },
        {
            "type": "Lunch",
            "name": "Uobei Shibuya Dogenzaka Store",
            "link": "https://maps.app.goo.gl/jqab3X1upFMHhSSY6",
            "desc": "High-speed chute delivery sushi. No rotating belt, made to order. Affordable and fast.",
            "image": ""
        },
        {
            "type": "Lunch",
            "name": "Global Store Kura Sushi",
            "link": "https://maps.app.goo.gl/PFWhedRhvAy2Sh2r5",
            "desc": "Global flagship store with a Harajuku aesthetic. Automated check-in, gamified eating (Bikkura Pon). Popular, book in advance.",
            "image": ""
        },
        {
            "type": "Walk & Shop",
            "name": "Cat Street",
            "link": "https://maps.app.goo.gl/51631xRdruxkBMvg9", # Using Shibuya Modi as start point ref
            "desc": "A hip haven of youth fashion and culture. Stretches about 1km between Shibuya and Harajuku. Pedestrianized backstreet with vintage shops and hipster coffee stands.",
            "image": ""
        }
    ]

    # 2. Read Background Content
    with open('scripts/shibuya_clean.md', 'r') as f:
        md_content = f.read()
    
    background_html = markdown_to_html(md_content)

    # 3. HTML Template
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shibuya & Harajuku Guide - Japan Trip 2025</title>
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
            background-color: #6f42c1; /* Purple for Shibuya */
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
                <li><a href="shibuya.html" class="active">Shibuya & Harajuku</a></li>
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
                <h1>Shibuya & Harajuku Guide</h1>
            </header>

            <section>
                <h2>Quick Suggestions</h2>
                <p>Curated list of spots in Shibuya and Harajuku.</p>
                
                <table class="address-table">
                    <thead>
                        <tr>
                            <th style="width: 30%;">Location</th>
                            <th style="width: 70%;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
"""
    
    # 4. Generate Table Rows
    table_rows = ""
    for item in suggestions:
        img_tag = ""
        if item["image"]:
            # Ensure path matches what we expect or is absolute/relative correctly
            # In shibuya.md it said src/assets... we want assets/... for web
            img_src = item["image"].replace("src/", "")
            img_tag = f'<img src="{img_src}" alt="{item["name"]}" style="float:right; width: 120px; margin: 0 0 10px 15px; border-radius: 4px; border: 1px solid #ccc;">'
        
        row = f"""
                        <tr>
                            <td>
                                <span class="location-type">{item["type"]}:</span>
                                <span class="location-name">{item["name"]}</span>
                                <a href="{item["link"]}" class="map-link" target="_blank">Google Maps</a>
                            </td>
                            <td class="description-text">
                                {img_tag}
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
"""
    html_template += background_html
    html_template += """
            </section>
        </main>
    </div>
    <script src="js/sw-register.js"></script>
</body>
</html>
"""

    with open('src/shibuya.html', 'w') as f:
        f.write(html_template)
    
    print("Created src/shibuya.html")

if __name__ == "__main__":
    generate_shibuya_page()
