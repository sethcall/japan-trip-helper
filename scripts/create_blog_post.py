import os
import sys
import glob
from datetime import datetime

def create_blog_post(date_str):
    blog_dir = f"blog/{date_str}"
    if not os.path.exists(blog_dir):
        print(f"Error: Directory {blog_dir} does not exist.")
        sys.exit(1)

    # Read notes
    notes_path = os.path.join(blog_dir, "notes.md")
    if not os.path.exists(notes_path):
        print(f"Error: {notes_path} does not exist.")
        sys.exit(1)

    with open(notes_path, 'r') as f:
        content = f.read()

    # Split title and body
    lines = content.strip().split('\n')
    title = lines[0].replace('# ', '').strip()
    body_paragraphs = []
    current_para = []
    
    for line in lines[1:]:
        if line.strip():
            current_para.append(line.strip())
        else:
            if current_para:
                body_paragraphs.append(" ".join(current_para))
                current_para = []
    if current_para:
        body_paragraphs.append(" ".join(current_para))

    # Find images
    assets_dir = f"src/assets/blog/{date_str}"
    web_assets_path = f"assets/blog/{date_str}"
    
    previews = sorted(glob.glob(os.path.join(blog_dir, "*_preview.png")))
    movies = sorted(glob.glob(os.path.join(blog_dir, "*.mov")))

    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    date_formatted = date_obj.strftime('%b %d, %A')

    # CSS
    css_styles = """
        .blog-content {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        .blog-text {
            font-size: 1.1em;
            line-height: 1.6;
            color: #333;
            margin-bottom: 20px;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 15px;
            margin-top: 30px;
        }
        .gallery-item {
            position: relative;
            cursor: pointer;
            overflow: hidden;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        .gallery-item:hover {
            transform: scale(1.02);
        }
        .gallery-item img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            display: block;
        }
        .video-item {
            width: 100%;
            border-radius: 8px;
            margin-bottom: 15px;
        }
        
        /* Modal */
        .modal {
            display: none; 
            position: fixed; 
            z-index: 1000; 
            left: 0;
            top: 0;
            width: 100%; 
            height: 100%; 
            overflow: auto; 
            background-color: rgba(0,0,0,0.9); 
        }
        .modal-content {
            margin: auto;
            display: block;
            max-width: 90%;
            max-height: 80vh;
            margin-top: 50px;
        }
        .modal-caption {
            margin: auto;
            display: block;
            width: 80%;
            max-width: 700px;
            text-align: center;
            color: #ccc;
            padding: 10px 0;
            height: 150px;
        }
        .close {
            position: absolute;
            top: 15px;
            right: 35px;
            color: #f1f1f1;
            font-size: 40px;
            font-weight: bold;
            transition: 0.3s;
            cursor: pointer;
        }
        .download-btn {
            display: inline-block;
            background-color: #d63384;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 10px;
        }
    """

    # Assemble HTML
    html_parts = []
    html_parts.append('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    html_parts.append('    <meta charset="UTF-8">\n')
    html_parts.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    html_parts.append(f'    <title>{title} - Japan Trip 2025</title>\n')
    html_parts.append('    <link rel="stylesheet" href="css/style.css">\n')
    html_parts.append('    <style>\n')
    html_parts.append(css_styles)
    html_parts.append('    </style>\n')
    html_parts.append('    <link rel="manifest" href="manifest.json">\n')
    html_parts.append('</head>\n<body>\n')
    html_parts.append('    <div class="layout">\n')
    html_parts.append('        <nav class="sidebar">\n')
    html_parts.append('            <h2>Menu</h2>\n')
    html_parts.append('            <ul>\n')
    html_parts.append('                <li><a href="index.html">Home</a></li>\n')
    html_parts.append('                <li><a href="itinerary.html">Itinerary</a></li>\n')
    html_parts.append('                <li><a href="sunday-schedule.html">Sunday Plan</a></li>\n')
    html_parts.append('                <li><a href="ginza-shopping.html">Ginza Shopping</a></li>\n')
    html_parts.append('                <li><a href="shibuya.html">Shibuya & Harajuku</a></li>\n')
    html_parts.append('                <li><a href="akihabara.html">Akihabara Arcade</a></li>\n')
    html_parts.append('                <li><a href="suggestions.html">Suggestions</a></li>\n')
    html_parts.append('                <li><a href="tips.html">General Travel Tips</a></li>\n')
    html_parts.append('                <li><a href="prince-park.html">Prince Park</a></li>\n')
    html_parts.append('                <li><a href="subway-tips.html">Subway Tips</a></li>\n')
    html_parts.append('                <li><a href="currency.html">Yen/Dollar</a></li>\n')
    html_parts.append('                <li><a href="words.html">Learn Words</a></li>\n')
    html_parts.append('                <li><a href="phrases.html">Learn Phrases</a></li>\n')
    html_parts.append('                <li><a href="install.html">Install App</a></li>\n')
    html_parts.append(f'                <li><a href="blog-{date_str}.html" class="active">Blog: {date_formatted}</a></li>\n')
    html_parts.append('            </ul>\n')
    html_parts.append('        </nav>\n')
    html_parts.append('        <main class="content">\n')
    html_parts.append('            <header>\n')
    html_parts.append(f'                <h1>{title}</h1>\n')
    html_parts.append('            </header>\n')
    html_parts.append('\n            <div class="blog-content">\n')

    import re

    for para in body_paragraphs:
        # Simple markdown bold parsing
        para = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', para)
        html_parts.append(f'                <p class="blog-text">{para}</p>\n')

    html_parts.append('                <h2>Gallery</h2>\n')
    html_parts.append('                <div class="gallery">\n')

    for p in previews:
        filename = os.path.basename(p)
        original_filename = filename.replace('_preview.png', '.png')
        img_src = f"{web_assets_path}/{filename}"
        orig_src = f"{web_assets_path}/{original_filename}"
        
        html_parts.append(f'                    <div class="gallery-item" onclick="openModal(\'{img_src}\', \'{orig_src}\')">\n')
        html_parts.append(f'                        <img src="{img_src}" alt="Gallery Image">\n')
        html_parts.append('                    </div>\n')

    html_parts.append('                </div>\n')
    html_parts.append('                <h2>Videos</h2>\n')
    html_parts.append('                <div class="video-gallery">\n')

    for m in movies:
        filename = os.path.basename(m)
        vid_src = f"{web_assets_path}/{filename}"
        html_parts.append('                    <div class="video-item">\n')
        html_parts.append('                        <video controls width="100%">\n')
        html_parts.append(f'                            <source src="{vid_src}" type="video/mp4">\n')
        html_parts.append(f'                            <source src="{vid_src}" type="video/quicktime">\n')
        html_parts.append('                            Your browser does not support the video tag.\n')
        html_parts.append('                        </video>\n')
        html_parts.append(f'                        <p><a href="{vid_src}" download>Download Video</a></p>\n')
        html_parts.append('                    </div>\n')

    html_parts.append('            </div>\n')
    html_parts.append('        </main>\n')
    html_parts.append('    </div>\n')
    html_parts.append('\n    <!-- Modal -->\n')
    html_parts.append('    <div id="myModal" class="modal">\n')
    html_parts.append('        <span class="close" onclick="closeModal()">&times;</span>\n')
    html_parts.append('        <img class="modal-content" id="img01">\n')
    html_parts.append('        <div class="modal-caption">\n')
    html_parts.append('            <a id="downloadLink" href="#" class="download-btn" download>Download Original</a>\n')
    html_parts.append('        </div>\n')
    html_parts.append('    </div>\n')
    html_parts.append('\n    <script>\n')
    html_parts.append('        function openModal(previewSrc, originalSrc) {\n')
    html_parts.append('            var modal = document.getElementById("myModal");\n')
    html_parts.append('            var modalImg = document.getElementById("img01");\n')
    html_parts.append('            var downloadLink = document.getElementById("downloadLink");\n')
    html_parts.append('            \n')
    html_parts.append('            modal.style.display = "block";\n')
    html_parts.append('            modalImg.src = originalSrc;\n')
    html_parts.append('            downloadLink.href = originalSrc;\n')
    html_parts.append('        }\n')
    html_parts.append('\n')
    html_parts.append('        function closeModal() {\n')
    html_parts.append('            var modal = document.getElementById("myModal");\n')
    html_parts.append('            modal.style.display = "none";\n')
    html_parts.append('        }\n')
    html_parts.append('        \n')
    html_parts.append('        window.onclick = function(event) {\n')
    html_parts.append('            var modal = document.getElementById("myModal");\n')
    html_parts.append('            if (event.target == modal) {\n')
    html_parts.append('                modal.style.display = "none";\n')
    html_parts.append('            }\n')
    html_parts.append('        }\n')
    html_parts.append('    </script>\n')
    html_parts.append('    <script src="js/sw-register.js"></script>\n')
    html_parts.append('</body>\n</html>\n')

    full_html = "".join(html_parts)
    
    output_file = f"src/blog-{date_str}.html"
    with open(output_file, 'w') as f:
        f.write(full_html)
    
    print(f"Created {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_blog_post.py YYYY-MM-DD")
        sys.exit(1)
    
    create_blog_post(sys.argv[1])
