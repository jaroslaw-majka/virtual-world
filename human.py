from typing import Tuple

from animal import Animal
from random import randrange


class Human(Animal):
    def __init__(self, world: object):
        self.strength = 5
        self.initiative = 4
        self.position = (randrange(world.n_axis) + 1, randrange(world.m_axis) + 1)
        self.world_reference = world

    def action(self):
        # Człowiek może przemieścić się jedynie na sąsiednie pole
        # ale kierunek jego ruchu definiowany jest przez uzytkownika poprzez wciśnięcie odpowiedniego klawisza
        action = self.movement_menu()
        self.walk_in_desired_direction(action)

    def collision(self):
        # Człowiek będzie posiadał specjalną umiejętność, którą można aktywować
        # która będzie wpływała na sposób działania tej metody przez 5 tur
        # potem ta umiejętność przez kolejnych 5 tur będzie nieaktywna
        pass

    def movement_menu(self) -> str:
        """
        Prints action menu for user to decide
        :return: str
        """
        print("1. Wykonaj ruch na sąsiednie pole")
        print("2. Użyj umiejętności")
        menu_choice = input("Wybierz akcje:")
        if menu_choice == '1':
            return input('W krótym kierunku chcesz się poruszyć (n, e, w, s): ')
        elif menu_choice == '2':
            # TODO implement special skill method
            pass

    def movement_sanity_check(self, new_position: Tuple) -> Tuple:
        """
        Checks if Char is not at the edge of the map and can move in the desired direction.
        :return: bool value
        """
        if new_position[0] <= 0 \
                or new_position[1] <= 0 \
                or new_position[0] > self.world_reference.n_axis \
                or new_position[1] > self.world_reference.m_axis:
            print('Nie można iść w tym kierunku, pozcyja nie zmieniona.')
        else:
            self.position = new_position

    def walk_in_desired_direction(self, direction: str) -> Tuple:
        """
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
        self.movement_sanity_check(new_position)
        print(self.position)
