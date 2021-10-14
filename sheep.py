from animal import Animal


class Sheep(Animal):
    def __init__(self, world: object, creation_time: int):
        super().__init__(world, creation_time)
        self.strength = 4
        self.initiative = 4
