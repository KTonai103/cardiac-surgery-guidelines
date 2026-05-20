#!/usr/bin/env python3
"""Convert Obsidian-flavored Markdown to styled HTML for cardiac surgery guideline comparison documents.

Handles: YAML frontmatter, callouts, highlights (==text==), wikilinks ([[link|display]]).
Uses pandoc for core Markdown→HTML conversion, then wraps with custom CSS template.
"""

import re
import subprocess
import sys
import os

# Callout type → (CSS border-color, CSS bg-color, icon label)
CALLOUT_STYLES = {
    "note":      ("#448aff", "#e8f0fe", "Note"),
    "info":      ("#448aff", "#e8f0fe", "Info"),
    "tip":       ("#00bfa5", "#e0f7f4", "Tip"),
    "success":   ("#00c853", "#e8f5e9", ""),
    "warning":   ("#ff9100", "#fff3e0", ""),
    "danger":    ("#ff5252", "#ffebee", ""),
    "important": ("#ff5252", "#ffebee", ""),
    "abstract":  ("#00b0ff", "#e1f5fe", ""),
    "question":  ("#64dd17", "#f1f8e9", "?"),
    "example":   ("#7c4dff", "#ede7f6", ""),
    "quote":     ("#9e9e9e", "#f5f5f5", ""),
    "bug":       ("#ff1744", "#fce4ec", "Bug"),
    "failure":   ("#ff5252", "#ffebee", ""),
    "todo":      ("#448aff", "#e8f0fe", "TODO"),
}

def strip_frontmatter(text):
    """Remove YAML frontmatter and extract title."""
    title = ""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[3:end]
            for line in fm.split("\n"):
                if line.startswith("title:"):
                    title = line[6:].strip().strip('"').strip("'")
            text = text[end+4:].lstrip("\n")
    return text, title

def convert_wikilinks(text):
    """Convert [[link|display]] to display text, [[link]] to link text."""
    text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', text)
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    return text

def convert_highlights(text):
    """Convert ==highlighted text== to <mark> tags."""
    return re.sub(r'==(.*?)==', r'<mark>\1</mark>', text)

def convert_callouts(text):
    """Convert Obsidian callout blocks to HTML divs."""
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        # Match callout start: > [!type] Optional title
        m = re.match(r'^> \[!(\w+)\]\s*(.*)$', lines[i])
        if m:
            ctype = m.group(1).lower()
            title_text = m.group(2).strip()
            style = CALLOUT_STYLES.get(ctype, CALLOUT_STYLES["note"])
            border_color, bg_color, default_label = style

            # Collect callout body
            body_lines = []
            # If title line has content after the type, it could be the title or single-line callout
            if title_text:
                # Check if next line is also a callout continuation
                if i + 1 < len(lines) and lines[i+1].startswith('> '):
                    # Title is on first line, body follows
                    pass
                else:
                    # Single-line callout: title IS the body
                    body_lines.append(title_text)
                    title_text = ""

            i += 1
            while i < len(lines) and lines[i].startswith('> '):
                body_lines.append(lines[i][2:])  # strip '> '
                i += 1

            # If no explicit title but had title_text as actual title
            display_title = title_text if title_text else default_label
            # If single-line callout with no body, title_text was moved to body
            if not body_lines and title_text:
                body_lines.append(title_text)
                display_title = default_label

            body_md = '\n'.join(body_lines)

            # Convert body markdown to HTML via pandoc
            body_html = pandoc_convert(body_md)

            title_html = f'<div class="callout-title" style="color:{border_color};font-weight:700;margin-bottom:4px;font-size:0.85rem;">{display_title}</div>' if display_title else ''
            callout_html = f'<div class="callout" style="background:{bg_color};border-left:4px solid {border_color};padding:12px 16px;margin:12px 0 20px;border-radius:4px;font-size:0.85rem;line-height:1.6;">{title_html}{body_html}</div>'
            result.append(callout_html)
        else:
            result.append(lines[i])
            i += 1

    return '\n'.join(result)

def pandoc_convert(md_text):
    """Convert markdown text to HTML body using pandoc."""
    try:
        proc = subprocess.run(
            ['pandoc', '-f', 'gfm', '-t', 'html5', '--wrap=none'],
            input=md_text, capture_output=True, text=True, check=True
        )
        return proc.stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"pandoc error: {e}", file=sys.stderr)
        return md_text

CSS_TEMPLATE = """
:root {
  --bg: #ffffff;
  --fg: #1a1a1a;
  --muted: #5c5c5c;
  --border: #d4d4d4;
  --accent: #2c3e50;
  --light-bg: #f7f8fa;
  --header-bg: #2c3e50;
  --header-fg: #ffffff;
  --link: #34495e;
  --jp-accent: #c0392b;
  --us-accent: #2980b9;
  --eu-accent: #27ae60;
  --sidebar-w: 280px;
  --sidebar-bg: #f4f6fa;
  --sidebar-hover: #e4eaf2;
  --sidebar-active: #d8e1ec;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

html { scroll-behavior: smooth; }

/* Responsive vector graphics — SVG must scale without bitmapping on mobile */
img, svg.flowchart {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1.5em auto;
}
svg.flowchart {
  width: 100%;
  max-width: 1100px;
}
figure.flowchart {
  margin: 1.5em -16px;
  padding: 0;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
figure.flowchart svg {
  min-width: 320px;
}

body {
  font-family: "Noto Sans JP", "Helvetica Neue", Arial, sans-serif;
  font-size: 14px;
  line-height: 1.7;
  color: var(--fg);
  background: var(--bg);
}

.layout {
  display: flex;
  align-items: flex-start;
}

main.content {
  flex: 1 1 auto;
  min-width: 0;
  max-width: 1100px;
  margin: 0 auto;
  padding: 40px 40px 80px;
}

/* Anchor offset so fixed headers don't hide target heading */
h1[id], h2[id], h3[id], h4[id] { scroll-margin-top: 16px; }

h1 {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.02em;
  border-bottom: 3px solid var(--accent);
  padding-bottom: 16px;
  margin-bottom: 24px;
}

h2 {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--accent);
  border-left: 4px solid var(--accent);
  padding-left: 12px;
  margin: 48px 0 12px;
}

h3 {
  font-size: 0.98rem;
  font-weight: 600;
  color: var(--fg);
  margin: 28px 0 8px;
}

h4 {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--muted);
  margin: 20px 0 6px;
}

p { margin: 8px 0; font-size: 0.88rem; }
strong { color: var(--fg); }

a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; }

hr {
  border: none;
  border-top: 1px solid var(--border);
  margin: 32px 0;
}

ul, ol {
  padding-left: 24px;
  margin: 8px 0;
  font-size: 0.88rem;
}

li { margin-bottom: 4px; }

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
  margin: 12px 0 20px;
  border: 1px solid var(--border);
  border-radius: 4px;
  overflow: hidden;
}

thead th {
  background: var(--header-bg);
  color: var(--header-fg);
  font-weight: 600;
  padding: 10px 12px;
  text-align: left;
  font-size: 0.8rem;
  letter-spacing: 0.02em;
}

tbody td {
  padding: 8px 12px;
  border-bottom: 1px solid #e8e8e8;
  vertical-align: top;
}

tbody td:first-child {
  font-weight: 600;
  color: var(--accent);
  background: var(--light-bg);
}

tbody tr:nth-child(even) td { background-color: #fafbfc; }
tbody tr:nth-child(even) td:first-child { background-color: #f0f1f3; }
tbody tr:hover td { background-color: #eef1f5; }
tbody tr:hover td:first-child { background-color: #e4e8ed; }

/* Blockquotes (fallback for any not converted to callouts) */
blockquote {
  background: var(--light-bg);
  border-left: 3px solid var(--border);
  padding: 10px 16px;
  margin: 12px 0 20px;
  font-size: 0.85rem;
  color: var(--muted);
  line-height: 1.6;
}

blockquote strong { color: var(--fg); }

/* Highlights */
mark {
  background: #fff3cd;
  padding: 1px 4px;
  border-radius: 2px;
  font-weight: 600;
}

/* Callout overrides - already inline styled, but ensure nested elements look right */
.callout p { margin: 4px 0; }
.callout ul, .callout ol { margin: 4px 0 4px 16px; }
.callout table { font-size: 0.8rem; }

/* Print */
@media print {
  body { max-width: 100%; padding: 20px; }
  table { font-size: 0.7rem; }
  h2 { break-after: avoid; }
}

/* ===== Sidebar (TOC) ===== */
.sidebar {
  position: sticky;
  top: 0;
  flex: 0 0 var(--sidebar-w);
  width: var(--sidebar-w);
  height: 100vh;
  overflow-y: auto;
  background: var(--sidebar-bg);
  border-right: 1px solid var(--border);
  padding: 20px 14px 32px;
  font-size: 0.82rem;
  z-index: 100;
}

.sidebar-header {
  margin-bottom: 14px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--border);
}

.sidebar .back-link {
  display: inline-block;
  font-size: 0.74rem;
  color: var(--muted);
  margin-bottom: 6px;
  letter-spacing: 0.02em;
}
.sidebar .back-link:hover { color: var(--accent); }

.sidebar-title {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border: none;
  margin: 0;
  padding: 0;
}

.toc {
  list-style: none;
  padding: 0;
  margin: 0;
}

.toc li { margin: 0; padding: 0; }

.toc a {
  display: block;
  padding: 5px 10px 5px 12px;
  color: var(--fg);
  border-left: 2px solid transparent;
  line-height: 1.4;
  transition: background 0.15s ease, border-color 0.15s ease, color 0.15s ease;
  text-decoration: none;
  word-break: break-word;
}

.toc a:hover {
  background: var(--sidebar-hover);
  text-decoration: none;
}

.toc a.active {
  border-left-color: var(--accent);
  background: var(--sidebar-active);
  color: var(--accent);
  font-weight: 700;
}

.toc-l2 a { font-weight: 600; font-size: 0.83rem; }
.toc-l3 a { padding-left: 26px; font-size: 0.78rem; color: #444; }
.toc-l4 a { padding-left: 40px; font-size: 0.74rem; color: var(--muted); }

/* Mobile toggle button */
.sidebar-toggle {
  display: none;
  position: fixed;
  top: 10px;
  left: 10px;
  z-index: 200;
  background: var(--accent);
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 1.1rem;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(0,0,0,0.25);
}

.sidebar-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.35);
  z-index: 99;
}

/* Print */
@media print {
  .sidebar, .sidebar-toggle, .sidebar-backdrop { display: none !important; }
  main.content { max-width: 100%; padding: 20px; }
  table { font-size: 0.7rem; }
  h2 { break-after: avoid; }
}

@media (max-width: 1024px) {
  .sidebar {
    position: fixed;
    top: 0; left: 0;
    height: 100vh;
    transform: translateX(-100%);
    transition: transform 0.22s ease;
    box-shadow: 2px 0 14px rgba(0,0,0,0.18);
  }
  .sidebar.open { transform: translateX(0); }
  .sidebar.open ~ .sidebar-backdrop { display: block; }
  main.content { padding: 56px 24px 60px; }
  .sidebar-toggle { display: block; }
}

@media (max-width: 768px) {
  main.content { padding: 56px 16px 60px; font-size: 13px; }
  h1 { font-size: 1.3rem; }
  table { font-size: 0.75rem; }
}
"""

def _slugify(text):
    """Generate URL-safe slug from heading text (Japanese-friendly)."""
    text = re.sub(r'<[^>]+>', '', text)
    text = text.strip()
    text = re.sub(r'[\s　]+', '-', text)
    # Keep word chars (\w covers Unicode letters/digits in Py3), Japanese ranges, hyphens
    text = re.sub(
        r'[^\w぀-ゟ゠-ヿ㐀-䶿一-鿿０-９Ａ-ｚ-]',
        '',
        text
    )
    text = re.sub(r'-+', '-', text).strip('-')
    return text or 'section'

def add_heading_ids_and_extract_toc(body_html):
    """Add id attributes to h1-h4 and return TOC list of (level, slug, text)."""
    toc = []
    used = {}

    def assign(text):
        base = _slugify(text)
        slug = base
        n = used.get(base, 0)
        if n:
            slug = f'{base}-{n}'
        used[base] = n + 1
        # If by chance the new slug collides with a previously used base, bump again
        while slug in used and slug != base:
            n += 1
            slug = f'{base}-{n}'
            used[base] = n + 1
        used.setdefault(slug, 1)
        return slug

    def repl(m):
        level = int(m.group(1))
        attrs = m.group(2) or ''
        content = m.group(3)
        text = re.sub(r'<[^>]+>', '', content).strip()
        # Skip empty headings
        if not text:
            return m.group(0)
        # If id already present, reuse it
        id_match = re.search(r'\bid\s*=\s*"([^"]+)"', attrs)
        if id_match:
            slug = id_match.group(1)
        else:
            slug = assign(text)
            attrs = f'{attrs} id="{slug}"'
        toc.append((level, slug, text))
        return f'<h{level}{attrs}>{content}</h{level}>'

    body_html = re.sub(
        r'<h([1-4])([^>]*)>(.*?)</h\1>',
        repl,
        body_html,
        flags=re.DOTALL
    )
    return body_html, toc

def build_sidebar(toc, back_href='../index.html', back_label='← ガイドラインポータル'):
    """Build sidebar HTML from TOC (skip h1 since it's the page title)."""
    items = []
    for level, slug, text in toc:
        if level < 2:
            continue
        # Escape minimal HTML in heading text (text has tags stripped already)
        safe = (text.replace('&', '&amp;')
                    .replace('<', '&lt;')
                    .replace('>', '&gt;'))
        items.append(f'<li class="toc-l{level}"><a href="#{slug}">{safe}</a></li>')

    toc_html = '\n      '.join(items) if items else '<li><em style="color:var(--muted);font-size:0.78rem;">(目次なし)</em></li>'
    return (
        '<aside class="sidebar" id="sidebar" aria-label="目次">\n'
        '  <div class="sidebar-header">\n'
        f'    <a class="back-link" href="{back_href}">{back_label}</a>\n'
        '    <div class="sidebar-title">目次</div>\n'
        '  </div>\n'
        '  <ul class="toc">\n'
        f'      {toc_html}\n'
        '  </ul>\n'
        '</aside>\n'
        '<div class="sidebar-backdrop" id="sidebar-backdrop"></div>\n'
        '<button class="sidebar-toggle" id="sidebar-toggle" aria-label="目次の表示切替" aria-controls="sidebar">☰ 目次</button>\n'
    )

SIDEBAR_JS = """
(function () {
  var sidebar = document.getElementById('sidebar');
  var toggle = document.getElementById('sidebar-toggle');
  var backdrop = document.getElementById('sidebar-backdrop');
  if (!sidebar) return;

  function close() { sidebar.classList.remove('open'); }
  function open() { sidebar.classList.add('open'); }
  if (toggle) {
    toggle.addEventListener('click', function () {
      sidebar.classList.toggle('open');
    });
  }
  if (backdrop) backdrop.addEventListener('click', close);

  // Close sidebar after clicking a link on narrow screens
  sidebar.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function () {
      if (window.matchMedia('(max-width: 1024px)').matches) close();
    });
  });

  // Active-link tracking via IntersectionObserver
  var linkMap = new Map();
  sidebar.querySelectorAll('a[href^="#"]').forEach(function (a) {
    var id = decodeURIComponent(a.getAttribute('href').slice(1));
    linkMap.set(id, a);
  });

  var headings = Array.prototype.slice.call(
    document.querySelectorAll('main.content h2[id], main.content h3[id], main.content h4[id]')
  );
  if (!headings.length || !linkMap.size || !('IntersectionObserver' in window)) return;

  var visible = new Set();
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) visible.add(e.target.id);
      else visible.delete(e.target.id);
    });
    // Pick the first visible heading in document order
    var activeId = null;
    for (var i = 0; i < headings.length; i++) {
      if (visible.has(headings[i].id)) { activeId = headings[i].id; break; }
    }
    // Fallback: heading nearest above current scroll
    if (!activeId) {
      var y = window.scrollY + 100;
      for (var j = headings.length - 1; j >= 0; j--) {
        if (headings[j].getBoundingClientRect().top + window.scrollY <= y) {
          activeId = headings[j].id;
          break;
        }
      }
    }
    linkMap.forEach(function (a) { a.classList.remove('active'); });
    if (activeId && linkMap.has(activeId)) {
      var link = linkMap.get(activeId);
      link.classList.add('active');
      // Keep the active item visible inside the sidebar
      var sRect = sidebar.getBoundingClientRect();
      var lRect = link.getBoundingClientRect();
      if (lRect.top < sRect.top + 40 || lRect.bottom > sRect.bottom - 40) {
        link.scrollIntoView({ block: 'nearest' });
      }
    }
  }, { rootMargin: '-15% 0px -70% 0px', threshold: 0 });
  headings.forEach(function (h) { observer.observe(h); });
})();
"""

def inline_svg_images(html, md_dir):
    """Replace <img src=".../*.svg" alt="..."> tags with the SVG file contents inline.

    Inline SVG renders as native vector on all devices including iPhone Safari,
    preventing the bitmap-rasterization that can occur when SVG is served via <img>.
    """
    def repl(m):
        src = m.group('src')
        alt = m.group('alt') or ''
        # Resolve relative path
        svg_path = src if os.path.isabs(src) else os.path.join(md_dir, src)
        if not os.path.exists(svg_path):
            return m.group(0)
        try:
            with open(svg_path, 'r', encoding='utf-8') as f:
                svg = f.read()
        except Exception:
            return m.group(0)
        # Strip XML declaration if present
        svg = re.sub(r'<\?xml[^?]+\?>\s*', '', svg)
        # Ensure svg tag has class for CSS targeting; strip explicit width/height to let viewBox + CSS scale
        svg = re.sub(r'<svg\b([^>]*)\bwidth="[^"]*"', r'<svg\1', svg, count=1)
        svg = re.sub(r'<svg\b([^>]*)\bheight="[^"]*"', r'<svg\1', svg, count=1)
        if 'class=' in svg[:200]:
            svg = re.sub(r'<svg\b([^>]*class=")([^"]*)"', r'<svg\1\2 flowchart"', svg, count=1)
        else:
            svg = re.sub(r'<svg\b', '<svg class="flowchart" role="img" aria-label="' + alt.replace('"', '&quot;') + '"', svg, count=1)
        return f'<figure class="flowchart">\n{svg}\n</figure>'

    # Match <img src="...svg" alt="..."> in any attribute order
    pattern = re.compile(
        r'<img\s+(?:[^>]*?\s)?src="(?P<src>[^"]+\.svg)"(?:\s+[^>]*?alt="(?P<alt>[^"]*)")?[^>]*/?>',
        re.IGNORECASE
    )
    # Also handle alt-before-src
    html = pattern.sub(repl, html)

    pattern2 = re.compile(
        r'<img\s+alt="(?P<alt>[^"]*)"\s+src="(?P<src>[^"]+\.svg)"[^>]*/?>',
        re.IGNORECASE
    )
    html = pattern2.sub(repl, html)
    return html


def convert_file(md_path, html_path):
    """Convert a single Obsidian MD file to styled HTML."""
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Step 1: Strip frontmatter
    text, title = strip_frontmatter(text)

    # Step 2: Convert wikilinks before other processing
    text = convert_wikilinks(text)

    # Step 3: Convert highlights (before callout processing since callouts use pandoc)
    text = convert_highlights(text)

    # Step 4: Convert callouts to HTML divs (this also internally uses pandoc)
    text = convert_callouts(text)

    # Step 5: Convert remaining markdown to HTML
    # The text now has a mix of markdown and HTML div callouts
    # We need to convert the markdown parts while preserving the HTML divs
    # Split by callout divs, convert markdown parts, rejoin
    parts = re.split(r'(<div class="callout".*?</div>\n?)', text, flags=re.DOTALL)
    converted_parts = []
    for part in parts:
        if part.startswith('<div class="callout"'):
            converted_parts.append(part)
        else:
            converted_parts.append(pandoc_convert(part))
    body_html = '\n'.join(converted_parts)

    # Step 5b: Inline SVG flowcharts for crisp vector rendering on mobile
    body_html = inline_svg_images(body_html, os.path.dirname(os.path.abspath(md_path)))

    # Step 6: Add IDs to all h1–h4 and extract TOC for sidebar
    body_html, toc = add_heading_ids_and_extract_toc(body_html)

    # Extract title from first h1 if not from frontmatter
    if not title:
        m = re.search(r'<h1[^>]*>(.*?)</h1>', body_html)
        if m:
            title = re.sub(r'<[^>]+>', '', m.group(1))

    # Determine relative back link to portal index.html
    base_dir = os.path.dirname(os.path.abspath(__file__))
    rel_dir = os.path.relpath(os.path.dirname(os.path.abspath(html_path)), base_dir)
    if rel_dir in ('', '.'):
        back_href = 'index.html'
    else:
        depth = len([p for p in rel_dir.split(os.sep) if p and p != '.'])
        back_href = ('../' * depth) + 'index.html'

    sidebar_html = build_sidebar(toc, back_href=back_href)

    # Build full HTML
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{CSS_TEMPLATE}</style>
</head>
<body>
<div class="layout">
{sidebar_html}
<main class="content">
{body_html}
</main>
</div>
<script>{SIDEBAR_JS}</script>
</body>
</html>
"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  {os.path.basename(html_path)} ({os.path.getsize(html_path):,} bytes)")

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    files = [
        ("AS_AVR_TAVI/AS_AVR_Guidelines_Comparison.md",
         "AS_AVR_TAVI/AS_AVR_Guidelines_Comparison.html"),
        ("AF_Surgery/AF_Surgery_Indications_Guideline_Comparison.md",
         "AF_Surgery/AF_Surgery_Indications_Guideline_Comparison.html"),
        ("MS_MV_Surgery/MS_MV_Surgery_Guidelines_Comparison.md",
         "MS_MV_Surgery/MS_MV_Surgery_Guidelines_Comparison.html"),
        ("Ascending Aorta/Ascending_Aorta_Surgery_Indications_Guideline_Comparison.md",
         "Ascending Aorta/Ascending_Aorta_Surgery_Indications_Guideline_Comparison.html"),
        ("Combined_VHD/Combined_VHD_Guidelines_Comparison.md",
         "Combined_VHD/Combined_VHD_Guidelines_Comparison.html"),
        ("LVAD/LVAD_Guidelines_Comparison.md",
         "LVAD/LVAD_Guidelines_Comparison.html"),
        ("Cardiomyopathy/Cardiomyopathy_Guidelines_Comparison.md",
         "Cardiomyopathy/Cardiomyopathy_Guidelines_Comparison.html"),
        ("AR_AVR/AR_Guidelines_Comparison.md",
         "AR_AVR/AR_Guidelines_Comparison.html"),
        ("Ross_Procedure/Ross_Procedure_Guidelines_Comparison.md",
         "Ross_Procedure/Ross_Procedure_Guidelines_Comparison.html"),
        ("MR_MV/MR_Guidelines_Comparison.md",
         "MR_MV/MR_Guidelines_Comparison.html"),
        ("Perioperative_Anticoagulation/Perioperative_Anticoagulation_Guidelines_Comparison.md",
         "Perioperative_Anticoagulation/Perioperative_Anticoagulation_Guidelines_Comparison.html"),
        ("Perioperative_Anticoagulation/Mechanical_Valve_Anticoagulation_INR_Targets.md",
         "Perioperative_Anticoagulation/Mechanical_Valve_Anticoagulation_INR_Targets.html"),
        ("MS_MV_Surgery/Atrial_MR_Definition_Summary.md",
         "MS_MV_Surgery/Atrial_MR_Definition_Summary.html"),
        ("Infective_Endocarditis/IE_Surgery_Guidelines_Comparison.md",
         "Infective_Endocarditis/IE_Surgery_Guidelines_Comparison.html"),
        ("TR_TV_Surgery/TR_TV_Surgery_Guidelines_Comparison.md",
         "TR_TV_Surgery/TR_TV_Surgery_Guidelines_Comparison.html"),
        ("Heart_Transplant/Heart_Transplant_Guidelines_Comparison.md",
         "Heart_Transplant/Heart_Transplant_Guidelines_Comparison.html"),
        ("Heart_Transplant/HighRisk_Pericardial_Redo_HTx_Analysis.md",
         "Heart_Transplant/HighRisk_Pericardial_Redo_HTx_Analysis.html"),
        ("CABG_Coronary_Revascularization/CABG_Coronary_Revascularization_Guidelines_Comparison.md",
         "CABG_Coronary_Revascularization/CABG_Coronary_Revascularization_Guidelines_Comparison.html"),
        ("Temporary_MCS/Temporary_MCS_Guidelines_Comparison.md",
         "Temporary_MCS/Temporary_MCS_Guidelines_Comparison.html"),
        ("HF_Management/HF_Management_Guidelines_Comparison.md",
         "HF_Management/HF_Management_Guidelines_Comparison.html"),
        ("CP_Pericardiectomy/CP_Pericardiectomy_Guidelines_Comparison.md",
         "CP_Pericardiectomy/CP_Pericardiectomy_Guidelines_Comparison.html"),
        ("CVCU_Emergency_Response/CVCU_Emergency_Response_Protocol.md",
         "CVCU_Emergency_Response/CVCU_Emergency_Response_Protocol.html"),
        ("CPB_Management/CPB_Management_Guidelines_Comparison.md",
         "CPB_Management/CPB_Management_Guidelines_Comparison.html"),
        ("CTEPH_PEA_Acute_PE_Surgery/CTEPH_PEA_Acute_PE_Surgery_Guidelines_Comparison.md",
         "CTEPH_PEA_Acute_PE_Surgery/CTEPH_PEA_Acute_PE_Surgery_Guidelines_Comparison.html"),
    ]

    print("Converting Obsidian MD → styled HTML:")
    for md_rel, html_rel in files:
        md_path = os.path.join(base, md_rel)
        html_path = os.path.join(base, html_rel)
        if os.path.exists(md_path):
            convert_file(md_path, html_path)
        else:
            print(f"  SKIP: {md_rel} not found")

    print("Done.")

if __name__ == "__main__":
    main()
