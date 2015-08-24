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
import random
from pychart import *

random.seed(0)
data1 = []
data2 = []
x1 = 0
x2 = 0
for i in range(0, 100, 5):
    x1 += random.randrange(0,3)
    x2 += random.randrange(0,3)
    data1.append([i, x1])
    data2.append([i, x2])

ar = area.T(size = (150, 120),
            x_axis = axis.X(format="%d"),
            y_axis = axis.Y(offset = 0, format="%d"),
            y_axis2 = axis.Y(offset = 150, format="%d", draw_tics_right = 1))

ar.add_plot(line_plot.T(data = data2))
ar.add_plot(bar_plot.T(data = data1))
ar.draw()

