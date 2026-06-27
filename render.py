import yaml
import glob
from jinja2 import Environment, FileSystemLoader
import os

# Ensure docs directory exists
os.makedirs('docs', exist_ok=True)

# 1. Aggregate ALL YAML files into a single context
context = {}
for file in glob.glob('data/*.yaml'):
    with open(file, 'r') as f:
        data = yaml.safe_load(f)
        if data:
            context.update(data)

# 2. Setup Jinja
env = Environment(loader=FileSystemLoader('src'))

# 3. Define mapping (Template -> Output)
render_map = {
    'main.tex.j2': 'docs/JNMansfield-Main-CV.tex',
    'addendum.tex.j2': 'docs/JNMansfield-Addendum.tex',
    'index.html.j2': 'docs/index.html'
}

# 4. Render
for template_file, output_file in render_map.items():
    template = env.get_template(template_file)
    with open(output_file, 'w') as f:
        f.write(template.render(context))

print("Build complete: Generated source files in /docs")
