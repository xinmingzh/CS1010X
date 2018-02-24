def fold2(op, term, a, next, b, base): 
    if a > b:
        return base
    else:
        return op (term(a), fold2(op, term, next(a), next, b, base))

def next(a):
    return a + 1

def geometric_series(a, r, n):
    #Fill in your code here
    return fold2(lambda x,y: x+y, lambda n: a*(r**(n-1)), 1, next, n, 0)


for n in range(1, 6):
    print(geometric_series(2, 2, n))


# print(geometric_series(1,2,4))
