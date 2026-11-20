# Jason Mansfield - Resume (CV)
**Platform Engineer | DevOps | LLMOps | USN/USCG Veteran**

[![View Live Resume](https://img.shields.io/badge/Live-Resume-blue)](https://trentonknight.github.io/cv/)
[![PDF Download](https://img.shields.io/badge/PDF-Download-orange)](./JNMansfield-Addendum.pdf)
[![GitHub](https://img.shields.io/badge/GitHub-trentonknight-8da5cb.svg?logo=github)](https://github.com/trentonknight)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-trentonknight-0077b5.svg?logo=linkedin)](https://www.linkedin.com/in/trentonknight/)

---

## Quick Summary

- **22+ years** continuous US Navy & USCG IT/Cyber active-duty service
- **Platform Engineer** specializing in GitOps, DevOps, LLMOps, and DevSecOps
- **DoD 8140.03 Compliance**: Covered under 20+ year service recency waiver
- **Clearance**: TS/SCI w/ CI Poly (Active)
- **Clearance History**: USN (2001-2005), USCG (2005-2023)

## Core Expertise

### Technical Stack
- **Orchestration**: Kubernetes, Helm, ArgoCD
- **IaC**: Terraform, Ansible
- **AI/ML**: Vertex AI, LLMOps, Llama Stack, Ollama
- **DevOps**: GitLab CI, Jenkins, GitHub Actions
- **Docker**: Multi-stage builds, Docker Compose

### Languages
- Python, Bash, JavaScript, Rust, Go

### Security
- Vault, Keycloak, Anchore, Nessus, Harness
- TACLANE, OVH
- TCTO compliance

---

## Professional Experience

### **24x7 Systems | CME**
*Platform Engineer / Lead | 2024 – Present*

- **Operations Leadership**: Manage K8s cluster stability and emergency response
- **AI Augmentation**: Integrated Vertex AI and Gemini for root-cause analysis
- **Automated Documentation**: Built self-service documentation pipelines

### **CACI International | EPT**
*DevOps Engineer | 2023 – 2024*

- **GitOps Orchestration**: Led GitLab and Vault infrastructure
- **State Enforcement**: Ensured 100% platform compliance with GitOps
- **Custom Tooling**: Built Python/Bash automation for API integrations

### **CACI International | Holladay, GA**
*Software Engineer | 2019 – 2023*

- Developed Python automation tools for infrastructure management
- Built Terraform modules for cloud resource provisioning
- Integrated Vertex AI for predictive maintenance workflows

---

## Military History

### **2021 – 2023 | USCG CYBER | COA Branch**
*IT Specialist 1st Class, Assessments Blue Team*

- Developed tactical "Ruck Kits" for field operators
- Instructed Cisco switch programming and TCTO compliance
- Authored technical guides for Nessus, Sharphound, Bloodhound

### **2017 – 2021 | USCG NOSC EOC**
*IT Specialist 1st Class, Watch Supervisor*

- Managed DODIN and bi-weekly leadership briefs
- Supervised junior analysts, provided technical training

### **2014 – 2017 | USCG CGC DILIGENCE**
*IT Specialist 2nd Class, Independent Network Admin*

- Managed dual Cisco 3750G stacks, Server 2008 R2
- TACLANE encryption systems
- KVH Satellite systems and shipboard WAN infrastructure

---

## Education

### **BS Computer Science**
*Regis University (ABET / NSA Center of Academic Excellence) | 2005*

- Dean's List (Spring 2013), GPA 3.413
- Mathematics: Calculus, Linear Algebra, Discrete Math
- CS Core: Systems Architecture, Algorithms, Data Structures
- **DoD 8140.03 § 3.2.b(1)(a)(3)**: 20+ years service waives recency requirement

---

## Certifications

- **CompTIA Security+** – Superseded by DoD 8140.03
- **CompTIA CySA+** – Superseded by DoD 8140.03

---

## Regulatory References

This resume complies with **DoD 8140.03** cybersecurity workforce qualification requirements:

1. **§ 3.2.b(1)(a)(3)**: 20+ years continuous service waives degree recency
2. **§ 3.2.b(1)(a)**: Professional experience supersedes legacy DoD 8570 baseline certs

---

## View the Full Resume

For a complete, detailed version with full professional history and references, please download the PDF addendum:

[📄 Download Full Career Addendum](./JNMansfield-Addendum.pdf)

---

## Contact

- 📧 **Email**: trentonknight@gmail.com
- 📞 **Phone**: (757) 753-0085
- 📍 **Location**: Clayton, NC

**LinkedIn**: [linkedin.com/in/trentonknight](https://www.linkedin.com/in/trentonknight/)  
**GitHub**: [github.com/trentonknight](https://github.com/trentonknight)  
**GitLab**: [gitlab.com/trentonknight](https://gitlab.com/trentonknight)

---

## System Requirements

### Containerized Build (Recommended)

This Jekyll site uses containerized builds via Podman/Podman Compose:

- **Podman** 4.0+ ([install](https://podman.io/getting-started/installation))
- **Podman Compose** 1.0+ ([install](https://github.com/poseidon/podman-compose))
- Docker-compatible environment
- Git (for dependency management)

### Development Environment (Optional)

For direct Ruby/Jekyll development:

- **Ruby** 3.0+
- **Bundler** 2.0+
- **Jekyll** 4.0+
- **GitHub Pages** gem 2.2.0+
- Git

---

## Development

### Containerized Build (Recommended)

```bash
# Start or stop the build containers
podman-compose down
podman-compose up

# Rebuild containers (after Gemfile changes)
podman-compose up --build

# Run the build in a new container
podman-compose run jekyll-runner

# View build logs
podman-compose logs jekyll-runner
```

**Development Environment:**

```bash
podman-compose up  # Starts all services (ruby + jekyll-runner)
```

**Build Commands:**

```bash
# Build and test the site
podman-compose run jekyll-runner

# Build with verbose output
podman-compose exec jekyll-runner bundle exec jekyll build --trace --verbose

# Rebuild everything
podman-compose up --build --no-start
```

**Enter a Running Container:**

```bash
podman-compose exec jekyll-runner bash
```

**View Output:**

```bash
ls -la _site/           # List generated files
tree _site/ | head -50  # Directory tree preview
```

---

### Development Environment (Optional - Not Recommended for Production)

```bash
# Setup: Install Ruby 3.0+ and bundler
gem install bundler

# Install dependencies
bundle install

# Build the site
bundle exec jekyll build

# Preview the site (requires Xcode command-line tools on macOS)
bundle exec jekyll serve
```

### Building for Production (Containerized)

```bash
podman-compose run jekyll-runner

# Output will be in the _site directory
# Copy or move files as needed
```

### Deploy to GitHub Pages

```bash
# Commit and push to main branch
git add .
git commit -m "Your changes"
git push origin main

# GitHub Actions will:
# 1. Build Jekyll site
# 2. Deploy to GitHub Pages automatically
# 3. Generate the live resume URL
```

**Configure GitHub Pages:**

1. Go to repository Settings
2. Navigate to Pages section
3. Build and deployment: "GitHub Actions"
4. Save

The site will be available at: `https://<your-username>.github.io/cv/`

---

## GitHub Actions

Automated build and deploy workflow on `push` to main/master:

- ✅ **Build**: Jekyll build with Ruby 3.4, GitHub Pages gem
- ✅ **Test**: Validates build succeeds
- ✅ **Artifact**: Uploads `_site/` directory (7-day retention)
- ✅ **Deploy**: Automatic deployment to GitHub Pages on push to main

**View Workflow Status:**

```bash
# Check workflow run status
git fetch origin
# Or view on GitHub: https://github.com/<username>/cv/actions

# Re-trigger workflow
# Go to Actions → Select workflow → Run workflow
```

**Environment Variables:**

See `.github/workflows/deploy.yml` for workflow configuration.

### Building for Production (Manual Container Build)

```bash
# Build gems
podman-compose build ruby

# Run jekyll build in container
podman-compose run jekyll-runner

# Output in _site directory
```

---

## File Structure

```
cv/
├── Dockerfile              # Container build configuration (multi-stage)
├── podman-compose.yml      # Podman compose configuration
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions workflow
├── Gemfile                 # Ruby dependencies
├── Gemfile.lock            # Locked dependencies (generated by container)
├── _config.yml             # Jekyll configuration (Deep Tech theme)
├── README.md               # This file
├── index.md                # Resume content (split-column layout)
├── styles/
│   ├── base.css            # Base styles
│   ├── custom.css          # Custom Deep Tech theme
│   └── STYLE.md            # Style documentation
├── _layouts/
│   ├── default.html        # Default template with split layout
│   └── base.html           # Base HTML template
└── images/                 # Your profile images
```

---

## Quick Start

### Local Development

```bash
# Start containers
podman-compose up

# Stop containers
podman-compose down

# Rebuild containers (after Gemfile changes)
podman-compose up --build

# Enter running container
podman-compose exec jekyll-runner bash
```

### Production Build

```bash
podman-compose run jekyll-runner
# Check output in _site directory
ls -la _site/
```

### GitHub Pages Deployment

```bash
git add .
git commit -m "Your changes"
git push origin main

# View build status: https://github.com/<username>/cv/actions
```

---

---

## Customization

To modify the theme colors, edit the `_config.yml` file:

```yaml
deepnavy: "#1A2E40"
slateteal: "#2E5A5E"
techpurple: "#5A4E8C"
softgrey: "#F2F2F2"
```

To update content, edit `index.md` and modify the YAML frontmatter and content sections.

---

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.

---

## License

This resume template is available under the MIT License.

---

**Made with ❤️ by Jason N. Mansfield**
