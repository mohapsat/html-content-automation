import os, sys
import subprocess
import jinja2
import time
from jinja2 import FileSystemLoader, Environment

templateLoader = FileSystemLoader("Templates")
templateEnv = Environment( loader = templateLoader)
TEMPLATE_FILE = "templ_page.jinja"
template = templateEnv.get_template( TEMPLATE_FILE )

templateVars = { "TXT_OBJ" : "A",
                 "IMG_OBJ" : "https://tse4.mm.bing.net/th?id=OIP.M2kQRwBlS5e9RT3e9fRVpgEiEs&pid=15.1" ,
                 "IMG_QR"  : "https://tse4.mm.bing.net/th?id=OIP.m-DfytVQR34XIAjUSRfuJQEsEs&pid=15.1"
                 }

outputText = template.render( templateVars )

rendered_filename = 'outFile.html'

f = open(rendered_filename,'w')
f.write(outputText)
f.close()