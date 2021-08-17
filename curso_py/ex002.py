from math import hypot

a , b = (float(x) for x in input('Set parts of triangule: ').split())
print(f'The hypotenuse of triangule is {hypot(a,b)}')