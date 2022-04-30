from enum import Enum
from typing import List, Union

class Mark(Enum):
    HEART = 1
    DIAMOND = 2
    CLOVER = 3
    SPADE = 4


class Number(Enum):
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NIEN = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2
    ACE = 1


class Color(Enum):
    BLACK = 0
    RED = 1


class Card:
    def __init__(
        self,
        card_mark: Mark,
        card_color: Color,
        card_number: Number
    ) -> None:
        self.mark: Mark = card_mark
        self.color: Color = card_color
        self.number: Number = card_number

    @property
    def point(self) -> Union[int, List[int]]:
        if self.is_alphabet_card():
            return 10
        elif self.number == Number.ACE:
            return [1, 11]
        else:
            return self.number.value

    @property
    def number_name(self) -> str:
        if self.number == Number.KING:
            return "♚"
        elif self.number == Number.QUEEN:
            return "♛"
        elif self.number == Number.JACK:
            return "J"
        elif self.number == Number.ACE:
            return "A"
        else:
            return str(self.number.value)

    @property
    def mark_name(self) -> str:
        if self.mark == Mark.HEART:
            return "♥ (HEART)"
        elif self.mark == Mark.DIAMOND:
            return "♦ (DIAMOND)"
        elif self.mark == Mark.CLOVER:
            return "♣ (CLOVER)"
        elif self.mark == Mark.SPADE:
            return "♠ (SPADE)"

    @property
    def number_str(self) -> str:
        return str(self.number.value)

    @property
    def mark_str(self) -> str:
        if self.mark == Mark.HEART:
            return "♥"
        elif self.mark == Mark.DIAMOND:
            return "♦"
        elif self.mark == Mark.CLOVER:
            return "♣"
        elif self.mark == Mark.SPADE:
            return "♠"

    def is_alphabet_card(self) -> bool:
        return (self.number == Number.KING  or
                self.number == Number.QUEEN or
                self.number == Number.JACK)

    def __str__(self) -> str:
        return f"{self.mark_str}{self.number_str}"

    def __repr__(self) -> str:
        return f"{self.mark_name} {self.number_name}"
