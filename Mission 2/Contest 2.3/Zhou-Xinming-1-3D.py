#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import pi, sin, cos

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.

def simpleoverlay(bb):
    return overlay(scale(0.5, bb), bb)
# Use one of the following methods to display your rune:
stereogram(simpleoverlay(make_cross(nova_bb)))
# anaglyph(<your rune>)
# hollusion(<your rune>)
