"""
Estimate = 30 minutes
Actual = 27 minutes
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50

class Guitar:
    """Represent information about guitar."""
    def __init__(self, name, year=0, cost=0):
        """Create a Guitar from the given values"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __repr__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculate how old the guitar is in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine whether a guitar is vintage or not."""
        if self.get_age() >= VINTAGE_AGE:
            return True
        else:
            return False

    def __lt__(self, other):
        """Sort the list of guitars by released year."""
        return self.year < other.year

def read_guitars_from_file(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)

def main():
    guitars = read_guitars_from_file('guitars.csv')
    print("Guitars:")
    display_guitars(guitars)
    # Sort guitars by year
    guitars.sort()
    print("\nSorted guitars (oldest to newest):")
    display_guitars(guitars)

if __name__ == "__main__":
    main()