#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))

# Your answer here:
# n = 9

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

"""
(i) thrice(thrice)(add1)(6)

# your answer here
Prints 33. Thrice means f(f(f)) (call it 3*). thrice(thrice) means 
3*(3*(3*(f))) which gives 27 executes of f (in this case add1) to initial 
value of 6.


(ii) thrice(thrice)(identity)(compose)

# your answer here
Prints function compose. The function identity returns input as output. 
Passing the output of identity into another identity 27 times simply returns 
the identity, so passing compose into thrice(thrice)(identity) simply gives 
back itself.

(iii) thrice(thrice)(sq)(1)

# your answer here
Prints 1. Squaring 1 27 times gives 1.

(iv) thrice(thrice)(sq)(2)

# your answer here
No response. The number gets very big as the number 2 is squared 27 times,
Amount of time needed to compute the results will be too long.

"""


###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        if x == 0:
            return 1
        if x == 1:
            return -1
        else:
            return x**2

    def op(x, y):
        return x + 2 * y

    n = t + 1

    # Do not modify this return statement
    return combine(f, op, n)

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    def f(x):
        # answer here
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            x -= 2
            if x == 0:
                return 0
            if x == 1:
                return 1
            else:
                a = 0
                b = 1
                while x > 1:
                    a, b = b, a + b
                    x -= 1
        return b
        
    def op(x, y):
        # answer here
        return x + y
        
    # do not modify this return statement
    return combine(f, op, n+1)

# print(new_fib(0))
# print(new_fib(1))
# print(new_fib(2))
# print(new_fib(5))
# print(new_fib(6))
# print(new_fib(7))

# Your answer here:
'''
ops must be a plus function, lambds x,y: x + y, as every number in the
sequence is the previous number + the pre - previous number, except for the
2 base cases 0 and 1.

sequence = 0 1 1 2 3 5 8 11 ...
starting with base 'result' value 0:
difference(f(i) - f(i-1)) = 0 1 0 1 1 2 3 5 8
for fib no. to be possibly computed using combine function,
this difference needs to be outputted by function f(x)
(eg. input 0/1/2/3/4/5/6 gives output 0/1/0/1/1/2/3)

For a while I believed it could not be done, and was writing up my explanation
for why so. But then I realised that it is possible using iterative loop 
instead of recursive loop, soooo :)
'''

# ++++++++++++++++++++++++++++++ END OF MISSION ++++++++++++++++++++++++++++++++
