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

def render():
    # 1. Setup Environment
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)

    # 2. Load Data
    context = {'base_asset_path': 'assets'} # Define global asset path
    for file in glob.glob(os.path.join(DATA_DIR, '*.yaml')):
        with open(file, 'r') as f:
            data = yaml.safe_load(f)
            if data:
                context.update(data)
                print(f"Loaded {os.path.basename(file)}")

    # 3. Synchronize Assets
    if os.path.exists('assets'):
        target_assets = os.path.join(DOCS_DIR, 'assets')
        if os.path.exists(target_assets):
            shutil.rmtree(target_assets)
        shutil.copytree('assets', target_assets)
        print("Assets synchronized.")

    # 4. Render HTML and Markdown
    env = Environment(loader=FileSystemLoader(SRC_DIR))
    templates = {
        'index.html.j2': 'index.html',
        'experience.html.j2': 'experience.html',
        'addendum.html.j2': 'addendum.html',
        'markdown.j2': 'resume.md'
    }

    for template_name, output_name in templates.items():
        template = env.get_template(template_name)
        output_path = os.path.join(DOCS_DIR, output_name)
        with open(output_path, 'w') as f:
            f.write(template.render(context))
        print(f"Generated {output_name}")

    # 5. Generate PDFs
    pdf_map = {
        'experience.html': 'JNMansfield-Professional-CV.pdf',
        'addendum.html': 'JNMansfield-Service-History.pdf'
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
