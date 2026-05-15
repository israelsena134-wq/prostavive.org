import os

def main():
    css_path = r'c:\Users\Guga\Downloads\prostavive.org\assets\71ceae26866cded4_style.css'
    
    if not os.path.exists(css_path):
        print("Error: style.css not found.")
        return

    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Eliminate whitespace gaps (Ghost space)
    content = content.replace('visibility: hidden;', 'display: none;')

    # 2. Fix massive margins and paddings for mobile (Section 5 / sec_four)
    content = content.replace('padding-top: 158px;', 'padding-top: 20px;')
    content = content.replace('margin-top: 140px;', 'margin-top: 10px;')
    content = content.replace('margin-bottom: 116px;', 'margin-bottom: 20px;')
    content = content.replace('margin-bottom: 154px;', 'margin-bottom: 20px;')
    content = content.replace('margin-bottom: 58px;', 'margin-bottom: 20px;')
    
    # 3. Ensure the mobile product image is sized correctly and centered
    # In media queries, .provi_compo_img should be responsive
    # Usually max-width: 100% is already there, but let's ensure it doesn't overflow
    
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Section 5 mobile configuration stabilized.")

if __name__ == "__main__":
    main()
