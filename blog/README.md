# Blog Processing

## Days

Days are in blog/YYYY_MM_DD, and images can be found within each day folder.

Any png or mv named IMG_XXXX* is an original image, and we don't want these shown on the website as they are huge... but we might actually to let you see thes raw one's if you click the preview. 

Anytime these are encountered with out a complimentary IMG_XXXX_preview.* file of the same name, then we need to process these with imagemagick, such that they are web ready ( i.e, say 720px wide at the most, and whatever quality options can be reduced to still be web ready). 

So do that when asked to add a blog entry.   

In terms of blog entries, let's do this.

As a top-left nav option ,we can have 'Blog: Dec 21, Thursady' (no need for year).  You would do such a blog corresponding to blog/2025-12-21 being present, for instance.
Any file you find in the blog called like notes.md, then use that to populate the text of the blog day, at the top of the page.  Any IMG_XXXX_preview.png files you find, or .mov, sshould be created in a gallery view below that top text. 

When you click the preview of an image, we can show a popup with the full version, also with a button to download the original file.

## Automation

We have established a script to automate the blog creation process.

1.  **Preparation**:
    *   Ensure `blog/YYYY-MM-DD/` exists.
    *   Ensure `notes.md` is present in that directory.
    *   Ensure images (`IMG_*.png`, `IMG_*.mov`) are present.
    
2.  **Image Processing**:
    *   Generate preview images:
        ```bash
        cd blog/YYYY-MM-DD
        for f in *.png; do magick "$f" -resize "720x>" "${f%.*}_preview.png"; done
        ```
    
3.  **Asset Deployment**:
    *   Copy the `blog/YYYY-MM-DD` directory to `src/assets/blog/YYYY-MM-DD`.
        ```bash
        mkdir -p src/assets/blog/YYYY-MM-DD
        cp blog/YYYY-MM-DD/* src/assets/blog/YYYY-MM-DD/
        ```
    
4.  **HTML Generation**:
    *   Run the python script:
        ```bash
        python3 scripts/create_blog_post.py YYYY-MM-DD
        ```
    *   This generates `src/blog-YYYY-MM-DD.html`.
    
5.  **Navigation Update**:
    *   The script adds the link to the generated file, but you must manually update `src/index.html` and other pages to include the new blog link in the sidebar if desired globally.