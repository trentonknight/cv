# Jekyll Resume Build Scripts

## Development

### Start Development Server
```bash
podman-compose up
```

### Stop Development Server
```bash
podman-compose down
```

### Rebuild Container
```bash
podman-compose up --build
```

## Build for Production

### Build and Test
```bash
podman-compose run jekyll-runner
```

### Build with Custom Config
```bash
podman-compose exec jekyll-runner bundle exec jekyll build --config _config.yml
```

### Build and Watch (Auto-reload on changes)
```bash
podman-compose up -d
```

Then edit files and check `_site` directory for output.

## GitHub Actions

GitHub Actions will:
1. Build Jekyll site on push to main/master
2. Deploy automatically to GitHub Pages
3. Store build artifacts for 7 days

## Debugging

### View Container Logs
```bash
podman-compose logs jekyll-runner
```

### Enter Running Container
```bash
podman-compose exec jekyll-runner bash
```

### Run Custom Commands
```bash
# Inside container
bundle exec jekyll build --trace
bundle exec rake
```

## Troubleshooting

### Gem Installation Issues
Edit `Gemfile` and ensure compatibility with Ruby 3.4

### Permission Errors
```bash
podman-compose down
rm -rf ./.jekyll-cache
podman-compose up --build
```

### Check Build Output
```bash
ls -la _site/
tree _site/ | head -50
```

## Environment Variables

You can override config values by setting environment variables:

```bash
JEKYLL_TIMEOUT_EXCESS=60 podman-compose run jekyll-runner
```

See `_config.yml` for available variables.

## Dockerfile Explanation

- Uses Ruby 3.4 Alpine (lightweight)
- Installs system dependencies for Ruby
- Runs `bundle install` to cache gems
- Multi-stage build for production

## Network Architecture

```
├── jekyll-build   (builds gems, no runtime)
├── ruby          (installs gems, shared cache)
└── jekyll-runner  (runs jekyll build)
     └── depends on: ruby
```

## Files Structure

```
.
├── Dockerfile
├── podman-compose.yml
├── Gemfile
├── Gemfile.lock
├── Makefile
├── _config.yml
├── _layouts/
│   ├── default.html
│   └── base.html
├── styles/
│   ├── custom.css
│   ├── base.css
│   └── STYLE.md
└── .github/
    └── workflows/
        └── deploy.yml
```

## Next Steps

1. **Test Locally:**
   ```bash
   podman-compose up --build
   ```

2. **Verify Build:**
   Check `_site` directory for expected files

3. **Commit and Push:**
   ```bash
   git add .
   git commit -m "Add containerized build setup"
   git push origin main
   ```

4. **Configure GitHub:**
   - GitHub will trigger the workflow
   - Build and deploy automatically
