import os

def fix_corruption(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reverse the bad replacement: any ../index.html that shouldn't be there
    # But wait, some might be valid. 
    # Actually, the most reliable way is to replace "../index.html" with "/" 
    # and then do the replacements properly.
    new_content = content.replace('../index.html', '/')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    root = r'c:\Users\Guga\Downloads\prostavive.org'
    fix_corruption(os.path.join(root, 'index.html'))
    assets_dir = os.path.join(root, 'assets')
    for filename in os.listdir(assets_dir):
        if filename.endswith('.html') or filename.endswith('.php'):
            fix_corruption(os.path.join(assets_dir, filename))

if __name__ == "__main__":
    main()
