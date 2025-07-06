"""
Estimate = 15 minutes
Actual =
"""

from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 2506.80)
print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected 100. Got {guitar2.get_age()}")