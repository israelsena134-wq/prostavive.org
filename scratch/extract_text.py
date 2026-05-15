import re
from bs4 import BeautifulSoup
import os

def extract_text(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # Remove scripts and styles
    for script in soup(["script", "style"]):
        script.extract()
    
    # Get text
    text = soup.get_text(separator='\n')
    
    # Clean up whitespace
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    return text

def main():
    root_dir = r'c:\Users\Guga\Downloads\prostavive.org'
    index_path = os.path.join(root_dir, 'index.html')
    
    content = "# Mapa do Site - ProstaVive\n\n"
    content += "## Página Principal (index.html)\n\n"
    
    if os.path.exists(index_path):
        text = extract_text(index_path)
        content += text
    
    # Check other HTML/PHP files in assets that might be pages
    assets_dir = os.path.join(root_dir, 'assets')
    if os.path.exists(assets_dir):
        for filename in os.listdir(assets_dir):
            if filename.endswith('.html') or filename.endswith('.php'):
                file_path = os.path.join(assets_dir, filename)
                # Try to find the original name from ASSET_MAP if possible
                # For now just list them
                content += f"\n\n---\n## Arquivo: {filename}\n\n"
                try:
                    text = extract_text(file_path)
                    content += text
                except Exception as e:
                    content += f"Erro ao extrair texto: {e}"

    with open(os.path.join(root_dir, 'mapa_site.md'), 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    main()
