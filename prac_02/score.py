"""
CP1404/CP5632 - Practical

"""

def main():
    score = float(input("Enter score: "))
    print(determine_score(score))
    
def determine_score(score):
    if score < 0 or score > 100:
        return "Your score is invalid"
    elif score >= 90:
        return "Excellent!"
    elif score >= 50:
        return "Pass!"
    else:
        return "Bad!"

main()

# another main function with random
import random
def main():
    score = random.randint(0, 100)
    print(score)
    print(determine_result(score))

def determine_result(score):
    if score < 0 or score > 100:
        return "Your score is invalid"
    elif score >= 90:
        return "Excellent!"
    elif score >= 50:
        return "Pass!"
    else:
        return "Bad!"

main()