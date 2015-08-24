import sys
sys.path.append("..")
sys.path.append("../demos")

import pychart.doc_support
from pychart import *
import list_sources
import re
import dircache
import os
import posixpath

target_dir="examples"
cwd = os.getcwd()

python_path = "python"
if sys.platform == "win32":
    python_path = "c:/Python22/python"

try:
    os.mkdir(target_dir)
except:
    pass

index_fp = open(target_dir + "/index.html", "w")
    
index_fp.write("<head><title>pychart Samples</title></head>\n<body>\n")

for file in list_sources.list_sources("../demos"):
    mo = re.match("^(.*).py$", file)
    assert mo
    basename = mo.group(1)
    pngFile = "%s/%s/%s.png" % (cwd, target_dir, basename)
    smallPngFile = "%s/%s/%s-small.png" % (cwd, target_dir, basename)
    src_file = "%s/%s/%s" % (cwd, target_dir, file)
    os.environ["PYTHONPATH"] = "..:" + os.environ.get("PYTHONPATH", "")
    if not os.access(pngFile, os.R_OK):
        print "Creating ", pngFile
        os.environ["PYCHART_OPTIONS"] = "color=yes scale=3 output=%s" % pngFile
        os.chdir("../demos")
        os.system(python_path + " " + file)
        os.chdir(cwd)

    if not os.access(smallPngFile, os.R_OK):
        print "Creating ", smallPngFile
        os.environ["PYCHART_OPTIONS"] = "color=yes scale=0.6 output=%s" % smallPngFile
        os.chdir("../demos")
        os.system(python_path + " " + file)
        os.chdir(cwd)

    if not os.access(src_file, os.R_OK):
        os.system("cp ../demos/%s %s" % (file, src_file))

    index_fp.write("<p><a href=\"%s.png\"><img src=\"%s-small.png\"></a>\n" % (basename, basename))
    index_fp.write("<p><a href=\"" + basename + ".py\">Source code</a>")

index_fp.write("</body>\n")
index_fp.close()

    

