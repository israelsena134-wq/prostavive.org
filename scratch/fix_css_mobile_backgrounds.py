import os

def main():
    root_dir = r'c:\Users\Guga\Downloads\prostavive.org'
    css_path = os.path.join(root_dir, 'assets', '71ceae26866cded4_style.css')
    
    if not os.path.exists(css_path):
        print("Error: style.css not found.")
        return

    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the core assets that need path fixing in CSS
    assets_to_fix = [
        '9a370b2027a99449_product12.png',
        '9df78bab712c7819_background1.png',
        'd12111c6d948f54f_background.png',
        'e8ce22339137d16a_background3.png'
    ]
    
    # In CSS (inside assets/), the path should be just "filename.png"
    # Replace "assets/filename.png" or "../images/original_filename.png" 
    # with just the correct hashed filename.
    
    # First, fix any existing assets/ prefixes
    for asset in assets_to_fix:
        content = content.replace(f'assets/{asset}', asset)
        content = content.replace(f'url({asset})', f'url("{asset}")') # Standardize to quotes
        content = content.replace(f'url(\'{asset}\')', f'url("{asset}")')

    # Also check for the legacy paths that might still be in media queries
    legacy_maps = {
        'product12.png': '9a370b2027a99449_product12.png',
        'background1.png': '9df78bab712c7819_background1.png',
        'background.png': 'd12111c6d948f54f_background.png',
        'background3.png': 'e8ce22339137d16a_background3.png',
        'banner-bg-mob.png': 'd12111c6d948f54f_background.png',
        'sec-4-mob-bg.png': 'e8ce22339137d16a_background3.png'
    }

    for old, new in legacy_maps.items():
        # Replace url(../images/old) or url(old) with url("new")
        content = content.replace(f'../images/{old}', new)
        content = content.replace(f'url({old})', f'url("{new}")')

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("CSS backgrounds for mobile repaired.")

if __name__ == "__main__":
    main()
