# Triangle Type Checker

# Ask the user for the lengths of the three sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the sides form a valid triangle
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    
    # Determine the type of triangle
    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The lengths do not form a valid triangle.")