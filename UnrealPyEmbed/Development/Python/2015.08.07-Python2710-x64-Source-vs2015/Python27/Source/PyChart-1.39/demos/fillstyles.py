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

x = 100
y = 500

can = canvas.default_canvas()

def drawRect(fill):
    global x, y
    name = pychart.doc_support.stringify_value(style)
    #print "name=", name
    name = re.sub("fill_style\\.", "", name)
    name = pychart.doc_support.break_string(name)
    height = font.text_height(name)[0] + 5

    can.rectangle(line_style.default, fill, x, y, x+15, y+15)
    tb = text_box.T(text=name, loc=(x, y-height), line_style=None,
                    fill_style = None)
    x = x + 50
    tb.draw()

for style in fill_style.standards.list():
    drawRect(style)
    if x >= chartdemo.MaxWidth:
        x=100
        y=y-40
