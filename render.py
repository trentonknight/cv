import yaml
import glob
import os
import shutil
from jinja2 import Environment, FileSystemLoader

# --- Configuration ---
DATA_DIR = 'data'
SRC_DIR = 'src'
DOCS_DIR = 'docs'

def render():
    # 1. Ensure docs directory exists
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)

    # 2. Aggregate ALL YAML files into a single context
    context = {}
    data_files = glob.glob(os.path.join(DATA_DIR, '*.yaml'))
    
    print(f"--- Loading data from {DATA_DIR}/ ---")
    for file in data_files:
        with open(file, 'r') as f:
            file_data = yaml.safe_load(f)
            if file_data:
                context.update(file_data)
                print(f"Loaded {os.path.basename(file)}: {list(file_data.keys())}")

    # 3. Setup Jinja Environment
    env = Environment(loader=FileSystemLoader(SRC_DIR))

    # 4. Define mapping (Template -> Output)
    render_map = {
        'main.tex.j2': 'docs/JNMansfield-Main-CV.tex',
        'addendum.tex.j2': 'docs/JNMansfield-Addendum.tex',
        'index.html.j2': 'docs/index.html'
    }

    # 5. Render Templates
    for template_name, output_path in render_map.items():
        template = env.get_template(template_name)
        with open(output_path, 'w') as f:
            f.write(template.render(context))
            print(f"Generated {output_path}")

    # 6. Asset Sync (Optional: Ensure docs/assets exists for your HTML/PDFs)
    if os.path.exists('assets'):
        if os.path.exists(os.path.join(DOCS_DIR, 'assets')):
            shutil.rmtree(os.path.join(DOCS_DIR, 'assets'))
        shutil.copytree('assets', os.path.join(DOCS_DIR, 'assets'))
        print("Synchronized assets/ to docs/assets/")

    print("--- Build Complete ---")

if __name__ == "__main__":
    render()
