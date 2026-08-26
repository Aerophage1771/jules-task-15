import os

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GermaineTutoring — Metropolitan Riviera Mockup</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Inter:wght@300..700&display=swap" rel="stylesheet">
<style>
:root {{
  /* Metropolitan Riviera Colors - Production Translation */
  --gt-navy: #081117;
  --gt-marine: #101E26;
  --gt-porcelain: #F5F6F4;
  --gt-mist: #AEB7B6;
  --gt-slate: #597078;
  --gt-oxblood: #632C36;
  --gt-white: #FFFFFF;
  --gt-black: #000000;

  /* Typography */
  --didone: 'Playfair Display', Didot, 'Bodoni MT', serif;
  --grotesque: 'Inter', system-ui, -apple-system, sans-serif;
}}

/* Base Resets */
*, *::before, *::after {{ box-sizing: border-box; }}
body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; background: var(--gt-navy); color: var(--gt-porcelain); font-family: var(--grotesque); -webkit-font-smoothing: antialiased; }}

/* Stage Visibility */
.stage {{ display: none; width: 100%; min-height: 100vh; }}
.stage.active {{ display: block; }}

/* Global Mockup Navigation */
.mockup-nav {{
  position: sticky; top: 0; z-index: 100;
  display: flex; justify-content: center;
  background: color-mix(in srgb, var(--gt-navy) 90%, transparent);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--gt-marine);
}}
.mockup-nav button {{
  appearance: none; border: none; background: transparent; color: var(--gt-mist);
  padding: 16px 24px; font-family: var(--grotesque); font-size: 13px; font-weight: 600;
  letter-spacing: 0.1em; text-transform: uppercase; cursor: pointer;
  transition: all 0.2s ease; border-bottom: 2px solid transparent;
}}
.mockup-nav button:hover {{ color: var(--gt-porcelain); }}
.mockup-nav button.active {{ color: var(--gt-porcelain); border-bottom-color: var(--gt-oxblood); }}

/* Editorial Elements */
h1, h2, h3, .hero-title {{ font-family: var(--didone); font-weight: 400; margin: 0; }}
.hero-title {{ font-size: clamp(48px, 8vw, 104px); line-height: 1.05; letter-spacing: 0.04em; text-transform: uppercase; }}
.hero-kicker {{ font-family: var(--grotesque); font-size: 14px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--gt-mist); font-weight: 500; margin-bottom: 12px; }}
.body-copy {{ font-size: clamp(16px, 1.2vw, 19px); line-height: 1.6; color: var(--gt-mist); max-width: 65ch; }}

/* Global Layout Containers */
.container {{ width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 24px; }}
.section-pad {{ padding: 80px 0; }}
.dark-section {{ background: var(--gt-navy); color: var(--gt-porcelain); }}
.marine-section {{ background: var(--gt-marine); color: var(--gt-porcelain); }}
.light-section {{ background: var(--gt-porcelain); color: var(--gt-navy); }}

/* Buttons & CTAs */
.btn-primary {{
  display: inline-flex; align-items: center; justify-content: center;
  padding: 14px 28px; background: var(--gt-porcelain); color: var(--gt-navy);
  font-family: var(--grotesque); font-weight: 600; font-size: 14px; letter-spacing: 0.08em;
  text-transform: uppercase; text-decoration: none; border-radius: 2px;
  transition: background 0.2s; cursor: pointer; border: none;
}}
.btn-primary:hover {{ background: var(--gt-mist); }}
.btn-outline {{
  display: inline-flex; align-items: center; justify-content: center;
  padding: 14px 28px; background: transparent; color: var(--gt-porcelain);
  border: 1px solid var(--gt-mist);
  font-family: var(--grotesque); font-weight: 600; font-size: 14px; letter-spacing: 0.08em;
  text-transform: uppercase; text-decoration: none; border-radius: 2px;
  transition: all 0.2s; cursor: pointer;
}}
.btn-outline:hover {{ background: var(--gt-marine); border-color: var(--gt-porcelain); }}
.btn-outline.dark {{ color: var(--gt-navy); border-color: var(--gt-slate); }}
.btn-outline.dark:hover {{ background: var(--gt-navy); color: var(--gt-porcelain); }}

{MARKETING_STYLES}
{COURSE_STYLES}
{BLOG_STYLES}

</style>
</head>
<body>

<nav class="mockup-nav" aria-label="Mockup Navigation">
  <button data-target="marketing" class="active">Marketing</button>
  <button data-target="course">Course Portal</button>
  <button data-target="blog">Blog</button>
</nav>

<div id="marketing" class="stage active">
  {MARKETING_HTML}
</div>

<div id="course" class="stage">
  {COURSE_HTML}
</div>

<div id="blog" class="stage">
  {BLOG_HTML}
</div>

<script>
  document.querySelectorAll('.mockup-nav button').forEach(btn => {{
    btn.addEventListener('click', () => {{
      document.querySelectorAll('.mockup-nav button').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.stage').forEach(s => s.classList.remove('active'));

      btn.classList.add('active');
      document.getElementById(btn.getAttribute('data-target')).classList.add('active');
      window.scrollTo(0,0);
    }});
  }});
</script>
</body>
</html>
"""

def generate():
    marketing_styles = ""
    course_styles = ""
    blog_styles = ""

    marketing_html = ""
    course_html = ""
    blog_html = ""

    # Read parts if they exist
    if os.path.exists('marketing.html'):
        with open('marketing.html', 'r') as f:
            marketing_html = f.read()
    if os.path.exists('course.html'):
        with open('course.html', 'r') as f:
            course_html = f.read()
    if os.path.exists('blog.html'):
        with open('blog.html', 'r') as f:
            blog_html = f.read()

    if os.path.exists('marketing.css'):
        with open('marketing.css', 'r') as f:
            marketing_styles = f.read()
    if os.path.exists('course.css'):
        with open('course.css', 'r') as f:
            course_styles = f.read()
    if os.path.exists('blog.css'):
        with open('blog.css', 'r') as f:
            blog_styles = f.read()

    final_html = HTML_TEMPLATE.format(
        MARKETING_STYLES=marketing_styles,
        COURSE_STYLES=course_styles,
        BLOG_STYLES=blog_styles,
        MARKETING_HTML=marketing_html,
        COURSE_HTML=course_html,
        BLOG_HTML=blog_html
    )

    with open('index.html', 'w') as f:
        f.write(final_html)

if __name__ == '__main__':
    generate()
