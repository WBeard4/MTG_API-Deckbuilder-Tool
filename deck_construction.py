from decklist import Decklist
from mtgsdk import Card

def deck_construction(deck):
    print(deck, "deck_cons")
    for i in deck.decklist:
        print(i.name)