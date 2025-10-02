###############################################################################
#  Program Name   : ex11.py
#  Author         : saif elmebayad
#  Task           :This program defines a function that takes a name and age and prints a sentence about you.
###############################################################################

def about_me(name, age):
    print(f"My name is {name} and I am {age} years old.")

# Example usage:
your_name = input("Enter your name: ")
your_age = input("Enter your age: ")

about_me(your_name, your_age)
