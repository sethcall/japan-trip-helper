import os
import glob

# Data for the Sunday Page
locations = [
    {
        "id": "zojoji-temple",
        "name": "Zojoji Temple",
        "type": "Temple",
        "address_en": "4-7-35 Shibakoen, Minato City, Tokyo 105-0011",
        "address_jp": "〒105-0011 東京都港区芝公園4-7-35",
        "desc": "The massive temple grounds are accessible early. Don't miss the Sangedatsumon Gate and Tokyo Tower view.",
        "map_query": "Zojoji+Temple+Tokyo"
    },
    {
        "id": "atago-shrine",
        "name": "Atago Shrine",
        "type": "Shrine",
        "address_en": "1-5-3 Atago, Minato City, Tokyo 105-0002",
        "address_jp": "〒105-0002 東京都港区愛宕1-5-3",
        "desc": "Famous for the steep 'Stone Steps of Success'. A serene power spot atop a hill.",
        "map_query": "Atago+Shrine+Tokyo"
    },
    {
        "id": "le-pain-quotidien-shiba",
        "name": "Le Pain Quotidien (Shiba Park)",
        "type": "Breakfast/Cafe",
        "address_en": "3-3-1 Shibakoen, Minato City, Tokyo 105-8560",
        "address_jp": "〒105-8560 東京都港区芝公園3-3-1",
        "desc": "Located directly in Shiba Park. Excellent coffee and bread baskets. Family-friendly.",
        "map_query": "Le+Pain+Quotidien+Shiba+Park"
    },
    {
        "id": "standard-products-ginza",
        "name": "Standard Products (Ginza)",
        "type": "Shopping",
        "address_en": "Marronnier Gate Ginza 2, 3-2-1 Ginza, Chuo City, Tokyo 104-0061",
        "address_jp": "〒104-0061 東京都中央区銀座3-2-1 マロニエゲート銀座2",
        "desc": "Minimalist, high-quality household goods. Located in Marronnier Gate Ginza 2 (6th Floor).",
        "map_query": "Standard+Products+Marronnier+Gate+Ginza"
    },
    {
        "id": "uniqlo-tokyo-ginza",
        "name": "Uniqlo Tokyo (Flagship)",
        "type": "Shopping",
        "address_en": "Marronnier Gate Ginza 2, 3-2-1 Ginza, Chuo City, Tokyo 104-0061",
        "address_jp": "〒104-0061 東京都中央区銀座3-2-1 マロニエゲート銀座2",
        "desc": "Global flagship store with custom t-shirt printing and flower shops inside.",
        "map_query": "Uniqlo+Tokyo+Ginza"
    },
    {
        "id": "itoya-ginza",
        "name": "G. Itoya (Ginza)",
        "type": "Stationery",
        "address_en": "2-7-15 Ginza, Chuo City, Tokyo 104-0061",
        "address_jp": "〒104-0061 東京都中央区銀座2-7-15",
        "desc": "A 12-story stationery store that feels like a museum. Opens at 10:00 AM on Sundays.",
        "map_query": "G.+Itoya+Ginza"
    },
    {
        "id": "ginza-miyuki-kan",
        "name": "Ginza Miyuki-kan",
        "type": "Dessert/Cafe",
        "address_en": "6-5-17 Ginza, Chuo City, Tokyo 104-0061",
        "address_jp": "〒104-0061 東京都中央区銀座6-5-17",
        "desc": "Legendary Mont Blanc cake (chestnut cream). Retro-European style kissaten atmosphere.",
        "map_query": "Ginza+Miyuki-kan+Main+Store"
    },
    {
        "id": "ginza-mitsukoshi",
        "name": "Ginza Mitsukoshi (Depachika)",
        "type": "Department Store",
        "address_en": "4-6-16 Ginza, Chuo City, Tokyo 104-8212",
        "address_jp": "〒104-8212 東京都中央区銀座4-6-16",
        "desc": "Explore the basement floors (Depachika) for art-like cakes, wagashi, and fruits.",
        "map_query": "Ginza+Mitsukoshi"
    },
    {
        "id": "don-quijote-roppongi",
        "name": "Don Quijote Roppongi",
        "type": "Shopping",
        "address_en": "3-14-10 Roppongi, Minato City, Tokyo 106-0032",
        "address_jp": "〒106-0032 東京都港区六本木3-14-10",
        "desc": "The chaos option. Sells everything from KitKats to luxury watches in a jungle-like display.",
        "map_query": "Don+Quijote+Roppongi"
    }
]

schedule = [
    ("07:00 - 08:30", "Walk Shiba Park, Zojoji Temple, and climb Atago Shrine stairs."),
    ("08:30 - 09:30", "Breakfast at Le Pain Quotidien (Shiba Park)."),
    ("10:00 - 10:30", "Transit to Ginza (Taxi recommended for ease)."),
    ("10:30 - 12:30", "Shop at Itoya (Stationery) and Marronnier Gate (Standard Products/Uniqlo)."),
    ("12:30", "Lunch in Ginza (plenty of options) + Mont Blanc for dessert."),
    ("Afternoon", "Walk the 'Pedestrian Paradise' on Ginza main street.")
]

# Sidebar links for consistency
sidebar_links = """
                <li><a href="index.html">Home</a></li>
                <li><a href="itinerary.html">Itinerary</a></li>
                <li><a href="sunday-schedule.html">Sunday Plan</a></li>
                <li><a href="suggestions.html">Suggestions</a></li>
                <li><a href="tips.html">Tips & Tricks</a></li>
                <li><a href="prince-park.html">Prince Park</a></li>
                <li><a href="words.html">Learn Words</a></li>
                <li><a href="phrases.html">Learn Phrases</a></li>
                <li><a href="install.html">Install App</a></li>
"""

# 1. Create Address Cards
for loc in locations:
    card_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{loc['name']} - Japan Trip 2025</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="manifest" href="../manifest.json">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <link rel="apple-touch-icon" href="../assets/infographics/app-icon.jpg">
    <link rel="icon" type="image/jpeg" href="../assets/infographics/app-icon.jpg">
</head>
<body>
    <div class="layout">
        <nav class="sidebar">
            <h2>Menu</h2>
            <ul>
{sidebar_links.replace('href="', 'href="../')}
            </ul>
        </nav>
        <main class="content">
            <div class="card-container">
                <div class="address-card">
                    <div class="card-header">
                        <div class="header-icon">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L2 22h20L12 2zm0 3.5l6 12.5H6l6-12.5z"/></svg>
                        </div>
                        <h2>こんにちは、この住所へ行きたいです<br><span style="font-size: 0.7em;">(Hi, I need to go to this address!)</span></h2>
                    </div>
                    <p style="text-align: center; color: #666; font-style: italic; margin-top: -10px; margin-bottom: 20px; font-size: 0.9em;">Show this to a taxi driver or friendly person.</p>
                    <div style="text-align: center; margin-bottom: 20px;">
                        <a href="https://www.google.com/maps/search/?api=1&query={loc['map_query']}" target="_blank" style="color: #007bff; font-weight: bold; text-decoration: none; font-size: 1.1em;">Google Maps</a>
                    </div>
                    
                    <div class="address-type">
                        TYPE: {loc['type']}
                    </div>

                    <div class="card-section">
                        <div class="section-title">行き先 (Destination)</div>
                        <div class="address-grid">
                            <div class="grid-header">Japanese (日本語)</div>
                            <div class="grid-header">English (英語)</div>
                            <div class="grid-content ja">...</div> <!-- Placeholder if no explicit JP name provided separate from address -->
                            <div class="grid-content">{loc['name']}</div>
                        </div>
                    </div>

                    <div class="card-section">
                        <div class="section-title">住所 (Address)</div>
                        <div class="address-grid">
                            <div class="grid-header">Japanese (日本語)</div>
                            <div class="grid-header">English (英語)</div>
                            <div class="grid-content ja">{loc['address_jp']}</div>
                            <div class="grid-content">{loc['address_en']}</div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </div>
    <script src="../js/sw-register.js"></script>
</body>
</html>
"""
    with open(f"src/cards/{loc['id']}.html", "w", encoding="utf-8") as f:
        f.write(card_html)
    print(f"Created card: src/cards/{loc['id']}.html")

# 2. Create Sunday Schedule Page
table_rows = ""
for loc in locations:
    table_rows += f"""
                    <tr>
                        <td>
                            <span class="location-type">{loc['type']}:</span>
                            <a href="cards/{loc['id']}.html" class="location-name">{loc['name']}</a>
                            <a href="https://www.google.com/maps/search/?api=1&query={loc['map_query']}" class="map-link" target="_blank">Google Maps</a>
                        </td>
                        <td class="description-text">{loc['desc']}</td>
                    </tr>
    """

schedule_rows = ""
for time, activity in schedule:
    schedule_rows += f"""
                    <tr>
                        <td style="font-weight: bold; width: 150px;">{time}</td>
                        <td>{activity}</td>
                    </tr>
    """

sunday_page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Sunday Strategy - Japan Trip 2025</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="manifest" href="manifest.json">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <link rel="apple-touch-icon" href="assets/infographics/app-icon.jpg">
    <link rel="icon" type="image/jpeg" href="assets/infographics/app-icon.jpg">
    <style>
        .address-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 40px;
        }}
        .address-table th, .address-table td {{
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #eee;
            vertical-align: top;
        }}
        .address-table th {{
            background-color: #6f42c1; /* Purple for Sunday Strategy */
            color: white;
            font-weight: bold;
            text-transform: uppercase;
            font-size: 0.9em;
        }}
        .address-table tr:hover {{
            background-color: #f9f9f9;
        }}
        .location-name {{
            font-weight: bold;
            font-size: 1.1em;
            color: #333;
            display: block;
            margin-bottom: 5px;
        }}
        .location-type {{
            font-size: 0.8em;
            color: #666;
            text-transform: uppercase;
            margin-right: 5px;
        }}
        .map-link {{
            display: inline-block;
            margin-top: 5px;
            color: #007bff;
            text-decoration: none;
            font-size: 0.9em;
        }}
        .map-link:hover {{
            text-decoration: underline;
        }}
        .description-text {{
            font-size: 0.95em;
            color: #555;
            line-height: 1.5;
        }}
        
        .schedule-section {{
            background-color: #fff3cd;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            border-left: 5px solid #ffc107;
        }}
        .schedule-section h2 {{
            margin-top: 0;
            color: #856404;
        }}
    </style>
</head>
<body>
    <div class="layout">
        <nav class="sidebar">
            <h2>Menu</h2>
            <ul>
{sidebar_links}
            </ul>
        </nav>
        <main class="content">
            <header>
                <h1>The Sunday Strategy</h1>
                <p style="font-size: 1.1em; color: #555;">Shiba Park Morning & Ginza Afternoon</p>
            </header>

            <section class="schedule-section">
                <h2>Suggested Schedule</h2>
                <table class="address-table" style="box-shadow: none; margin-top: 10px;">
                    <tbody>
{schedule_rows}
                    </tbody>
                </table>
            </section>

            <section>
                <h2>Sunday Locations</h2>
                <p>Click on any location name to see the address card.</p>
                <table class="address-table">
                    <thead>
                        <tr>
                            <th style="width: 30%;">Location</th>
                            <th style="width: 70%;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
{table_rows}
                    </tbody>
                </table>
            </section>
        </main>
    </div>
    <script src="js/sw-register.js"></script>
</body>
</html>
"""

with open("src/sunday-schedule.html", "w", encoding="utf-8") as f:
    f.write(sunday_page_html)
print("Created src/sunday-schedule.html")

# 3. Update Sidebar in other files
all_html_files = glob.glob('src/*.html') + glob.glob('src/cards/*.html')
target_link = 'sunday-schedule.html'

for file_path in all_html_files:
    if file_path.endswith('sunday-schedule.html'):
        continue # Already set
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if target_link in content:
        continue # Already has link
        
    # Logic to insert link
    # Insert after 'Itinerary'
    if file_path.startswith('src/cards/'):
        target = '<li><a href="../itinerary.html">Itinerary</a></li>'
        insert = '                <li><a href="../sunday-schedule.html">Sunday Plan</a></li>'
    else:
        target = '<li><a href="itinerary.html">Itinerary</a></li>'
        insert = '                <li><a href="sunday-schedule.html">Sunday Plan</a></li>'
        
    if target in content:
        new_content = content.replace(target, target + '\n' + insert)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated sidebar in {file_path}")
