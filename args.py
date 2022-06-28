
import datetime
import yaml

with open("./cv.yaml","r") as yaml_file:
    cv = yaml.safe_load(yaml_file)
    #print(cv)

args_jinja2 = {
    "page_title" : "Yasser Saied CV",
    "datetime" : datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p"),
    "cv" : cv,
}