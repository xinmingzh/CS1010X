import math

a, b, c = 3, 11, 9

x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

print(x1, x2)
print(round(max(x1, x2), 2))
