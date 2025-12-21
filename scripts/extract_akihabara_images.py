import re
import os
import base64

def extract_images():
    md_file = 'akihabara_shopping.md'
    output_dir = 'src/assets/photos/akihabara'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(md_file, 'r') as f:
        content = f.read()
        
    # Find all image definitions: [imageX]: <data:image/png;base64,...>
    # The regex needs to capture the ID and the base64 data.
    # Note: The data might span multiple lines if wrapped, but usually in these dumps it's one long line.
    # The truncated output showed <data:image/png;base64,....  we need to handle the closing >
    
    matches = re.findall(r'\[(image\d+)\]:\s*<data:image/(png|jpeg|jpg);base64,([^>]+)>', content)
    
    print(f"Found {len(matches)} images.")
    
    for img_id, ext, b64_data in matches:
        try:
            # Decode base64
            img_data = base64.b64decode(b64_data)
            
            # Determine filename
            filename = f"{img_id}.{ext}"
            output_path = os.path.join(output_dir, filename)
            
            # Write to file
            with open(output_path, 'wb') as f:
                f.write(img_data)
            
            print(f"Saved {output_path}")
            
        except Exception as e:
            print(f"Error saving {img_id}: {e}")

if __name__ == "__main__":
    extract_images()
