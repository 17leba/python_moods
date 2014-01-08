import os
import jinja2
import web
from jinja2 import Environment, PackageLoader

a = web.config.get('_session')
print web.config