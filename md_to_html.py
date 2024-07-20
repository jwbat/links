import os
import markdown2


markdown_files = ['index.md', 'notes.md']


for md_file in markdown_files:
    html_file = md_file.replace('.md', '.html')

    with open(md_file, 'r') as f:
        markdown_content = f.read()


    markdown_content = markdown_content.replace('{{ site.baseurl }}', '.')
    html_content = markdown2.markdown(markdown_content)

    with open(html_file, 'w') as f:
        f.write(html_content)
