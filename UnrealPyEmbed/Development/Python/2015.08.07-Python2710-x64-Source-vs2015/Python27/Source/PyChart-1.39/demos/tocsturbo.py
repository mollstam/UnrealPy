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

def create_line_plot(label, ycol):
    return line_plot.T(label=label,
                      tick_mark=tocslib.get_tick_mark(label),
                      line_style=tocslib.get_line_style(label),
                      data=data, ycol=ycol)

def create_graph(data):
    ar = area.T(size=(tocslib.width, tocslib.height),
                x_range = (1,3),
                x_axis = axis.X(label="/bNumber of nodes with fast disks"),
                y_axis = axis.Y(label="/bIncrease in\nMessages//second", 
                                label_offset=(tocslib.xlabel_offset, None)),
                legend=legend.T())
    
    ar.add_plot(create_line_plot("D4", 2),
                create_line_plot("D2", 1),
                create_line_plot("S4", 5),
                create_line_plot("S2", 4),
                create_line_plot("R", 3))

    return ar

data = chart_data.read_str(" ",
                           "0 0 0 0 0 0 0",
                           "1 45 63 2 9 30",
                           "2 118 133 3 20 53",
                           "3 174 194 3 31 71")
ar = create_graph(data)
ar.y_range = (0,200)
ar.y_axis.tic_interval=50
ar.legend=None
ar.draw()

tocslib.label(ar, "(a)").draw()

data = chart_data.read_str(" ",
                           "0 0 0 0 0 0 0",
                           "1 10 26.5 2 4 9",
                           "2 29 53 3 10 18",
                           "3 48 79 3 16 28")

ar = create_graph(data)
ar.y_range = (0,100)
ar.y_axis.label=None
ar.y_axis.tic_interval=25
ar.loc = tocslib.loc2
ar.draw()

tocslib.label(ar, "(b)").draw()
