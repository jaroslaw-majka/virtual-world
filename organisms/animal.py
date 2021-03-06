from organisms.organism import Organism
from random import choice


class Animal(Organism):
    def __init__(self, world: object, creation_time: int):
        super().__init__(world, creation_time)

    def action(self) -> None:
        """
        Default Organism movement during the turn
        """
        self.move_in_desired_direction(self.world_reference)

    def collision(self, encountered_organism):
        """
        Checks strength of both organisms and returns weaker one for deletion
        """
        # TODO Make below prints beauty!
        print(f'{self} at {self.position} encountered '
              f'{encountered_organism} at {encountered_organism.position}')
        if self.strength > encountered_organism.strength:
            print(f'{self} won!')
            return encountered_organism
        else:
            print(f'{encountered_organism} won!')
            return self

    def multiplication(self, possible_fields: list, world: object, creation_time: int) -> object:
        created_animal = self.__class__(world, creation_time)
        created_animal.position = choice(possible_fields)
        return created_animal

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
