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

data = [(10, 20, 30, 5), (20, 65, 33, 5), (30, 55, 30, 5), (40, 45, 51, 7),
	(50, 25, 27, 3), (60, 75, 30, 5), (70, 80, 42, 5), (80, 62, 32, 5),
	(90, 42, 39, 5), (100, 32, 39, 4)]

# The attribute y_coord_system="category" tells that the Y axis values
# should be taken from samples, y_category_col'th column of
# y_category_data.  Thus, in this example, Y values will be
# [40,50,60,70,80].
ar = area.T(y_coord = category_coord.T(data[3:8], 0),
            x_grid_style=line_style.gray50_dash1,
            x_grid_interval=20,
            x_range = (0,100), 
            x_axis=axis.X(label="X label"),
            y_axis=axis.Y(label="Y label"),
            bg_style = fill_style.gray90,
            border_line_style = line_style.default,
            legend = legend.T(loc=(80,10)))

# Below call sets the default attributes for all bar plots.
chart_object.set_defaults(bar_plot.T, direction="horizontal", data=data)

ar.add_plot(bar_plot.T(label="foo", width=3, cluster_sep=2, cluster=(0,3)))
ar.add_plot(bar_plot.T(label="bar", width=7, cluster_sep=1,
                       hcol=2, cluster=(1,3)))
ar.add_plot(bar_plot.T(label="baz", width=5, hcol=3, cluster=(2,3)))
ar.draw()



