MENU = "G - Get a valid score\nP - Print result\nS - Show stars\nQ - Quit"

def main():
    print(MENU)
    choice = input(">>> ").upper()
    score = float(input("Enter score: "))