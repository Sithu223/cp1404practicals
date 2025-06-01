"""
CP1404/CP5632 - Practical
"""

import random

def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Your score is invalid!")
        score = float(input("Enter score: "))

    result = determine_score(score)
    print(result)
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    random_result = determine_score(random_score)
    print(random_result)

def determine_score(score):
    if score >= 90:
        return "Excellent!"
    elif score >= 50:
        return "Passable!"
    else:
        return "Bad!"

main()

