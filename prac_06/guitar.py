"""
Estimate = 30 minutes
Actual =
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
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __repr__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"
