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

data = chart_data.read_str(",",
                    "/8No\nReplication,23,105",
                    "/8Replication,9,38",
                    "/8Replication\nwith NVRAM,13,48")

ar = area.T(y_range=(0,150),
            size=(tocslib.width*1.3, tocslib.height),
            x_coord=category_coord.T(data, 0),
            y_axis = axis.Y(label="/bMessages//second", tic_interval=50),
            x_axis = axis.X(label=None),
            legend=legend.T(loc=(70,50)))

ar.add_plot(bar_plot.T(label="With one disk//node",
                       cluster = (0,2), data = data, width=15,
                       fill_style=fill_style.white),
            bar_plot.T(label="With three disks//node",
                       cluster = (1,2), data = data, width=15, hcol=2))

ar.draw()









