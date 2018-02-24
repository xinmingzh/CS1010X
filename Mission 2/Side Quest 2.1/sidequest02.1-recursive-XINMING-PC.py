#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
import math

##########
# Task 1 #
##########

def tree(n, bb):
    # Fill in code here
    if n == 1:
        return bb
    else:
        return overlay_frac(1/n, tree(n-1, scale((n-1)/n, bb)), bb)

# Test
# show(tree(5, circle_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def helix(bb, n):
    # outputs a helix of n numbers of runes
    # top layer starts from rune at 6 o'clock position, spiral down in anti-clockwise direction

    def helix_layer(i):
        # takes in an integer corresponding to the layer of helix
        # outputs an individual layer of helix
        # 0 refers to top layer, n-1 refers to bottom layer
        return translate(radius * math.sin(i * math.pi * 2/n), radius * math.cos(i * math.pi * 2/n), bb_scaled)

    scaling = 2/n
    radius = 0.5 - 1/n
    bb_scaled = scale(scaling, bb)
    helix = helix_layer(0)

    def helix_x(bb, n):
        if n == 1:
            return helix_layer(
        else:
            return overlay_frac(1/n, helix_layer(n)
    for i in range(n-1):
        helix = overlay_frac((i+1)/(i+2), helix, helix_layer(i+1))

    return helix
 
# Test
# show(helix(make_cross(rcross_bb), 7))
