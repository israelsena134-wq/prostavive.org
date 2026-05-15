import os
import re

ASSET_MAP = {
    "https://prostavive.org/": "index.html",
    "https://prostavive.org/home-assets/css/style.css": "71ceae26866cded4_style.css",
    "https://prostavive.org/home-assets/images/bottles.png": "610d36e2adcf641d_bottles.png",
    "https://prostavive.org/home-assets/images/LOGO-pv.png": "6ad0acd64218fa26_LOGO-pv.png",
    "https://prostavive.org/css/bootstrap.css": "a29236eed54ff257_bootstrap.css",
    "https://prostavive.org/home-assets/images/image7.png": "eb209ad7bcd4016c_image7.png",
    "https://prostavive.org/home-assets/images/555075784.png": "7f8b19a9ca1f529d_555075784.png",
    "https://prostavive.org/home-assets/images/image8.png": "002cc4a4d9b27a18_image8.png",
    "https://prostavive.org/home-assets/images/image9.png": "e65032efb50fa512_image9.png",
    "https://prostavive.org/home-assets/images/product.png": "891339e05e9a04a8_product.png",
    "https://prostavive.org/home-assets/images/image10.png": "5cfc235a847cc242_image10.png",
    "https://prostavive.org/home-assets/images/image11.png": "a42053b2962a864e_image11.png",
    "https://prostavive.org/home-assets/images/product12.png": "9a370b2027a99449_product12.png",
    "https://prostavive.org/home-assets/images/image13.png": "3d93f1d72013c774_image13.png",
    "https://prostavive.org/home-assets/images/image14.png": "b8e4964e40443265_image14.png",
    "https://prostavive.org/home-assets/images/image15.png": "ca849e872e0c8d88_image15.png",
    "https://prostavive.org/home-assets/images/rbc-image.png": "27af857857521337_rbc-image.png",
    "https://prostavive.org/home-assets/images/Supplement-Facts.png": "782069daa9a03543_Supplement-Facts.png",
    "https://prostavive.org/home-assets/images/image4.png": "6455409ea53c7daa_image4.png",
    "https://prostavive.org/home-assets/images/image5.png": "a73697dea2ac2272_image5.png",
    "https://prostavive.org/home-assets/images/Layer-91.png": "97086f4c1465ad5c_Layer-91.png",
    "https://prostavive.org/home-assets/images/image3.png": "6feccc8a1b527137_image3.png",
    "https://prostavive.org/home-assets/images/Layer-92.png": "b949aab248ef0d5e_Layer-92.png",
    "https://prostavive.org/home-assets/images/Layer-93.png": "fd5c38d6bae79356_Layer-93.png",
    "https://prostavive.org/home-assets/images/image6.png": "38df7b28d9eb7e86_image6.png",
    "https://prostavive.org/home-assets/images/Layer-94.png": "a2291fdff5d24044_Layer-94.png",
    "https://prostavive.org/home-assets/images/button1.png": "cfc7c8d0ed0a566b_button1.png",
    "https://prostavive.org/home-assets/images/MBG.png": "d1847e3fcd583ee2_MBG.png",
    "https://prostavive.org/home-assets/images/bar.png": "57894651308d7a14_bar.png",
    "https://prostavive.org/home-assets/images/money-back-guarantee.png": "4210b7448925a5d3_money-back-guarantee.png",
    "https://prostavive.org/home-assets/images/image17.png": "23b874ab4a73f881_image17.png",
    "https://prostavive.org/home-assets/images/strip.png": "d2f69f6345ec94af_strip.png",
    "https://prostavive.org/home-assets/images/4-images.png": "7d08264936f5e615_4-images.png",
    "https://prostavive.org/home-assets/images/payment-option-img.png": "500fb1596ee9340d_payment-option-img.png",
    "https://prostavive.org/home-assets/images/shipping_order-img1.png": "2dcfaf24cdc3992f_shipping_order-img1.png",
    "https://prostavive.org/home-assets/images/order-button.png": "434f30674a74f47d_order-button.png",
    "https://prostavive.org/home-assets/images/1-bottle.png": "c022b01f1095967b_1-bottle.png",
    "https://prostavive.org/home-assets/images/free-offer-2-nw-color.png": "76dbe696abc31090_free-offer-2-nw-color.png",
    "https://prostavive.org/home-assets/images/6-bottle.png": "dd1c44dc49d343d7_6-bottle.png",
    "https://prostavive.org/home-assets/images/3-bottle.png": "22059b65515973f8_3-bottle.png",
    "https://prostavive.org/home-assets/images/6-mob.png": "125e4eb074aa6a5e_6-mob.png",
    "https://prostavive.org/home-assets/images/3-mob.png": "e9549a9d80ca717b_3-mob.png",
    "https://prostavive.org/home-assets/images/1-mob.png": "2fd3367f84fd001f_1-mob.png",
    "https://prostavive.org/home-assets/images/order-button-mob.png": "1c3f88b01d7b63d2_order-button-mob.png",
    "https://prostavive.org/contact.php": "f6cc064843f34b01_contact.php",
    "https://prostavive.org/refunds.php": "83dedddda9046ce9_refunds.php",
    "https://prostavive.org/disclaimer.php": "8f9543aa441b7e12_disclaimer.php",
    "https://prostavive.org/privacy.php": "844b3ad2b33e3130_privacy.php",
    "https://prostavive.org/terms.php": "3f4778f3e9fc4fbd_terms.php",
    "https://prostavive.org/references.php": "a5c38e75f0b1c9c6_references.php",
    "https://prostavive.org/shipping": "2329481c3defa328_shipping.html",
    "https://prostavive.org/contact.php#return": "268908007a902523_contact.php",
}

ROOT_RELATIVE = {
    "/privacy.php": "844b3ad2b33e3130_privacy.php",
    "/terms.php": "3f4778f3e9fc4fbd_terms.php",
    "/disclaimer.php": "8f9543aa441b7e12_disclaimer.php",
    "/references.php": "a5c38e75f0b1c9c6_references.php",
    "/contact.php": "f6cc064843f34b01_contact.php",
    "/refunds.php": "83dedddda9046ce9_refunds.php",
    "/shipping": "2329481c3defa328_shipping.html",
    "/css/bootstrap.css": "a29236eed54ff257_bootstrap.css",
    "/images/LOGO-pv.png": "6ad0acd64218fa26_LOGO-pv.png",
    "/": "index.html",
}

def replace_in_content(content, is_in_assets):
    # Sort keys by length descending
    all_keys = sorted(list(ASSET_MAP.keys()) + list(ROOT_RELATIVE.keys()), key=len, reverse=True)
    combined = {**ASSET_MAP, **ROOT_RELATIVE}

    def get_target(key):
        val = combined[key]
        if is_in_assets:
            return "../index.html" if val == "index.html" else val
        else:
            return "index.html" if val == "index.html" else "assets/" + val

    # Use regex to find href, src, url attributes
    # Match href="...", src="...", url(...)
    patterns = [
        (r'(href=["\'])([^"\']*)(["\'])', 2),
        (r'(src=["\'])([^"\']*)(["\'])', 2),
        (r'(url\()([^)]*)(\))', 2)
    ]

    for pattern, idx in patterns:
        def repl(match):
            original_url = match.group(idx)
            # Check if this URL is in our map
            # Strip trailing ? or /
            clean_url = original_url.split('?')[0].rstrip('/')
            if not clean_url and original_url == '/': clean_url = '/'
            
            # Try to match the original or the clean version
            matched_key = None
            if original_url in combined: matched_key = original_url
            elif clean_url in combined: matched_key = clean_url
            elif original_url.replace('&amp;', '&') in combined: matched_key = original_url.replace('&amp;', '&')

            if matched_key:
                target = get_target(matched_key)
                # Re-construct the match
                groups = list(match.groups())
                groups[idx-1] = target
                return "".join(groups)
            return match.group(0)

        content = re.sub(pattern, repl, content)
    
    return content

def main():
    root = r'c:\Users\Guga\Downloads\prostavive.org'
    
    # index.html
    idx_path = os.path.join(root, 'index.html')
    with open(idx_path, 'r', encoding='utf-8') as f:
        c = f.read()
    new_c = replace_in_content(c, False)
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(new_c)

    # assets
    assets_dir = os.path.join(root, 'assets')
    for filename in os.listdir(assets_dir):
        if filename.endswith('.html') or filename.endswith('.php'):
            path = os.path.join(assets_dir, filename)
            with open(path, 'r', encoding='utf-8') as f:
                c = f.read()
            new_c = replace_in_content(c, True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_c)

if __name__ == "__main__":
    main()
