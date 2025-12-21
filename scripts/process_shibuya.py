import re
import base64
import os

def process_shibuya_background():
    input_file = 'shibuya_background.md'
    output_dir = 'src/assets/photos/shibuya'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as f:
        lines = f.readlines()

    clean_lines = []
    image_map = {} # Map label -> filename

    # Pass 1: Extract definitions
    for line in lines:
        # Check if line is an image definition
        # Format: [image1]: <data:image/png;base64,.....>
        if line.startswith('[image') and '<data:image/' in line:
            try:
                # Naive parsing to avoid complex regex on huge strings
                label_end = line.find(']:')
                label = line[1:label_end] # image1
                
                type_start = line.find('image/') + 6
                type_end = line.find(';', type_start)
                img_ext = line[type_start:type_end]
                
                data_start = line.find('base64,') + 7
                data_end = line.find('>', data_start)
                b64_data = line[data_start:data_end]
                
                filename = f"{label}.{img_ext}"
                filepath = os.path.join(output_dir, filename)
                
                with open(filepath, "wb") as img_file:
                    img_file.write(base64.b64decode(b64_data))
                
                image_map[label] = f"assets/photos/shibuya/{filename}"
                
            except Exception as e:
                # If parsing fails, just keep the line? No, probably unwanted.
                # But let's just ignore errors and assume standard format for now.
                pass
        else:
            # We will handle usage replacement in Pass 2
            pass

    # Pass 2: Reconstruct content with replacements
    for line in lines:
        if line.startswith('[image') and '<data:image/' in line:
            continue # Skip definition lines
        
        # Replace usage: ![alt][image1] -> ![alt](path)
        # We can iterate over our found map
        current_line = line
        for label, path in image_map.items():
            # Replace [label] with (path) if it follows ]
            # Be careful not to replace other things.
            # Usage in MD is ![Alt Text][label]
            # We want to change it to ![Alt Text](path)
            
            # Simple string replace might be dangerous if label is common word, but "image1" is specific.
            # Regex for specific label usage:
            # (!\[.*?\])(\[label\]) -> \1(path)
            
            # Escape brackets for regex
            
            pattern = r'(!\[.*?\].*?)\[(' + label + r')\]'
            current_line = re.sub(pattern, f'\1({path})', current_line)
            
        clean_lines.append(current_line)

    print("".join(clean_lines))

if __name__ == "__main__":
    process_shibuya_background()