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
import sys

data = [("foo", 10),("bar", 20), ("baz", 30), ("ao", 40)]

ar = area.T(size=(150,150), legend=legend.T(),
            x_grid_style = None, y_grid_style = None)

plot = pie_plot.T(data=data, arc_offsets=[0,10,0,10],
                  shadow = (2, -2, fill_style.gray50),
                  label_offset = 25,
                  arrow_style = arrow.a3)
ar.add_plot(plot)
ar.draw()


