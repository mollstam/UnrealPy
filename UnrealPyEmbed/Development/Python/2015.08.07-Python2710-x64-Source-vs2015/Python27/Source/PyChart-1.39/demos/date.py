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
import sys
import datetime
from pychart import *

def date_to_ordinal(s):
    month, day, year = map(int, s.split("/"))
    return datetime.date(year, month, day).toordinal()

def format_date(ordinal):
    d = datetime.date.fromordinal(int(ordinal))
    return "/a60{}" + d.strftime("%b %d, %y")

data = [["10/5/1983", 10], ["3/5/1984", 15],
        ["11/10/1984", 16], ["2/22/1985", 20]]
data = chart_data.transform(lambda x: [date_to_ordinal(x[0]), x[1]], data)

ar = area.T(x_coord = category_coord.T(data, 0),
            y_range = (0, None),
            x_axis = axis.X(label = "Date", format = format_date),
            y_axis = axis.Y(label = "Value"))
ar.add_plot(bar_plot.T(data = data))
ar.draw()
