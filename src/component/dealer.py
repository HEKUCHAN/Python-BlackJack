from typing import List



from .entity import Entity
from cards import Card, Number


class Dealer(Entity):
    def __init__(self, name) -> None:
        super().__init__(name)

    @property
    def hide_hand_cards(self) -> List[Card]:
        return self.hand_cards[:self.cards_len - 1]

    @property
    def cards_len(self) -> int:
        return len(self.hand_cards)

    def is_more_17(self) -> bool:
        return self.count_cards() >= 17

    def hide_count_cards(self) -> int:
        count: int = 0

        for card in self.hide_hand_cards:
            if card.number == Number.ACE:
                count += 11
            else:
                count += card.point

        if count > 21 and self.hide_has_ace():
            for _i in range(self.hide_count_ace()):
                if count <= 21:
                    break
                count -= 10

        return count

    def hide_has_ace(self):
        for card in self.hide_hand_cards:
            if card.number == Number.ACE:
                return True
        else:
            return False

    def hide_count_ace(self):
        count = 0

        for card in self.hide_hand_cards:
            if card.number == Number.ACE:
                count += 1

        return count

    def show_cards(self) -> None:
        print(f"{self.name}のカード:")
        cards_list: List[str] = []

        for card in self.hide_hand_cards:
            card_string: str = f"[ {card.mark_str}{card.number_name} ]"
            cards_list.append(card_string)

        cards_list.append("[ * ]")

        print(
            " ".join(cards_list),
            f"({self.hide_count_cards()})"
        )

    def show_all_cards(self) -> None:
        print(f"{self.name}のカード:")
        cards_list: List[str] = []

        for card in self.hand_cards:
            card_string: str = f"[ {card.mark_str}{card.number_name} ]"
            cards_list.append(card_string)

        print(
            " ".join(cards_list),
            f"({self.count_cards()})"
        )
