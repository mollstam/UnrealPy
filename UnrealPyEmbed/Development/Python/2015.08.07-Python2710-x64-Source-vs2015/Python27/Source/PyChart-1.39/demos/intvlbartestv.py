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

data = [("Foo", (10, 7, 10, 5, 5, 12, 13, 5, 10, 3),
         (7,10,8,16,9,3)),
        ("Bar", (5, 10, 12, 10, 9, 3),
         (10,10,13,6,9,13),)]

ar = area.T(y_coord = category_coord.T(data, 0),
            x_grid_style=line_style.gray50_dash1,
            x_grid_interval=20, x_range = (0,100),
            x_axis=axis.X(label="X label"),
            y_axis=axis.Y(label="Y label"),
            legend = legend.T(loc=(80, 40)))

chart_object.set_defaults(interval_bar_plot.T, direction="horizontal",
                          width=3, cluster_sep = 5, data=data)
ar.add_plot(interval_bar_plot.T(line_styles = [line_style.default, None],
                                fill_styles = [fill_style.red, None],
                                label="foo", cluster=(0,2)),
            interval_bar_plot.T(line_styles = [line_style.default, None],
                                fill_styles = [fill_style.blue, None],
                                label="bar", hcol=2, cluster=(1,2)))

can = canvas.default_canvas()
can.set_title("Interval bar test")
can.set_author("John Doe")
ar.draw()
