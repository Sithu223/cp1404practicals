"""
Estimate = 20 minutes
Actual =
"""

import datetime
from prac_07.project import Project

MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new projects\n(U)pdate"\
        "project\n(Q)uit")
FILENAME = "projects.txt"
projects = []

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects(FILENAME)
        elif choice == "S":
            save_projects(FILENAME)
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_projects()
        elif choice == "U":
            update_projects()
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """Read the file, load projects data, and store as a list."""
    with open(filename, "r") as file:
        file.readline()
        for line in file:
            name, start_date, priority, cost_estimate, completion = line.strip().split("\t")
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion)))