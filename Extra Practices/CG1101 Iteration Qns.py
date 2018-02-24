from math import *

# Question 1: Prfect Numbers
'''
A perfect number is a positive integer that is equal to the sum of its
proper divisors. A proper divisor is a positive integer other than the
number itself that divides the number evenly(i.e. no remainder).

For example, 6 is the smallest perfect number,because the sum of its
proper divisors 1, 2, and 3is equal to 6. 8 is not a perfect number
because 1 + 2 + 4 is not equal to 8.

Write a function perfect_number that accepts a positive integer in the
range [1, 10000] and returns True/False depending on whether the number
is a perfect number or not.
'''
def perfect_number(number):
    if number == 1:
        return False
    root = 2
    sum_root = 1
    while root <= int(sqrt(number)):
        if number % root == 0:
            sum_root += root + number/root
        root += 1
    if root == sqrt(number):
        sum_root += root
    return sum_root == number

# print(perfect_number(6)) # Examples of perfect numbers: 6, 28, 496, 8128


# Question 2: Print Pattern
'''
Write a function pattern that reads in a positive integer input and
returns a stylized pattern as demonstrated in the sample runs.
'''
def pattern(number):
    # Fill in your code here
    output = ""
    for i in range(1, number+1):
        output += "#" + "-" * i
    return output

# print(pattern(1))  #-
# print(pattern(4))  #-#--#---#----
# print(pattern(7))  #-#--#---#----#-----#------#-------


# Question 3: Invert Number
'''
Write a function invert_number that reads in a positive integer,
reverses the order of each of its digit and returns out the inverted value.
For example, if input number is 12345, your program output should be 54321.
'''
def invert_number(num):
    inverted = ''
    for i in str(num):
        inverted = i + inverted

    return int(inverted)

# print(invert_number(1234))  # 4321
# print(invert_number(32120)) # 2123


# Question 4: Reversed Numbers
'''
You are to write a single function reverse_number that reads two positive
integers low and high, that returns how many integers in the range [low, high]
whose reverse is the same as the original value. You may assume that low ≤ high.
For example, if low is 150 and high is 202, then there are 6 integers in the
range [150, 202] whose reverse is the same as itself. They are: 151, 161, 171,
181, 191, and 202.

You are given the invert_number function from the previous task. You are not
allowed to use any array / string methods for this task.
'''
def reversed_numbers(low, high):
    counter = 0
    while True:
        if low > high:
            return counter
        else:
            inverted = ''
            for i in str(low):
                inverted = i + inverted
            if int(inverted) == low:
                counter += 1
            low += 1

# print(reversed_numbers(150, 202))   # 6
# print(reversed_numbers(12, 21))     # 0
# print(reversed_numbers(1000, 3000)) # 20


# Question 5: Count Substring
'''
Write a program count_substring that reads a string (less than 20 characters)
from the user and stores it into a character array. 

Using just one loop, devise an algorithm that counts the number of substrings
that begin with character 'A' and ends with character 'X'. For example, given
the input string "CAXAAYXZA", there are four substrings that begin with 'A'
and ends with 'X', namely: "AX", "AXAAYX", "AAYX", and "AYX".

You can assume that the input string is composed of English upper case
letters only.
'''
def count_substring(string):
    a = 0
    b = 0
    for i in string:
        if i == 'A':
            a += 1
        elif i == 'X':
            b += a
    return b

# print(count_substring("CAXAAYXZA"))  # 4
# print(count_substring("AAXOXXA"))    # 6
# print(count_substring("AXAXAXAXAX")) # 15


# ++++++++++++++++++++++++++++ END OF EXERCISE +++++++++++++++++++++++++++++++
