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

data = [ (0, 10, 30, 40, 60), (10, 20, 40, 50, 55), (20, 10, 35, 38, 43),
         (30, 8, 30, 35, 39), (40, 8, 20, 28, 39) ]

ar = area.T(x_axis = axis.X(label="X axis"),
            y_grid_interval = 10, y_grid_style = line_style.white,
            y_axis = axis.Y(label="Y axis"),
            y_grid_over_plot=1, legend = legend.T())

if theme.use_color:
    colors = [ fill_style.darkseagreen, fill_style.white, fill_style.brown ]
else:
    colors = [ fill_style.gray90, fill_style.white, fill_style.gray50 ]
ar.add_plot(range_plot.T(label="foo", data=data, fill_style = colors[0]))
ar.add_plot(range_plot.T(label="bar", data=data, min_col=2, max_col=3,
                         fill_style = colors[1]))
ar.add_plot(range_plot.T(label="baz", data=data, min_col=3, max_col=4,
                         fill_style = colors[2]))
ar.draw()
