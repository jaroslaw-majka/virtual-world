from animal import Animal


class Fox(Animal):
    def __init__(self, world: object, creation_time: int):
        super().__init__(world, creation_time)
        self.strength = 3
        self.initiative = 7
        self.position = self.starting_position(self.world_reference)

    # TODO override action method
