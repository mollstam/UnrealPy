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

def draw_rect(color):
    global x, y
    name = pychart.doc_support.stringify_value(color)
    name = re.sub("color\\.", "", name)
    name = pychart.doc_support.break_string(name)
    fill = fill_style.Plain(bgcolor = color)
    can.rectangle(line_style.default, fill, x, y, x+15, y+15)
    height = font.text_height(name)[0] + 5
    tb = text_box.T(text="/hL" + name, loc=(x, y-height), line_style=None)
    x = x + 50
    tb.draw()

for style in color.standards.list():
    if (not theme.use_color and style.r == style.g and style.g == style.b) or \
       theme.use_color:
        draw_rect(style)
        if x >= chartdemo.MaxWidth:
            x=100
            y=y-60

