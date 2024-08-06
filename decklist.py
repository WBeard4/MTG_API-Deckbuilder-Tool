from mtgsdk import Card

class Decklist:
    def __init__(self, decklist, decklist_name):
        self.decklist = decklist
        self.decklist_name = decklist_name

        # This will convert the cards from the multiverse_id to the Card class from mtgsdk,if the decklist is a previously saved decklist
        if self.decklist != []:
            print(self.decklist)
            for count, card in enumerate(self.decklist):
                self.decklist[count] = Card.find(card) 

    def add_to_decklist():
        pass

    def remove_from_decklist():
        pass

    def show_current_decklist(self):
        for card in self.decklist:
            print(card.name)

    def save_decklist():
        pass