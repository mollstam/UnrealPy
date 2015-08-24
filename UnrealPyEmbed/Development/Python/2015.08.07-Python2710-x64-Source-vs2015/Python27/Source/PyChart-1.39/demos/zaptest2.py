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
import random
random.seed(0)
theme.get_options()

can = canvas.default_canvas()

class zap_x_coord(linear_coord.T):
    # Method get_data_range is inherited from linear_coord.T.
    def get_canvas_pos(self, size, val, min, max):
        # Zap X values between 15 and 35.
        if val <= 15:
            return linear_coord.T.get_canvas_pos(self, size, val, 0, 30)
        elif val <= 35:
            return linear_coord.T.get_canvas_pos(self, size, 15, 0, 30)
        else:
            return linear_coord.T.get_canvas_pos(self, size, val - 20, 0, 30)
        
    def get_tics(self, min, max, interval):
        # Don't draw tick marks between 20 and 30.
        tics = linear_coord.T.get_tics(self, min, max, interval)
        newtics = []
        
        # XXX should be using for..if construction ..
        for item in tics:
            if item < 20 or item > 30:
                newtics.append(item)
        return newtics

data = map(lambda x: (x, random.random() * 2 * x, random.random() * 4 * x),
           range(1,50))

ar = area.T(x_axis = axis.X(label = "X"),
            x_coord = zap_x_coord(),
            y_axis = axis.Y(label = "Y"))
ar.add_plot(line_plot.T(label = "foo", data = data, ycol = 1),
            line_plot.T(label = "bar", data = data, ycol = 2))
ar.draw()

            
zap.zap_vertically(can, line_style.default, fill_style.white,
                   ar.x_pos(14), ar.y_pos(0),
                   ar.x_pos(14) + 6, ar.y_pos(200),
                   4, 6)

                     

