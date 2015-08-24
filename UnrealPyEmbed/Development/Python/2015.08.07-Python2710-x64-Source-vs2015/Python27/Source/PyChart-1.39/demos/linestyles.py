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
import chartdemo
import re

can = canvas.default_canvas()

x = 100
y = 500

def drawLine(style):
    global x, y
    name = pychart.doc_support.stringify_value(style)
    name = re.sub("line_style\\.", "", name)
    name = pychart.doc_support.break_string(name)
    can.line(style, x, y, x+40, y)
    #print "name=", name
    height = font.text_height(name)[0] + 5
    tb = text_box.T(text=name, loc=(x, y-height), line_style=None)
    x = x + 60
    tb.draw()

for style in line_style.standards.list():
    drawLine(style)
    if x >= chartdemo.MaxWidth:
        x=100
        y=y-40
