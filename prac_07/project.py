"""
Estimate = 20 minutes
Actual =
"""

class Project:
    """Represent information about a project."""
    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, completion_percentage=0):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

