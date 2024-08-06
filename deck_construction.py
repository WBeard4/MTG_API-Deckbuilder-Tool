# This function will mostly call the class functions, and provide a menu to add and remove cards

from decklist import Decklist
from mtgsdk import Card

def deck_construction(deck):
    # Couple of print statements to check the decklist is being handled properly
    '''print(deck, "deck_cons")
    for i in deck.decklist:
        print(i.name)'''

    # Inputting the name of a card, searching for it, and adding to deccklist. Filtering out multiple, as we are ignoring which set the card is from for now
    def add_card():
        deck.add_to_decklist()

    while True:    
        menu_choice = int(input('''
    Please choose from the following options: 
        1. Add card to Decklist
        2. Remove card from decklist
        3. Show current decklist
        9. Exit to main menu
    '''))

        if menu_choice == 1:
            add_card()
        elif menu_choice == 3:
            print(f"Current Decklist - {deck.decklist_name}")
            for card in deck.decklist:
                print(card.name)
        elif menu_choice == 9:
            break
        else:
            print("Invalid choice, please choose again")
