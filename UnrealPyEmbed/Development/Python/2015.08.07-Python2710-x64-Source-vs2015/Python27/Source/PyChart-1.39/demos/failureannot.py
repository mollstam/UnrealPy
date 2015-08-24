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
import failure

can = canvas.default_canvas()
can.round_rectangle(line_style.gray70_dash1, None, -60, 140, 280, 180, 10)
can.show(200, 142, "/H{}/14{}text_box.T")

tb = text_box.T(text="/H{}/14{}axis.X", loc=(-80, 0), line_style = None)
tb.add_arrow((0, 25), "rm", arrow=arrow.fat1)
tb.draw()

tb = text_box.T(text="/H{}/14{}axis.Y", loc=(00, -45), line_style = None)
tb.add_arrow((30, 0), "ct", arrow=arrow.fat1)
tb.draw()

tb = text_box.T(text="/H{}/14{}legend.T", loc=(240, 100), line_style = None)
tb.add_arrow((250, 80), "cb", arrow=arrow.fat1)
tb.draw()

tb = text_box.T(text="/o{}/14{}plots", loc=(180, 100), line_style = None)
tb.add_arrow((170, 70), "lb", arrow=arrow.fat1)
tb.draw()

