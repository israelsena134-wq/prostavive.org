import os
import re

def main():
    root_dir = r'c:\Users\Guga\Downloads\prostavive.org'
    index_path = os.path.join(root_dir, 'index.html')
    assets_dir = os.path.join(root_dir, 'assets')
    
    if not os.path.exists(index_path):
        print("Error: index.html not found.")
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the core assets list
    assets = os.listdir(assets_dir)
    
    # 1. Manual critical mappings (Hashed names)
    manual_maps = {
        'product12.png': '9a370b2027a99449_product12.png',
        'free-offer-2.png': '76dbe696abc31090_free-offer-2-nw-color.png',
        'free-shipping.png': '2dcfaf24cdc3992f_shipping_order-img1.png',
        'image13.png': '3d93f1d72013c774_image13.png',
        'image14.png': 'b8e4964e40443265_image14.png',
        'image15.png': 'ca849e872e0c8d88_image15.png'
    }

    # 2. General replacement for legacy prefixes
    # Replace all variations of /home-assets/images/ and similar with assets/
    legacy_prefixes = [
        '/home-assets/imagesassets/',
        '/home-new//home-assets/images/',
        '/home-assets/images/',
        'home-assets/images/'
    ]
    
    for prefix in legacy_prefixes:
        content = content.replace(prefix, 'assets/')

    # 3. Ensure hashed names are used where possible
    for old_name, hashed_name in manual_maps.items():
        # Match src="assets/old_name" or src="assets/old_name?query"
        pattern = f'src=["\']assets/{re.escape(old_name)}(\\?[^"\']*)?["\']'
        replacement = f'src="assets/{hashed_name}"'
        content = re.sub(pattern, replacement, content)

    # 4. Remove leading slashes from any remaining assets/ paths
    content = content.replace('src="/assets/', 'src="assets/')
    content = content.replace('href="/assets/', 'href="assets/')

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Mapping complete: Legacy paths replaced and hashed assets connected.")

if __name__ == "__main__":
    main()
