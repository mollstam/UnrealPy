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

data = chart_data.read_csv("lines.csv")

xaxis=axis.X(label="X", tic_interval=10)
yaxis=axis.Y(label="Y", tic_interval=10)
ar = area.T(x_range=(0,100), y_range=(0,100), x_axis=xaxis, y_axis=yaxis)
eb = error_bar.error_bar2(tic_len=5, hline_style=line_style.gray50)
ar.add_plot(line_plot.T(label="foo", data=data, error_bar=eb, y_error_minus_col=3),
            line_plot.T(label="bar", data=data, ycol=2, error_bar=eb, y_error_minus_col=3))
ar.draw()

tb = text_box.T(loc=(40, 130), text="This is\nimportant!", line_style=None)
tb.add_arrow((ar.x_pos(data[6][0]), ar.y_pos(data[6][1])), "cb")
tb.draw()

ar = area.T(loc=(200, 0), x_range=(0,100), y_range=(0,100),
            x_axis=xaxis, y_axis=yaxis, legend=legend.T())
ar.add_plot(line_plot.T(label="foo", data=data, data_label_format="/8{}%d"),
            line_plot.T(label="bar", data=data, ycol=2))
ar.draw()
