import os

base_path = r"C:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file"

# 1. Fix typos globally in HTML files
files = [f for f in os.listdir(base_path) if f.endswith('.html')]

for filename in files:
    filepath = os.path.join(base_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('Resent Post', 'Recent Post')
    new_content = new_content.replace('Fast Name', 'First Name')
    
    # 2. Update specific links in cause-list.html
    if filename == "cause-list.html":
        # Link for Royal Promise Outreach
        new_content = new_content.replace(
            '<h4 class="mb-2"><a href="cause-single.html" class="primary-hover">Royal Promise Outreach', 
            '<h4 class="mb-2"><a href="cause-single-royal-promise.html" class="primary-hover">Royal Promise Outreach'
        )
        # Link for Education Outreach (Charity Showcases a Nation's Kindness)
        new_content = new_content.replace(
            '<h4 class="mb-2"><a href="cause-single.html" class="primary-hover">Charity\n                                        Showcases a\n                                        Nation\'s <br> Kindness</a></h4>',
            '<h4 class="mb-2"><a href="cause-single-education-outreach.html" class="primary-hover">Charity Showcases a Nation\'s Kindness</a></h4>'
        )
        # Fix the other link for Education Outreach (the image link) - this is harder due to duplicates, but I'll try
        # Actually, replace based on context
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")

# 3. Specific fix for cause-single-education-outreach.html
# Add a tag if it's missing or update it
outreach_file = os.path.join(base_path, "cause-single-education-outreach.html")
if os.path.exists(outreach_file):
    with open(outreach_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Ensure it's linked correctly in sidebar recent posts
    new_content = content.replace('blog-single.html', 'blog-single.html') # placeholder
    # Maybe add the tag "Education" back if appropriate. 
    # Current code around line 296:
    # <img src="assets/images/cause/cause-single-image.jpg" alt="image">
    # </div>
    new_content = content.replace(
        '<img src="assets/images/cause/cause-single-image.jpg" alt="image">\n                            </div>',
        '<img src="assets/images/cause/cause-single-image.jpg" alt="image">\n                                <span class="cause-tag">Education</span>\n                            </div>'
    )
    if content != new_content:
        with open(outreach_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Final polish for Education Outreach file")
