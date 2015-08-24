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
can = canvas.default_canvas()
x, y = (100, 500)

def show_text(str):
    global x, y
    can.show(x, y, str)
    can.show(x + 200, y, "/12/C" + font.quotemeta(str))
    y -= 20

show_text("/12/hLLeft align")
show_text("/12/hRRight align")
show_text("/12/hCCenter align")
show_text("/a20/12/hRAngled text")

def show_textv(str):
    global x, y
    can.show(x, y, str)
    x += 150

y -= 40
x = 100
show_textv("/12/vT//12//vTTop align")
show_textv("/12/vM//12//vT/12Middle align")
show_textv("/12/vB//12//vT/12Bottom align")

y -= 40
x = 100
show_text("/16/HHelvetica")
show_text("/12/CCourier")
show_text("/12/NHelvetica-Narrow")
show_text("/12/PPalatino-Roman")
show_text("/12/AAvantgarde")
show_text("/12/T/iTimes-Italic")
show_text("/12/F{ZapfDingbats}ZapfDingbats")

