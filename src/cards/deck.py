import random
from typing import Any, List


from cards import Card, Mark, Number, Color


class Deck:
    def __init__(self):
        self.cards: List[Card] = self.create_deck()

    def first_draw(self) -> List[Card]:
        first_card: Card = self.draw()
        second_card: Card = self.draw()

        return [first_card, second_card]

    def draw(self) -> Card:
        deck_length: int = len(self.cards)

        random_number = random.randrange(deck_length)
        random_card: Card = self.cards[random_number]

        self.cards.remove(random_card)

        return random_card

    def shuffle(self) -> None:
        self.cards = random.shuffle(self.cards)

    @classmethod
    def shuffle(cls, cards: List[Any]) -> List[Card]:
        return random.shuffle(cards)

    @classmethod
    def create_deck(cls) -> List[Card]:
        cards_list: List[Card] = []

        for mark in Mark:
            for num in Number:
                if num == Mark.CLOVER or num == Mark.SPADE:
                    card = Card(
                        card_number=num,
                        card_mark=mark,
                        card_color=Color.BLACK
                    )
                else:
                    card = Card(
                        card_number=num,
                        card_mark=mark,
                        card_color=Color.RED
                    )

                cards_list.append(card)

        cls.shuffle(cards_list)

        return cards_list
