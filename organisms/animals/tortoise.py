from organisms.animal import Animal


class Tortoise(Animal):
    def __init__(self, world: object, creation_time: int):
        super().__init__(world, creation_time)
        self.strength = 2
        self.initiative = 1

    # TODO Override action and collision methods
