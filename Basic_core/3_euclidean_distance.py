import math

x = int(input("Enter ther value for x_coordinate :"))

y = int(input("Enter ther value for y_coordinate :"))

dist = int(math.sqrt(x**2 + y**2))
#math.sqrt(): Taking the square root of that sum and storing in dist
print(f"Euclidean Distance from ({x},{y} to (0,0) = {dist}")