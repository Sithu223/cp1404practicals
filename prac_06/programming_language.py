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

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.language_name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        return str(self)