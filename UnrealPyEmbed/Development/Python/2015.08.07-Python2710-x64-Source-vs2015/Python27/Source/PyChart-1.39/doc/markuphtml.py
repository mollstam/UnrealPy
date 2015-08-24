import re
import sys

pats = (
    ("theme.get_options()", "options"),
    ("area.T", "module-area"), 
    ("interval_bar_plot.T", "module-interval-bar-plot"),
    ("bar_plot.T", "module-bar-plot"),
    ("line_plot.T", "module-line-plot"),
    ("range_plot.T", "module-range-plot"),
    ("pie_plot.T", "module-pie-plot"),
    ("color\\.", "module-color"),
    ("line_style\\.", "module-line-style"),
    ("fill_style\\.", "module-fill-style"),
    ("tick_mark\\.", "module-tick-mark"),
    ("log_coord\\.T", "module-coord"),
    ("linear_coord\\.T", "module-coord"),
    ("category_coord\\.T", "module-coord"),
    ("error_bar\\.", "module-error-bar"),
    ("text_box\\.T", "module-text-box"),
    ("arrow\\.T", "module-arrow"),
    ("axis\\.", "module-axis"),
    ("chart_data\\.", "module-chart-data"),
    ("legend\\.", "module-legend"),
    ("theme\\.", "options"),
    ("canvas\\.", "module-canvas"),
    ("zap\\.", "module-zap"),
    )

re_pats = {}
for pat, repl in pats:
    re_pats[re.compile("(" + pat + ")")] = repl

def hackimgref(mo):
    path = mo.group(1)
    i = path.rfind("/")
    path2 = path[(i+1):]
    print >>sys.stderr, "PATH=", path, path2
    return 'SRC="%s"' % path2
    
in_example = False
for l in sys.stdin.readlines():
    l = re.sub('SRC="(/nfs[^\"]+)"', hackimgref, l)
               
    if re.match(".*<pre[^>]*>", l):
        in_example = True
    elif l.find("</pre>") >= 0:
        in_example = False
        
    if not in_example:
        l = re.sub("<head>", """<head><style type="text/css">\npre {background-color: #e0e0e0}\n</style>\n""", l)
        print l,
        continue

    for str, ref in pats:
        l = re.sub("(" + str + ")", "<a href=\"%s.html\">\\1</a>" % ref, l)
        #l = re.sub(str, "<a href=\"%s.html\">\\1</a>" % ref, l)
    print l,
    
        

        
        
