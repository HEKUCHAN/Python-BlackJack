from .entity import Entity


class Player(Entity):
    def __init__(self, name, money) -> None:
        super().__init__(name)
        self.money: int = money