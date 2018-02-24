#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import math

##########
# Task 1 #
##########

# Simplifed Order notations:

# 4^n * n^2
# Ans: 4^n

# n * 3^n
# Ans: 3^n

# 1000000000n^2
# Ans: n^2

# 2^n/1000000000
# Ans: 2^n

# n^n + n^2 + 1
# Ans: n^n

# 4^n + 2^n
# Ans: 4^n

# 1^n
# Ans: 1

# n^2
# Ans: n^2

# Faster order of growth in each group:

#   i. 4^n
#  ii. 2^n
# iii. n^n
#  iv. n^2


##########
# Task 2 #
##########

# Time complexity: n
# Space complexity: n


##########
# Task 3 #
##########

# Time complexity of bar: n
# Time complexity of foo: n^2

# Space complexity of bar: n
# Space complexity of foo: n^2

def improved_foo(n):
    # Fill in code here
    result = 0
    for i in range(1, n+1):
        result += ((i + 1) * i)/2
        print(result)
    return result

# Improved time complexity: n
# Improved space complexity: 3
