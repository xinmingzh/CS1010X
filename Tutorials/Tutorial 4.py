# CS1010X
# Tutorial 4

# Question 1

def calc_integral(f, a, b, n):
    # Put your code here #
    h = (b-a)/n
    y = lambda k: f(a + k * h)
    sum_y = y(0) + y(n)
    for i in range(1, n):
        if i%2 != 0:
            sum_y += 4 * y(i)
        else:
            sum_y += 2 * y(i)
    return (h/3) * sum_y

# print(calc_integral(lambda x: x*x*x, 0, 1, 100))


# Question 2
'''
Write a function g(k) that solves the following product
using the higher order function fold.
'''
def fold(op, f, n):
    if n == 0:
        return f(0)
    return op(f(n), fold(op, f, n-1))

def g(k):
    return fold(lambda x,y: x*y, lambda x: x-(x+1)**2, k)

# print(g(0))
# print(g(8))


# Question 3

def accumulate(combiner, base, term, a, next, b):
    if a > b:
        return base
    else:
        return combiner(term(a), accumulate(combiner, base, term, next(a),next, b))

# print(accumulate(lambda x, y: x*y, 1, lambda x: x**2 + 1, 0, lambda x: x+2, 5) == 85)
# print(accumulate(lambda x, y: x+y, 1, lambda x: x**2 + 1, 0, lambda x: x+2, 5) == 24)
# print(accumulate(lambda x, y: x+y, 1, lambda x: x**2 + 1, 1, lambda x: x+2, 5) == 39)


# Question 4
'''
Define the function sum discussed in lecture in terms of accumulate.
'''
def sum(term, a, next, b):
    return accumulate(lambda x,y: x+y, 0, term, a, next, b)

#print(sum(lambda x: x*2, 1, lambda x: x+1, 5) == 30)
#print(sum(lambda x: x*2, 0, lambda x: x+2, 10) == 60)
#print(sum(lambda x: x**2, 1, lambda x: x+1, 5) == 55)


# Question 5
'''
Now give an iterative solution
'''
def accumulate_iter(combiner, null_value, term, a, next, b):
    total = null_value
    while True:
        if a > b:
            return total
        else:
            total = combiner(term(a), total)
            a = next(a)

# print(accumulate_iter(lambda x,y: x+y, 0, lambda x: x*x, 1, lambda x: x+1, 5) == 55)
# print(accumulate_iter(lambda x,y: x+y, 1, lambda x: x*x, 1, lambda x: x+1, 5) == 56)
# print(accumulate_iter(lambda x,y: x*y, 1, lambda x: x*x, 1, lambda x: x+1, 5) == 14400)


# Question 6
'''
A point can be represented as a pair of numbers: the x coordinate and the y coordinate. 
Based on this representation of a point, define a point constructor make_point.
Define selector x_point which returns the x coordinate of a given point.
Define selector y_point which returns the y coordinate of a given point.
'''
def make_point(x, y):
    return x, y

def x_point(p):
    return p[0]
    
def y_point(p):
    return p[1]

p1 = make_point(2, 3)

# print(x_point(p1) == 2)
# print(y_point(p1) == 3)


# Question 7
'''
A line segment has two endpoints. It can be represented by a pair of points: a starting point and an ending point. 
Based on this representation of a line segment, define a line segment constructor make_segment. 
Define selector start_segment which returns the starting point of a given line segment.
Define selector end_segment which returns the ending point of a given line segment.
'''
def make_segment(p1, p2):
    #Your code here
    return p1, p2
    
def start_segment(s):
    #Your code here
    return s[0]

def end_segment(s):
    #Your code here
    return s[1]

p1 = make_point(2, 3)
p2 = make_point(5, 7)

#print(x_point(start_segment(make_segment(p1, p2))) == 2)
#print(y_point(start_segment(make_segment(p1, p2))) == 3)
#print(x_point(end_segment(make_segment(p1, p2))) == 5)
#print(y_point(end_segment(make_segment(p1, p2))) == 7)


# Question 8
'''
Finally, using the selectors and constructors which you have defined,
define a function midpoint_segment that takes a line segment as argument and returns its midpoint.
'''
def midpoint_segment(segment):
    #Your code here
    p3 = segment[0]
    p4 = segment[1]
    midx = (p3[0] + p4[0])/2
    midy = (p3[1] + p4[1])/2
    return midx, midy

p1 = make_point(2, 3)
p2 = make_point(5, 7)
s = make_segment(p1, p2)

# print(x_point(midpoint_segment(s)) == 3.5)
# print(y_point(midpoint_segment(s)) == 5.0)
