from math import sqrt

# CG1101 Recursion and Iternation Questions
# NUS Compter Science

# Question 1: Legendre's Conjecture
'''
Legendre's conjecture (proposed by Adrien-Marie Legendre in 1912) states that
there is at least one prime number in range [n^2, (n + 1)^2] for every positive
integer n.

Implement the function legendre that takes in an input parameter n and tests
Legendre's conjecture over a range of numbers from 1 up to the input number n.

This means if the input is 4, you should check that there is at least one prime
between 1^2 and 2^2, and at least one prime between 2^2 and 3^2, and at least
one prime between 3^2 and 4^2, and at least one prime between 4^2 and 5^2.

As you might have guessed, the one and only return value of this function is
True. You can pass this question by simply writing return True but you will
just be compromising your own learning.

Note: Coursemology will limit your runtime. You will need an efficient way of
doing this to clear the question
'''
def legendre(n):
    # code to test Legendre's conjecture over a range of numbers from 1 up to
    # the input number n.
    def is_prime(num):
        for divisor in range(2, int(sqrt(num))):
            if num % divisor == 0:
                return False
        return True
    
    counter = 0
    for i in range(1, n+1):
        a, b = i ** 2, (i + 1) ** 2
        for j in range(a, b):
            if is_prime(j):
                counter += 1
        if counter == 0:
            return False
    return True

# print(legendre(500))


# Question 2: Legendre's Conjecture - Part 2!
'''
Now, implement the function legendre_n to test Legendre's Conjecture for a
specific number n.

Given an integer n, the function legendre_n should return the number of prime
numbers between n^2 and (n+1)^2.
'''
def legendre_n(n):
    """Returns the number of primes between n**2 and (n+1)**2"""
    def is_prime(num):
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    counter = 0
    for i in range(n**2+1, (n+1)**2):
        if is_prime(i):
            counter += 1
    return counter

# print(legendre_n(500))


# Question 3: Goldbach's Conjecture
'''
Goldbach's conjecture (proposed by Christian Goldbach in 1742) is one of the
oldest unsolved problems in number theory. It states: every even integer greater
than 2 can be written as the sum of two primes.

Implement a function: def goldbach(n) to test Goldbach's Conjecture over a range
of even numbers from 4 up to the input number n. This means that if the input is
8, you should check that 4 can be written as a sum of two primes (2 + 2) and 6
can be written as a sum of two primes (3 + 3) and 8 can be written as a sum of two
primes (3 + 5).

You may assume that input number n is always greater or equal to 4.
'''
def goldbach(n):
    # code to test Goldbach's Conjecture on an input n
    def is_prime(sum):
        for i in range(2, int(sqrt(sum))+1):
            if sum % i == 0:
                return False
        return True

    if n == 4:
        if is_prime(2):
            return True
    a, b = 3, 3
    for i in range(3, int(n/2+1)):
        c, d = a, b
        while d > 3:
            if is_prime(c) and is_prime(d):
                break
            else:
                c += 2
                d -= 2
        if d < 3:
            return False
        
        if i % 2 == 0:
            a += 2
        else:
            b += 2
    return True

# print(goldbach(6))


# Question 4: Maclaurin Series
'''
In mathematics, the Taylor series is a representation of a function as an infinite
sum of terms calculated from the values of its derivatives at a single point. It
may be regarded as the limit of the Taylor polynomials. Taylor series are named
after the English mathematician Brook Taylor. If the series is centered at zero,
the series is also called a Maclaurin series, named after the Scottish mathematician
Colin Maclaurin.

As an example, an approximation for e^x is:


Implement a function:
def maclaurin(x, n):
that reads in two positive integers x and n, calculate e^x up to the nth term in
the Maclaurin series. i.e.,   

Define n! as a function factorial in your program. You should correct your output to
3 decimal places. (You may use round(value, n) to round value to n decimal places)
'''
def maclaurin(x, n):
    # code that approximates e^x up to the nth term
    def factorial(n):
        add = 1
        for i in range(1, n+1):
            add = add * i
        return add
        
    add = 1
    for i in range(1, n):
        add += x**i/factorial(i)
    return round(add, 3)

# print(maclaurin(2, 2))    # 3.0
# print(maclaurin(2, 10))   # 7.389
# print(maclaurin(2, 11))   # 7.389
# print(maclaurin(16, 5))   # 3558.333


# Question 5: Conway Sequence
'''
The Conway’s recursive sequence is defined by the following recurrence relation for
any positive integer n.

Implement the function conway that reads in a positive integer n, and returns a(n).
'''
def conway(n):
    # code that implements Conway's recursive sequence.
    if n == 1 or n == 2:
        return 1
    else:
        return conway(conway(n-1)) + conway(n-conway(n-1))

# print(conway(1))    # 1
# print(conway(2))    # 1
# print(conway(6))    # 4
# print(conway(15))   # 8


# Question 5: Recursive Sum
'''
Write a recursive function recursive_sum to accept a non-negative integer x and
calculate f(x) based on the following formula.
'''
def recursive_sum(n):
    # Fill in your code here
    if n == 0 or n == 1 or n == 2:
        return 1
    elif n % 2 == 0:
        return recursive_sum(n-1) + recursive_sum(n-2) + recursive_sum(n-3)
    else:
        return recursive_sum(n-1) + recursive_sum(n-2)

# print(recursive_sum(2))     # 1
# print(recursive_sum(3))     # 2
# print(recursive_sum(6))     # 12
# print(recursive_sum(9))     # 54

# +++++++++++++++++++++++++++++++ END OF EXERCISE ++++++++++++++++++++++++++++++++++
