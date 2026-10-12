import os
import weasyprint
import base64
from PIL import Image

current_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Prepare cropped screenshots optimized for PDF page layout from full page screenshot
im_full = Image.open(os.path.join(current_dir, "screenshot_full_page.png"))

# Hero section overview (y=0 to 520)
im_hero = im_full.crop((80, 0, 1200, 520))
im_hero.save(os.path.join(current_dir, "pdf_img_1_hero.png"))

# Projects Showcase (y=520 to 1100)
im_proj = im_full.crop((80, 520, 1200, 1100))
im_proj.save(os.path.join(current_dir, "pdf_img_2_projects.png"))

# Core Tech Skills 7-card row (y=1100 to 1380)
im_tech = im_full.crop((80, 1100, 1200, 1380))
im_tech.save(os.path.join(current_dir, "pdf_img_3_tech_skills.png"))

# Contact & Footer (y=1380 to 1900)
im_contact = im_full.crop((80, 1380, 1200, 1900))
im_contact.save(os.path.join(current_dir, "pdf_img_4_contact.png"))

def get_base64_img(filename):
    path = os.path.join(current_dir, filename)
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

img1_hero = get_base64_img("pdf_img_1_hero.png")
img2_proj = get_base64_img("pdf_img_2_projects.png")
img3_tech = get_base64_img("pdf_img_3_tech_skills.png")
img4_contact = get_base64_img("pdf_img_4_contact.png")
img5_mobile = get_base64_img("screenshot_2_mobile_view.png")
img6_tablet = get_base64_img("screenshot_3_tablet_view.png")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Practical: Personal Portfolio Webpage | Aadesh Khande</title>
  <style>
    @page {{
      size: letter;
      margin: 0.44in 0.55in 0.44in 0.55in;
      @bottom-right {{
        content: "Page " counter(page) " of " counter(pages);
        font-size: 8pt;
        color: #64748b;
        font-family: Arial, sans-serif;
      }}
    }}

    body {{
      font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
      font-size: 8.8pt;
      line-height: 1.38;
      color: #0f172a;
      margin: 0;
      padding: 0;
    }}

    .header-meta {{
      margin-bottom: 6pt;
      font-size: 8.8pt;
      line-height: 1.32;
      border-bottom: 1.2pt solid #cbd5e1;
      padding-bottom: 5pt;
    }}

    .header-meta strong {{
      color: #1e293b;
    }}

    .practical-title {{
      font-size: 11pt;
      font-weight: bold;
      text-decoration: underline;
      margin-top: 4pt;
      margin-bottom: 6pt;
      line-height: 1.3;
      color: #0f172a;
    }}

    .links-top {{
      margin-bottom: 7pt;
      font-size: 8.4pt;
      background: #f8fafc;
      padding: 5pt 8pt;
      border-left: 3pt solid #2563eb;
      border-radius: 2pt;
    }}

    .links-top a {{
      color: #2563eb;
      text-decoration: underline;
    }}

    .section-title {{
      font-size: 9.6pt;
      font-weight: bold;
      color: #1e293b;
      margin-top: 7pt;
      margin-bottom: 3.5pt;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 2pt;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }}

    p {{
      margin: 0 0 5pt 0;
      text-align: justify;
    }}

    ul {{
      margin: 0 0 6pt 15pt;
      padding: 0;
    }}

    li {{
      margin-bottom: 3pt;
    }}

    .code-box {{
      font-family: "Courier New", Courier, monospace;
      font-size: 7.6pt;
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      border-radius: 3pt;
      padding: 5pt 7pt;
      margin: 4pt 0 6pt 0;
      line-height: 1.3;
      color: #0f172a;
    }}

    .screenshot-card {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 4pt;
      padding: 4pt;
      margin: 5pt 0 7pt 0;
      text-align: center;
      page-break-inside: avoid;
    }}

    .screenshot-img {{
      width: 100%;
      height: auto;
      display: block;
      border-radius: 2pt;
    }}

    .screenshot-caption {{
      font-size: 7.8pt;
      font-weight: bold;
      color: #475569;
      margin-top: 3pt;
      text-align: center;
    }}

    .two-col-grid {{
      display: flex;
      gap: 8pt;
      margin: 5pt 0 7pt 0;
      page-break-inside: avoid;
    }}

    .col-img-card {{
      flex: 1;
      border: 1px solid #cbd5e1;
      border-radius: 3pt;
      padding: 4pt;
      text-align: center;
      background: #ffffff;
    }}

    .col-img-card img {{
      width: 100%;
      height: auto;
      max-height: 240pt;
      object-fit: contain;
      display: block;
    }}

    .page-break {{
      page-break-after: always;
    }}

    .final-links-card {{
      background: #eff6ff;
      border: 1.5pt solid #3b82f6;
      border-radius: 4pt;
      padding: 7pt 10pt;
      margin-top: 8pt;
      page-break-inside: avoid;
    }}

    .final-links-title {{
      font-size: 9pt;
      font-weight: bold;
      color: #1d4ed8;
      margin-bottom: 4pt;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .final-links-list {{
      margin: 0 0 0 14pt;
      font-size: 8.3pt;
    }}

    .final-links-list li {{
      margin-bottom: 2.5pt;
    }}

    .final-links-list a {{
      color: #1d4ed8;
      font-weight: bold;
      text-decoration: underline;
    }}
  </style>
</head>
<body>

  <!-- ========================================================================
       PAGE 1: HEADER, OBJECTIVES, ARCHITECTURE, HERO SECTION OVERVIEW
       ======================================================================== -->
  <div class="header-meta">
    <table style="width: 100%; border: none; font-size: 8.8pt;">
      <tr>
        <td style="width: 55%; border: none; padding: 0;">
          <strong>Student Name:</strong> Aadesh Khande<br>
          <strong>Course:</strong> B.Tech Computer Engineering (FSD)<br>
          <strong>Subject:</strong> Web Technology (Lab Practical)
        </td>
        <td style="width: 45%; border: none; padding: 0; text-align: right;">
          <strong>Topic:</strong> Personal Portfolio (HTML5 &amp; CSS3)<br>
          <strong>Directory:</strong> <code>/Portfolio_FSD/</code><br>
          <strong>Email:</strong> <code>contact@aadeshkhande.com</code>
        </td>
      </tr>
    </table>
  </div>

  <div class="practical-title">
    Practical Assignment: Design and Development of a Responsive Personal Portfolio Webpage Using Pure HTML5 and CSS3
  </div>

  <div class="links-top">
    <strong>Project Deployment &amp; Repository:</strong><br>
    • Live Application: <a href="https://javascript-assignment-sable-one.vercel.app/" target="_blank">https://javascript-assignment-sable-one.vercel.app/</a><br>
    • GitHub Source Code: <a href="https://github.com/debugonaut/javascript-assignment.git" target="_blank">https://github.com/debugonaut/javascript-assignment.git</a>
  </div>

  <div class="section-title">1. Objective and Student Profile</div>
  <p>
    The objective of this assignment is to design, develop, and deliver a clean, production-ready personal portfolio webpage for <strong>Aadesh Khande</strong>, a Third-Year Computer Science undergraduate and full stack developer. Built strictly with <strong>pure HTML5 and vanilla CSS3</strong>, the portfolio demonstrates proficiency in responsive web design, semantic HTML markup, accessible interactive navigation, and minimalist visual aesthetics without reliance on external CSS or JavaScript libraries.
  </p>

  <div class="section-title">2. Architectural Design &amp; Visual Design System</div>
  <p>
    The design language balances minimalist editorial typography with modern software showcase aesthetics:
  </p>
  <ul>
    <li><strong>Zero Runtime Dependencies:</strong> Pure HTML5 markup and vanilla CSS3 styling with no third-party UI frameworks.</li>
    <li><strong>Design System Tokens (<code>:root</code>):</strong> Standardized color palette including subtle backgrounds (<code>#ffffff</code>, <code>#fbfbfa</code>), soft green CTA accents (<code>#ebf2eb</code>), sunny yellow avatar badge (<code>#fed347</code>), and crisp charcoal typography.</li>
    <li><strong>Developer Portrait &amp; Resume CTAs:</strong> The developer portrait (<code>image.png</code>) is centered inside a yellow circle, accompanied by dual actions: "Contact Me" and "View / Download Resume" linking directly to <code>resume_2-2.pdf</code>.</li>
    <li><strong>Smooth Anchor Navigation:</strong> Implements CSS <code>scroll-behavior: smooth</code> linking the top navigation bar seamlessly to the About, Projects, Skills, and Contact sections.</li>
    <li><strong>Zero Emojis:</strong> Pure typographic minimalism using clean geometric icons and SVG vectors.</li>
  </ul>

  <div class="screenshot-card">
    <img src="{img1_hero}" class="screenshot-img" style="max-height: 185pt; object-fit: contain;" alt="Desktop Hero Section Overview">
    <div class="screenshot-caption">Figure 1: Desktop Hero Section Overview — Top Navigation, Introduction Heading, TY CS Undergrad Bio, Resume CTA, and Circular Avatar Badge (image.png)</div>
  </div>

  <!-- ========================================================================
       PAGE 2: PROJECTS SHOWCASE & CORE TECHNOLOGIES
       ======================================================================== -->
  <div class="page-break"></div>

  <div class="section-title">3. Projects Showcase Section (Some of my work)</div>
  <p>
    The Projects section highlights three authentic production systems built by Aadesh Khande, using real landing page and console screenshots as thumbnails. Each card features dedicated <strong>Vercel Live Deployment</strong> and <strong>GitHub Source Code</strong> action links:
  </p>
  <ul>
    <li>
      <strong>1. Video Playback Tracker:</strong> Cross-browser extension (Chrome &amp; Firefox) and web platform that automatically tracks and preserves video playback timestamps across all streaming sites.
      <br>• Vercel Live: <a href="https://rewind-player.vercel.app" target="_blank">https://rewind-player.vercel.app</a>
      <br>• GitHub: <a href="https://github.com/debugonaut/video-playback-tracker.git" target="_blank">https://github.com/debugonaut/video-playback-tracker.git</a>
    </li>
    <li>
      <strong>2. Groomly:</strong> Pet grooming marketplace and salon management platform connecting pet owners with verified local salons, smart booking, and analytics.
      <br>• Vercel Live: <a href="https://groomly-ruddy.vercel.app" target="_blank">https://groomly-ruddy.vercel.app</a>
      <br>• GitHub: <a href="https://github.com/debugonaut/Groomly.git" target="_blank">https://github.com/debugonaut/Groomly.git</a>
    </li>
    <li>
      <strong>3. Thermalwatch AI:</strong> Context-aware satellite thermal intelligence system detecting, categorizing, and monitoring industrial thermal anomalies and wildfires across India.
      <br>• Live Deployment: <a href="https://sih26ekaant.web.app" target="_blank">https://sih26ekaant.web.app</a>
      <br>• GitHub: <a href="https://github.com/debugonaut/ThermalWatch-AI.git" target="_blank">https://github.com/debugonaut/ThermalWatch-AI.git</a>
    </li>
  </ul>

  <div class="screenshot-card">
    <img src="{img2_proj}" class="screenshot-img" style="max-height: 195pt; object-fit: contain;" alt="Projects Showcase 3-Card Grid">
    <div class="screenshot-caption">Figure 2: Projects Showcase Section — Video Playback Tracker, Groomly, and Thermalwatch AI with Landing Page Hero Thumbnails &amp; Dual Vercel/GitHub Action Buttons</div>
  </div>

  <div class="section-title">4. Core Technologies Section (Technologies I work with)</div>
  <p>
    The Skills section focuses on core tools and technologies across modern full stack development. It is styled with 7 rounded cards featuring crisp, scalable SVG icons, subtle borders, and smooth hover elevation states:
  </p>
  <ul>
    <li><strong>HTML &amp; CSS:</strong> Semantic HTML5 structure, Flexbox, CSS Grid layouts, custom variables, and responsive media queries.</li>
    <li><strong>JavaScript &amp; React:</strong> ES6+ syntax, async logic, component architecture, state management, and modern client UI flows.</li>
    <li><strong>Node.js, Git &amp; Figma:</strong> Server-side JavaScript APIs, distributed version control, and design system wireframing.</li>
  </ul>

  <div class="screenshot-card">
    <img src="{img3_tech}" class="screenshot-img" style="max-height: 110pt; object-fit: contain;" alt="Technologies I work with 7 Icon Cards">
    <div class="screenshot-caption">Figure 3: Technologies Section — Eyebrow (SKILLS), Heading (Technologies I work with), and 7 Official SVG Tech Cards (HTML, CSS, JS, React, Node.js, Git, Figma)</div>
  </div>

  <!-- ========================================================================
       PAGE 3: CONTACT SECTION, SOCIAL FOOTER & RESPONSIVE VERIFICATION
       ======================================================================== -->
  <div class="page-break"></div>

  <div class="section-title">5. Contact Section &amp; Social Footer</div>
  <p>
    The Contact section is engineered with a modern two-column layout: editorial copy on the left inviting collaboration, and a responsive form on the right directing inquiries directly to <code>contact@aadeshkhande.com</code>. The section terminates in a clean footer featuring copyright metadata and vector social icons:
  </p>
  <ul>
    <li><strong>Form Elements:</strong> Responsive two-column input row for Name and Email, full-width Message textarea, and a high-contrast dark submit button.</li>
    <li><strong>Social Links:</strong> Direct links with SVG icons for GitHub (<code>https://github.com/debugonaut</code>), LinkedIn (<code>aadeshkhande</code>), and direct email to <code>contact@aadeshkhande.com</code>.</li>
  </ul>

  <div class="screenshot-card">
    <img src="{img4_contact}" class="screenshot-img" style="max-height: 155pt; object-fit: contain;" alt="Contact Form and Social Footer">
    <div class="screenshot-caption">Figure 4: Modern Contact Section &amp; Footer — Section Eyebrow (CONTACT), Form Layout, and Social Links (GitHub, LinkedIn, Email)</div>
  </div>

  <div class="section-title">6. Multi-Device Responsive Verification (Mobile &amp; Tablet)</div>
  <p>
    The portfolio adapts seamlessly across mobile, tablet, and desktop viewports using CSS media queries (<code>@media (max-width: 880px)</code> and <code>@media (max-width: 640px)</code>). On mobile screens, the hero rearranges into a centered flow with the circular portrait at top, project cards stack vertically, input fields collapse into single columns, and all touch targets adhere to accessibility standards (&gt;44px):
  </p>

  <div class="two-col-grid">
    <div class="col-img-card">
      <img src="{img5_mobile}" alt="Mobile iPhone Viewport Screenshot">
      <div class="screenshot-caption">Figure 5: Mobile Viewport (iPhone 390x844)<br>Stacked Centered Layout &amp; Responsive Nav</div>
    </div>
    <div class="col-img-card">
      <img src="{img6_tablet}" alt="Tablet iPad Viewport Screenshot">
      <div class="screenshot-caption">Figure 6: Tablet Viewport (iPad 768x1024)<br>Fluid Responsive Two-Column Layout</div>
    </div>
  </div>

  <!-- ========================================================================
       PAGE 4: TECHNICAL ACCOMPLISHMENTS, CODE HIGHLIGHTS & FINAL LINKS
       ======================================================================== -->
  <div class="page-break"></div>

  <div class="section-title">7. Key Implementation Code Highlights</div>
  <p>
    The codebase showcases clean semantic structure, custom CSS variables, and modular card styling:
  </p>

  <div class="code-box">
/* Project Card Action Links &amp; Responsive Grid */
.projects-cards-row {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}}
.card-links-row {{
  display: flex;
  align-items: center;
  gap: 0.55rem;
  margin-top: auto;
  padding-top: 0.75rem;
  border-top: 1px solid #f0f0ee;
  flex-wrap: wrap;
}}
.card-link-live {{
  background: #edf7ed;
  color: #1f5127;
  border: 1px solid #cbe5cc;
}}
.card-link-github {{
  background: #f5f5f4;
  color: #333333;
  border: 1px solid #e5e5e3;
}}
@media (max-width: 880px) {{
  .projects-cards-row {{ grid-template-columns: repeat(2, 1fr); }}
}}
@media (max-width: 640px) {{
  .projects-cards-row {{ grid-template-columns: 1fr; }}
}}
  </div>

  <div class="section-title">8. Summary of Technical Accomplishments &amp; Conclusion</div>
  <ul>
    <li><strong>100% Pure HTML5 &amp; CSS3:</strong> Built entirely without client-side JavaScript libraries, CSS frameworks, or runtime builders, achieving instantaneous load times and zero layout shifts.</li>
    <li><strong>Real Portfolio Projects:</strong> Showcases Video Playback Tracker, Groomly, and Thermalwatch AI with authentic landing page thumbnails and active Vercel / GitHub links.</li>
    <li><strong>Production-Grade Polish:</strong> Personalized directly for Aadesh Khande (TY CS Undergrad), with resume access (<code>resume_2-2.pdf</code>) and direct email integration (<code>contact@aadeshkhande.com</code>).</li>
    <li><strong>Full Device Responsiveness:</strong> Rigorously verified across desktop (1280px), tablet (768px), and mobile (390px) viewports with zero layout bugs.</li>
  </ul>

  <!-- FINAL LINKS CARD (AT THE LAST, AS SPECIFIED BY USER) -->
  <div class="final-links-card">
    <div class="final-links-title">
      Portfolio &amp; Featured Projects Deployment Links
    </div>
    <ul class="final-links-list">
      <li>
        <strong>Main Portfolio URL:</strong> 
        <a href="https://javascript-assignment-sable-one.vercel.app/" target="_blank">https://javascript-assignment-sable-one.vercel.app/</a>
      </li>
      <li>
        <strong>Main Portfolio GitHub:</strong> 
        <a href="https://github.com/debugonaut/javascript-assignment.git" target="_blank">https://github.com/debugonaut/javascript-assignment.git</a>
      </li>
      <li>
        <strong>Video Playback Tracker:</strong>
        Vercel: <a href="https://rewind-player.vercel.app" target="_blank">https://rewind-player.vercel.app</a> | 
        GitHub: <a href="https://github.com/debugonaut/video-playback-tracker.git" target="_blank">https://github.com/debugonaut/video-playback-tracker.git</a>
      </li>
      <li>
        <strong>Groomly:</strong>
        Vercel: <a href="https://groomly-ruddy.vercel.app" target="_blank">https://groomly-ruddy.vercel.app</a> | 
        GitHub: <a href="https://github.com/debugonaut/Groomly.git" target="_blank">https://github.com/debugonaut/Groomly.git</a>
      </li>
      <li>
        <strong>Thermalwatch AI:</strong>
        Live Demo: <a href="https://sih26ekaant.web.app" target="_blank">https://sih26ekaant.web.app</a> | 
        GitHub: <a href="https://github.com/debugonaut/ThermalWatch-AI.git" target="_blank">https://github.com/debugonaut/ThermalWatch-AI.git</a>
      </li>
      <li>
        <strong>Contact Email Address:</strong> 
        <a href="mailto:contact@aadeshkhande.com">contact@aadeshkhande.com</a>
      </li>
    </ul>
  </div>

</body>
</html>
"""

output_pdf_path = os.path.join(current_dir, "Aadesh_Khande_Portfolio_FSD.pdf")
print("Compiling PDF with WeasyPrint...")
weasyprint.HTML(string=html_content).write_pdf(output_pdf_path)
print(f"Generated PDF: {output_pdf_path} ({os.path.getsize(output_pdf_path)} bytes)")

# Also copy to parent Aadesh folder and root Portfolio_FSD for ease of access
parent_pdf = os.path.join(current_dir, "..", "202401100090_WT_Portfolio_FSD.pdf")
root_pdf = "/Users/aadeshkhande/Documents/Professional/College/WEB Tech/Portfolio_FSD/Aadesh_Khande_Portfolio_FSD.pdf"

with open(output_pdf_path, "rb") as src:
    pdf_bytes = src.read()
    with open(parent_pdf, "wb") as dst1:
        dst1.write(pdf_bytes)
    with open(root_pdf, "wb") as dst2:
        dst2.write(pdf_bytes)

print("PDF copied to parent and root Portfolio_FSD successfully!")
