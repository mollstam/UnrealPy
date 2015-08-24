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

def createbar_plot(ar, label, ycol, base, clu):
    baseBar = bar_plot.T(label=None, fill_style = None, line_style=None,
                        data=base, hcol=ycol, cluster=(clu,5))
    bar = bar_plot.T(label=label,
                     fill_style = fill_style.standards.nth(ycol),
                     data=data, hcol=ycol, cluster=(clu,5), stack_on = baseBar)
    ar.add_plot(baseBar, bar)
    
def createGraph(data, base):
    ar = area.T(size=(tocslib.width, tocslib.height),
                x_range = (0.5,3.5),
                x_axis = axis.X(label="/bNumber of nodes with fast disks",
                                tic_interval=lambda x,y: range(1, 3, 1)),
                y_axis = axis.Y(label="/bMessages//second", 
                                label_offset=(tocslib.xlabel_offset, None)),
                legend=legend.T())
    
    createbar_plot(ar, "D4", 2, base, 0)
    createbar_plot(ar, "D2", 1, base, 1)
    createbar_plot(ar, "S4", 5, base, 2)
    createbar_plot(ar, "S2", 4, base, 3)
    createbar_plot(ar, "R", 3, base, 4)
    return ar

base_nonrepl =    [  [0, 791,    778,    693.2, 766.88, 753.09],
                     [1, 791,    778,    693.2, 766.88, 753.09],
                     [2, 791,    778,    693.2, 766.88, 753.09],
                     [3, 791,    778,    693.2, 766.88, 753.09]]
base_repl = [[0, 362.53, 373.34, 325.00, 360.4, 363.23],
             [1, 362.53, 373.34, 325.00, 360.4, 363.23],
             [2, 362.53, 373.34, 325.00, 360.4, 363.23],
             [3, 362.53, 373.34, 325.00, 360.4, 363.23]]

data = chart_data.read_str(" ",
                           "0 0 0 0 0 0 0",
                           "1 45 63 2 9 30",
                           "2 118 133 3 20 53",
                           "3 174 194 3 31 71")
ar = createGraph(data, base_nonrepl)
#area.y_range = (0,200)
ar.y_range = (600,1000)
ar.y_axis.tic_interval=50
ar.legend=None

ar.draw()
tocslib.label(ar, "(a)").draw()

data = chart_data.read_str(" ",
                           "0 0 0 0 0 0 0",
                           "1 10 26.5 2 4 9",
                           "2 29 53 3 10 18",
                           "3 48 79 3 16 28")

ar = createGraph(data, base_repl)
#area.y_range = (0,100)
ar.y_range = (300,500)
ar.y_axis.label=None
ar.y_axis.tic_interval=25
ar.loc = tocslib.loc2
ar.draw()
tocslib.label(ar, "(b)").draw()


