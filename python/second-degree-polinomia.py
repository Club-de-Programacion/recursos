import math

# Coefficients
a = 1
b = 2
c = -12

# Discriminant
discriminant = b**2 - 4*a*c

# Roots calculation using quadratic formula
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    roots = (root1, root2)
else:
    roots = None

print(roots)
