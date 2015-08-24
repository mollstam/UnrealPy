from pychart import *
import pychart.doc_support
import optik
import string
import sys
import re

parser = optik.OptionParser()
parser.add_option("-S", "--ps", action="store_true", default=None)
parser.add_option("-D", "--pdf", action="store_true", default=None)
parser.add_option("-X", "--pychart-dir", action="store", default=None)
opt, argv = parser.parse_args(sys.argv[1:])

ftype = "png"
pychart_dir = ".."

if opt.ps:
    ftype="pdf"
elif opt.pdf:
    ftype="eps"
if opt.pychart_dir:
    pychart_dir = opt.pychart_dir

def resubfunc(mo):
    typename = re.sub("_", "-", mo.group(1))
    return "\\xref{module-%s}" % typename

def xxx(mo):
    xx = "var"
    return "\\" + xx + "{" + mo.group(1) + "}"

def format_doc_string(str):
    str = re.sub("<<([^>]+)>>", resubfunc, str)
    str = re.sub("<([^>]+)>", xxx, str)
    str = re.sub("\|([^|]+)\|", "\\code{\\1}", str)
    str = str.replace("#", "\\#")
    str = str.replace("%", "\\%")
    str = str.replace("@pxref", "\\pxref")
    str = str.replace("@xref", "\\xref")
    str = str.replace("@code", "\\code")
    str = str.replace("@samp", "\\code")
    str = str.replace("@var", "\\var")
    str = str.replace("@example", "\\begin{verbatim}")
    str = str.replace("@end example", "\\end{verbatim}")
    str = re.sub("@cindex ([^\n]+)", "\\index{\\1}", str)
    return str

def outputClassAttrs(moduleName, className):
    x = pychart.doc_support.modules[moduleName]
    v = x[className]
    keys = v.keys.keys()
    keys.sort()
    for key in keys:
        if key[0] == '_':
            continue
        val = v.keys[key]

        type_str = pychart.doc_support.stringify_type(val[0])

        print "\\begin{memberdesc}{%s}\n\\textbf{Type:} %s" % (key, type_str)
        if False:
            print "\\label{%s.%s.%s}" % (moduleName.replace("_","-"),
                                         className.replace("_","-"),
                                         key.replace("_", "-"))
	mm = re.match("(.*)\\.T$", str(type_str))
	if mm:
	    print "(\\pxref{module-%s})" % re.sub("_", "-", mm.group(1))

        if len(val) > 3:
            print "\\textbf{Default:} %s." % format_doc_string(val[3]),
        else:
            print "\\textbf{Default:} %s." % format_doc_string(str(pychart.doc_support.stringify_value(val[1]))),

        print ""
        print ""

        if len(val) > 2:
            print format_doc_string(val[2])

	print "\\end{memberdesc}"
    #print "@end multitable";

def copy_file(src, dest):
    sys.stderr.write("%s->%s\n" % (src, dest))
    infp = open(src, "rb")
    outfp = open(dest, "wb")
    outfp.writelines(infp.readlines())
    infp.close()
    outfp.close()

nodeNames = []
nodeReplaces = []
demoDir = pychart_dir + "/demos/"

def scan_nodes(fp):
    global nodeNames
    for line in fp.readlines():
        mo_node = re.match("^@node ([^,]*)", line)
        if mo_node:
            nodeNames.append(re.compile("\\b(" + mo_node.group(1) + ")\\b"))

def include_text_file(file):
    fp = open(file, "r")
    print "\\noindent\\bfcode{%s}\n\n" % file
    print "\\begin{verbatim}"

    line = fp.readline()
    if line.startswith('#'):
        # Skip the first comment block. It's usually a copyright statement.
        while True:
            line = fp.readline()
            assert line
            if not line.startswith('#'):
                break
    print line,
    for line in fp.readlines():
        line = string.expandtabs(line)
        print line,
    fp.close()
    print "\\end{verbatim}"

def format_doc(str):
    out = ""
    empty_line_found = False
    in_example = None

    for line in string.split(str, "\n"):
        if empty_line_found and len(line) > 0 and line[0] != ' ':
            if not in_example:
                out = out + "\\begin{verbatim}\n"
                in_example = True
            out = out + line + "\n"
        else:
            if line == "":
                empty_line_found = True

            if in_example:
                out = out + line + "\n\\end{verbatim}\n"
            else:
                # Do some formatting.
                line = format_doc_string(line)
                out = out + line + "\n"
            in_example = None
    if in_example:
        out = out + "\n\end{verbatim}\n"
    return out

fp = open(argv[0], "r")

scan_nodes(fp)

fp.seek(0)

while True:
    line = fp.readline()
    if line == "": break

    mo7 = re.match("@xximage\\{(.*),\\}", line)

    line = line.replace("@chart{}", "PyChart")
    line = line.replace("@shadow", "Parameter \\var{shadow} is either None or tuple (\\var{xdelta, ydelta, shadowstyle}). If non-None, a shadow of \\var{shadowstyle} (\\pxref{module-fill-style}) is drawn beneath the polygon at the offset (\\var{xdelta, ydelta}).")

    mo = re.match("^%%([^.]+)\\.(.*)", line)
    if mo:
        outputClassAttrs(mo.group(1), mo.group(2))
        continue

    mo = re.match("^@samplechartandcode\{([^,]*),(.*)\}", line)

    if mo:
        basename = mo.group(1)
        description = mo.group(2)
        for ext in ["png", "eps", "pdf"]:
            copy_file("%s%s-c.%s" % (demoDir, basename, ext),
                      "%s.%s" % (basename, ext))

        print "\\includegraphics{%s}\n" % (basename)
        print description, "\n"
        print "Below is the source code that produces the above chart."
        include_text_file(demoDir + basename + ".py")
        continue

    mo = re.match("^@samplecode\{(.*)\}", line)
    if mo:
        basename = mo.group(1)
        include_text_file(demoDir + basename + ".py")
        continue

    mo = re.match("^@samplechart\{(.*)\}", line)
    if mo:
        basename = mo.group(1)
        for ext in ["png", "eps", "pdf"]:
            copy_file("%s%s-c.%s" % (demoDir, basename, ext),
                      "%s.%s" % (basename, ext))
        print "\\includegraphics{%s}\n" % (basename)
        continue

    mo = re.match("^@pydescribe\{(.*)\}", line)
    if mo:
        obj_name = mo.group(1)
        obj = eval(obj_name)
        print format_doc(str(obj.__doc__)), "\n"
        continue

    print line,
