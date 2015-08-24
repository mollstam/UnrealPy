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
import pychart.line_style

theme.get_options()
chartSize = (180, 110)

can = canvas.default_canvas()

font.defaultSize = 9
chart_object.set_defaults(legend.Entry)
xaxis = axis.X(label="Timeline\n(seconds)", label_offset = (120, 30),
               format="/a-30{}%d", tic_interval = 100)

yaxis = axis.Y(label = "Messages//second")

ar = area.T(size=chartSize, x_axis=xaxis, x_range=(0,800),
            y_grid_interval = 100,
            y_axis=yaxis, y_range=(400,700))
ar.legend = legend.T(loc = (ar.loc[0] + chartSize[0]+30,
                            ar.loc[1] + chartSize[1]/2))

data = chart_data.read_csv("failure.csv")
ar.add_plot(line_plot.T(label="no failure", data=data, ycol=4, line_style=line_style.gray50))
ar.add_plot(line_plot.T(label="one failure", data=data, ycol=1))
ar.add_plot(line_plot.T(label="three failures", data=data, ycol=2, line_style=line_style.black_dash2))

ar.draw()

yloc = ar.loc[1] + ar.size[1] + 50
ytip = ar.loc[1] + ar.size[1]
ybot = ar.loc[1]

def describeEvent(seconds, label, off):
    x1 = ar.x_pos(seconds)
    can.line(line_style.black_dash1, x1, ybot, x1, ytip)
    tb = text_box.T(text=label, loc=(x1+off, yloc), shadow=(2,-2,fill_style.gray70))
    tb.add_arrow((x1, ytip))
    tb.draw()
    
describeEvent(300, "Nodes\nfail", -100)
describeEvent(320, "New membership\ndetermined", -50)
describeEvent(600, "Nodes\nrecover", 0)
describeEvent(620, "New membership\ndetermined", 50)
