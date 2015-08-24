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
theme.get_options()

data = [(10, 20, 30), (20, 65, 33),
	(30, 55, 30), (40, 45, 51),
	(50, 25, 27), (60, 75, 30)]

ar = area.T(size = (150,120),
            y_grid_interval=10,
            x_axis=axis.X(label="X label", label_offset=(0,-7)),
            y_axis=axis.Y(label="Y label"),
            legend = legend.T(), y_range = (0, None))

ar.add_plot(bar_plot.T(label="foo", data=data),
            line_plot.T(label="bar", data=data, ycol=2))
ar.draw()
