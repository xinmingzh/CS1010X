from runes import *

def cyclone(bb, n):
    if n == 1:
        return bb
    else:
        return beside(turn_upside_down(bb), quarter_turn_right(cyclone(bb, n-1)))

show(cyclone(rcross_bb, 15))
