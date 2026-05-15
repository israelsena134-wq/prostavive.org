import os

def main():
    root_dir = r'c:\Users\Guga\Downloads\prostavive.org'
    suspicious_terms = ['eval(', 'base64', 'window.location.replace', 'atob(', 'btoa(', 'String.fromCharCode']
    
    print("--- SECURITY SCAN START ---")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip .git
        if '.git' in dirpath:
            continue
            
        for f in filenames:
            if f.endswith(('.html', '.js', '.php')):
                path = os.path.join(dirpath, f)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                        content = file.read()
                        for term in suspicious_terms:
                            if term in content:
                                # Find line number
                                lines = content.splitlines()
                                for i, line in enumerate(lines):
                                    if term in line:
                                        print(f"[SUSPICIOUS] '{term}' found in {f} on line {i+1}: {line.strip()[:100]}")
                except Exception as e:
                    print(f"Error reading {f}: {e}")
    print("--- SECURITY SCAN END ---")

if __name__ == "__main__":
    main()
