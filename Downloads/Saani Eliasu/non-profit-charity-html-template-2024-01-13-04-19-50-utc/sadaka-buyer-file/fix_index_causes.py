import os
import re

base_path = r"C:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file"

files_to_update = [
    'index.html', 
    'index-2.html', 
    'index-one-page.html', 
    'index-2-one-page.html'
]

for filename in files_to_update:
    filepath = os.path.join(base_path, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    # 1. Update the link text and <br> across multiple lines for the Title
    # It looks like:
    # Construct\s+Dwellings\s+African Impoverished Women
    pattern = r'Construct\s+Dwellings\s+African\s+Impoverished\s+Women'
    replacement = r'Beach clean up exercise'
    new_content = re.sub(pattern, replacement, new_content)

    # 2. Update alt text (for the update_alts script and any existing alt text)
    # The previous script might not have caught it if it was alt="image" or something else
    
    # 3. Update the category tag from Medical to Environment
    tag_pattern = r'(<img src="assets/images/cause/cause-image3\.jpg"[^>]*>\s*)<span class="cause-tag">Medical</span>'
    tag_replace = r'\g<1><span class="cause-tag">Environment</span>'
    new_content = re.sub(tag_pattern, tag_replace, new_content)

    # Update the alt="image" to alt="Beach clean up exercise" for cause-image3.jpg specifically
    alt_pattern = r'(<img src="assets/images/cause/cause-image3\.jpg"\s+)alt="image"'
    alt_replace = r'\g<1>alt="Beach clean up exercise"'
    new_content = re.sub(alt_pattern, alt_replace, new_content)
    
    # Ensure goal is 40,000 (already is) and raised is 35,000 (already is in index.html, let's verify)
    # Actually wait, in index.html line 674 it says:
    # <h6>Raised : <span>GH₵35.000</span></h6>
    # So it's already 35k. I will just leave it.

    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")

print("Done updating Beach Clean Up cause in indexes.")
