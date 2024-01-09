import random


class Deck:
    def __init__(self, suits: list=["♥", "♣", "♦", "♠"], values: list=range(1, 14)) -> None:
        self.suits = suits
        self.values = values
        self.cards = []

        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(self, suit, value)) #* Adds cards for each of the suits and values
    
    def display_deck(self, sorted: bool=False) -> str:
        line_index = -1
        last_suit = None
        if sorted: #* Checks for a sorted list
            to_return  = [""]*len(self.suits) #* Makes an empty list with all the suits
            for card in self.cards:
                if card.suit != last_suit:
                    line_index += 1
                    last_suit = card.suit #* Sets the old suit to the new one
                else:
                    to_return[line_index] += ", "

                to_return[line_index] += str(card)

            tto_return = ""
            for line in to_return:
                tto_return += f"{line}\n" #* #Converts the list to a string
            to_return = tto_return
        else:
            to_return  = ""
            for card in self.cards:
                to_return += f"{str(card)}" if self.cards.index(card) == len(self.cards)-1 else f"{str(card)}, " #* Adds a comma if it's not the last in its section
        
        return to_return
    
    def shuffle(self):
        random.shuffle(self.cards)

class Card:
    def __init__(self, deck: Deck, suit: str=None, value: int=None) -> None:
        if suit == None and value == None:
            self.suit = random.choice(deck.suits)
            self.value = random.choice(deck.values)
        else:
            self.suit = suit
            self.value = value

    def __str__(self) -> str:
        return f"{self.suit}{self.value}"

if __name__ == "__main__":
    deck_2 = Deck()
    print(deck_2.display_deck(True))
    deck_2.shuffle()
    print(deck_2.display_deck())
