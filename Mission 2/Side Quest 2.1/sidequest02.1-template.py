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
    tree = scale(1/n, bb)
    for i in range(n-1):
        tree_layer = scale((i+2)/n, bb)
        tree = overlay_frac((i+1)/(i+2), tree, tree_layer)
    return tree

# Test
# show(tree(5, pentagram_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def xm():
    n = 0
    result = overlay(translate(n, n, make_cross(rcross_bb)), translate(n, -1*n, make_cross(rcross_bb)))
    show(result)
    result = overlay_frac(2/3, result, translate(-1*n, n, make_cross(rcross_bb)))
    result = overlay_frac(3/4, result, translate(-1*n, n, make_cross(rcross_bb)))
    return result
    
 
# Test
show(helix(make_cross(rcross_bb), 7))
