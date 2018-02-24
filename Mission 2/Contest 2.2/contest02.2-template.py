#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.

def cyclone(bb, n):
    if n == 1:
        return bb
    else:
        return beside(turn_upside_down(bb), quarter_turn_right(cyclone(bb, n-1)))

show(cyclone(rcross_bb, 15))



