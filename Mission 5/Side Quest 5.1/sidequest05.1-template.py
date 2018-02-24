#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# unit_circle draws a series of points in a circular shape with points equally
# spread apart

# alternative_unit_circle draws a series of points also in a circular shape but
# points are more squeezed when t is closer to 0 and more spaced out when t is
# closer to 1.

# This is because variable t in cos(2*pi*t) and sin(2*pi*t) in unit_circle is
# replaced by t**2. When we look at how t and t**t changes from t == 0 to t == 1,
# t increases linearly while t**2 increases more slowly at first but becomes faster
# and even surpasses the rate of increase of t as t approaches 1. t**2 Increase
# more slowly means less dist between each point, which explains points being more
# packed at the beginning.


##########
# Task 2 #
##########

# (a)
def spiral(t):
    return make_point(t*sin(2*pi*t), t*cos(2*pi*t))
    "your answer here"

# draw_connected_scaled(1000, scale_xy(-1,1)(spiral))

# make_point(sin(pi*t) - 0.5*t, cos(pi*t) - 0.5*t)
# make_point(sin(2*pi*t), cos(2*pi*t))

# (b)
def heart(t):
    if t < 0.5:
        return spiral(2 * t)
    else:
        return scale_xy(-1, 1)(spiral)(2 * t - 1)
    
    "your answer here"

draw_connected_scaled(1000, heart)
