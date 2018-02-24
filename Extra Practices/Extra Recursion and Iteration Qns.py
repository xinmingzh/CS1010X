# Extra Practices Recursive and Iteration Questions
# NUS CS1010X

# Question 1: Infinite Loop!
'''
Modify the following code so that foobar(n) returns the sum of all
positive odd numbers less than or equal to n.

def foobar(n):
    i, result = 1, 0
    while i <= n:
        if i % 2 == 1:
            result = result + i
'''
def foobar(n):
    i, result = 1, 0
    while i <= n:
        if i % 2 == 1:
            result = result + i
        i += 1
    return result

# print(foobar(1))    # 1
# print(foobar(10))   # 25


# Question 2: Factorial recursive
'''
Define a recursive function factorial_recursive that takes an argument
n and calculates the factorial of n.
'''
def factorial_recursive(n):
    """Calculates n! using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

# print(factorial_recursive(3))   # 6
# print(factorial_recursive(5))   # 120
# print(factorial_recursive(0))   # 1


#Question 3: Factorial Iteration
'''
Define an iterative function factorial_iteration that takes an argument
n and calculates the factorial of n.
'''
def factorial_iteration(n):
    """Calculates n! using iteration"""
    result = 1
    while n > 0:
        result = result * n
        n -= 1
    return result

# print(factorial_recursive(3))   # 6
# print(factorial_recursive(5))   # 120
# print(factorial_recursive(0))   # 1\


#Question 4: Exponentiation recursive
'''
Define a recursive function exponentiation_recursive that takes two
arguments, x and e that returns x raise by the exponent e
'''
def exponentiation_recursive(x, e):
    """Calculates x^e using recursion"""
    if e == 0:
        return 1
    else:
        return x * exponentiation_recursive(x, e-1)

# print(exponentiation_recursive(4,2))    # 16
# print(exponentiation_recursive(2,5))    # 32
# print(exponentiation_recursive(-1,5))   # -1
# print(exponentiation_recursive(20,0))   # 1


#Question 5: Exponentiation iteration
'''
Define an iterative function exponentiation_iteration that takes two
arguments, x and e that returns x raise by the exponent e
'''
def exponentiation_iteration(x, e):
    """Calculates x^e iteratively"""
    result = 1
    while e > 0:
        result = result * x
        e -= 1
    return result

# print(exponentiation_recursive(4,2))    # 16
# print(exponentiation_recursive(2,5))    # 32
# print(exponentiation_recursive(-1,5))   # -1
# print(exponentiation_recursive(20,0))   # 1


# Question 6: Occurence
'''
Implement a function occurrence(s1, s2)that receives two strings and
returns the number of times that the second string occurs in the first
string. No overlap of occurrence shall be counted.

For example, string "CS1010S" contains two occurrence of string "10".
As another example, string "110101" contains only 1 occurrence of "101".

Devise the algorithm well and you should aim to avoid using nested
loops to complete the task.

Check sample test cases for input and output format.
'''
def occurrence(s1, s2):
    """Counts the number of occurrences of s2 in s1"""
    s2len = len(s2)
    count = 0
    while len(s1) >= len(s2):
        if s2 in s1[:s2len]:
            count += 1
            s1 = s1[s2len:]
        else:
            s1 = s1[1:]
    return count

# print(occurrence('101110', '10'))   # 2
# print(occurrence('101010', '10'))   # 3
# print(occurrence('101010', '101'))  # 1
# print(occurrence('1111', '11'))     # 2
# print(occurrence('101100', '10'))   # 2


# Question 7: Star Wars Recursive
'''
Define a recursive function star_wars_recursive that takes an argument
num_enemy_ships and returns a string command to take down all the enemy
ships.

The string command will comprise of alternating beams: '*-' and '*--'

For example:
star_wars_recursive(3) will return '*-*--*-'
star_wars_recursive(6) will return '*-*--*-*--*-*--'
star_wars_recursive(0) will return ''

In a more detailed example:
star_wars_recursive(3) is formed using '*-' + '*--' + '*-'
'''
def star_wars_recursive(num_enemy_ships):
    """Take down enemy ships!!"""
    if num_enemy_ships == 0:
        return ''
    else:
        if num_enemy_ships%2==0:
            n = '*--'
        else:
            n = '*-'
        return star_wars_recursive(num_enemy_ships - 1) + n

# print(star_wars_recursive(3))   # *-*--*-
# print(star_wars_recursive(7))   # *-*--*-*--*-*--*-
# print(star_wars_recursive(0))   # 
# print(star_wars_recursive(2))   # *-*--


# Question 8: Star wars iteration
'''
Define a iterative function star_wars_iteration that takes an argument
num_enemy_ships and returns a string command to take down all the enemy
ships.

The string command will comprise of alternating beams: '*-' and '*--'

For example:
star_wars_iteration(3) will return '*-*--*-'
star_wars_iteration(6) will return '*-*--*-*--*-*--'
star_wars_iteration(0) will return ''
'''
def star_wars_iteration(num_enemy_ships):
    """Releases just enough pulses to take down enemy ships"""
    result = ''
    while num_enemy_ships > 0:
        if num_enemy_ships % 2 == 0:
            n = '*--'
        else:
            n = '*-'
        result = n + result
        num_enemy_ships -= 1
    return result

# print(star_wars_recursive(3))   # *-*--*-
# print(star_wars_recursive(7))   # *-*--*-*--*-*--*-
# print(star_wars_recursive(0))   # 
# print(star_wars_recursive(2))   # *-*--

# +++++++++++++++++++++++++++++ END OF EXERCISE ++++++++++++++++++++++++++++++
