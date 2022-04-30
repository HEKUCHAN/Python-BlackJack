from typing import List
from functools import singledispatchmethod


from cards import Card, Number


class Entity:
    def __init__(self, name) -> None:
        self.name = name
        self.hand_cards: List[Card] = []

    def push_card(self, card: Card) -> None:
        self.hand_cards.append(card)

    @singledispatchmethod
    def set_cards(self, cards: List[Card]) -> None:
        self.hand_cards = cards

    @set_cards.register
    def _selected_set_card_(self, card: Card, key: int) -> None:
        self.hand_cards[key] = card

    def clear_card(self) -> None:
        self.hand_cards.clear()

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

        return count

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
        print()
        print(f"{self.name}のカード:")
        cards_list: List[str] = []
        for card in self.hand_cards:
            card_string: str = f"[ {card.mark_str}{card.number_name} ]"
            cards_list.append(card_string)

        print(" ".join(cards_list), f"({self.count_cards()})")
