from typing import Tuple

from organism import Organism


class Animal(Organism):
    def __init__(self):
        pass

    def action(self):
        # każde zwierze w swojej turze przesuwa się na wybrane losowo, sąsiednie pole
        pass

    def multiplication(self):
        # zwierzęta w ramach metody kolizja jeżeli napotkają zwierzę tego samego gatunku nie zmieniają swego położenia
        # a obok nich pojawia się trzecie zwierzę tego samego gatunku.
        pass

    def movement_sanity_check(self, new_position: Tuple, world_reference: object) -> Tuple:
        """
        Checks if Char is not at the edge of the map and can move in the desired direction.
        :return: bool value
        """
        if new_position[0] <= 0 \
                or new_position[1] <= 0 \
                or new_position[0] > world_reference.n_axis \
                or new_position[1] > world_reference.m_axis:
            print('Nie można iść w tym kierunku, pozcyja nie zmieniona.')
        else:
            self.position = new_position

    def walk_in_desired_direction(self, direction: str, world_reference: object) -> Tuple:
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
