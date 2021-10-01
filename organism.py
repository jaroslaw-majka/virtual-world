from typing import Tuple
from random import choice, randrange


class Organism:
    def __init__(self, world: object):
        self.strength = None
        self.initiative = None
        self.position = self.starting_position(self.world_reference)
        self.world_reference = world

    def action(self):
        """
        Default Organism movement during the turn
        """
        self.move_in_desired_direction(choice('news'), self.world_reference)

    def collision(self, encountered_organism):
        """
        Checks strength of both organisms and returns stronger one - this is default solution
        :param encountered_organism: object of encounteres organism
        :return: object of winning organism
        """
        # TODO Make below prints beauty!
        print(f'{self} encountered {encountered_organism}')
        if self.strength > encountered_organism.strength:
            print(f'{self} won!')
            return self
        else:
            print(f'{encountered_organism} won!')
            return encountered_organism

    def movement_sanity_check(self, new_position: Tuple, world_reference: object) -> Tuple:
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
            self.position = new_position

    def move_in_desired_direction(self, direction: str, world_reference: object) -> Tuple:
        """
        :param world_reference: world reference object for world dimensions check
        :param direction: str value of the direction
        :return: updated position
        """
        if direction == 'n':
            new_position = (self.position[0] + 1, self.position[1])
        elif direction == 's':
            new_position = (self.position[0] - 1, self.position[1])
        elif direction == 'e':
            new_position = (self.position[0], self.position[1] + 1)
        elif direction == 'w':
            new_position = (self.position[0], self.position[1] - 1)
        self.movement_sanity_check(new_position, world_reference)
        print(self.position)

    def starting_position(self, world_reference):
        return randrange(world_reference.n_axis) + 1, randrange(world_reference.m_axis) + 1
