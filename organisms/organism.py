from typing import Tuple
from random import randrange
from random import choice


class Organism:
    def __init__(self, world: object, creation_time: int, position=None):
        self.world_reference = world
        self.creation_time = creation_time
        self.position = self.set_position(position)

    def action(self) -> None:
        """Default Organism movement during the turn"""
        proposed_position = self.proposed_position(self.world_reference)
        if self.field_free(self.world_reference, proposed_position):
            print(f'{self} moved from {self.position} to {proposed_position}')
            self.position = proposed_position
        else:
            print('Position occupied.')
            # TODO 3. If occupied trigger collision method

    # TODO Use decorator for position setter and getter
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

    def proposed_position(self, world_reference: object, direction=None) -> Tuple:
        def map_range_check(proposed_position) -> Tuple:
            if not proposed_position:
                return False
            elif proposed_position[0] <= 0 \
                    or proposed_position[1] <= 0 \
                    or proposed_position[0] > world_reference.n_axis \
                    or proposed_position[1] > world_reference.m_axis:
                return False
            else:
                return proposed_position

        def propose_position(move_direction) -> Tuple:
            if not move_direction:
                move_direction = choice('news')

            if move_direction == 'n':
                new_position = (self.position[0] + 1, self.position[1])
            elif move_direction == 's':
                new_position = (self.position[0] - 1, self.position[1])
            elif move_direction == 'e':
                new_position = (self.position[0], self.position[1] + 1)
            else:
                new_position = (self.position[0], self.position[1] - 1)
            return new_position

        possible_new_position = None
        if direction:
            return map_range_check(propose_position(direction))
        else:
            while not map_range_check(possible_new_position):
                possible_new_position = propose_position(direction)
        return possible_new_position

    def field_free(self, world_reference: object, proposed_position: Tuple) -> object:
        for idx in range(len(world_reference.organisms_list)):
            if proposed_position == world_reference.organisms_list[idx].position:
                return world_reference.organisms_list[idx]
