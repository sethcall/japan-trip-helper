import re
import os

def parse_dessert_markdown(content):
    locations = []
    lines = content.split('\n')
    
    # Pre-defined locations based on the input to ensure accuracy
    location_names = [
        "Roasted COFFEE LABORATORY",
        "Good good not bad",
        "THE MATCHA TOKYO HARAJUKU",
        "Colombin Harajuku",
        "NOA COFFEE",
        "Sadaharu AOKI"
    ]
    
    for name in location_names:
        try:
            # Find the start of the section for this location
            start_marker = f"{name} Click to open side panel"
            start_idx = -1
            
            for idx, line in enumerate(lines):
                if start_marker in line:
                    start_idx = idx
                    break
            
            if start_idx != -1:
                # Basic info
                loc = {
                    "name": name,
                    "desc": "",
                    "type": "Dessert/Cafe",
                    "highlights": "",
                    "map": ""
                }
                
                # Get Description (usually next line or next non-empty line)
                for k in range(start_idx + 1, len(lines)):
                    if lines[k].strip():
                        loc["desc"] = lines[k].strip()
                        break
                
                # Iterate until next location or end to find details
                for j in range(start_idx + 1, len(lines)):
                    line = lines[j].strip()
                    if "Click to open side panel" in line and not line.startswith(name):
                        break
                        
                    if line.startswith("* **Best for:**"):
                        loc["type"] = line.replace("* **Best for:**", "").strip()
                    elif line.startswith("* **Highlights:**"):
                        loc["highlights"] = line.replace("* **Highlights:**", "").strip()
                    elif line.startswith("* **Map:**"):
                        match = re.search(r'\((.*?)\)', line)
                        if match:
                            loc["map"] = match.group(1)
                            
                locations.append(loc)
        except Exception as e:
            print(f"Error parsing {name}: {e}")
            
    return locations

def generate_html_table(locations):
    html = """
            <section>
                <h2>Suggested Desserts & Coffee</h2>
                <p>Popular spots located directly along or very close to your route.</p>
                <table class="address-table">
                    <thead>
                        <tr>
                            <th style="width: 30%;">Location</th>
                            <th style="width: 70%;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
    """
    
    for loc in locations:
        row = f"""
                        <tr>
                            <td>
                                <span class="location-type">{loc['type']}</span>
                                <span class="location-name">{loc['name']}</span>
                                <a href="{loc['map']}" class="map-link" target="_blank">Google Maps</a>
                            </td>
                            <td class="description-text">
                                {loc['desc']}<br>
                                <div style="margin-top:5px;"><strong>Highlights:</strong> {loc.get('highlights', '')}</div>
                            </td>
                        </tr>
        """
        html += row
        
    html += """
                    </tbody>
                </table>
            </section>
    """
    return html

def generate_background_content(content):
    html = '<section class="detailed-guide" style="background: white; padding: 30px; border-radius: 8px; margin-top: 40px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">'
    html += '<h2 style="color: #0056b3; border-bottom: 2px solid #e7f3ff; padding-bottom: 10px;">Dessert & Coffee Guide Details</h2>'
    
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("###"):
            html += f"<h3>{line.replace('###', '').replace('**', '').strip()}</h3>"
        elif "Click to open side panel" in line:
            title = line.split(" Click to open")[0].strip()
            if "Star rating" not in line:
                 html += f"<h4>{title}</h4>"
        elif line.startswith("*"):
            clean_line = line.replace("*", "", 1).strip()
            clean_line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', clean_line)
            clean_line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', clean_line)
            html += f"<ul><li>{clean_line}</li></ul>"
        elif "Star rating" in line or line.startswith("Opens in a new window"):
            continue
        else:
            if not line.startswith("Here are some"):
                 html += f"<p>{line}</p>"

    html += "</section>"
    return html

def update_monday_page():
    md_file = 'monday_plan_desserts.md'
    html_file = 'src/monday-schedule.html'
    
    with open(md_file, 'r') as f:
        md_content = f.read()
        
    locations = parse_dessert_markdown(md_content)
    table_html = generate_html_table(locations)
    background_html = generate_background_content(md_content)
    
    with open(html_file, 'r') as f:
        page_content = f.read()
        
    new_section = table_html + "\n" + background_html
    
    parts = page_content.rsplit('</main>', 1)
    if len(parts) == 2:
        new_page_content = parts[0] + new_section + "\n        </main>" + parts[1]
        
        with open(html_file, 'w') as f:
            f.write(new_page_content)
        print("Updated src/monday-schedule.html")
    else:
        print("Could not find closing main tag")

if __name__ == "__main__":
    update_monday_page()