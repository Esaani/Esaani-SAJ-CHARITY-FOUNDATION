import os

dir_path = r"C:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file"
old_title_single = "Aiding the Homeless Population in South Africa"
new_title = "School Books Support Project for Orphanage and Needy Students"

old_title_split_1 = "Aiding the Homeless Population"
old_title_split_2 = "in South Africa"
new_title_split_1 = "School Books Support Project for"
new_title_split_2 = "Orphanage and Needy Students"

for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # Replace single line occurrences
        if old_title_single in content:
            content = content.replace(old_title_single, new_title)
            changed = True
            
        # Replace multi-line occurrences (often found in sliders or titles)
        if "Aiding the Homeless" in content:
             content = content.replace(
                "Aiding the Homeless <br> Population in <br> South Africa", 
                "School Books Support Project <br> for Orphanage <br> and Needy Students"
             )
             content = content.replace(
                "Aiding the Homeless \n                                    Population in \n                                    South Africa", 
                "School Books Support Project \n                                    for Orphanage \n                                    and Needy Students"
             )
             content = content.replace(
                "Aiding the Homeless \n                                Population in \n                                South Africa", 
                "School Books Support Project \n                                for Orphanage \n                                and Needy Students"
             )

             # Project grid items
             content = content.replace(
                 "Aiding the Homeless Population <br>\n                                        in South Africa",
                 "School Books Support Project <br>\n                                        for Orphanage and Needy Students"
             )

             # Attempt a regex replace for the split version just in case
             import re
             content = re.sub(
                 r'Aiding the Homeless\s*<br>\s*Population in\s*<br>\s*South Africa',
                 r'School Books Support Project <br> for Orphanage <br> and Needy Students',
                 content
             )
             content = re.sub(
                 r'Aiding the Homeless\s*Population\s*<br>\s*in South Africa',
                 r'School Books Support Project <br> for Orphanage and Needy Students',
                 content
             )
             
             # Also replace the single line "Aiding the Homeless Population in South Africa"
             content = re.sub(r'Aiding the Homeless Population in South Africa', new_title, content)
             changed = True


        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
