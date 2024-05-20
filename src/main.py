import os
import shutil
import markdown


from copystatic import copy_files_recursive

# copy staic files
dir_path_static = "./static"
dir_path_public = "./public"
copy_files_recursive(dir_path_static, dir_path_public)

# generate page from markdown
with open("content/index.md", "r") as f:
    md_content = f.read()

# converting the above markdown content into html content
html_content = markdown.markdown(md_content)

with open('template.html') as f:
    template = f.read()

page_content = template.replace('{{content}}', html_content)

with open('public/index.html', 'w') as f:
    f.write(page_content)






def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    

main()
