class Pokemon:

    def __init__(self, us_name, jap_name, ssn):
        """Create a Pokémon object with a US name, Japanese name, and Pokédex number."""
        self.US_name = us_name
        self.JAP_name = jap_name
        self.SSN = ssn

    def __gt__(self, other):
        return self.SSN > other.SSN

    def __lt__(self, other):
        return self.SSN < other.SSN

    def __eq__(self, other):
        return self.SSN == other.SSN

    def __str__(self):
        return f"{self.US_name}, {self.JAP_name}, {self.SSN}"
