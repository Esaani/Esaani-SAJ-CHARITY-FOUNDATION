import os
import re

dir_path = r"C:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file"

for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Replace single line occurrences
        content = content.replace("Aiding the Homeless Population in South Africa", "School Books Support Project for Orphanage and Needy Students")
        
        # Replace occurrences in causes/projects list where it might be split with <br> or newlines
        content = re.sub(
            r'Aiding the Homeless\s*<br>\s*Population in\s*<br>\s*South Africa',
            'School Books Support Project <br> for Orphanage <br> and Needy Students',
            content
        )
        content = re.sub(
            r'Aiding the Homeless\s*\n\s*Population in\s*\n\s*South Africa',
            'School Books Support Project \n                                    for Orphanage \n                                    and Needy Students',
            content
        )
        content = re.sub(
            r'Aiding the Homeless Population\s*<br>\s*in South Africa',
            'School Books Support Project <br>\n                                        for Orphanage and Needy Students',
            content
        )

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
