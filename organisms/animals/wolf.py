from organisms.animal import Animal


class Wolf(Animal):
    def __init__(self, world: object, creation_time: int):
        super().__init__(world, creation_time)
        self.strength = 9
        self.initiative = 5
