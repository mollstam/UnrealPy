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
import tocslib

size=120

can = canvas.default_canvas()

arrow.T(line_style=line_style.T(width=1)).draw([(0,0),(0,size)])
arrow.T(line_style=line_style.T(width=1)).draw([(0,0),(size,0)])
font.defaultSize=10
font.defaultLineHeight=8
can.show(-5,60,"/hC/a90/oManageability")
can.show(10,-3, "/hL/vT/oPerformance&availability\n/o//cost")

def circle(x,y,str):
    can.ellipsis(line_style.default, fill_style.black, x, y, 2)
    can.show(x+5,y, "/T/vM" + str)

circle(size*0.2,size*0.8,"/l8Monolithic\n/l8Server")
circle(size*0.4,size*0.6,"/l8Cluster-based\n/l8operating system")
circle(size*0.6,size*0.4,"/l8Distributed\n/l8file system")
circle(size*0.8,size*0.2,"/l8Static\n/l8partitioning")
circle(size*0.8,size*0.8,"Porcupine");

