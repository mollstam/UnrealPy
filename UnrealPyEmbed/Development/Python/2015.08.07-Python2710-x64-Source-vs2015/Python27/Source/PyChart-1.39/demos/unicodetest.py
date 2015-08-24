# -*- coding: utf-8 -*-
#
# Copyright (C) 2005 by Yasushi Saito (yasushi.saito@gmail.com)
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
can = canvas.default_canvas()
x, y = (100, 500)
def show_text(str):
    global x, y
    can.show(x, y, str)
    can.show(x + 200, y, "/12/C" + font.quotemeta(str))
    y -= 20

show_text(unicode('Zürich', 'utf-8'))
show_text(unicode('X äöü Y', 'utf-8'))

