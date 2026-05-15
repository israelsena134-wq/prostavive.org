import os
import re

def main():
    root_dir = r'c:\Users\Guga\Downloads\prostavive.org'
    index_path = os.path.join(root_dir, 'index.html')
    
    if not os.path.exists(index_path):
        print("Error: index.html not found.")
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix JQuery path
    content = content.replace('src="/js/jquery.js"', 'src="assets/cde2e5c8bf73b290_jquery.js"')
    content = content.replace('src="js/jquery.js"', 'src="assets/cde2e5c8bf73b290_jquery.js"')

    # 2. Fix corrupted shipping image paths
    # Match strings like assets/2329481c3defa328_shipping.html_order-img1.png
    content = re.sub(r'assets/2329481c3defa328_shipping\.html_order-img\d+\.png', 'assets/2dcfaf24cdc3992f_shipping_order-img1.png', content)

    # 3. Final cleanup of any /home-assets/ that might have survived
    content = content.replace('/home-assets/images/', 'assets/')
    content = content.replace('src="/assets/', 'src="assets/')

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Final production fixes applied successfully via script.")

if __name__ == "__main__":
    main()
