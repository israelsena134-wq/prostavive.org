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

    # Find all src="..." and href="..."
    patterns = [
        r'src=["\']([^"\']+)["\']',
        r'href=["\']([^"\']+)["\']'
    ]
    
    all_paths = []
    for p in patterns:
        all_paths.extend(re.findall(p, content))
    
    print("\n--- FINAL PRODUCTION AUDIT ---")
    broken = []
    for path in sorted(set(all_paths)):
        # Skip remote, anchors, and data
        if path.startswith('http') or path.startswith('#') or path.startswith('data:'):
            continue
            
        # Clean path (remove query params)
        clean_path = path.split('?')[0]
        full_path = os.path.normpath(os.path.join(root_dir, clean_path))
        
        if not os.path.exists(full_path):
            # Special check for PHP files which might be in root
            if clean_path.endswith('.php') and os.path.exists(os.path.join(root_dir, clean_path)):
                continue
            
            # Special check for assets folder
            if not clean_path.startswith('assets/') and os.path.exists(os.path.join(assets_dir, clean_path)):
                # This should have been caught, but just in case
                print(f"[WARNING] Path '{path}' is in assets but missing prefix.")
                broken.append(path)
                continue

            print(f"[BROKEN] {path} -> Not found at {full_path}")
            broken.append(path)
        else:
            # print(f"[OK] {path}")
            pass

    if not broken:
        print("\nSUCCESS: No broken links found in index.html!")
    else:
        print(f"\nFAILURE: Found {len(broken)} broken links!")

if __name__ == "__main__":
    main()
