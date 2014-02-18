#!/usr/bin/env python3

import os.path
import importlib

import yaml
import jinja2
import humanize

def normpath(p):
    return os.path.join(os.path.dirname(__file__), p)

config_path = normpath("config.yaml")
config = yaml.safe_load(open(config_path))

ret = {}
for name, keys in config.items():
    m = importlib.import_module("modules.%s" % name)
    ret[name] = m.MAIN(**keys)

env = jinja2.Environment(loader=jinja2.FileSystemLoader(normpath("templates")),
                         extensions=['jinja2.ext.do']) 
template = env.get_template("default.html")
print(template.render(d=ret, humanize=humanize)) 
