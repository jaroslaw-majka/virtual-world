from animal import Animal


class Fox(Animal):
    def __init__(self, world: object, creation_time: int):
        self.strength = 3
        self.initiative = 7
        self.creation_time = creation_time
        self.world_reference = world
        self.position = self.starting_position(self.world_reference)

    # TODO override action method
