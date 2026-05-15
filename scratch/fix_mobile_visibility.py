import os
import re

def main():
    css_path = r'c:\Users\Guga\Downloads\prostavive.org\assets\71ceae26866cded4_style.css'
    
    if not os.path.exists(css_path):
        print("Error: style.css not found.")
        return

    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Force visibility for the mobile product image wrapper
    # We replace any display: none or visibility: hidden on .provi_compo_img_wrap_mob
    
    # Use regex to find all instances of .provi_compo_img_wrap_mob blocks
    pattern = r'(\.provi_compo_img_wrap_mob\s*\{[^}]*?)(display:\s*none;|visibility:\s*hidden;)'
    
    def replace_hidden(match):
        prefix = match.group(1)
        # Replace the hidden property with visible ones
        return f'{prefix}display: block; visibility: visible;'

    # Apply the replacement multiple times until no more matches
    new_content = content
    while True:
        temp = re.sub(pattern, replace_hidden, new_content)
        if temp == new_content:
            break
        new_content = temp

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("CSS visibility for .provi_compo_img_wrap_mob fixed.")

if __name__ == "__main__":
    main()
