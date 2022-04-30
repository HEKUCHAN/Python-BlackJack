from .entity import Entity


class Dealer(Entity):
    def __init__(self, name) -> None:
        super().__init__(name)

    def is_more_17(self) -> bool:
        return self.count_cards() >= 17

    def show_cards() -> None:
        pass

    def show_all_cards() -> None:
        pass
