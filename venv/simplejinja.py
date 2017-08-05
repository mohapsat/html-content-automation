import os, sys
import subprocess
import jinja2
import time
from jinja2 import FileSystemLoader, Environment

# In this case, we will load templates off the filesystem.
# This means we must construct a FileSystemLoader object.
#
# The search path can be used to make finding templates by
#   relative paths much easier.  In this case, we are using
#   absolute paths and thus set it to the filesystem root.

templateLoader = FileSystemLoader("Templates")

# ref: http://web1-buzz.shutterfly.com/h/sfly/y/2017/P44962_mmb.html


# An environment provides the data necessary to read and
#   parse our templates.  We pass in the loader object here.

templateEnv = Environment( loader = templateLoader)

# This constant string specifies the template file we will use.
TEMPLATE_FILE = "templ_simplejinja.jinja"

# Read the template file using the environment object.
# This also constructs our Template object.
template = templateEnv.get_template( TEMPLATE_FILE )

# Specify any input variables to the template as a dictionary.
templateVars = { "title" : "My Title",
                 "description" : "Returned description." }

# Finally, process the template to produce our final text.
outputText = template.render( templateVars )

# print outputText
# timestamp, int to remove decical, str to allow concat
rendered_filename = 'jinjaOut_' + str(int(time.time())) + '.html'
# print filename

f = open(rendered_filename,'w')
f.write(outputText)
f.close()
