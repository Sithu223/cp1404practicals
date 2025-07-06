"""
Estimate = 15 minutes
Actual =
"""

class ProgrammingLanguage:
    """Represent information about a programming language."""
    def __init__(self, language_name, typing, reflection, year=0):
        """Create a ProgrammingLanguage from given values."""
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year