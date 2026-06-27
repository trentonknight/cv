import yaml
import glob
from jinja2 import Environment, FileSystemLoader
import os

# Ensure docs directory exists
os.makedirs('docs', exist_ok=True)

# 1. Aggregate ALL YAML files into a single context
context = {}
data_files = glob.glob('data/*.yaml')
print(f"--- Loading data from: {data_files} ---")

for file in data_files:
    with open(file, 'r') as f:
        file_data = yaml.safe_load(f)
        if file_data:
            context.update(file_data)
            print(f"Loaded {os.path.basename(file)}: Keys found -> {list(file_data.keys())}")

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
        print(f"Generated {output_file}")

print("--- Build Complete ---")
