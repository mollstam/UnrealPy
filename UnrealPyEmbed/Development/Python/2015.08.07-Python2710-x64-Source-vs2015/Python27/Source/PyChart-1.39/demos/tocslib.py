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
import copy

width=pychart_util.inch_to_point(1.7)
height=pychart_util.inch_to_point(1.2)
loc2 = (width+36, 0)

def label(ar, text):
    return text_box.T(text=text, line_style = None, loc=(ar.loc[0]+ar.size[0]/2, ar.loc[1]-40))

tickSize=3
lWidth=1.2
def get_tick_mark(p):
    if p == "PN":
        return tick_mark.Diamond(size=tickSize)
    elif p == "PRV":
        return tick_mark.Triangle(size=tickSize)
    elif p == "PR":
        return tick_mark.X(size=tickSize*1.2,line_style=line_style.T(width=1))
    elif p == "SP" or p == "SM":
        return tick_mark.Square(size=tickSize)
    elif p == "D4":
        return tick_mark.Diamond(size=tickSize)
    elif p == "D2":
        return tick_mark.DownTriangle(size=tickSize)
    elif p == "D1":
        return tick_mark.Square(size=tickSize)
    elif p == "R":
        return tick_mark.Circle(size=tickSize)
    elif p == "S4":
        return tick_mark.Diamond(size=tickSize)
    elif p == "S2":
        return tick_mark.Plus(size=tickSize)
    elif p == "S1":
        return tick_mark.Square(size=tickSize)
    else:
        return None
    #else:
    #    pychart_util.error("tick_mark:", p)

greyscale_line_styles = {
    "PN" : line_style.T(width=lWidth),
    "PRV": line_style.T(width=lWidth,color=color.gray50),
    "PR": line_style.T(width=lWidth,dash=line_style.dash1),
    "D4": line_style.T(width=lWidth),
    "D2": line_style.T(width=lWidth,dash=line_style.dash1, color=color.gray70),
    "D1": line_style.T(width=lWidth,dash=line_style.dash2),
    "S4": line_style.T(width=lWidth),
    "S2": line_style.T(width=lWidth,dash=line_style.dash1,color=color.gray70),
    "S1": line_style.T(width=lWidth,dash=line_style.dash2,color=color.gray70),
    "R": line_style.T(width=lWidth,color=color.gray50),
    "SM": line_style.T(width=lWidth),
    "SP": line_style.T(width=lWidth),
    }

def hack(l):
    x = copy.deepcopy(l)
    x.width = lWidth
    return x
    
color_line_styles = {
    "PN" : hack(line_style.standards.nth(0)),
    "PRV":  hack(line_style.standards.nth(1)),
    "PR":  hack(line_style.standards.nth(2)),
    "D4":  hack(line_style.standards.nth(3)),
    "D2":  hack(line_style.standards.nth(4)),
    "D1":  hack(line_style.standards.nth(5)),
    "S4":  hack(line_style.standards.nth(6)),
    "S2":  hack(line_style.standards.nth(7)),
    "S1":  hack(line_style.standards.nth(8)),
    "R":  hack(line_style.standards.nth(9)),
    "SM":  hack(line_style.standards.nth(10)),
    "SP":  hack(line_style.standards.nth(11)),
    }

def get_line_style(p):
    if not theme.use_color:
        styles = greyscale_line_styles
    else:
        styles = color_line_styles
    if styles.has_key(p):
        return styles[p]
    else:
        pychart_util.error("unknown policy:", p)

width2=pychart_util.inch_to_point(2.1)
height=pychart_util.inch_to_point(1.2)
xlabel_offset=-35
