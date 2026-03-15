import os
import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements for Beach Clean Up
    # Goal: Link to cause-single-beach-clean-up.html
    # Handle both heading links and button links
    
    # 1. Heading links for Beach Clean Up
    content = content.replace(
        '<a href="cause-single.html" class="primary-hover">Beach clean up exercise',
        '<a href="cause-single-beach-clean-up.html" class="primary-hover">Beach clean up exercise'
    )
    
    # 2. Heading links for Healthy Meals (multiline)
    content = re.sub(
        r'<a href="cause-single\.html" class="primary-hover">Provide(\s+)Healthy(\s+)Meals to(\s+)an Impoverished Rural Child</a>',
        r'<a href="cause-single-healthy-meals.html" class="primary-hover">Provide\1Healthy\2Meals to\3an Impoverished Rural Child</a>',
        content,
        flags=re.MULTILINE
    )

    # 3. Button links which usually point to royal-promise or cause-single
    # We need to be careful here to only replace buttons in the specific sections.
    # However, since we are doing this per file, and the images are unique in those sections, 
    # we can try to find the specific swiper-slide blocks.
    
    # For index-one-page.html and index.html, the slider sections are repetitive.
    # I'll use a more targeted approach for buttons by looking at the context.
    
    # Find all swiper-slides
    slides = re.findall(r'<div class="swiper-slide">.*?</div>\s+</div>\s+</div>', content, re.DOTALL)
    
    for slide in slides:
        if 'cause-image3.jpg' in slide or 'Beach clean up exercise' in slide:
            new_slide = slide.replace('cause-single-royal-promise.html#donation-section', 'cause-single-beach-clean-up.html')
            new_slide = new_slide.replace('cause-single.html#donation-section', 'cause-single-beach-clean-up.html')
            content = content.replace(slide, new_slide)
        elif 'cause-image4.jpg' in slide or 'Impoverished Rural Child' in slide:
            new_slide = slide.replace('cause-single-royal-promise.html#donation-section', 'cause-single-healthy-meals.html')
            new_slide = new_slide.replace('cause-single.html#donation-section', 'cause-single-healthy-meals.html')
            content = content.replace(slide, new_slide)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

files_to_update = [
    'index-one-page.html',
    'index.html',
    'cause.html',
    'cause-list.html'
]

working_dir = r"c:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file"

for filename in files_to_update:
    filepath = os.path.join(working_dir, filename)
    if os.path.exists(filepath):
        print(f"Updating {filename}...")
        update_file(filepath)
    else:
        print(f"Skipping {filename} (not found).")
