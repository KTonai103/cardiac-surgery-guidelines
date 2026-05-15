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
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: "Noto Sans JP", "Helvetica Neue", Arial, sans-serif;
  font-size: 14px;
  line-height: 1.7;
  color: var(--fg);
  background: var(--bg);
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 32px 80px;
}

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

@media (max-width: 768px) {
  body { padding: 20px 16px 60px; font-size: 13px; }
  h1 { font-size: 1.3rem; }
  table { font-size: 0.75rem; }
}
"""

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

    # Extract title from first h1 if not from frontmatter
    if not title:
        m = re.search(r'<h1[^>]*>(.*?)</h1>', body_html)
        if m:
            title = re.sub(r'<[^>]+>', '', m.group(1))

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
{body_html}
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
