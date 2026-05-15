import os
import re

def main():
    css_path = r'c:\Users\Guga\Downloads\prostavive.org\assets\71ceae26866cded4_style.css'
    
    if not os.path.exists(css_path):
        print("Error: style.css not found.")
        return

    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Force the dark blue background for .sec_four in ALL mobile views
    # We'll search for .sec_four blocks inside media queries and ensure the background is correct.
    # The correct hashed filename for background3 is e8ce22339137d16a_background3.png
    
    # We'll replace ANY background: url(...) inside a .sec_four block in mobile media queries
    # to use the correct background image.
    
    # Also, eliminate the visibility: hidden and massive paddings.
    
    # Regex to find .sec_four blocks and replace their content
    # This is a bit complex due to different media queries, so we'll do a series of targeted replaces.

    # Fix background filename (remove any assets/ prefix and fix corrupted names)
    content = content.replace('e8ce22339137d16a_e8ce22339137d16a_background3.png', 'e8ce22339137d16a_background3.png')
    content = content.replace('assets/e8ce22339137d16a_background3.png', 'e8ce22339137d16a_background3.png')
    
    # Ensure .sec_four background is NEVER white in mobile
    # We find .sec_four rules in media queries
    
    # Targeted fix for the 'ghost space' and background visibility
    replacements = {
        'visibility: hidden;': 'display: none;',
        'padding-top: 158px;': 'padding-top: 20px;',
        'margin-top: 140px;': 'margin-top: 10px;',
        'margin-bottom: 116px;': 'margin-bottom: 20px;',
        'margin-bottom: 154px;': 'margin-bottom: 20px;',
        'margin-bottom: 58px;': 'margin-bottom: 20px;',
        'background: url(e8ce22339137d16a_background3.png);': 'background: url("e8ce22339137d16a_background3.png") !important; background-size: cover !important;',
        'background: url("e8ce22339137d16a_background3.png");': 'background: url("e8ce22339137d16a_background3.png") !important; background-size: cover !important;'
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    # 2. Add a global override at the end of the CSS to be ABSOLUTELY SURE
    override = """
/* FINAL MOBILE FIX FOR SECTION 5 */
@media screen and (max-width: 767px) {
    .sec_four {
        background: url("e8ce22339137d16a_background3.png") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        padding: 40px 15px !important;
    }
    .sec_four_mid_wrap {
        padding: 0 !important;
        margin: 0 !important;
    }
    .provi_compo_img_wrap {
        display: none !important;
    }
    .provi_compo_img_wrap_mob {
        display: block !important;
        visibility: visible !important;
        margin: 20px auto !important;
        text-align: center !important;
    }
    .sec_four_end_wrap {
        padding-top: 20px !important;
        margin-top: 0 !important;
    }
}
"""
    if "/* FINAL MOBILE FIX FOR SECTION 5 */" not in content:
        content += override

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Section 5 mobile total repair applied.")

if __name__ == "__main__":
    main()
