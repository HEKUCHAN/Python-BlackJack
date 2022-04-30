from .entity import Entity


class Player(Entity):
    def __init__(self, name) -> None:
        super().__init__(name)
