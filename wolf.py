from animal import Animal


class Wolf(Animal):
    def __init__(self, world: object, creation_time: int):
        self.strength = 9
        self.initiative = 5
        self.creation_time = creation_time
        self.world_reference = world
        self.position = self.starting_position(self.world_reference)
