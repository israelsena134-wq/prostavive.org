import re

def main():
    path = r'c:\Users\Guga\Downloads\prostavive.org\index.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the mappings based on ASSET_MAP in the file
    mappings = {
        'https://prostavive.org/privacy.php?': 'assets/844b3ad2b33e3130_privacy.php',
        'https://prostavive.org/terms.php?': 'assets/3f4778f3e9fc4fbd_terms.php',
        'https://prostavive.org/disclaimer.php?': 'assets/8f9543aa441b7e12_disclaimer.php',
        'https://prostavive.org/references.php?': 'assets/a5c38e75f0b1c9c6_references.php',
        'https://prostavive.org/contact.php#return?': 'assets/268908007a902523_contact.php',
        'https://prostavive.org/refunds.php?': 'assets/83dedddda9046ce9_refunds.php',
        'https://prostavive.org/contact.php?': 'assets/f6cc064843f34b01_contact.php',
        'https://prostavive.org/shipping?': 'assets/2329481c3defa328_shipping.html',
        
        # FAQ section links
        '/home-assets/images/Supplement-Facts.png?': 'assets/782069daa9a03543_Supplement-Facts.png',
        
        # Checkout links (extracted from ASSET_MAP in index.html)
        'https://provive.pay.clickbank.net/?cbitems=PROVIVE-006&cbfid=57914&cbskin=45220&vtid=homed&cbexit=3820&__user_id=338ab01e8205090c1da078d9eabf7053&__page_id=3&__page_version=a&__hostname=prostavive.org&vq=01.CF1FBAEA2DF2292656EAF55E324661730EE03492CBD254B9F404FDB26B27AB4102067E38B1C839051A5B695603827641AA13269A': 'assets/6da9f50a86b8d0f5_file.html',
        'https://provive.pay.clickbank.net/?cbitems=PROVIVE-003-1&cbfid=57914&cbskin=45219&vtid=homed&cbexit=3820&__user_id=338ab01e8205090c1da078d9eabf7053&__page_id=3&__page_version=a&__hostname=prostavive.org&vq=01.CF1FBAEA2DF2292656EAF55E324661730EE03492CBD254B9F404FDB26B27AB4102067E38B1C839051A5B695603827641AA13269A': 'assets/aab514bdf9fb1cd0_file.html',
        'https://provive.pay.clickbank.net/?cbitems=PROVIVE-001-1&cbfid=57914&cbskin=45218&vtid=homed&cbexit=3820&__user_id=338ab01e8205090c1da078d9eabf7053&__page_id=3&__page_version=a&__hostname=prostavive.org&vq=01.CF1FBAEA2DF2292656EAF55E324661730EE03492CBD254B9F404FDB26B27AB4102067E38B1C839051A5B695603827641AA13269A': 'assets/3d3bb573ac872fd9_file.html',
        
        'https://provive.pay.clickbank.net/?cbitems=PROVIVE-006&cbfid=57914&cbskin=45217&vtid=homem&cbexit=3820&__user_id=338ab01e8205090c1da078d9eabf7053&__page_id=3&__page_version=a&__hostname=prostavive.org&vq=01.CF1FBAEA2DF2292656EAF55E324661730EE03492CBD254B9F404FDB26B27AB4102067E38B1C839051A5B695603827641AA13269A': 'assets/edd993e4a957ced3_file.html',
        'https://provive.pay.clickbank.net/?cbitems=PROVIVE-003-1&cbfid=57914&cbskin=45216&vtid=homem&cbexit=3820&__user_id=338ab01e8205090c1da078d9eabf7053&__page_id=3&__page_version=a&__hostname=prostavive.org&vq=01.CF1FBAEA2DF2292656EAF55E324661730EE03492CBD254B9F404FDB26B27AB4102067E38B1C839051A5B695603827641AA13269A': 'assets/4dc682ee190a704c_file.html',
        'https://provive.pay.clickbank.net/?cbitems=PROVIVE-001-1&cbfid=57914&cbskin=45215&vtid=homem&cbexit=3820&__user_id=338ab01e8205090c1da078d9eabf7053&__page_id=3&__page_version=a&__hostname=prostavive.org&vq=01.CF1FBAEA2DF2292656EAF55E324661730EE03492CBD254B9F404FDB26B27AB4102067E38B1C839051A5B695603827641AA13269A': 'assets/1402bb3698d8b6c3_file.html',
    }

    # Perform replacements
    new_content = content
    for original, local in mappings.items():
        # Handle &amp; in HTML content
        original_escaped = original.replace('&', '&amp;')
        new_content = new_content.replace(original, local)
        new_content = new_content.replace(original_escaped, local)

    # Also fix mailto and support links if possible
    new_content = new_content.replace('https://support@prostavive.org/', 'mailto:support@prostavive.org')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replacements completed.")

if __name__ == "__main__":
    main()
