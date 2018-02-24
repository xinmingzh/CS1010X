#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(bb, n):
    # Fill in code here
    if n == 1:
        return bb
    bb_fractal = bb
    for i in range(n-1):
        bb_fractal = beside(bb, stack(bb_fractal, bb_fractal))
    return bb_fractal

# Test
# show(fractal(make_cross(rcross_bb), 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(bb, n):
    # Fill in code here
    if n == 1:
        return bb
    else:
        return beside(bb, stack(fractal_iter(bb, n-1), fractal_iter(bb, n-1)))

# Test
# show(fractal_iter(make_cross(rcross_bb), 3))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(bb1, bb2, n):
    # Fill in code here
    if n%2 == 0:
        bb_fractal = bb2
    else:
        bb_fractal = bb1
    while True:
        if n == 1:
            return bb_fractal
        elif n%2 == 0:
            bb_fractal = beside(bb1, stack(bb_fractal, bb_fractal))
            n = n - 1
        else:
            bb_fractal = beside(bb2, stack(bb_fractal, bb_fractal))
            n = n - 1

# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(bb1, bb2, n):
    # Fill in code here
    bb_fractal = bb1 if n%2==1 else bb2
    def reverse_count(bb1, bb2, a):
        if a ==n:
            return bb_fractal
        else:
            return beside(bb1 if a%2==1 else bb2, stack(reverse_count(bb1, bb2, a+1), reverse_count(bb1, bb2, a+1)))
    return reverse_count(bb1, bb2, 1)

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(bb1, bb2, bb3, bb4):
    # Fill in code here
    bb_layer4 = beside(stack(blank_bb, blank_bb), stack(bb1, blank_bb))
    bb_layer3 = beside(stack(blank_bb, blank_bb), stack(blank_bb, bb2))
    bb_layer2 = beside(stack(blank_bb, bb3), stack(blank_bb, blank_bb))
    bb_layer1 = beside(stack(bb4, blank_bb), stack(blank_bb, blank_bb))
    return overlay(overlay(bb_layer1, bb_layer2), overlay(bb_layer3, bb_layer4))

# Test
show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
