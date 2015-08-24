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
import sys

theme.get_options()

can = canvas.default_canvas()
size = (300, 200)
ar = area.T(size = size, legend=None, y_range = (9000, 9500),
            x_axis = axis.X(format="7//%d//2002", label="Date"),
            y_axis = axis.Y(format="%d", label="Dow Jones"))
ar.add_plot(line_plot.T(data=[ [1,9379], [2, 9054], [3, 9007], [4, 9109], [5, 9243] ]))
            
ar.draw()
can.show(ar.x_pos(4), ar.y_pos(9070), "/a45{}Dow Jones")

ar = area.T(size = size, legend=None, y_range = (940, 990),
            x_axis = None, y_axis = axis.Y(format="%d", offset=300, tic_len=-6,
                                           label_offset=(50, 0),
                                           label="S&P 500"))
ar.add_plot(line_plot.T(data=[ [1,989], [2, 953], [3, 948], [4, 968], [5, 989] ]))
            
ar.draw()

can.show(ar.x_pos(4), ar.y_pos(970), "/a50{}S&P 500")




