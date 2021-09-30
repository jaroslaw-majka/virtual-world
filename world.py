from human import Human
from wolf import Wolf
from sheep import Sheep
from fox import Fox
from tortoise import Tortoise
from antelope import Antelope


class World:
    organisms_list = []
    
    def __init__(self):
        self.n_axis = None
        self.m_axis = None
        self.turn_since_start = 0
        self.main()

    def make_a_turn(self):
        # Sprawi, że organizmy wykonają swój ruch zgodnie z założeniami.
        while True:
            # Human.action(World.human)
            self.make_a_move()
            self.turn_since_start += 1

    def create_world(self) -> object:
        """
        Creates a new world filled with organisms
        """
        self.n_axis = int(input('Podaj szerokość świata: '))
        self.m_axis = int(input('Podaj długość świata: '))
        for idx in range(self.number_of_starting_animals()):
            self.create_organism()
        # TODO Remove below prints
        World.organisms_list.insert(0, self.create_human())
        print(f'Pozycja człowieka: {[]}')
        print(World.organisms_list)
        self.movement_queue()

    def start_menu(self) -> None:
        """
        Start menu printed for player
        """
        print('1. Nowa gra (swtórz nowy świat)')
        print('2. Wczytaj grę')
        print('0. Wyjdź')

    def main(self) -> None:
        """
        Start Menu interface with input for player
        """
        self.start_menu()
        user_input = input('Wybierz jedną z opcji: ')
        if user_input == '1':
            self.create_world()
            self.make_a_turn()
        elif user_input == '2':
            # TODO implement saving and loading
            pass
        elif user_input == '3':
            quit()

    def create_human(self) -> object:
        """
        Creates object of Human class
        """
        return Human(self, self.turn_since_start)

    def number_of_starting_animals(self) -> int:
        """
        Calculates number of animals of same species to be created at the world creation
        """
        number_of_animals = self.n_axis * self.m_axis // 100
        if number_of_animals < 2:
            return 2
        else:
            return number_of_animals

    def free_field_check(self, organism) -> object:
        """
        Checks if the field is empty, if not returns an object that is occupying it.
        """
        for idx in range(len(World.organisms_list)):
            if organism.position == World.organisms_list[idx].position:
                return World.organisms_list.pop(idx)

    def encounter(self, moving_organism, occupying_organism) -> None:
        """
        Triggers encounter when called
        :param moving_organism: organism that moved onto the field
        :param occupying_organism: organism that defends the field
        """
        World.organisms_list.append(moving_organism.collision(occupying_organism))

    def create_organism(self) -> None:
        """
        Creates organisms when world is created.
        """
        organism_list = [Wolf(self, self.turn_since_start),
                         Sheep(self, self.turn_since_start),
                         Fox(self, self.turn_since_start),
                         Tortoise(self, self.turn_since_start),
                         Antelope(self, self.turn_since_start)]
        for idx in range(len(organism_list)):
            occupying_organism = self.free_field_check(organism_list[idx])
            if not occupying_organism:
                World.organisms_list.append(organism_list[idx])
            else:
                self.encounter(organism_list[idx], occupying_organism)

    def movement_queue(self) -> list:
        """
        Creates ordered by initiative list for organisms to make a move
        If initiative is equal orders organisms by their age
        """
        starting_initiative = max(World.organisms_list, key=lambda organism: organism.initiative).initiative
        final_list = []
        while starting_initiative != 0:
            final_list += sorted([animal for animal in World.organisms_list if animal.initiative == starting_initiative],
                                 key=lambda element: element.creation_time)
            print(final_list)
            starting_initiative -= 1
        return final_list

    def make_a_move(self):
        ordered_list = self.movement_queue()
        for idx in range(len(ordered_list)):
            ordered_list[idx].action()
