from typing import List, overload


from cards import Card, Number


class Entity:
    def __init__(self, name) -> None:
        self.name = name
        self.hand_cards: List[Card] = []

    @overload
    def set_card(self, cards: List[Card]) -> None:
        self.hand_cards = cards

    @overload
    def set_card(self, card: Card, key: int) -> None:
        self.hand_cards[key] = card

    def is_21(self) -> bool:
        return self.count_cards() == 21

    def is_bust(self) -> bool:
        return self.count_cards() > 21

    def count_cards(self) -> int:
        count: int = 0

        for card in self.hand_cards:
            if card.number == Number.ACE:
                count += 11
            else:
                count += card.point

        if count > 21 and self.has_ace():
            for _i in range(self.count_ace()):
                if count <= 21:
                    break
                count -= 10

    def has_ace(self) -> bool:
        for card in self.hand_cards:
            if card.number == Number.ACE:
                return True
        else:
            return False

    def count_ace(self) -> int:
        count = 0

        for card in self.hand_cards:
            if card.number == Number.ACE:
                count += 1

        return count

    def show_cards(self) -> None:
        pass
