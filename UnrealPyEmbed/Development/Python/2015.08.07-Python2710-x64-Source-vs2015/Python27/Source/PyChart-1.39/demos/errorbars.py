#
# Copyright (C) 2000-2005 by Yasushi Saito (yasushi.saito@gmail.com)
# 
# Pychart is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2, or (at your option) any
# later version.
#
# Pychart is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
from pychart import *
import pychart.doc_support
import re

can = canvas.default_canvas()

x = 100
y = 500

ar = area.T()

q=30
m=60

def draw_error_bar(e):
    global x, y
    name = pychart.doc_support.stringify_value(e)
    name = re.sub("error_bar\\.", "", name)
    tb = text_box.T(text="/hC" + name, loc=(x, y-m-20), line_style=None)
    tb.draw()
    e.draw(can, (x, y), y-m, y+m, y-q, y+q)
    x = x + 50

xmin = x

for e in error_bar.standards.list():
    draw_error_bar(e)

xmax = x

can.line(line_style.gray70_dash1, xmin-20, y, xmax, y)

can.line(line_style.gray70_dash1, xmin-20, y-q, xmax, y-q)
can.line(line_style.gray70_dash1, xmin-20, y+q, xmax, y+q)
tb = text_box.T(text="quartile", loc=(xmax+40, y), line_style=None)
tb.add_arrow(tipLoc=(xmax+55, y+q)) #, tail='tc')
tb.add_arrow(tipLoc=(xmax+55, y-q)) #, tail='bc')
tb.draw()

tb = text_box.T(text="min//\nmax", loc=(xmax+80, y), line_style=None)
tb.add_arrow(tipLoc=(xmax+95, y+m)) #, tail='tc')
tb.add_arrow(tipLoc=(xmax+95, y-m)) #, tail='bc')
tb.draw()

