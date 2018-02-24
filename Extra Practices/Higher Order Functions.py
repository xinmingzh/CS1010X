# Extra Practices on Higher Order Functions
# NUS CS1010X

# Question 3
def decimal_to_binary(number):
    # code to convert number into its binary representation
    n = 0
    binary = ''
    while 2 ** n <= number:
        n += 1
    if number >= 1:
        n -= 1
    for i in range(n, -1, -1):
        if 2 ** i <= number:
            binary = binary + str(1)
            number -= 2 ** i
        else:
            binary = binary + str(0)
    return binary

# print(decimal_to_binary(1))


# Question 4
'''
plus is a function that takes in two numbers and return the sum.
Given the following functions:
'''
add1 = lambda x: x + 1

def compose(f, g):
    return lambda x: f(g(x))

def repeated(f, n):
    if n == 0:
        return lambda x: x
    else:
        return compose(f, repeated(f, n - 1))
'''
Can you implement plus using repeated and add1? You may assume that
the two input numbers are both non-negative.
Hint: x + y may be considered as x + 1 for y times.
'''
def plus(x, y):
    # Your code here
    return x + repeated(add1, y)(0)

# print(plus(5, 7))


# Question 5: *Hard* Basic Morphology - Part 2
'''
Other than just binary and decimal, we can have numbers of any base.
Common bases that we work with include octal, hexadecimal and base64.

Here is a table of numbers from 0 to 15 in each of the above mentioned
bases except base64.

http://www.themathwebsite.com/TogglerNumbers/Octal.GIF

Write a function make_decimal_to_n_ary_converter that accepts a number
n where 1 < n < 17, and returns a number converter that converts a given
decimal number into that of base n.
'''
def make_decimal_to_n_ary_converter(n):
    # return a number converter that takes a decimal number and returns
    # its string representation in base n
    def make_decimal_to_n_ary(num):
        power = 0
        output = ''
        while n ** power <= num:
            power += 1
        if num > 0:
            power -= 1
        for i in range(power, -1, -1):
            if n ** i > num:
                output = output + '0'
            elif (num // n ** i) in range(0, 10):
                output = output + str(num // n ** i)
            elif num // n ** i == 10:
                output = output + 'A'
            elif num // n ** i == 11:
                output = output + 'B'
            elif num // n ** i == 12:
                output = output + 'C'
            elif num // n ** i == 13:
                output = output + 'D'
            elif num // n ** i == 14:
                output = output + 'E'
            elif num // n ** i == 15:
                output = output + 'F'
            num = num % n ** i
        return output
    return make_decimal_to_n_ary

decimal_to_binary = make_decimal_to_n_ary_converter(2)
decimal_to_octal = make_decimal_to_n_ary_converter(8)
decimal_to_hexadecimal = make_decimal_to_n_ary_converter(16)


decimal_to_binary = make_decimal_to_n_ary_converter(2)
decimal_to_octal = make_decimal_to_n_ary_converter(8)
decimal_to_hexadecimal = make_decimal_to_n_ary_converter(16)

# print(decimal_to_binary(213))                       # 11010101
# print(decimal_to_octal(213))                        # 325
# print(decimal_to_hexadecimal(213))                  # D5
# print(make_decimal_to_n_ary_converter(15)(213))     # E3


# Question 6: *Hard* Basic Morphology - Part 3
'''
Now, converting from decimal to other bases is useful, but we need to
be able to convert back too!

Write a function hexadecimal_to_decimal that takes a string representation
of a hexadecimal number and converts it into a decimal number.
'''
def hexadecimal_to_decimal(hex_number):
    # return the decimal number that hex_number represents
    decimal = 0
    power = len(hex_number) - 1
    for i in hex_number:
        if i == 'A':
            decimal += 16 ** power * 10
        elif i == 'B':
            decimal += 16 ** power * 11
        elif i == 'C':
            decimal += 16 ** power * 12
        elif i == 'D':
            decimal += 16 ** power * 13
        elif i == 'E':
            decimal += 16 ** power * 14
        elif i == 'F':
            decimal += 16 ** power * 15
        else:
            decimal += 16 ** power * int(i)
        power -= 1
    return decimal

# print(hexadecimal_to_decimal('F'))          # 15
# print(hexadecimal_to_decimal('0'))          # 0
# print(hexadecimal_to_decimal('DEADBEEF'))   # 3735928559


# Question 7: *Hard* Basic Morphology - Part 4
'''
To step things up, now, we want to be able to convert a number from
any base to decimal.

Write a function make_n_ary_to_decimal_converter that takes a number
n where 1 < n < 17 and returns a number converter that converts string
representations of numbers of base n into decimal numbers.
'''
def make_n_ary_to_decimal_converter(n):
    # return a number converter that takes a string representation of
    # a base n number and returns its decimal equivalent
    def n_ary_to_decimal(number):
    # return the decimal number that hex_number represents
        decimal = 0
        power = len(number) - 1
        for i in number:
            if i == 'A':
                decimal += n ** power * 10
            elif i == 'B':
                decimal += n ** power * 11
            elif i == 'C':
                decimal += n ** power * 12
            elif i == 'D':
                decimal += n ** power * 13
            elif i == 'E':
                decimal += n ** power * 14
            elif i == 'F':
                decimal += n ** power * 15
            else:
                decimal += n ** power * int(i)
            power -= 1
        return decimal
    return n_ary_to_decimal
    

binary_to_decimal = make_n_ary_to_decimal_converter(2)
octal_to_decimal = make_n_ary_to_decimal_converter(8)
hexadecimal_to_decimal = make_n_ary_to_decimal_converter(16)

# print(binary_to_decimal('100101'))                      # 37
# print(octal_to_decimal('53316'))                        # 22222
# print(hexadecimal_to_decimal('CAFEBABE'))               # 3405691582
# print(make_n_ary_to_decimal_converter(14)('DABBAD00'))  # 1452039540


# Question 8: *Hard* Basic Morphology - Part 5
'''
Finally, we want to be able to convert numbers from any base, to any
other base!

Write a function make_p_ary_to_q_ary_converter that takes two numbers
p and q, and returns a converter that takes a string representation of
a number in base p, and returns the string representation of the number
in base q. 
Note that make_decimal_to_n_ary_converter and make_n_ary_to_decimal_
converter have already been defined for you.

As usual, assume 1 < p, q < 17.
'''
