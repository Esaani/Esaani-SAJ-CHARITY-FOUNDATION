import os
import re

directory = "C:\\Users\\esaan\\Downloads\\Saani Eliasu\\non-profit-charity-html-template-2024-01-13-04-19-50-utc\\sadaka-buyer-file"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # 1. Look for the Education Outreach block
        edu_start_pattern = re.compile(r'Education Outreach</a></h4>.*?<a href="cause-single-royal-promise\.html" class="btn-inner">', re.DOTALL)
        if edu_start_pattern.search(content):
            content = re.sub(r'(Education Outreach</a></h4>.*?<a href=")cause-single-royal-promise\.html(" class="btn-inner">)', 
                             r'\1cause-single-education-outreach.html\2', content, flags=re.DOTALL)
            changed = True

        # 2. Correct "Foods" to "Education" in the Education Outreach block
        # We find the Education Outreach title and look back for the tag
        edu_tag_pattern = re.compile(r'<span class="cause-tag">Foods</span>\s*</div>\s*<div class="cause__content">\s*<h4 class="mb-4 mt-20"><a href="cause-single-education-outreach\.html"', re.DOTALL)
        if edu_tag_pattern.search(content):
            content = re.sub(r'<span class="cause-tag">Foods</span>(\s*</div>\s*<div class="cause__content">\s*<h4 class="mb-4 mt-20"><a href="cause-single-education-outreach\.html")', 
                             r'<span class="cause-tag">Education</span>\1', content, flags=re.DOTALL)
            changed = True

        # 3. Ensure "Food" tag for Royal Promise is consistent (previously might have been Education Outreach)
        # (This is just a double check)

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Refined {filename}")
