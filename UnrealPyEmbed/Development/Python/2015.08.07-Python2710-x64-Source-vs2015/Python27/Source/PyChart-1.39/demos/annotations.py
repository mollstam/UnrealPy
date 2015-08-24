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

tb = text_box.T(loc=(100,100), text="Without frame")
tb.add_arrow((50, 100))
tb.add_arrow((180, 100))
tb.draw()

tb = text_box.T(loc=(100,130), text="/hCMulti\n/bLine")
tb.add_arrow((50, 120))
tb.add_arrow((180, 100))
tb.draw()

tb = text_box.T(loc=(100,160), text="Fat arrow", line_style=None)
tb.add_arrow((180, 140), tail='rm', arrow = arrow.fat1)
tb.draw()

text_box.T(loc=(180, 100), text="/a90Funny background",
           fill_style = fill_style.gray70).draw()

text_box.T(loc=(180, 140), text="/hL/20Big/oText\n/24/bHuge/oText",
           fill_style = None).draw()

