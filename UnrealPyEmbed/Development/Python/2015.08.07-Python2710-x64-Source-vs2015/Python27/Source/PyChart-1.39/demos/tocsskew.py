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
import tocslib
ymin=0

width=tocslib.width
height=tocslib.height

def CreateSkewGraph(data, ymax, interval):
    return area.T(x_coord=category_coord.T(data, 0),
                  size=(width, height),
                  x_axis = axis.X(label="/bSkew"),
                  y_axis = axis.Y(label="", tic_interval=interval,
                                  label_offset=(-40,None)),
                  y_range=(ymin, ymax),
                  legend=None)

data = chart_data.read_str(" ",
    "0 689.2780916 791.9442379 778.0596226 693.2 734.99 766.8875721 753.09 289.93",
    "0.25 690.984838 801.0757878 812.0217771 705.3 383.4590857 418.7825131 463.6420009 148.26",
    "0.5 683.2219825 769.5098419 784.2037828 710.23 190.9876947 217.3046324 274.7908102 75.13",
    "1 694.9 780.03 780.02 716 26.37 49.13 89.86 12.03784649")

def create_line_plot(label, data, col):
    return line_plot.T(label=label, data=data, ycol=col,
                      tick_mark=tocslib.get_tick_mark(label),
                      line_style=tocslib.get_line_style(label))

ar = CreateSkewGraph(data, 1000, 200)
ar.y_axis.label = "/bMessages//second"
ar.legend = legend.T(loc=(50+width*2, 0), shadow=(2,-2,fill_style.gray50))
ar.add_plot(create_line_plot("D4", data, 3),
            create_line_plot("D2", data, 2),
            create_line_plot("D1", data, 1),
            create_line_plot("R", data, 4),
            create_line_plot("S4", data, 7),
            create_line_plot("S2", data, 6),
            create_line_plot("S1", data, 5),
            create_line_plot("SM", data, 8))
ar.draw()
tocslib.label(ar, "(a)").draw()

data = chart_data.read_str(" ",
                    "0 327.88 362.53 373.34 325.0067623 322.89 360.4 363.23",
                    "0.25 330.2 355.671277 353.1399808 315.9811765 165.0281937 177.9464914 192.3867494",
                    "0.5 325.8804905 345.7156968 351.6724777 318.34 78.83 109.29 138.27",
                    "1 323.0343 352.83 353.31 323.93 20.37 48.334 77.45")

ar = CreateSkewGraph(data, 400, 100)
ar.loc = tocslib.loc2
ar.add_plot(create_line_plot("D4", data, 3),
            create_line_plot("D2", data, 2),
            create_line_plot("D1", data, 1),
            create_line_plot("R", data, 4),
            create_line_plot("S4", data, 7),
            create_line_plot("S2", data, 6),
            create_line_plot("S1", data, 5))

ar.draw()
tocslib.label(ar, "(b)").draw()
