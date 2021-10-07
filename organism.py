from typing import Tuple
from random import choice, randrange


class Organism:
    def __init__(self, world: object):
        self.world_reference = world
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
            print('Nie można iść w tym kierunku, pozycja nie zmieniona.')
        else:
            print(f'{self} moved to {new_position}')
            self.position = new_position

    # def move_in_desired_direction(self, world_reference: object, direction=None) -> None:
    #     """
    #     :param world_reference: world reference object for world dimensions check
    #     :param direction: str value of the direction
    #     :return: updated position
    #     """
    #     if not direction:
    #         direction = choice('news')
    #
    #     if direction == 'n':
    #         new_position = (self.position[0] + 1, self.position[1])
    #     elif direction == 's':
    #         new_position = (self.position[0] - 1, self.position[1])
    #     elif direction == 'e':
    #         new_position = (self.position[0], self.position[1] + 1)
    #     else:
    #         new_position = (self.position[0], self.position[1] - 1)
    #     self.movement_sanity_check(new_position, world_reference)

    def starting_position(self, world_reference: object) -> Tuple:
        return randrange(world_reference.n_axis) + 1, randrange(world_reference.m_axis) + 1
