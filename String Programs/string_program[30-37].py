"""
30.Write a Python program to print the following floating numbers
 upto 2 decimal places
"""
num1 = 45.2564178
print("Original Number: ", num1)
print("Formatted Number: " + "{:.2f}".format(num1))


"""
31.Write a Python program to print the following floating numbers
 upto 2 decimal places with a sign.
"""
print("Formatted Number with sign: " + "{:+.2f}".format(num1))


"""
32. Write a Python program to print the following floating numbers
with no decimal places.
"""
print("Formatted Number with no decimal places: " + "{:.0f}".format(num1))


"""
33.Write a Python program to print the following integers with
zeros on the left of specified width.
"""
num2 = 63
print("The original Number is: ", num2)
print("Formatted Number(left padding, width 3): " + "{:0>3d}".format(num2))


"""
34.Write a Python program to print the following integers
with '*' on the right of specified width
"""
print("Formatted Number(right padding, width 4): " + "{:*< 5d}".format(num2))


"""
35.Write a Python program to display a number with a comma separator
"""
num3 = 500000000
print("The original number is: ", num3)
print("Formatted Number with comma separator: " + "{:,}".format(num3))


"""
36.Write a Python program to format a number with a percentage.
"""
num4 = 0.25
print("Original Number: ", num4)
print("Formatted Number with percentage: " + "{:.2%}".format(num4))


"""
37.Write a Python program to display a number in left, right
and center aligned of width 10.
"""
num5 = 18
print("\nOriginal Number: ", num5)
print("Left aligned (width 10)   :" + "{:< 10d}".format(num5))
print("Right aligned (width 10)  :" + "{:10d}".format(num5))
print("Center aligned (width 10) :" + "{:^10d}".format(num5))
