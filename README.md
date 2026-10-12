# Aadesh Khande — Personal Portfolio Webpage

> Production-ready personal portfolio for **Aadesh Khande**, a Third-Year Computer Science undergraduate and full stack developer. Built using **strictly pure HTML5 and vanilla CSS3** (zero frameworks, zero JavaScript runtime dependencies), featuring responsive layouts, modern software showcase cards, scalable SVG tech stack iconography, an accessible contact form, and complete multi-device compatibility.

---

## Student & Project Metadata

- **Student Name:** Aadesh Khande
- **Role:** Third-Year Computer Science Undergraduate & Full Stack Developer
- **Email:** `contact@aadeshkhande.com`
- **Course:** B.Tech Computer Engineering / Web Technology (FSD)
- **Directory:** `/Portfolio_FSD/`
- **Generated Report:** `Aadesh_Khande_Portfolio_FSD.pdf` (and `202401100090_WT_Portfolio_FSD.pdf`)

### Live Project & Source Code Links
- **Live Deployed Portfolio URL:** [https://javascript-assignment-sable-one.vercel.app/](https://javascript-assignment-sable-one.vercel.app/)
- **GitHub Source Code Repository:** [https://github.com/debugonaut/javascript-assignment.git](https://github.com/debugonaut/javascript-assignment.git)

---

## Architectural & Design Overview

1. **Top Site Navigation:**
   - Fixed/sticky minimal header with brand anchor (`Aadesh Khande`) and navigation links (`About`, `Projects`, `Skills`, `Contact`).
2. **Hero / Introduction:**
   - Greeting: `Hi, I am Aadesh Khande`
   - Subheading: `TY Computer Science Undergrad & Full Stack Developer`
   - Bio: Passionate about building clean, efficient, and reliable web applications. Loves architecting intuitive digital experiences and exploring modern software development from elegant frontend interfaces to robust backend systems.
   - Primary Actions:
     - Pill button (`Contact Me`) leading smoothly to `#contact`.
     - Outline button (`View / Download Resume`) linking to `resume_2-2.pdf` / `resume.pdf`.
   - Circular Portrait Framing: Developer avatar (`image.png`) framed in a sunny-yellow circle (`#fed347`) with calibrated optical scaling.
3. **Projects Showcase (`Some of my work`):**
   - Responsive 3-card grid featuring real landing page and console hero thumbnails:
     - **Video Playback Tracker:** Cross-browser extension (Chrome & Firefox) and web platform that automatically tracks and preserves video playback timestamps across all streaming sites.
       - Live Demo: `https://rewind-player.vercel.app`
       - GitHub: `https://github.com/debugonaut/video-playback-tracker.git`
     - **Groomly:** Pet grooming marketplace & salon management platform connecting pet owners with verified local salons, smart booking, and analytics.
       - Live Demo: `https://groomly-ruddy.vercel.app`
       - GitHub: `https://github.com/debugonaut/Groomly.git`
     - **Thermalwatch AI:** Context-aware satellite thermal intelligence system detecting, categorizing, and monitoring industrial thermal anomalies and wildfires across India.
       - Live Demo: `https://sih26ekaant.web.app`
       - GitHub: `https://github.com/debugonaut/ThermalWatch-AI.git`
   - Dual action links on each card for both Vercel Live Deployment and GitHub Source Code repository.
4. **Skills & Core Technologies (`Technologies I work with`):**
   - 7 official vector SVG icon cards:
     - **HTML** (HTML5 semantic structure)
     - **CSS** (Modern CSS3 styling & responsive layouts)
     - **JavaScript** (ES6+ logic and algorithms)
     - **React** (Component architecture and UI flows)
     - **Node.js** (Backend runtimes and RESTful services)
     - **Git** (Distributed version control)
     - **Figma** (UI/UX prototyping and design systems)
5. **Contact & Social Connectivity (`Get in touch`):**
   - Two-column modern contact section with editorial invitation on the left and form inputs on the right (Name, Email, Message, Send Message).
   - Direct form action targeting `mailto:contact@aadeshkhande.com`.
   - Social footer with SVG icons linked to GitHub (`https://github.com/debugonaut`), LinkedIn (`aadeshkhande`), and Email (`contact@aadeshkhande.com`).
6. **Zero Emojis & Pure Minimalism:**
   - Pure typography, SVG vector assets, and restrained color palette for an elegant, professional finish.

---

## Responsive Formats for All Devices

- **Mobile Viewports (< 640px):**
  - Hero flexes into a single centered column with avatar placed at top.
  - Project cards collapse into a stacked single-column layout.
  - Form fields stack into single-column inputs.
  - Navigation links wrap cleanly with touch targets exceeding 44px.
- **Tablet Viewports (640px – 880px):**
  - Proportional two-column hero with fluid text scaling.
  - Responsive multi-card projects layout.
- **Desktop (881px+):**
  - Full width layout with 980px max container constraint, balanced margins, and smooth hover micro-interactions.

---

## Directory Structure

```
Portfolio_FSD/
├── index.html                   # Semantic HTML5 portfolio webpage
├── styles.css                   # Vanilla CSS3 stylesheet with design tokens
├── image.png                    # Developer avatar image
├── project_1_travel.png         # Travel Guide browser mockup
├── project_2_task.png           # Task Manager browser mockup
├── project_3_furniture.png      # Furniture Store browser mockup
├── screenshot_1_hero_overview.png
├── screenshot_2_mobile_view.png
├── screenshot_3_tablet_view.png
├── screenshot_full_page.png
├── capture_screenshots.py       # Screenshot automation script
├── generate_pdf_report.py       # WeasyPrint PDF report compiler
├── Aadesh_Khande_Portfolio_FSD.pdf # Final 4-page academic & practical report
└── README.md                    # Project documentation
```

---

## Local Development & Server

To run locally:
```bash
python3 -m http.server 3000
```
Open [http://localhost:3000](http://localhost:3000) in your web browser.
