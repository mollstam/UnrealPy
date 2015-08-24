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

data = [(10, 20, 3.0), (20, 65, 2.5),
        (30, 55, 5.0), (40, 45, 3.0), (50, 25, 2.0)]

ar = area.T(x_axis=axis.X(label="X", format="/a-30{}%d", tic_interval=20),
            y_axis = axis.Y())
ar.add_plot(bar_plot.T(data=data,
                       line_style=None, fill_style = fill_style.gray50,
                       error_bar = error_bar.bar2, error_minus_col=2))
ar.draw()
