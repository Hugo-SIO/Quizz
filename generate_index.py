import os

output_file = "index.html"
base_dir = "dossiers"  # dossier que tu veux lister

html_header = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Index des fichiers</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 2em; background: #f9f9f9; }
        h1 { color: #333; }
        ul { list-style-type: none; padding-left: 0; }
        li { margin: 0.5em 0; }
        a { text-decoration: none; color: #007bff; }
        a:hover { text-decoration: underline; }
        .folder { font-weight: bold; }
    </style>
</head>
<body>
<h1>Index des fichiers</h1>
<ul>
"""

html_footer = """
</ul>
</body>
</html>
"""

def generate_index():
    lines = [html_header]
    for root, dirs, files in os.walk(base_dir):
        rel_root = os.path.relpath(root, base_dir)
        if rel_root == ".":
            rel_root = ""
        if dirs:
            for d in dirs:
                path = os.path.join(rel_root, d).replace("\\", "/")
                lines.append(f'<li class="folder"><a href="{base_dir}/{path}/">{d}/</a></li>')
        if files:
            for f in files:
                path = os.path.join(rel_root, f).replace("\\", "/")
                lines.append(f'<li><a href="{base_dir}/{path}">{f}</a></li>')
    lines.append(html_footer)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    generate_index()
