from decklist import Decklist
from mtgsdk import Card

def deck_construction(deck):
    # Couple of print statements to check the decklist is being handled properly
    print(deck, "deck_cons")
    for i in deck.decklist:
        print(i.name)

    # Inputting the name of a card, searching for it, and adding to deccklist. Filtering out multiple, as we are ignoring which set the card is from for now
    def add_card():
        deck.add_to_decklist()
    def save_decklist():
        for card in deck:
            pass
        
    add_card()
