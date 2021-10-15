from organisms.animal import Animal


class Antelope(Animal):
    def __init__(self, world: object, creation_time: int):
        super().__init__(world, creation_time)
        self.strength = 4
        self.initiative = 4

    # TODO Override action and collision methods
