import math

def magnitude ( x1 , y1 , x2 , y2 ):
    # Returns the magnitude of the vector
    # between the points (x1 , y1) and (x2 , y2 ).

    return math.hypot((x1-x2),(y1-y2))

#test
#print(magnitude(2, 2, 5, 6))

def foo1():
    i = 0
    result = 0 
    while i < 10:   
       result += i      
       i += 1   
    return result
# print(foo1())

def f1(g):
    return g(2)

def sum_even_factorials(n):
    # Returns the sum of factorials of even numbers 
    # that are less than or equal to n.
    result = 0
    for i in range(n+1):
        if i%2 == 0:
            fact_sum = 1
            for j in range(1, i+1):
                fact_sum = fact_sum * j
            print(fact_sum)
            result += fact_sum
        else:
            continue
    return result

# print(sum_even_factorials(3))

def f(n):
    # Your code here
    if n < 3:
        return 1
    else:
        return f(n-1) + 2*f(n-2) + 3*f(n-3)
"""
for i in range(1, 11):
    print(f(i), f(i)/i)
"""

def is_fib(n):
    if n == 1:
        return True
    else:
        prev, guess = 0, 1
        while guess < n:
            prev, guess = guess, prev + guess
            if guess == n:
                return True
    return False
