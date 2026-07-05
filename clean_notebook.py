import json
import sys

def fix_notebook(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Safely remove the invalid top-level widgets metadata
    if 'metadata' in data and 'widgets' in data['metadata']:
        del data['metadata']['widgets']
        print(f"Successfully removed 'metadata.widgets' from {file_path}")
    else:
        print("No top-level 'metadata.widgets' found.")
        
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fix_notebook(sys.argv[1])
    else:
        print("Usage: python clean_notebook.py <your_notebook.ipynb>")
