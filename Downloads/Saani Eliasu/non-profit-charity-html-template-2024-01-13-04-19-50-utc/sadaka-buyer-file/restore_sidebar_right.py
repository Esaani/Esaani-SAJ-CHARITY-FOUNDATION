import os

files_to_update = [
    "event-single.html",
    "event-list.html",
    "contact.html",
    "cause-single.html",
    "cause-single-education-outreach.html",
    "cause-single-royal-promise.html",
    "cause-list.html",
    "blog-single.html",
    "blog-classic.html"
]

base_path = r"C:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file"

for filename in files_to_update:
    filepath = os.path.join(base_path, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Swap classes to move sidebar to the Right
        # Original (currently Left):
        # col-lg-8 order-1 order-lg-2
        # col-lg-4 order-2 order-lg-1
        
        # New (Right):
        # col-lg-8 order-1 order-lg-1
        # col-lg-4 order-2 order-lg-2
        
        new_content = content.replace('col-lg-8 order-1 order-lg-2', 'col-lg-8 order-1 order-lg-1')
        new_content = new_content.replace('col-lg-4 order-2 order-lg-1', 'col-lg-4 order-2 order-lg-2')
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No changes needed for {filename}")
    else:
        print(f"File not found: {filename}")
