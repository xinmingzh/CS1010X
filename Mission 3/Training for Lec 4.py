def sum_odd_n(n):
    """Sums integers from 1 to n using a for loop"""
    total = 0
    for i in range(1, 2*n, 2):
        total += i
    return total

#test
#print(sum_odd_n(3))

def sum_odd_n_1(n):
    """Sums integers from 1 to n using a while loop"""
    total = 0
    count = 1
    while count <= n:
        total += 1 + (count - 1) * 2
        count += 1
    return total

#test
#print(sum_odd_n_1(3))

def sum_odd_n_r(n):
    """Sums odd integers from 1 to n using recursion"""
    if n == 1:
        return 1
    else:
        return 1 + (n - 1) * 2 + sum_odd_n_r(n-1)

#test
#print(sum_odd_n_r(3))

def sum_n_squares(n):
    result = 0
    for counter in range(n+1):
        # Your code here    
        result += counter ** 2
        counter += 1
    return result

#test
print(sum_n_squares(3))

