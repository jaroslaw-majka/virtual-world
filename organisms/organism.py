from typing import Tuple
from random import randrange
from random import choice


class Organism:
    def __init__(self, world: object, creation_time: int, position=None):
        self.world_reference = world
        self.creation_time = creation_time
        self.position = self.set_position(position)

    def action(self) -> None:
        """
        Default Organism movement during the turn
        """
        self.move_in_desired_direction(self.world_reference)

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
        def free_fields_available() -> bool:
            world_size = world_reference.n_axis * world_reference.m_axis
            return world_size != len(world_reference.organisms_list)

        def list_of_free_fields() -> list:
            return [(n_position + 1, m_position + 1)
                    for n_position in range(world_reference.n_axis)
                    for m_position in range(world_reference.m_axis)
                    if (n_position + 1, m_position + 1) not in
                    [organism.position for organism in world_reference.organisms_list]]

        if free_fields_available():
            return choice(list_of_free_fields())
        else:
            return randrange(world_reference.n_axis) + 1, randrange(world_reference.m_axis) + 1

    def set_position(self, position):
        if position:
            return position
        else:
            return self.starting_position(self.world_reference)

    def move_in_desired_direction(self, world_reference: object, direction=None) -> None:
        """
        :param world_reference: world reference object for world dimensions check
        :param direction: str value of the direction
        :return: updated position
        """
        if not direction:
            direction = choice('news')

        if direction == 'n':
            new_position = (self.position[0] + 1, self.position[1])
        elif direction == 's':
            new_position = (self.position[0] - 1, self.position[1])
        elif direction == 'e':
            new_position = (self.position[0], self.position[1] + 1)
        else:
            new_position = (self.position[0], self.position[1] - 1)
        self.movement_sanity_check(new_position, world_reference)
