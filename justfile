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
    python3 -m http.server 8000 --directory docs

# Combined task: Render and then launch the preview
dev: render
    @just preview

# Clean up only generated HTML and PDF files, leaving assets untouched
clean:
    find docs/ -type f \( -name "*.html" -o -name "*.pdf" \) -delete

# Full reset: Remove the entire docs directory
distclean:
    rm -rf docs
