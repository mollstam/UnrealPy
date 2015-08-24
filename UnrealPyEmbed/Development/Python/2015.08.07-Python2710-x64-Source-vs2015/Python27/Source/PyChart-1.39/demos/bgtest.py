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
data = [(10, 20, 5, 5), (20, 65, 5, 5),
        (30, 55, 4, 4), (40, 45, 2, 2), (50, 25, 3, 3)]

ar = area.T(x_axis = axis.X(label = "X label"),
            y_axis = axis.Y(label = "Y label"))
ar.add_plot(bar_plot.T(label="foo", data = data,
                       fill_style = fill_style.gray90,
                       error_bar = error_bar.bar3,
                       error_minus_col = 2,
                       error_plus_col = 3))
canvas.default_canvas().set_background(fill_style.diag, -100, -100, 300, 300)
ar.draw()

