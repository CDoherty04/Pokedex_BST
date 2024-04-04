class Pokemon:

    def __init__(self, us_name, jap_name, pokemon_id):
        """Create a Pokémon object with a US name, Japanese name, and Pokédex number."""
        self.US_name = us_name
        self.JAP_name = jap_name
        self.id = pokemon_id

    def __gt__(self, other):
        if isinstance(other, int):
            return self.id > other
        return self.id > other.id

    def __lt__(self, other):
        if isinstance(other, int):
            return self.id < other
        return self.id < other.id

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        return self.id == other.id

    def __repr__(self):
        return f"US_name={self.US_name}, Japanese_name={self.JAP_name}, id={self.id}"
