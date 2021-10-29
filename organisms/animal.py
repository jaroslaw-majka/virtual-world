from organisms.organism import Organism
from random import choice


class Animal(Organism):
    def __init__(self, world: object, creation_time: int):
        super().__init__(world, creation_time)

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
