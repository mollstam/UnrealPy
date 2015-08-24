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
y = 100

def draw_tick(tick):
    global x, y
    name = pychart.doc_support.stringify_value(tick)
    name = re.sub("tick_mark\\.", "", name)
    name = pychart.doc_support.break_string(name)
    height = font.text_height(name)[0] + 10
    tick.draw(can, x, y+tick.size/2)
    tb = text_box.T(text="/12" + name, loc=(x, y-height), line_style=None)
    x = x + 70
    tb.draw(can)

for tick in tick_mark.standards.list():
    draw_tick(tick)
    if x >= chartdemo.MaxWidth:
        x = 100
        y = y + 45
