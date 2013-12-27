import os
import jinja2
from jinja2 import Environment, PackageLoader

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader('%s/templates/' % os.path.dirname(__file__))
)
template = env.get_template('index.html')
print template.render(the='variables',go='here')