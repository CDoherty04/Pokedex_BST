from bst import BST
from pokemon import Pokemon


def print_menu():
    """Prints the menu options"""
    choice = input("\nChoose one of the following:\n"
                   "1) Add\n"
                   "2) Print\n"
                   "3) Quit\n")
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

    def run(self):
        """Runs the program through the Executive class"""
        while True:
            choice = print_menu().lower()
            print()

            match choice:
                case "1":
                    self.add()
                case "add":
                    self.add()
                case "2":
                    self.ordered_print()
                case "print":
                    self.ordered_print()
                case "3":
                    quit()
                case "quit":
                    quit()
                case _:
                    print("That is an invalid option")
