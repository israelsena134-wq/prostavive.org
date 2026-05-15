import os

def main():
    root_dir = r'c:\Users\Guga\Downloads\prostavive.org'
    index_path = os.path.join(root_dir, 'index.html')
    
    if not os.path.exists(index_path):
        print("Error: index.html not found.")
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The verified Hop-link
    hop_link = "https://aeb98q-0zh-3c8zn2n-9zafr9z.hop.clickbank.net/"
    
    # Replace the placeholder in the silent activation script
    if 'YOUR_BUYGOODS_AFFILIATE_LINK_HERE' in content:
        new_content = content.replace('YOUR_BUYGOODS_AFFILIATE_LINK_HERE', hop_link)
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Silent Cookie Activation link updated successfully.")
    else:
        print("Placeholder not found. It might have been updated already or the tag is different.")

if __name__ == "__main__":
    main()
