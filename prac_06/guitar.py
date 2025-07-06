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