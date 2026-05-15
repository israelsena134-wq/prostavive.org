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

    # Define official-congruent meta tags
    official_title = "ProstaVive™ Official Site - Most Potent Prostate Health Formula"
    official_desc = "Discover ProstaVive, the most potent and fast-acting formula for prostate health and strong flow. Based on the latest clinical studies for maximum prostate support."

    # Update Title
    if '<title>' in content:
        content = re.sub(r'<title>.*?</title>', f'<title>{official_title}</title>', content)
    else:
        # Inject title if missing (unlikely but safe)
        content = content.replace('<head>', f'<head>\n    <title>{official_title}</title>')

    # Update Meta Description
    if 'name="description"' in content:
        content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{official_desc}">', content)
    else:
        # Inject meta description
        content = content.replace('<head>', f'<head>\n    <meta name="description" content="{official_desc}">')

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("SEO Congruence updated: Title and Meta Description matched to official offer.")

if __name__ == "__main__":
    main()
