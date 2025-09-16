import os

# Nom du fichier à générer
index_file = "index.html"

# Fonction pour générer la liste des fichiers et dossiers
def list_files(startpath='.'):
    html = "<ul>\n"
    for root, dirs, files in os.walk(startpath):
        # Ignorer le fichier index.html lui-même
        if index_file in files:
            files.remove(index_file)
        rel_path = os.path.relpath(root, startpath)
        indent = '  ' * (rel_path.count(os.sep))
        html += f"{indent}<li>{os.path.basename(root)}/\n<ul>\n"
        for f in files:
            html += f"{indent}  <li><a href='{os.path.join(rel_path, f)}'>{f}</a></li>\n"
        html += f"{indent}</ul>\n</li>\n"
    html += "</ul>\n"
    return html

# Génération du contenu HTML
html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Index du dépôt</title>
</head>
<body>
<h1>Index du dépôt</h1>
{list_files()}
</body>
</html>
"""

# Écriture dans index.html
with open(index_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"{index_file} généré avec succès !")
