"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user enters something
that is not a valid integer for either the numerator or the denominator
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters 0 as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, I can change the code to check that the denominator is not zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator cannot be zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")