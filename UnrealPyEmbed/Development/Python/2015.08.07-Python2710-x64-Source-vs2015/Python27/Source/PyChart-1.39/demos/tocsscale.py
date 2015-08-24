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
                    "2 56.11176043 19.72962276 26.27090859 14.99",
                    "4 108.040603 41.39483239 55.59 47.5618015",
                    "8 224.4335486 80.348324 110.23 89.62",
                    "16 425.6517423 148.7731912 207.34 169.24",
                    "30 790.9817461 273.8225464 385.24 289.93")

ar = area.T(size=(tocslib.width2, tocslib.height),
            x_axis = axis.X(label="/bCluster size"),
            y_axis = axis.Y(label="/bMessages//second", tic_interval=200,
                            label_offset=(tocslib.xlabel_offset, None)),
            legend=legend.T())
ar.add_plot(line_plot.T(label="Porcupine no replication",
                        tick_mark=tocslib.get_tick_mark("PN"),
                        line_style=tocslib.get_line_style("PN"),
                        data=data, ycol=1),
             line_plot.T(label="Porcupine with\nreplication, NVRAM",
                        tick_mark=tocslib.get_tick_mark("PRV"),
                        line_style=tocslib.get_line_style("PRV"),
                        data=data, ycol=3),
             line_plot.T(label="Porcupine with replication",
                        tick_mark=tocslib.get_tick_mark("PR"),
                        line_style=tocslib.get_line_style("PR"),
                        data=data, ycol=2),
             line_plot.T(label="Sendmail+popd",
                        data=data, ycol=4,
                        tick_mark=tocslib.get_tick_mark("SP"),
                        line_style=tocslib.get_line_style("SP")))

ar.draw()

