# Styles Configuration

## Theme: Deep Tech

This custom theme uses a Deep Tech color scheme with split-page layout.

### Available Colors

deepnavy: "#1A2E40"
slateteal: "#2E5A5E"
techpurple: "#5A4E8C"
softgrey: "#F2F2F2"
accent: "#2E5A5E"

### Default Values

- **deepnavy**: Primary accent color (headers, titles, buttons)
- **slateteal**: Secondary accent color (body text, tags, highlights)
- **techpurple**: Tertiary accent color (decorative elements)
- **softgrey**: Background color
- **accent**: Alternate accent color

### Color Usage

- **Headers/Titles**: deepnavy (strong, authoritative)
- **Body Text**: slateteal (readable, professional)
- **Tags/Highlights**: slateteal with border or gradient
- **Background**: softgrey (clean, modern)
- **Buttons/CTAs**: gradient of deepnavy to slateteal
- **Accents**: techpurple (subtle highlights)

### Typography

Primary Font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif
Font Size: 16px base
Line Height: 1.6
Font Weight:
  - Headers: 700 (bold)
  - Body: 400 (normal)
  - Date tags: 600 (semi-bold)

### Layout

**Split Column Layout:**
- Left column (300px sticky sidebar): About, Specialization, Compliance
- Right column (flexible): Experience, Military History, Education
- Mobile: Stacks vertically, sidebar becomes static at top

**Responsive Breakpoints:**
- Desktop: 768px+
- Tablet: 480px - 768px
- Mobile: < 480px

### Components

**Experience Item:**
- Role: Bold, large (1.1rem)
- Date: Badge style with background color
- Company: Smaller, lighter text
- Bullets: Custom arrow (▸) with proper indentation

**Military Item:**
- Header: Bold, date on left, branch on right
- Content: Paragraph with proper indentation

**Education:**
- School: Bold
- Degree: Italic or lighter
- Details: Bulleted list with custom bullets (•)

**Tags:**
- Rounded rectangle style
- Border in accent color
- Hover: Invert colors

### Responsive Design

**Desktop (> 768px):**
- Split two-column grid
- Sidebar is sticky (follows scroll)

**Tablet (480px - 768px):**
- Reduced padding and margins
- Smaller font sizes
- Sidebar still sticky

**Mobile (< 480px):**
- Single column
- Sidebar at top (not sticky)
- Experience items stack vertically

### Print Styles

- Colors optimized for B&W printing
- Split layout becomes single column
- Page breaks after sections
- Images simplified to grayscale

---

## Updating Colors

Edit the _config.yml file in the root directory:

deepnavy: "#1A2E40"
slateteal: "#2E5A5E"
techpurple: "#5A4E8C"
softgrey: "#F2F2F2"
accent: "#2E5A5E"

Changes will reflect on all pages automatically.

---

## Fonts

No external fonts are required. Uses system fonts for optimal performance.

Available system fonts:
- **macOS**: San Francisco, Helvetica Neue, Arial
- **Windows**: Segoe UI, Consolas
- **Linux**: Cantarell, DejaVu Sans Mono

---

## Accessibility

- **Contrast Ratios**: All text meets WCAG AA standards (4.5:1 for body, 7:1 for headers)
- **Color Blindness**: Colors chosen to work for deuteranopia and protanopia
- **Focus States**: All interactive elements have visible focus indicators
- **Screen Readers**: Semantic HTML with proper heading hierarchy

---

## Browser Support

Chromium-based browsers only (as required by GitHub Pages):
- Google Chrome
- Edge
- Opera
- Brave
- Arc

Tested on Chrome 120+
