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
data = [["Jan", 10], ["Feb", 22], ["Mar", 30]]

ar = area.T(x_coord = category_coord.T(data, 0), y_range = (0, None),
            x_axis = axis.X(label="Month"),
            y_axis = axis.Y(label="Value"))
ar.add_plot(bar_plot.T(data = data, label = "Something"))
ar.draw()
