import re
import os
import base64

def extract_images():
    md_file = 'shibuya_crossing_train_guide.md'
    output_dir = 'src/assets/photos/shibuya'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(md_file, 'r') as f:
        content = f.read()
        
    # Find all image definitions: [imageX]: <data:image/png;base64,...>
    matches = re.findall(r'\[(image\d+)\]:\s*<data:image/(png|jpeg|jpg);base64,([^>]+)>', content)
    
    print(f"Found {len(matches)} images.")
    
    # We need to offset the image numbering to avoid overwriting existing images in shibuya folder
    # Existing images are image1, image2, image3. Let\'s start from image4.
    
    start_index = 4
    image_map = {} # Map old ID to new filename
    
    for i, (img_id, ext, b64_data) in enumerate(matches):
        try:
            # Decode base64
            img_data = base64.b64decode(b64_data)
            
            # Determine new filename
            new_id = f"image{start_index + i}"
            filename = f"{new_id}.{ext}"
            output_path = os.path.join(output_dir, filename)
            
            # Write to file
            with open(output_path, 'wb') as f:
                f.write(img_data)
            
            print(f"Saved {output_path}")
            image_map[img_id] = filename
            
        except Exception as e:
            print(f"Error saving {img_id}: {e}")
            
    return image_map

def format_content(text, image_map):
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    return text

def markdown_to_html(md_text, image_map):
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

        # Headers - Shift levels down by 1 to fit into existing page hierarchy (h1 -> h2)
        if line.startswith('# '):
            content = format_content(line[2:], image_map)
            html_lines.append(f'<h2>{content}</h2>')
        elif line.startswith('## '):
            content = format_content(line[3:], image_map)
            html_lines.append(f'<h3>{content}</h3>')
        elif line.startswith('### '):
            content = format_content(line[4:], image_map)
            html_lines.append(f'<h4>{content}</h4>')
        elif line.startswith('#### '):
            content = format_content(line[5:], image_map)
            html_lines.append(f'<h5>{content}</h5>')
        
        # Reference Style Images ![][image1]
        elif line.startswith('![][image'):
            # Extract the image number
            match = re.search(r'image(\d+)', line)
            if match:
                old_id = f"image{match.group(1)}"
                if old_id in image_map:
                    filename = image_map[old_id]
                    src = f"assets/photos/shibuya/{filename}"
                    html_lines.append(f'<img src="{src}" alt="Shibuya Train Guide Image" style="max-width:100%; height:auto; margin: 20px 0; display:block;">')
            else:
                html_lines.append(f'<p><em>Image placeholder: {line}</em></p>')

        # Lists
        elif line.startswith('* '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            content = line[2:]
            content = format_content(content, image_map)
            html_lines.append(f'<li>{content}</li>')
        
        # Standard Paragraphs
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            
            content = format_content(line, image_map)
            html_lines.append(f'<p>{content}</p>')
            
    if in_list:
        html_lines.append('</ul>')
        
    return '\n'.join(html_lines)

def update_shibuya_page():
    # 1. Extract Images
    image_map = extract_images()
    
    # 2. Read Markdown Content
    with open('shibuya_crossing_train_guide.md', 'r') as f:
        md_content = f.read()
    
    # 3. Convert to HTML
    train_guide_html = markdown_to_html(md_content, image_map)
    
    # 4. Update src/shibuya.html
    shibuya_path = 'src/shibuya.html'
    with open(shibuya_path, 'r') as f:
        html_content = f.read()
        
    # Find insertion point: Before the "Works cited" section or end of background content
    # The current page has a specific structure. Let\'s look for the <h4><strong>Works cited</strong></h4> or similar anchor.
    # In previous turns, we saw <h4><strong>Works cited</strong></h4> (generated from bold).
    
    insertion_marker = "<h4><strong>Works cited</strong></h4>"
    
    if insertion_marker in html_content:
        # Insert before Works cited
        new_content = html_content.replace(insertion_marker, f"{train_guide_html}\n{insertion_marker}")
    else:
        # Append to the end of the background-content section
        # Look for closing section tag
        new_content = html_content.replace("</section>\n        </main>", f"{train_guide_html}\n</section>\n        </main>")
        
    with open(shibuya_path, 'w') as f:
        f.write(new_content)
        
    print(f"Updated {shibuya_path} with Train Watching Guide.")

if __name__ == "__main__":
    update_shibuya_page()