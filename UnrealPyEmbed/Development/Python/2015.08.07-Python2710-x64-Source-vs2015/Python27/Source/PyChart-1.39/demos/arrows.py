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
x = 100
y = 500

def draw(obj):
    global x, y
    name = pychart.doc_support.stringify_value(obj)
    name = re.sub("arrow\\.", "", name)
    obj.draw(((x, y), (x, y+30)))
    tb = text_box.T(text="/hC" + name, loc=(x, y-12), line_style=None)
    tb.draw()
    x = x + 50

for style in arrow.standards.list():
    draw(style)
    
    
