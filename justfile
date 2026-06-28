# List all available commands
default:
    @just --list

# Render all HTML/PDF artifacts
render:
    uv run render.py

# Format code and yaml files
format:
    uv run ruff format .
    
# Lint code and check project files
lint:
    uv run ruff check .

# Run all quality checks
check:
    uv run ruff format --check .
    uv run ruff check .

# Start a local web server to preview the docs/ folder
preview:
    @echo "Previewing at http://localhost:8000"
    @cd docs && python3 -m http.server 8000

# Combined task: Render and then launch the preview
dev: render
    @just preview

# Clean up build artifacts
clean:
    rm -rf docs/*.html
    rm -rf docs/*.pdf
