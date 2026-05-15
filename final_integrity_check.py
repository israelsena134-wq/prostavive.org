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

    # Get all files in assets
    assets = os.listdir(assets_dir)
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico')
    asset_images = [f for f in assets if f.lower().endswith(image_extensions)]

    print("\n--- FINAL INTEGRITY CHECK: ASSETS vs HTML ---")
    
    # Find all image-like patterns in HTML
    # We look for src="..." or any string ending in image extensions
    html_srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
    
    missing_in_html = []
    broken_in_html = []
    
    # Check if all images in HTML exist
    for src in html_srcs:
        if src.startswith('http') or src.startswith('data:'):
            continue
        
        clean_src = src.split('?')[0]
        full_path = os.path.normpath(os.path.join(root_dir, clean_src))
        
        if not os.path.exists(full_path):
            print(f"[BROKEN LINK IN HTML] {src}")
            broken_in_html.append(src)

    # Check if all images in assets are used (or at least mapped)
    for img in asset_images:
        # Check if the exact hashed name is in the HTML
        if img in content:
            # print(f"[OK] {img} is mapped.")
            pass
        else:
            # If not, check if its 'base name' (after the underscore) is mentioned with a legacy path
            if '_' in img:
                base_name = img.split('_', 1)[1]
                if base_name in content:
                    print(f"[POTENTIAL MISSING MAPPING] Asset '{img}' exists but HTML uses a legacy path for '{base_name}'")
                    missing_in_html.append((base_name, img))

    # --- CORRECTION LOGIC ---
    if broken_in_html or missing_in_html:
        print("\nApplying final corrections...")
        for src in broken_in_html:
            # Try to find a match in assets
            basename = os.path.basename(src).split('?')[0]
            match = None
            for img in asset_images:
                if img == basename or img.endswith('_' + basename):
                    match = img
                    break
            
            if match:
                new_path = f"assets/{match}"
                content = content.replace(src, new_path)
                print(f"Fixed: {src} -> {new_path}")
            else:
                print(f"Warning: No asset match found for broken link: {src}")

        # Also map any missing hashed assets
        for base, hashed in missing_in_html:
            # Find legacy patterns like /home-assets/images/base or assets/base
            # and replace with assets/hashed
            pattern = f'src=["\'][^"\']*{re.escape(base)}[^"\']*["\']'
            content = re.sub(pattern, f'src="assets/{hashed}"', content)
            print(f"Fixed legacy reference: {base} -> assets/{hashed}")

        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("\nAll identified mappings have been fixed.")
    else:
        print("\nPERFECT: All images are correctly mapped!")

if __name__ == "__main__":
    main()
