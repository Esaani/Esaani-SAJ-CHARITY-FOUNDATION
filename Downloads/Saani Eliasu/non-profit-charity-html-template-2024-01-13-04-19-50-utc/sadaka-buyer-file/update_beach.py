import os
import re

base_path = r"C:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file"

files_to_update = ['cause.html', 'cause-list.html', 'update_alts.py']

for filename in files_to_update:
    filepath = os.path.join(base_path, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    # 1. Update the link text and <br> across multiple lines
    pattern = r'Construct Dwellings\s*African\s*<br>\s*Impoverished Women'
    replacement = r'Beach clean up <br> exercise'
    new_content = re.sub(pattern, replacement, new_content)

    # 2. Update alt text (for the update_alts script and any existing alt text)
    new_content = new_content.replace('Construct Dwellings African Impoverished Women', 'Beach clean up exercise')
    
    # 3. Update the category tag from Medical to Environment (specifically for this cause block)
    # The structure looks like:
    # <img src="assets/images/cause/cause-image3.jpg" alt="Beach clean up exercise">
    # <span class="cause-tag">Medical</span>
    tag_pattern = r'(<img src="assets/images/cause/cause-image3\.jpg"[^>]*>\s*)<span class="cause-tag">Medical</span>'
    tag_replace = r'\g<1><span class="cause-tag">Environment</span>'
    new_content = re.sub(tag_pattern, tag_replace, new_content)

    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")

print("Done updating Beach Clean Up cause.")
