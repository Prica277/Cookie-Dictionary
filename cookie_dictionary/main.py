""" 
Filename: main.py
Author: Alex Price
Description: The bulk of the code running to make the project work.
"""
import utilities
import json
from cookie_recipes import recipes

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
            pick_recipe()
            # print("\nWe're working hard to bring this function up and running! Why not try another function?")
        elif choice == "2":
            # opens a new file that allows the user to pick the recipe and then 
            # change the amount desired. It would then adjust the ingredient amounts accordingly.
            print("\nSorry, this function is still under construction! Why not try another function?")
        elif choice == "3":
            # edits the main cookie dictionary to add the newest recipe.
            print("\nWe're still hammering out the bugs in this function. Why not try another function?")
    if choice == "4":
        print("\nGoodbye!")

def pick_recipe():
    """opens up the main cookie dictionary to search from."""
    
    print("\nHere's all the recipies you currently have to pick from: ")
    for cookie in recipes.keys():
        print("\n" + cookie)
    
    # gets the user's input and converts it into the style that the dictionary is named so that the code can find it.
    user_cookie = input("Enter the cookie type you're looking for! Be sure to spell it correctly: ")
    user_cookie = user_cookie.lower()
    user_recipe = ""
    for i in range(len(user_cookie)):
        if user_cookie[i] == " ":
            user_recipe = user_recipe + "_"
        else:
            user_recipe = user_recipe + user_cookie[i]
    print("You chose " + user_recipe + ". Is this right?")
    cont = input("Y/N: ")
    cont = cont.upper()
    if cont == "N":
        #loops through the entire process again and returns to this check.
        pick_recipe()
    elif cont == "Y": 
        print("Hooray!")
        #continues to the next step.
        display_recipe(user_recipe, recipes)
    else:
        print("Sorry, you've encountered an error. Please try again.")
        pick_recipe()

def display_recipe(user_recipe, recipes):
    recipe = recipes.get(user_recipe)
    if recipe:
        for key, value in recipe.items():
            print(key + ": " + value)

if __name__ == "__main__":
    main()