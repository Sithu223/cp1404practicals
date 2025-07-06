"""
Estimate = 30 minutes
Actual =
"""

CURRENT_YEAR = 2025
VINTAGE_YEAR = 50

class Guitar:
    """Represent information about guitar."""
    def __init__(self, name, year = 0, cost = 0):
        """Create a Guitar from given values"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __repr__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculate how old the guitar is in years."""
        return CURRENT_YEAR - self.year