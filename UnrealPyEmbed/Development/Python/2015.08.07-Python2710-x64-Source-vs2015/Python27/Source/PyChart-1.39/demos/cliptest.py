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

data = [(10, 20), (20, 65), (30, 55), (40, 45)]

# tic_angle is the angle X values are displayed below the axis.
xaxis = axis.X(label="Stuff")
yaxis = axis.Y(label="Value")

ar = area.T(x_axis=xaxis, y_axis=yaxis)

plot = line_plot.T(label="foo", data=data, xcol=0, ycol=1,
                   tick_mark=tick_mark.star)

ar.add_plot(plot)
can.ellipsis(line_style.T(width=1.5,dash=(4,4)), None, 30, 20, 80, 0.8)
can.clip_ellipsis(30, 20, 80, 0.8)
ar.draw(can)
can.endclip()


