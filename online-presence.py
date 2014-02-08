#!/usr/bin/env python3

import os.path
import importlib

import yaml

import pyjade
import jinja2

def normpath(p):
    return os.path.join(os.path.dirname(__file__), p)

config_path = normpath("config.yaml")
config = yaml.safe_load(open(config_path))

ret = {}
for name, keys in config.items():
    m = importlib.import_module("modules.%s" % name)
    ret[name] = m.MAIN(**keys)

env = jinja2.Environment(loader=jinja2.FileSystemLoader(normpath("templates")),
                         extensions=['pyjade.ext.jinja.PyJadeExtension']) 
template = env.get_template("default.html.jade") 
print(template.render(d=ret)) 
