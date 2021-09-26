from animal import Animal
from random import randrange


class Human(Animal):
    def __init__(self, world: object):
        self.strength = 5
        self.initiative = 4
        self.position = (randrange(world.n_axis), randrange(world.m_axis))
        self.world_reference = world

    def action(self):
        # Człowiek może przemieścić się jedynie na sąsiednie pole
        # ale kierunek jego ruchu definiowany jest przez uzytkownika poprzez wciśnięcie odpowiedniego klawisza
        action = self.movement_menu()
        print(action)

    def collision(self):
        # Człowiek będzie posiadał specjalną umiejętność, którą można aktywować
        # która będzie wpływała na sposób działania tej metody przez 5 tur
        # potem ta umiejętność przez kolejnych 5 tur będzie nieaktywna
        pass

    def movement_menu(self) -> str:
        print("1. Wykonaj ruch na sąsiednie pole")
        print("2. Uzyj umiejętności")
        menu_choice = input("Wybierz akcje:")
        if menu_choice == '1':
            return input('W krótym kierunku chcesz się poruszyć (n, e, w, s): ')
        elif menu_choice == '2':
            # TODO implement special skill method
            pass

    def movement_sanity_check(self) -> bool:
        # TODO Implement method
        '''
        Checks if Char is not at the edge of the map and can move in the desired direction.
        :return: bool value when user can
        '''
        return True