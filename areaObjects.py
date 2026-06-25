import math

# Input dimensions
a = float(input("Enter first parallel side of trapezium: "))
b = float(input("Enter second parallel side of trapezium: "))
h = float(input("Enter height of trapezium: "))
r = float(input("Enter radius of circle: "))

# Calculate areas
area_trapezium = 0.5 * (a + b) * h
area_circle = math.pi * r * r
area_shaded = area_trapezium - area_circle

# Display results
print("\nArea of Trapezium is:", area_trapezium)
print("Area of Circle is:", round(area_circle, 2))
print("Area of Shaded Part is:", round(area_shaded, 2))