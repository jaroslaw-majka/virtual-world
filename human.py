from animal import Animal
from random import randrange


class Human(Animal):
    def __init__(self, world: object, creation_time):
        self.strength = 5
        self.initiative = 4
        self.world_reference = world
        self.position = self.starting_position(self.world_reference)
        self.creation_time = creation_time

    def action(self):
        # Człowiek może przemieścić się jedynie na sąsiednie pole
        # ale kierunek jego ruchu definiowany jest przez uzytkownika poprzez wciśnięcie odpowiedniego klawisza
        action = self.movement_menu()
        if action in 'news':
            self.move_in_desired_direction(self.world_reference, action)

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
        print("3. Zakończ grę")
        menu_choice = input("Wybierz akcje: ")
        if menu_choice == '1':
            return input('W krótym kierunku chcesz się poruszyć (n, e, w, s): ')
        elif menu_choice == '2':
            # TODO implement special skill method
            pass
        elif menu_choice == '3':
            quit()
