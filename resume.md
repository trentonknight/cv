---
layout: null
permalink: /resume.md
---
# Jason N. Mansfield
**Platform Engineer & DevOps · GitOps, LLMOps & DevSecOps**  
Flowers · Clayton, NC (`35.6574° N, 78.3614° W`) · Remote (≤25% Travel)  
Phone: (757) 753-0085 · Email: trentonknight@gmail.com  
GitHub: https://github.com/trentonknight · GitLab: https://gitlab.com/trentonknight · LinkedIn: https://www.linkedin.com/in/trentonknight/

---

## About & Specialization
Platform Engineer with expertise in designing secure, cloud-native systems. Specialized in **GitOps / DevOps**, **Platform Engineering**, **LLMOps / AI Infrastructure**, and **DevSecOps**, backed by 22+ years of continuous active-duty U.S. Navy and U.S. Coast Guard service.

---

## Experience
{% for stop in site.data.expedition %}
### {{ stop.title }} — {{ stop.org }}{% if stop.org_url and stop.org_url != "" %} ([{{ stop.org_url }}]({{ stop.org_url }})){% endif %}
*{{ stop.period }}* | {{ stop.location }}{% if stop.coords and stop.coords != "" %} (`{{ stop.coords }}`){% endif %}

{% for bullet in stop.highlights %}- {{ bullet }}
{% endfor %}
{% endfor %}

---

## Technical Stack & Languages
- **Cloud, Platform & GitOps:** AWS (EC2, RDS, S3), Kubernetes, Terraform, ArgoCD, Helm, Rafay, Azure, Docker, Keycloak, Vault / OpenBao, JFrog Artifactory, Anchore, Harness
- **AI / LLMOps:** Llama Stack, Ollama, Vertex AI, Gemini, Docling, Pandas, Hugging Face Diffusers, SDXL
- **Languages & Markup:** Python, Rust, Bash / Shell, SQL, YAML, JavaScript, LaTeX (Sphinx)

---

## Technical Research & Applied AI
- **LLMOps & Local Inference:** Orchestrating local model deployments via Llama Stack and Ollama; engineering custom Modelfiles and external prompting strategies to tune model behaviors.
- **RAG & ETL Pipelines:** Utilizing Docling for high-fidelity document parsing and Pandas for structured data transformation to optimize RAG context-window precision.
- **Systems Tooling:** Implementing high-performance utility tools in Rust to enhance existing Python-based infrastructure automation and CLI tooling.
- **Generative Art Pipelines:** Exploring Hugging Face Diffusers and SDXL pipelines for procedural game textures and automated concept generation.

---

## Education
### B.S. in Computer Science — Regis University
*2007 – 2013* | Denver, CO (`39.7875° N, 105.0325° W`) · ABET Accredited · NSA Center of Academic Excellence
- **Honors & Standing:** Dean’s List (Spring 2013) · GPA 3.413
- **Mathematics (17 credits):** Calculus, Linear Algebra, Discrete Math
- **Computer Science Core:** Systems Architecture, Algorithms, Data Structures, Software Engineering, OOP (Java/C++)

---

## Clearance & Standards Governance (DoD 8140.03)
{{ site.data.standards.intro }}
{% for item in site.data.standards.provisions %}
- **{{ item.title }}** (`{{ item.cite }}`): {{ item.description }}
{% endfor %}

---

## Publications
- **“Monolithic IT Architecture: We’re Not Stonehenge Anymore.”** — *U.S. Naval Institute Proceedings*, Vol. 147/11/1,425 (Nov 2021): https://www.usni.org/magazines/proceedings/2021/november/monolithic-it-architecture-were-not-stonehenge-anymore

---

## Extended Service & Systems Log (1999 – Present)
{% for stop in site.data.addendum %}
### {{ stop.title }} — {{ stop.org }}{% if stop.org_url and stop.org_url != "" %} ([{{ stop.org_url }}]({{ stop.org_url }})){% endif %}
*{{ stop.period }}* | {{ stop.location }}{% if stop.coords and stop.coords != "" %} (`{{ stop.coords }}`){% endif %}{% if stop.category and stop.category != "" %} | {{ stop.category }}{% endif %}

{% for bullet in stop.highlights %}- {{ bullet }}
{% endfor %}
{% endfor %}

---

## Supervisory & Professional References
{% for group in site.data.contacts %}
### {{ group.organization }}{% if group.period and group.period != "" %} ({{ group.period }}){% endif %}
{% for person in group.people %}- **{{ person.name }}**{% if person.relationship and person.relationship != "" %} *({{ person.relationship }})*{% endif %}{% if person.role and person.role != "" %} — {{ person.role }}{% endif %}{% if person.phone and person.phone != "" %} | Tel: {{ person.phone }}{% endif %}{% if person.email and person.email != "" %} | Email: {{ person.email }}{% endif %}{% if person.notes and person.notes != "" %} | {{ person.notes }}{% endif %}
{% endfor %}
{% endfor %}

