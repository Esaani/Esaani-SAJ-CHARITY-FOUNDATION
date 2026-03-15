import os

directory = r"c:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file"

# The target URL to replace
paystack_url = "https://paystack.shop/pay/sajfoundation-donate"
replacement_url = "donate.html"

# We also want to replace href="#" for "DONATE NOW" buttons that are likely intended for the donation page 
# (excluding those that are already correct or are inside the donate.html itself)

for filename in os.listdir(directory):
    if filename.endswith(".html") and filename != "donate.html":
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # 1. Replace the Paystack Shop link in the dropdowns
        if paystack_url in content:
            content = content.replace(paystack_url, replacement_url)
            changed = True

        # 2. Specifically target the "DONATE NOW" buttons that might have href="#"
        # We look for common patterns in this template
        # Pattern 1: Banner buttons
        # <a href="#" class="btn-inner"> <span class="btn-text"> DONATE NOW </span> </a>
        # Let's use a more robust replacement for DONATE NOW links that are just hash
        
        # This regex looks for <a> tags containing "DONATE NOW" (case insensitive) with href="#"
        import re
        content, count = re.subn(r'(<a\s+[^>]*?href=)"#"([^>]*?>\s*<span\s+[^>]*?>\s*DONATE\s+NOW\s*</span>)', 
                                 r'\1"donate.html"\2', content, flags=re.IGNORECASE)
        if count > 0:
            changed = True
            
        # Also handle cases without span if they exist
        content, count2 = re.subn(r'(<a\s+[^>]*?href=)"#"([^>]*?>\s*DONATE\s+NOW\s*</a>)', 
                                  r'\1"donate.html"\2', content, flags=re.IGNORECASE)
        if count2 > 0:
            changed = True

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")

print("Update complete.")
