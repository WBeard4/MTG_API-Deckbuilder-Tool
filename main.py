#https://github.com/MagicTheGathering/mtg-sdk-python

# Import classes from API
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

query = input("Please input a card name: ").title()

try:
    # Currently provided the name, colour identity, mana cost and sets of card entered
    card = Card.where(name=query).all()
    for i in card:
        if i.name == query:
            print(i.name, i.colors, i.cmc, i.set)

    print(f"The converted mana cost of {card} is {card.cmc}")

except Exception as error:
    print("Error: ", error)
