from jinja2 import Environment, FileSystemLoader

import args

fileLoader = FileSystemLoader("templates")
env_jinja2 = Environment(loader=fileLoader)

temp_jinja2 = env_jinja2.get_template("index.html")
# temp_jinja2.globals.update(args.math_functions)
rend_jinja2 = temp_jinja2.render(args.args_jinja2)

index_html = "index.html"
with open(f"./{index_html}", "w") as index_file:
    index_file.write(rend_jinja2)