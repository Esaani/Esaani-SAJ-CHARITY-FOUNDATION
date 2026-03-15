import os
import re

base_path = r"C:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file"

image_alt_map = {
    "cause-image1.jpg": "Royal Promise Outreach Aid for the Needy",
    "cause-image2.jpg": "Charity Showcases a Nation's Kindness",
    "cause-image3.jpg": "Beach clean up exercise",
    "cause-image4.jpg": "Help Children Rise out of Poverty",
    "cause-image5.jpg": "Provide Healthy Meals to an Impoverished Rural Child",
    "cause-single-image.jpg": "Cause Detail Main Image"
}

files_to_update = ['cause.html', 'cause-list.html', 'cause-single.html', 'cause-single-education-outreach.html', 'cause-single-royal-promise.html']

for filename in files_to_update:
    filepath = os.path.join(base_path, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    for img_name, alt_text in image_alt_map.items():
        pattern = r'(src="[^"]*' + img_name + r'")\s+alt="image"'
        replacement = r'\1 alt="' + alt_text + '"'
        new_content = re.sub(pattern, replacement, new_content)

    if filename == 'cause-single-education-outreach.html':
        new_content = re.sub(
            r'(src="[^"]*cause-single-image\.jpg")\s+alt="Cause Detail Main Image"',
            r'\1 alt="Education Outreach Program"',
            new_content
        )
        new_content = re.sub(
            r'(src="[^"]*cause-single-image\.jpg")\s+alt="image"',
            r'\1 alt="Education Outreach Program"',
            new_content
        )

    if filename == 'cause-single-royal-promise.html':
        new_content = re.sub(
            r'(src="[^"]*cause-single-image\.jpg")\s+alt="Cause Detail Main Image"',
            r'\1 alt="Royal Promise Outreach Program"',
            new_content
        )
        new_content = re.sub(
            r'(src="[^"]*cause-single-image\.jpg")\s+alt="image"',
            r'\1 alt="Royal Promise Outreach Program"',
            new_content
        )

    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated alt texts in {filename}")

print("Done updating alt texts.")
