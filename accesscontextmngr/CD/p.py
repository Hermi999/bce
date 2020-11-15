#!/usr/bin/env python

import yaml
from os import listdir, makedirs
from os.path import isfile, join, exists

# optional args
desc = ""
cF = ""

# create new folder for rendered yaml files
newpath = './rendered'
if not exists(newpath): 
    makedirs(newpath)

# get all files in folder
path = "."
files = [f for f in listdir(path) if isfile(join(path, f))]

# only iterate through yaml files
for f in files:
    if "yaml" == f.split(".")[-1]:
        print(f)

        with open(f, 'r') as yaml_file:
            try:
                data = yaml.safe_load(yaml_file)
                for item, doc in data.items():
                    if item == "name":
                        # print("name:", doc)
                        name = doc
                        filename = newpath + "/" + name.split("/")[3] + ".yaml"
                        # print("fn:", filename)
                    if item == "description":
                        # print("description:", doc)
                        desc = "--description='" + doc + "'"
                    if item == "title":
                        # print("title:", doc)
                        title = doc
                    if item == "basic":
                        for k, v in doc.items():
                            if k == "combiningFunction":
                                # print("cF:", v)
                                cF = "--combine-function=" + v
                            if k == "conditions":
                                # print("conditions:", v)
                                cond = v
                    if item == "advanced":
                        print("not implemented yet")

                # create new file
                with open(filename, "w", encoding="utf8") as outfile:
                    yaml.dump(cond, outfile, default_flow_style=False, allow_unicode=True)    

                # return gcloud commands
                print(f"gcloud access-context-manager levels $ACTION {name} --basic-level-spec={filename} {cF} --title={title} {desc}")

            except yaml.YAMLError as exc:
               print(exc)
