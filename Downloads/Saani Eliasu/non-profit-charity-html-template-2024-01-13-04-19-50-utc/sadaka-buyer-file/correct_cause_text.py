import os

directory = r"c:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file"

old_text = "Royal Promise Outreach: Orphanage Feeding, Mentorship and Youth Development"
new_text = "Orphanage Feeding, Mentorship and Youth Development"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_text in content:
                new_content = content.replace(old_text, new_text)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Done!")
