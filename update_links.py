import os
import re

directory = "C:\\Users\\esaan\\Downloads\\Saani Eliasu\\non-profit-charity-html-template-2024-01-13-04-19-50-utc\\sadaka-buyer-file"

# Regex for the multiline title "Charity\nShowcases a\nNation's Kindness"
kindness_pattern = re.compile(r"Charity\s+Showcases\s+a\s+Nation's\s+Kindness", re.MULTILINE)

# Pattern for the Royal Promise link replacement
royal_promise_title = "Royal Promise Outreach: Orphanage Feeding, Mentorship and Youth Development"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # 1. Replace Charity Kindness with Education Outreach and its target link
        if kindness_pattern.search(content):
            # Also replace the link nearby. This is tricky due to proximity.
            # We'll search for the specific link that precedes this title in the template.
            # Usually: <a href="cause-single.html" ...>Charity...
            content = re.sub(r'href="cause-single\.html"([^>]*>)\s*Charity\s+Showcases\s+a\s+Nation\'s\s+Kindness', 
                             r'href="cause-single-education-outreach.html"\1Education Outreach', content, flags=re.MULTILINE)
            content = kindness_pattern.sub("Education Outreach", content)
            changed = True

        # 2. Replace Royal Promise links (already updated the text earlier, just need the link)
        if royal_promise_title in content:
            content = content.replace('href="cause-single.html" class="primary-hover">' + royal_promise_title, 
                                      'href="cause-single-royal-promise.html" class="primary-hover">' + royal_promise_title)
            # Other variations
            content = content.replace('href="cause-single.html" class="btn-inner"', 'href="cause-single-royal-promise.html" class="btn-inner"')
            changed = True

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
