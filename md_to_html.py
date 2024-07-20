import markdown2


md_file   = 'index.md'
html_file = 'index.html'

with open(md_file, 'r') as f:
    markdown_content = f.read()

markdown_content = markdown_content.replace('{{ site.baseurl }}', '.')
html_content     = markdown2.markdown(markdown_content)

with open(html_file, 'w') as f:
    f.write(html_content)
