    #
# CS1010X --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

# range of viewport:
# x range ( -0.013104838 : 1.011088709 )
# y range ( -0.011088709 : 1.013104838 )
##########
# Task 1 #
##########

# (a) unit_line_at_y : (Number) --> Curve
# your answer here

# (b) a_line : (Unit_interval) --> Point
# your answer here

# (c)
def vertical_line(point, length):
    return lambda t: make_point(x_of(point), y_of(point) - length * t)
    "your answer here"
    

#draw_connected(200, vertical_line(make_point(0.5, 0.75), 0.5))
draw_connected(200, vertical_line(make_point(0.498991935, 0.751512097), 0.501008064))


def unit_line_at_Y(y):
    return lambda t: make_point(t, y)

#draw_connected(200, unit_line_at_y(-0.011088709))

# (d) vertical_line : (point, number) --> Curve
# your answer here

# (e)
# draw_connected(200, vertical_line(make_point(-0.013104838, 1.01), 0.5))

##########
# Task 2 #
##########

# (a) vertical line with gradient 1 to test suitable range of x and y values
#     use different types of curves to test such as circle, 1/x, x^2, x^3, etc.
# your answer here

# (b)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point(-x_of(pt), y_of(pt))
        "your answer here"

    return reflected_curve
	
#draw_connected_scaled(200, arc)
#draw_connected_scaled(200, reflect_through_y_axis(arc))
