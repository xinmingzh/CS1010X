#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def R_T(bb):
    return quarter_turn_right(bb)
def L_T(bb):
    return quarter_turn_left(bb)

def egyptian(bb, n):
    columnbb = stackn(n-2, bb)
    rowbb = L_T(stackn(n, R_T(bb)))
    middle_row = L_T(stack_frac((n-1)/n, stack_frac(1/(n-1), R_T(columnbb), R_T(bb)), R_T(columnbb)))
    return stack_frac((n-1)/n, stack_frac(1/(n-1), rowbb, middle_row), rowbb)

# Test
show(egyptian(heart_bb, 10))
