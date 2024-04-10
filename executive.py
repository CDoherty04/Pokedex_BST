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


def choose_tree():
    """Gets user input to decide whether to manipulate the main tree or the copied tree"""

    while True:

        # Get valid input for which tree should be used
        tree = input("Would you like to add to the (1) main tree or (2) the copy? ")

        if tree == "main" or tree == "main tree" or tree == "1":
            return "main"
        elif tree == "copy" or tree == "the copy" or tree == "2":
            return "copy"

        # Only break when valid input is given
        else:
            print("That's an invalid input, try typing '1' or '2'")


class Executive:

    def __init__(self):
        """Creates the initial Binary Search Tree"""
        self.pokedex = BST()
        self.copy = None

    def add(self):
        """User input determines the attributes of the added Pokémon to the Pokédex"""

        # Mark which tree is being manipulated by default
        tree = "main"

        # If a copy exists choose which tree should be manipulated
        if self.copy:
            tree = choose_tree()

        us_name = input("What is the US name: ")
        jap_name = input("What is the Japanese name: ")

        while True:
            try:
                pokemon_id = int(input("What is the Pokedex number: "))
            except ValueError:
                print("\nThe Pokedex number was invalid.\n")
                continue

            try:
                new_pokemon = Pokemon(us_name, jap_name, pokemon_id)
                if tree == "main":
                    self.pokedex.add(new_pokemon)
                else:
                    self.copy.add(new_pokemon)
                break
            except ValueError:
                print("\nCannot add duplicates\n")

    def search(self):
        """Prompt the user for an id. Either print all information OR tell the user that the Pokémon doesn't exist.
        The program should not crash if an id causes your BST to raise an exception."""

        # Mark which tree is being manipulated by default
        tree = "main"

        # If a copy exists choose which tree should be manipulated
        if self.copy:
            tree = choose_tree()

        try:
            given_id = int(input("Which Pokemon ID are you searching for: "))

            try:
                if tree == "main":
                    print(self.pokedex.search(given_id))
                else:
                    print(self.copy.search(given_id))
            except KeyError:
                print("That Pokemon doesn't seem to exist")
            except AttributeError:
                print("That Pokemon doesn't exist in the Pokedex")

        except ValueError:
            print("Pokedex numbers use integers, that input is not valid")

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
            print(_pokemon)

    def remove(self):
        """Given a Pokédex number, remove that entry from the BST. When removing, the maximum value
        from the target's LST should be the replacement candidate """

        # Mark which tree is being manipulated by default
        tree = "main"

        # If a copy exists choose which tree should be manipulated
        if self.copy:
            tree = choose_tree()

        try:
            if tree == "main":
                self.pokedex.remove(int(input("Enter a Pokemon number to remove: ")))
            else:
                self.copy.remove(int(input("Enter a Pokemon number to remove: ")))

        except ValueError:
            print("Invalid input, enter an integer")

    def copy_tree(self):
        """Creates a deep copy of the BST. The user can only select this option once.
        If the user tries to make multiple copies, issue a message stating that a copy already exists.
        Once the user makes a copy, ask which tree they wish to use each subsequent time they request an
        Add, Search, or Remove operation"""

        # Only allow one copy
        if self.copy:
            print("A copy already exists")
        else:
            self.copy = self.pokedex.copy()
            if self.copy:
                print("A copy was successfully made")
            else:
                print("Nothing to copy")

    def run(self):
        """Runs the program through the Executive class"""

        # Have the user enter an input file
        input_file = input("File name: ")

        # Invalid file names will automatically raise an error
        with open(input_file, "r") as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines]

        for line in lines:
            # Add each Pokémon in the given file to the Pokédex
            self.pokedex.add(Pokemon(line.split("\t")[0], line.split("\t")[2], int(line.split("\t")[1])))

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
                case "5": self.copy_tree()
                case "copy": self.copy_tree()
                case "6": quit()
                case "quit": quit()
                case _: print("That is an invalid option")
