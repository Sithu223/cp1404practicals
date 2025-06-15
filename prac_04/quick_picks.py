import random

from kivy.input.providers.probesysfs import get_inputs

MIN_VALUE = 1
MAX_VALUE = 45
NUMBERS_PER_LINE = 6

def main():
    number_of_quick_picks = get_input()
    for i in range(number_of_quick_picks):
        quick_picks = generate_quick_picks()
        display_quick_picks(quick_picks)

def get_input():
    number_of_quick_picks = int(input("How many quick picks? "))
    return number_of_quick_picks

def generate_quick_picks():
    numbers = []