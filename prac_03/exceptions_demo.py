"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
    A ValueError happens if the user enters a non-numeric value, such as a string, instead of a number when a function
    that requires a number as an input.

2. When will a ZeroDivisionError occur?
    A ZeroDivisionError occurs when the user divides a number by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    To avoid the possibility of a ZeroDivisionError, we can add "except ZeroDivisionError" with using
    "try-except" function.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")