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

data = chart_data.read_str(" ",
                    "2 663.8954 466.1732719",
                    "4 1136.591805 767.7338263",
                    "8 1975.892086 1562.30366",      
                    "16 3095.491197 2401.061551",
                    "30 4838.670793 3836.058")

ar = area.T(size=(tocslib.width2, tocslib.height),
            x_axis = axis.X(label="/bCluster size"),
            y_axis = axis.Y(label="/bMessages//second", tic_interval=1000,
                            label_offset=(tocslib.xlabel_offset*1.2, None)),
            legend=legend.T())
ar.add_plot(line_plot.T(label="No replication",
                        tick_mark=tocslib.get_tick_mark("PN"),
                        line_style=tocslib.get_line_style("PN"),
                        data=data, ycol=1),
             line_plot.T(label="With replication",
                        tick_mark=tocslib.get_tick_mark("PR"),
                        line_style=tocslib.get_line_style("PR"),
                        data=data, ycol=2))

ar.draw()

