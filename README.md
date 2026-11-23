# Jason N. Mansfield — Curriculum Vitae

Cartographic, topo-inspired Jekyll curriculum vitae and reference site for **Jason N. Mansfield** (Platform Engineer & DevOps · GitOps, LLMOps & DevSecOps), backed by structured YAML datasets, expandable experience and reference views, per-section clipboard copy tools, and dynamic pure-Markdown export endpoints.

- **Live Site:** https://trentonknight.github.io/cv/
- **Location Datum:** Flowers · Clayton, NC (`35.6574° N, 78.3614° W`) · Remote (≤25% Travel)

---

## Architecture Overview

### Pages
- **`index.html` (`/`):** Main Curriculum Vitae featuring the contact block, quick-jump section navigation, **Copy Full .md** button, per-section **Copy Section** buttons, **Professional & Military Experience** with one-line scope summaries and expandable `<details>` duty dropdowns (**Expand All / Collapse All**), **Technical Stack & Languages**, **Applied AI & Systems Engineering**, **Education**, **Clearance & Standards Governance (DoD 8140.03)**, and **Publications**.
- **`addendum/index.html` (`/addendum/`):** **Professional & Command References** grouped by organization and service period inside collapsible `<details>` sections (**Expand All / Collapse All**), with structured Markdown clipboard copy (`Copy Section` and `Copy Full .md`).
- **`compliance/index.html` (`/compliance/`):** **DoD 8140.03 / CWQP & Contracting Qualification Reference** featuring the Specification Ledger table (`#compliance-*` deep-link anchors), **Position Qualification Verification Questions**, **Contracting Terms & Primary Policy References**, Markdown pipe-table copy (`Copy Table`), and `Copy Full .md`.

### Dynamic Markdown Endpoints (`.txt`)
All `.txt` endpoints use `layout: null` with a `.txt` extension so Jekyll evaluates Liquid `site.data` loops without converting Markdown to HTML. Each serves raw Markdown directly to browsers, ATS parsers, and the **Copy Full .md** buttons:
- **`resume.txt` (`/resume.txt`):** Full plain-Markdown curriculum vitae generated from `_data/expedition.yml` and `_data/standards.yml`.
- **`references.txt` (`/references.txt`):** Structured Markdown list of supervisory, engineering, and command references generated from `_data/contacts.yml`.
- **`table.txt` (`/table.txt`):** Plain-Markdown pipe table of the DoD 8140.03 / CWQP Qualification Matrix, verification questions, and contracting terms.

### Data Layer (`_data/`)
- **`_data/expedition.yml`:** Experience stops (`id`, `title`, `org`, `org_url`, `location`, `coords`, `period`, `compliance_anchor`, `compliance_label`, optional `summary`, and `highlights`).
- **`_data/contacts.yml`:** Supervisory, peer, and military command references grouped by `organization` and `period`, with nested `people` entries (`name`, `relationship`, `role`, `phone`, `email`, `linkedin`, `notes`).
- **`_data/standards.yml`:** Clearance badge text (`clearance.badge_text`), overview copy (`intro`), and DoD 8140.03 provisions (`provisions`).

### Styling & Includes
- **`assets/css/cv.css`:** Shared cartographic styling, specification ledgers, navigation bars, document index switchers, and responsive layout rules.
- **`_includes/trail-map.html` & `_includes/compass.svg`:** Route map and compass SVG elements included across the site.

---

## Local Build & Hosting

### Prerequisites
- Ruby (`>= 3.0`) and Bundler (`gem install bundler`)

### Install & Serve Locally
```bash
git clone [https://github.com/trentonknight/cv.git](https://github.com/trentonknight/cv.git)
cd cv
bundle install
bundle exec jekyll serve --livereload
```

Open `http://127.0.0.1:4000/cv/` (or `http://127.0.0.1:4000/` depending on your `_config.yml` `baseurl`) to preview all pages and `.txt` endpoints:
- `/` — Main CV
- `/addendum/` — Professional & Command References
- `/compliance/` — DoD 8140.03 & Contracting Reference
- `/resume.txt` — Raw Markdown CV
- `/references.txt` — Raw Markdown References
- `/table.txt` — Raw Markdown Qualification Matrix

### Production Build Check
Verify zero Liquid warnings and clean static output in `_site/`:
```bash
rm -rf _site && bundle exec jekyll build
```

