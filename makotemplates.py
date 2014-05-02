"""from mako.template import Template
print Template("hello ${data}!").render(data="world")"""

"""from mako.template import Template

mytemplate = Template("hello ,${name}")
print mytemplate.render(name="Pavan")"""

from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO

mytemplate = Template("hello, ${name}!")
buf = StringIO()
ctx = Context(buf, name="jack")
mytemplate.render_context(ctx)
print buf.getvalue()
