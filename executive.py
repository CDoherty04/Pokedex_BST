from bst import BST
from pokemon import Pokemon


def print_menu():
    """Prints the menu options"""
    choice = input("\nChoose one of the following:\n"
                   "1) Add\n"
                   "2) Search\n"
                   "3) Print\n"
                   "4) Remove\n"
                   "5) Copy\n"
                   "6) Quit\n")
    return choice


class Executive:

    def __init__(self):
        """Creates the initial Binary Search Tree"""
        self.pokedex = BST()

    def add(self):
        """User input determines the attributes of the added Pokémon to the Pokédex"""
        us_name = input("What is the US name: ")
        jap_name = input("What is the Japanese name: ")
        ssn = input("What is the Pokedex number: ")

        new_pokemon = Pokemon(us_name, jap_name, ssn)
        try:
            self.pokedex.add(new_pokemon)
        except ValueError:
            print("Cannot add duplicates")

    def search(self):
        """Prompt the user for their SSN. Either print all information OR tell the user that the Pokémon doesn't exist.
        The program should not crash if an id causes your BST to raise an exception."""
        pass

    def ordered_print(self):
        """Prints the tree in a user-specified order"""

        while True:
            order = input("Which order would you like to print in?\n"
                          "1) Pre Order\n"
                          "2) In Order\n"
                          "3) Post Order\n")

            print()

            # List of nodes that are taken in a certain order to be printed later
            pokemon = []

            if order == "1":
                self.pokedex.preorder(pokemon.append)
                break
            elif order == "2":
                self.pokedex.inorder(pokemon.append)
                break
            elif order == "3":
                self.pokedex.postorder(pokemon.append)
                break
            else:
                print("That is not a valid option, enter 1, 2, or 3.")

        for _pokemon in pokemon:
            print(str(_pokemon))

    def remove(self):
        """Given a Pokédex number, remove that entry from the BST. When removing, the maximum value
        from the target's LST should be the replacement candidate """
        pass

    def copy(self):
        """Creates a deep copy of the BST. The user can only select this option once.
        If the user tries to make multiple copies, issue a message stating that a copy already exists.
        Once the user makes a copy, ask which tree they wish to use each subsequent time they request an
        Add, Search, or Remove operation"""
        pass

    def run(self):
        """Runs the program through the Executive class"""
        while True:
            choice = print_menu().lower()
            print()

            match choice:
                case "1": self.add()
                case "add": self.add()
                case "2": self.search()
                case "search": self.search()
                case "3": self.ordered_print()
                case "print": self.ordered_print()
                case "4": self.remove()
                case "remove": self.remove()
                case "5": self.copy()
                case "copy": self.copy()
                case "6": quit()
                case "quit": quit()
                case _: print("That is an invalid option")
