import os
import markdown2


markdown_files = ['index.md', 'notes.md']


for md_file in markdown_files:
    with open(md_file, 'r') as f:
        markdown_content = f.read()

    html_content = markdown2.markdown(markdown_content)
    # html_content = f'<link rel="stylesheet" type="text/css" href="styles.css">\n{html_content}'

    html_file = md_file.replace('.md', '.html')
    with open(html_file, 'w') as f:
        f.write(html_content)
