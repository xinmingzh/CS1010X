#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

# Functions List:
# connect_rigidly(curve1, curve2)
# connect_ends(curve1, curve2)
# gosperize(curve)
# gosper_curve(level)
# show_connected_gosper(level)
# show_points_gosper(level, num_points, initial_curve)

# gosperize_with_angle(theta)(curve)             - returns one level of transformation given angle and curve (using complicated geometry)
# gosper_curve_with_angle(level, angle_at_level) - repeats transpormation with different angle for each level of transformation
# put_in_standard_position(curve)                - forced start point at 0,0 and end point at 1,0
# your_gosperize_with_angle(theta)               - improved version of gosperize_with_angle

# kochize(level)
# show_connected_koch(level, num_points)
# snowflake()

##########
# Task 1 #
##########

def kochize(level):
    if level == 0:
        return unit_line
    else:
        curve1 = kochize(level-1)
        return put_in_standard_position(connect_ends(connect_ends(connect_ends((curve1), rotate(pi/3)(curve1)), rotate(-pi/3)(curve1)), curve1))
    "your answer here"

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

# show_connected_koch(0, 4000)
# show_connected_koch(2, 4000)
# show_connected_koch(4, 4000)
# show_connected_koch(5, 4000)

##########
# Task 2 #
##########

def snowflake():
    curve1 = kochize(5)
    return connect_ends(connect_ends(curve1, rotate(-2*pi/3)(curve1)), rotate(2*pi/3)(curve1))
    "your answer here"

# draw_connected_scaled(10000, snowflake())
