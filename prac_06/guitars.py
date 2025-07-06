"""
Estimate = 20 minutes
Actual =
"""

from prac_06.guitar import Guitar
def main():
    guitars = []
    name = input("Name: ").title()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
