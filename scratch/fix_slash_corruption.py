import os
import re

def fix_slash_corruption(content):
    # The corruption replaced '/' with 'index.html'
    # We need to be careful. 
    # 1. </script> became <index.htmlscript> or similar? No, </script> is </script>.
    # Wait, if '/' became 'index.html', then '</script>' became '<index.htmlscript>'.
    # Let's check: 101: })();<index.htmlscript>
    # Yes! 
    
    # Strategy: 
    # Replace '<index.html' with '</'
    content = content.replace('<index.html', '</')
    
    # Replace 'assetsindex.html' with 'assets/'
    content = content.replace('assetsindex.html', 'assets/')
    
    # Replace 'imageindex.html' with 'image/'
    content = content.replace('imageindex.html', 'image/')
    
    # Replace 'index.htmlindex.html' with '//' (for protocols or comments)
    content = content.replace('index.htmlindex.html', '//')
    
    # Replace 'index.html' with '/' in common patterns
    # but NOT when it's standing alone as a filename in a link we want to keep.
    # Actually, most 'index.html' that are NOT preceded by a space or quote are likely slashes.
    
    # Let's fix the closing tags first.
    content = re.sub(r'<index.html([a-z]+)>', r'</\1>', content)
    
    # Fix the script logic slashes
    content = content.replace('index.html\s+index.html', '/\\s+/')
    
    # Fix 'index.html' followed by a word (like index.htmlapi)
    content = re.sub(r'index.html([a-z])', r'/\1', content)
    
    return content

def main():
    root = r'c:\Users\Guga\Downloads\prostavive.org'
    files = [os.path.join(root, 'index.html')]
    assets_dir = os.path.join(root, 'assets')
    for f in os.listdir(assets_dir):
        if f.endswith('.html') or f.endswith('.php'):
            files.append(os.path.join(assets_dir, f))
            
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = fix_slash_corruption(content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {file_path}")

if __name__ == "__main__":
    main()
