import re

def final_cleanup(content):
    # Fix the closing tags with index.html
    # <meta ... index.html> -> <meta ... />
    content = content.replace('index.html>', ' />')
    
    # Fix regex literals that got broken
    # index.html([^=]+)=(.*)index.html -> /([^=]+)=(.*)/
    content = re.sub(r'index.html([^ \n]+)index.html', r'/\1/', content)
    
    # Fix split(/[&]+/)
    content = content.replace('index.html&+index.html', '/[&]+/')
    
    # Fix clarity URL
    content = content.replace('msindex.html0.8.64', 'ms/0.8.64')
    
    # Fix any other ms/ index.html patterns
    content = content.replace('msindex.html', 'ms/')
    
    # Fix double slashes
    content = content.replace('index.htmlindex.html', '//')
    
    # Fix assets/ slashes if any are left
    content = content.replace('assetsindex.html', 'assets/')
    
    # Fix og:url content="index.html" -> content="/"? 
    # Usually og:url should be a full URL, but if it was "/" it became "index.html".
    content = content.replace('content="index.html"', 'content="/"')

    # Fix the beacon script that I accidentally broke in the previous step
    # It should have a src.
    # Looking at the previous view_file (line 1369):
    # src="assets/aca73fc574e12740_v833ccba57c9e4d2798f2e76cebdd0.js"
    if "data-cf-beacon=" in content and 'src=""' in content:
        content = content.replace('src=""', 'src="assets/aca73fc574e12740_v833ccba57c9e4d2798f2e76cebdd0.js"')
    elif "data-cf-beacon=" in content and 'defer=""></script>' in content:
        content = content.replace('defer=""></script>', 'defer="" src="assets/aca73fc574e12740_v833ccba57c9e4d2798f2e76cebdd0.js"></script>')

    return content

file_path = r'c:\Users\Guga\Downloads\prostavive.org\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = final_cleanup(content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Final cleanup of index.html done.")
