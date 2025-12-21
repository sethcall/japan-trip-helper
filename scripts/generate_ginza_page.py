import os
import glob

# Data for Ginza Shopping Page (Using Sunday data + Ginza Six + Don Quijote)
locations = [
    {
        "id": "standard-products-ginza",
        "name": "Standard Products",
        "jp_name": "スタンダードプロダクツ 銀座",
        "type": "Shopping",
        "category": "Home Goods",
        "map_query": "Standard+Products+Marronnier+Gate+Ginza",
        "desc": "Minimalist, high-quality household goods. Located in Marronnier Gate Ginza 2 (6th Floor)."
    },
    {
        "id": "uniqlo-tokyo-ginza",
        "name": "Uniqlo Tokyo",
        "jp_name": "ユニクロ 銀座店",
        "type": "Shopping",
        "category": "Clothing",
        "map_query": "Uniqlo+Tokyo+Ginza",
        "desc": "Global flagship store with custom t-shirt printing and flower shops inside."
    },
    {
        "id": "itoya-ginza",
        "name": "G. Itoya",
        "jp_name": "銀座・伊東屋",
        "type": "Stationery",
        "category": "Stationery",
        "map_query": "G.+Itoya+Ginza",
        "desc": "A 12-story stationery store that feels like a museum."
    },
    {
        "id": "ginza-six",
        "name": "Ginza Six",
        "jp_name": "GINZA SIX",
        "type": "Complex",
        "category": "Luxury / Art",
        "map_query": "Ginza+Six",
        "desc": "Luxury shopping complex with a rooftop garden and art installations."
    },
    {
        "id": "ginza-mitsukoshi",
        "name": "Ginza Mitsukoshi",
        "jp_name": "銀座三越",
        "type": "Depachika",
        "category": "Food / Gifts",
        "map_query": "Ginza+Mitsukoshi",
        "desc": "Explore the basement floors (Depachika) for art-like cakes, wagashi, and fruits."
    },
    {
        "id": "ginza-miyuki-kan",
        "name": "Ginza Miyuki-kan",
        "jp_name": "銀座みゆき館",
        "type": "Dessert",
        "category": "Cafe / Cake",
        "map_query": "Ginza+Miyuki-kan+Main+Store",
        "desc": "Legendary Mont Blanc cake (chestnut cream). Retro-European style kissaten atmosphere."
    },
    {
        "id": "don-quijote-ginza",
        "name": "Don Quijote Ginza",
        "jp_name": "ドン・キホーテ 銀座本館",
        "type": "Shopping",
        "category": "Chaos / Souvenirs",
        "map_query": "Don+Quijote+Ginza+Honkan",
        "desc": "The chaos option in Ginza. Sells everything from KitKats to luxury watches."
    }
]

# Generate Table Rows
table_rows = ""
for loc in locations:
    table_rows += f"""
                        <tr>
                            <td>
                                <span class="location-type">{loc['type']}:</span>
                                <a href="cards/{loc['id']}.html" class="location-name">{loc['name']}</a>
                                <span style="font-size:0.8em; display:block; color:#777;">{loc['jp_name']}</span>
                                <a href="https://www.google.com/maps/search/?api=1&query={loc['map_query']}" class="map-link" target="_blank">Google Maps</a>
                            </td>
                            <td><span style="display:inline-block; padding: 4px 8px; background-color: #eee; border-radius: 4px; font-size: 0.85em; font-weight: bold; color: #555;">{loc['category']}</span></td>
                            <td class="description-text">{loc['desc']}</td>
                        </tr>
    """

page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ginza Shopping - Japan Trip 2025</title>
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
            background-color: #6c757d; /* Gray for Shopping */
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
    </style>
</head>
<body>
    <div class="layout">
        <nav class="sidebar">
            <h2>Menu</h2>
            <ul>
                <!-- Sidebar will be updated by script -->
                REPLACE_ME_SIDEBAR
            </ul>
        </nav>
        <main class="content">
            <header>
                <h1>Ginza Shopping</h1>
            </header>

            <section style="text-align: center; margin-bottom: 30px;">
                <img src="assets/photos/ginza.jpg" alt="Ginza District" style="max-width: 30%; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <p style="font-size: 1.1em; color: #555; margin-top: 15px;">A guide to shopping in Tokyo's premier district.</p>
            </section>

            <section>
                <h2>Ginza Shopping Directory</h2>
                <table class="address-table">
                    <thead>
                        <tr>
                            <th style="width: 30%;">Location</th>
                            <th style="width: 15%;">Category</th>
                            <th style="width: 55%;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
{table_rows}
                    </tbody>
                </table>
            </section>

            <section class="detailed-guide" style="background: white; padding: 30px; border-radius: 8px; margin-top: 40px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                <h2 style="color: #007bff; border-bottom: 2px solid #eee; padding-bottom: 10px;">Detailed Guide (Original Content)</h2>
                
                <h3>The "Norma" Shop: Standard Products (Ginza Flagship)</h3>
                <p>This is likely <strong>Standard Products</strong>, a new brand by Daiso that has become a massive hit in Japan. It features minimalist, high-quality household goods (often compared to Muji but cheaper).</p>
                <ul>
                    <li><strong>Location:</strong> <strong>Marronnier Gate Ginza 2</strong> (6th Floor).</li>
                    <li><strong>Why it fits:</strong> It opens at 11:00 AM. This complex houses the global flagships for <strong>DAISO</strong>, <strong>Standard Products</strong>, and <strong>THREEPPY</strong> all on one floor. It is the ultimate destination for "quirky," useful, and uniquely Japanese affordable goods.</li>
                </ul>

                <h3>Uniqlo Tokyo (Flagship)</h3>
                <p>Also in Marronnier Gate. This is the global flagship with custom t-shirt printing and flower shops inside.</p>

                <h3>Itoya (Stationery)</h3>
                <p>A 12-story stationary store that feels like a museum. It opens at 10:00 AM on Sundays, making it a perfect first stop before Standard Products opens.</p>

                <h3>Pedestrian Paradise</h3>
                <p>From 12:00 PM on Sundays, the main street of Ginza (Chuo-dori) is closed to cars, allowing you to walk freely in the middle of the road.</p>

                <h3>Department Store Basements (Depachika)</h3>
                <p><strong>Ginza Mitsukoshi</strong> or <strong>Matsuya Ginza</strong> (Basement floors). If the family can't decide, go here. You will find glass cases filled with art-like cakes, wagashi (traditional sweets), and fruits. It is a visual spectacle and you can buy individual items to bring back to the hotel.</p>
                
                <h3>The "Quirky" & Culture Fix</h3>
                <h4>Advertising Museum Tokyo (Caretta Shiodome)</h4>
                <ul>
                    <li><strong>Why:</strong> If you walk from Hamamatsucho towards Ginza, you pass Shiodome. This free museum showcases the history of Japanese advertising. It is fascinatingly "quirky" to see how Japan marketed products in the Edo period vs. today.</li>
                    <li><strong>Note:</strong> Closed Sundays and Mondays. <em>Since today is Sunday, skip this for today and visit later in the week if interested.</em></li>
                </ul>

                <h4>Don Quijote (Roppongi or Ginza)</h4>
                <ul>
                    <li><strong>The Ultimate Quirky Shop:</strong> If "Standard Products" is too clean for you, <strong>Don Quijote</strong> is the chaos option. The Roppongi store is near your hotel, but the <strong>Mega Don Quijote in Shibuya</strong> is the most famous. It sells everything from KitKats to luxury watches in a jungle-like display.</li>
                </ul>
            </section>
        </main>
    </div>
    <script src="js/sw-register.js"></script>
</body>
</html>
"""

# Write the file
with open("src/ginza-shopping.html", "w", encoding="utf-8") as f:
    f.write(page_html)

# Update Sidebars
root_files = glob.glob('src/*.html')
card_files = glob.glob('src/cards/*.html')

for file_path in root_files + card_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'REPLACE_ME_SIDEBAR' in content:
        sidebar = """
                <li><a href="{p}index.html">Home</a></li>
                <li><a href="{p}itinerary.html">Itinerary</a></li>
                <li><a href="{p}sunday-schedule.html">Sunday Plan</a></li>
                <li><a href="{p}ginza-shopping.html">Ginza Shopping</a></li>
                <li><a href="{p}shibuya.html">Shibuya & Harajuku</a></li>
                <li><a href="{p}akihabara.html">Akihabara Arcade</a></li>
                <li><a href="{p}suggestions.html">Suggestions</a></li>
                <li><a href="{p}tips.html">General Travel Tips</a></li>
                <li><a href="{p}prince-park.html">Prince Park</a></li>
                <li><a href="{p}subway-tips.html">Subway Tips</a></li>
                <li><a href="{p}currency.html">Yen/Dollar</a></li>
                <li><a href="{p}words.html">Learn Words</a></li>
                <li><a href="{p}phrases.html">Learn Phrases</a></li>
                <li><a href="{p}install.html">Install App</a></li>
        """
        prefix = "../" if "/cards/" in file_path else ""
        new_sidebar = sidebar.format(p=prefix)
        content = content.replace("REPLACE_ME_SIDEBAR", new_sidebar)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)