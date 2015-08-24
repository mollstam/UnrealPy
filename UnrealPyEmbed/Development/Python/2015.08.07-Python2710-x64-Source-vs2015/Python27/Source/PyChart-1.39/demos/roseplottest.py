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

theme.use_color = 1

data1 = [ 0.27027027,  0.74324324,  0.          ,
          0.34459459  ,0.47297297  ,0.06756757,
          0.90540541  ,1.          ,0.40540541  ,
          0.33783784  ,0.33783784  ,0.16216216]
data2 = [ 0.93333333,  0.46666667  ,0.26666667  ,
          0.60666667  ,0.6         ,0.73333333,
          0.22666667,  0.72        ,0.13333333  ,
          0.46666667  ,1.          ,0.29333333]
data = [('/7Model', data1), ('/7Station', data2)]
        
ar = area.T(legend=legend.T(loc=(100,-5), right_fudge=0, left_fudge=3))

plot = rose_plot.T(data=data, sector_centred=True)
ar.add_plot(plot)
ar.draw()

