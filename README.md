# Jason N. Mansfield — Curriculum Vitae

Cartographic, topo-inspired Jekyll curriculum vitae and career addendum site for **Jason N. Mansfield** (Platform Engineer & DevOps · GitOps, LLMOps & DevSecOps), backed by structured YAML datasets, per-section clipboard copy tools, and a dynamic pure-Markdown export endpoint.

- **Live Site:** https://trentonknight.github.io/cv/
- **Last Deployed:** By `@trentonknight` (`trentonknight`) · 2 hours ago
- **Location Datum:** Flowers · Clayton, NC (`35.6574° N, 78.3614° W`) · Remote (≤25% Travel)

---

## Architecture Overview

### Pages & Endpoints
- **`index.html` (`/`):** Main Curriculum Vitae featuring the Comms Beacon contact block, quick-jump triage bar, interactive **Copy Full .md** action, per-section **Copy Section** buttons with whitespace/indentation normalization, Career Expedition Route & Experience, Field Loadout stack manifest, Field Recon applied AI notes, Academic Basecamp education quadrant, DoD 8140.03 governance/clearance cards, and USNI publication dispatch.
- **`addendum/index.html` (`/addendum/`):** Extended Service & Systems Log (`1999 – Present`) and Supervisory & Professional References grouped by organization, with clickable phone, email, and LinkedIn links and per-section clipboard copy support.
- **`resume.txt` (`/resume.txt`):** Uses `layout: null` and `permalink: /resume.txt` with a `.txt` extension so Jekyll evaluates Liquid `site.data` loops without running Markdown-to-HTML conversion. This serves raw Markdown text directly to viewers and powers the **Copy Full .md** button.

### Data Layer (`_data/`)
- **`_data/expedition.yml`:** Primary experience waypoints, roles, dates, locations, coordinates, compliance links, and highlights.
- **`_data/addendum.yml`:** Full chronological service and systems log entries (`1999 – Present`) across industry, DoD SkillBridge, U.S. Coast Guard, U.S. Navy, and pre-service basecamps.
- **`_data/contacts.yml`:** Supervisory and professional references grouped by organization and period, including `name`, `relationship`, `role`, `phone`, `email`, `linkedin`, and `notes`.
- **`_data/standards.yml`:** Clearance badge text, overview copy, and DoD 8140.03 qualification/reciprocity provisions.

### Styling & Includes
- **`assets/css/cv.css`:** Cartographic styling, quadrant cards, navigation bars, and responsive layout rules.
- **`_includes/trail-map.html` & `_includes/compass.svg`:** Visual route map and compass elements included across the CV pages.

---

## Local Build & Verification

Build the site locally with Jekyll:

```bash
bundle exec jekyll build

