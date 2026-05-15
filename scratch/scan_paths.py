import re
import os

def main():
    root_dir = r'c:\Users\Guga\Downloads\prostavive.org'
    index_path = os.path.join(root_dir, 'index.html')
    
    if not os.path.exists(index_path):
        print("Error: index.html not found.")
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all src="..." and href="..."
    srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
    
    print("\n--- NON-ASSETS SRC PATHS ---")
    for s in srcs:
        if 'assets/' not in s and not s.startswith('http') and not s.startswith('data:'):
            print(s)

if __name__ == "__main__":
    main()
