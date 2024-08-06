#https://github.com/MagicTheGathering/mtg-sdk-python
# Currently working towards a text based decklist builder. You will be able to add and remove cards, find out mana costs and colour identities, more features once this is all implemented
# Decklists will be saved as using just the multiverse_id, which is a unique 6 digit identifier for each card, and the fastest way to find each card. This allows the data saved to be much smaller

# Import classes from API, likely only going to be using Card, grabbing all now for testing
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

import sys

# Created a seperate decklist class, which deals with finding, adding and removing cards from the opened decklist
from decklist import Decklist
# Created a deck_construction function in a different file, to keep things tidy. this will handle most of the Decklist class calls
from deck_construction import deck_construction

def find_card():
    query = input("Please input a card name: ").title()

    try:
        # Currently provided the name, colour identity, mana cost and sets of card entered
        # Eventually we want to only return 1 card, not worried out sets for now. This is currently here so I can see all the results I need
        card = Card.where(name=query).all()

        # .all() retuns all cards that contain the entered word, whereas im looking for specific matches, which is the loop below
        for i in card:
            if i.name == query:
                print(i.name, i.colors, i.cmc, i.set, i.multiverse_id)
                print(i)

        print(f"The converted mana cost of {card[0].name} is {card[0].cmc}")
        return(card[0])

    # Index error means that the card wasnt found
    except IndexError:
        print("Card not found, please try again.")
        find_card()
    except Exception as error:
        print("Error: ", error)
    

def open_decklist():
    # If the input decklist exists in saved_decklists folder, open the file, then create a list using the multiverse_ids, which will be the decklist for class creation
    # Also passes the decklist name to the class
    decklist_name = input("Please input the name of the decklist: ")
    try:
        decklist_contents = []
        with open(f"saved_decklists\{decklist_name}.txt", "r") as file:
            for line in file:
                decklist_contents.append(line.strip())
        deck = Decklist(decklist_contents, decklist_name)

        print("Current Decklist: ")
        deck.show_current_decklist()
        print("Entering Deck Construction... ")
        deck_construction(deck)


    except Exception as error:
        print(error)

def new_decklist():
    # Creates a new blank list, and creates a class with no values yet
    # Decklist_name will also be a blank screen, as this can be chosen when saving
    pass

def show_saved_decklists():
    # Show the names of the decklists saved in saved_decklists folder
    pass

def delete_decklist():
    # Delete decklist from saved_decklists folder
    pass

def main():
    #find_card() # temp function here to test
    # Creating a basic menu, that allows the user to open previously saved decklists, create a new one, and add or remove cards from the decklists
    while True:
        menu_choice = int(input('''
    Please choose from the following options: 
        1. Open Decklist
        2. Create New Decklist
        3. Show Saved Decklists
        4. Delete Decklist
        9. Exit Program
    '''))

        if menu_choice == 1:
            open_decklist()
        elif menu_choice == 2:
            new_decklist()
        elif menu_choice == 3:
            show_saved_decklists
        elif menu_choice == 4:
            delete_decklist()
        elif menu_choice == 9:
            sys.exit("Exiting program")
        else:
            print("Invalid choice, please choose again")
        



main()