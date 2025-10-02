###############################################################################
#  Program Name   : ex7.py
#  Author         : saif elmebayad
#  Task           : This program asks the user for two numbers and prints the larger number.
###############################################################################

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"The larger number is {num1}")
elif num2 > num1:
    print(f"The larger number is {num2}")
else:
    print("Both numbers are equal")



