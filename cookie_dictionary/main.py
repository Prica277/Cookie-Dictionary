""" 
Filename: main.py
Author: Alex Price
Description: The bulk of the code running to make the project work.
"""
import utilities
import json
import cookie_dictionary

def main():
    # Create a menu of choices upon starting the program
    new_menu = """
    Here is your list of options:

        1 - Option 1: Pick a recipe
        2 - Option 2: Change measurements of a recipe
        3 - Option 3: Save a new recipe
        4 - Option 4: Quit
    """
    options = ("1", "2", "3", "4")
    choice = ""
    while choice != "4":
        choice = utilities.get_menu_choice(new_menu, options)
        if choice == "1":
            # opens up the main cookie dictionary to search from.
            #pick_recipe()
            print("\nWe're working hard to bring this function up and running! Why not try another function?")
        elif choice == "2":
            # opens a new file that allows the user to pick the recipe and then 
            # change the amount desired. It would then adjust the ingredient amounts accordingly.
            print("\nSorry, this function is still under construction! Why not try another function?")
        elif choice == "3":
            # edits the main cookie dictionary to add the newest recipe.
            print("\nWe're still hammering out the bugs in this function. Why not try another function?")
    if choice == "4":
        print("\nGoodbye!")

if __name__ == "__main__":
    main()