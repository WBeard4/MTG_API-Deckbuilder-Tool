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
                print(self.decklist[count])

    def save_decklist(self, card):
        with open(f"saved_decklists\\{self.decklist_name}.txt", "a") as file:
            file.write(card.id + '\n')

    def add_to_decklist(self):
        while True:
            card_to_add = input("Please input the name of the card you would like to add: ").title().strip()
            try:
                print(f"Searching for {card_to_add}")
                cards = Card.where(name=card_to_add).all()
                print(f"Found {len(cards)} cards")
                card_added = False
                for card in cards:
                    try:
                        if card.name == card_to_add:
                            print(card.name)
                            print(card.set)
                            print(card.id)
                            self.decklist.append(card)
                            self.save_decklist(card)
                            print(f"{card.name} added to decklist")
                            card_added = True
                            break

                        else:
                            print(f"Similar card found: {card.name}, {card.set}")
                    except AttributeError as e: # Some versions dont have a multiverse_id, so this will skip those
                        print(f"Attribute error {e}")
                        continue
                    except Exception as error:
                        print("Decklist.add_to_decklist error:", error)
            except:
                print("it broke")
            
            if card_added:
                break
            else:
                print(f"Unable to find {card_to_add}, please try again and make sure the card is entered correctly")

    def remove_from_decklist():
        pass

    def show_current_decklist(self):
        for card in self.decklist:
            print(card.name)

