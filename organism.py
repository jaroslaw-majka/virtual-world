from typing import Tuple
from random import choice, randrange


class Organism:
    def __init__(self, world: object, creation_time: int):
        self.world_reference = world
        self.creation_time = creation_time
        self.position = self.starting_position(self.world_reference)

    def movement_sanity_check(self, new_position: Tuple, world_reference: object) -> None:
        """
        Checks if Char is not at the edge of the map and can move in the desired direction.
        :return: bool value
        """
        if new_position[0] <= 0 \
                or new_position[1] <= 0 \
                or new_position[0] > world_reference.n_axis \
                or new_position[1] > world_reference.m_axis:
            print(f'{self} tried to make an invalid move. Position remains unchanged')
        else:
            print(f'{self} moved to {new_position}')
            self.position = new_position

    def starting_position(self, world_reference: object) -> Tuple:
        return randrange(world_reference.n_axis) + 1, randrange(world_reference.m_axis) + 1
