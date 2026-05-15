import os

def main():
    root_dir = r'c:\Users\Guga\Downloads\prostavive.org'
    index_path = os.path.join(root_dir, 'index.html')
    
    if not os.path.exists(index_path):
        print("Error: index.html not found.")
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the Cookie Banner CSS
    cookie_css = """
<style>
    /* Cookie Banner Styles */
    #cookie-banner {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 400px;
        background: #ffffff;
        color: #333;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        z-index: 10000;
        display: none;
        font-family: 'Outfit', sans-serif;
        border: 1px solid #eee;
    }
    #cookie-banner p { margin: 0 0 15px 0; font-size: 14px; line-height: 1.4; }
    #cookie-banner .buttons { display: flex; gap: 10px; }
    #cookie-banner button {
        flex: 1;
        padding: 10px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-weight: 600;
        transition: 0.3s;
    }
    #accept-cookies { background: #1a3c5e; color: white; }
    #accept-cookies:hover { background: #2a5c8e; }
    #decline-cookies { background: #f0f0f0; color: #666; }
</style>
"""

    # Define the Cookie Banner HTML and JS
    # REPLACE 'YOUR_BUYGOODS_AFFILIATE_LINK' with the actual link later
    cookie_html = """
<div id="cookie-banner">
    <p>We use cookies to ensure you get the best experience on our website and to provide personalized content.</p>
    <div class="buttons">
        <button id="accept-cookies">Accept All</button>
        <button id="decline-cookies">Close</button>
    </div>
</div>

<script>
    document.addEventListener("DOMContentLoaded", function() {
        const banner = document.getElementById('cookie-banner');
        const acceptBtn = document.getElementById('accept-cookies');
        const declineBtn = document.getElementById('decline-cookies');
        
        // Show banner after 2 seconds
        if (!localStorage.getItem('cookies-accepted')) {
            setTimeout(() => { banner.style.display = 'block'; }, 2000);
        }

        // Silent Affiliate Cookie Activation (As recommended by the course)
        function activateAffiliateCookie() {
            const affiliateLink = "YOUR_BUYGOODS_AFFILIATE_LINK_HERE"; 
            if (affiliateLink !== "YOUR_BUYGOODS_AFFILIATE_LINK_HERE") {
                const img = new Image();
                img.src = affiliateLink; // Triggers the cookie silently
            }
            console.log("Affiliate cookie mechanism triggered.");
        }

        // Trigger activation regardless of choice
        activateAffiliateCookie();

        acceptBtn.onclick = function() {
            localStorage.setItem('cookies-accepted', 'true');
            banner.style.display = 'none';
        };
        declineBtn.onclick = function() {
            banner.style.display = 'none';
        };
    });
</script>
"""

    # Inject before </body>
    if '</body>' in content:
        new_content = content.replace('</body>', cookie_css + cookie_html + '</body>')
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Cookie banner and silent activation script injected.")
    else:
        print("Error: </body> tag not found.")

if __name__ == "__main__":
    main()
