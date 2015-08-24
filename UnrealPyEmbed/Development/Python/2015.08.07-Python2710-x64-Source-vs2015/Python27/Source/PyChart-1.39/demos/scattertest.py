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
import random
random.seed(0)

def randomdata():
    data = []
    for i in range(0, 30):
        data.append((random.random() * 1000, random.random() * 1000))
    return data

theme.get_options()
chart_object.set_defaults(line_plot.T, line_style=None)

tick1 = tick_mark.Circle(size=2)
tick2 = tick_mark.Circle(size=2, fill_style=fill_style.black)
xaxis = axis.X(label="foo", format="/a-60{}%d")
yaxis = axis.Y(label="bar")

ar = area.T(x_axis=xaxis, y_axis=yaxis,
            x_grid_interval=100, x_grid_style=line_style.gray70_dash3,
            legend = legend.T(loc=(350, 50)), loc = (0, 0))

ar.add_plot(line_plot.T(label="plot1", data=randomdata(), tick_mark=tick1))
ar.add_plot(line_plot.T(label="plot2", data=randomdata(), tick_mark=tick2))
ar.draw()

xaxis = axis.X(label="foo", format="/a-30{}%d")
yaxis = axis.Y(label="bar")
ar = area.T(x_axis=xaxis, y_axis=yaxis,
            x_coord=log_coord.T(), y_coord=log_coord.T(), loc = (200, 0),
            legend = None)

ar.add_plot(line_plot.T(label="plot1", data=randomdata(), tick_mark=tick1))
ar.add_plot(line_plot.T(label="plot2", data=randomdata(), tick_mark=tick2))
ar.draw()
