import yaml
import glob
import os
import shutil
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# --- Configuration ---
DATA_DIR = 'data'
SRC_DIR = 'src'
DOCS_DIR = 'docs'
ASSETS_DIR = 'assets'

def render():
    # 1. Setup Environment
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)

    # 2. Load Data
    context = {'base_asset_path': 'assets'}
    for file in glob.glob(os.path.join(DATA_DIR, '*.yaml')):
        filename = os.path.basename(file)
        key = os.path.splitext(filename)[0]
        with open(file, 'r') as f:
            data = yaml.safe_load(f)
            
            # Smart unwrapping
            if isinstance(data, dict) and key in data and len(data) == 1 and not isinstance(data[key], list):
                context[key] = data[key]
            else:
                context[key] = data
            print(f"Loaded {filename} into context['{key}']")

    # 3. Synchronize Assets (Always happens so docs/ stays self-contained)
    target_assets = os.path.join(DOCS_DIR, ASSETS_DIR)
    if os.path.exists(target_assets):
        shutil.rmtree(target_assets)
    if os.path.exists(ASSETS_DIR):
        shutil.copytree(ASSETS_DIR, target_assets)
        print("Assets synchronized to docs/assets/.")

    # 4. Render HTML
    env = Environment(loader=FileSystemLoader(SRC_DIR))
    
    pages = [
        {'template': 'index.html.j2', 'output': 'index.html', 'page_id': 'index'},
        {'template': 'experience.html.j2', 'output': 'experience.html', 'page_id': 'exp'},
        {'template': 'service.html.j2', 'output': 'service.html', 'page_id': 'svc'},
        {'template': 'contacts.html.j2', 'output': 'contacts.html', 'page_id': 'con'}
    ]

    for p in pages:
        template = env.get_template(p['template'])
        output_path = os.path.join(DOCS_DIR, p['output'])
        
        page_context = context.copy()
        page_context['page'] = p['page_id']
        
        with open(output_path, 'w') as f:
            f.write(template.render(page_context))
        print(f"Generated {p['output']}")

    # 5. Generate PDFs
    pdf_map = {
        'experience.html': 'JNMansfield-Professional-CV.pdf',
        'service.html': 'JNMansfield-Service-History.pdf',
        'contacts.html': 'JNMansfield-Contact-List.pdf'
    }

    for html_file, pdf_file in pdf_map.items():
        print(f"Generating {pdf_file}...")
        HTML(
            filename=os.path.join(DOCS_DIR, html_file),
            base_url=DOCS_DIR
        ).write_pdf(os.path.join(DOCS_DIR, pdf_file))

    print("--- Build Complete: All artifacts generated. ---")

if __name__ == "__main__":
    render()
