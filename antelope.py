from animal import Animal


class Antelope(Animal):
    def __init__(self, world: object, creation_time: int):
        self.strength = 4
        self.initiative = 4
        self.creation_time = creation_time
        self.world_reference = world
        self.position = self.starting_position(self.world_reference)

    # TODO Override action and collision methods
