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
import math

def format_x_axis(x):
    return str(int(x*2/math.pi)) + "//2"
ar = area.T(x_axis=axis.X(label="X (unit is Pi)", format=format_x_axis,
                          tic_interval=math.pi/2.0),
            y_axis = axis.Y(label="Y"),
            y_range=(-1,1), x_range=(0, math.pi*4), legend = legend.T())
sindata = chart_data.func(lambda x: math.sin(x), 0, math.pi*4, 0.1)
cosdata = chart_data.func(lambda x: math.cos(x), 0, math.pi*4, 0.1)
sin2data = chart_data.func(lambda x: math.sin(x)/2, 0, math.pi*4, 0.1)
cos2data = chart_data.func(lambda x: math.cos(x)/2, 0, math.pi*4, 0.1)
ar.add_plot(line_plot.T(label="sin(x)", data=sindata),
            line_plot.T(label="sin(x)//2", data=sin2data),
            line_plot.T(label="cos(x)", data=cosdata),
            line_plot.T(label="cos(x)//2", data=cos2data))
ar.draw()

