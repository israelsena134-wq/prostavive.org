import re

def final_polish(content):
    # Fix the status / 100 corruption
    content = content.replace('status index.html 100', 'status / 100')
    
    # Fix any remaining index.html that should be /
    # But be careful not to break legitimate assets/ index.html (which shouldn't exist now)
    # Actually, let's just target the status code one since it's the most obvious one left.
    
    # Also check for clarity.msindex.html or similar
    content = content.replace('clarity.msindex.html', 'clarity.ms/')
    
    return content

file_path = r'c:\Users\Guga\Downloads\prostavive.org\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = final_polish(content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Final polish done.")
