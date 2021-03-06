from organisms.animals.human import Human
from organisms.animals.wolf import Wolf
from organisms.animals.sheep import Sheep
from organisms.animals.fox import Fox
from organisms.animals.tortoise import Tortoise
from organisms.animals.antelope import Antelope


class World:
    organisms_list = []

    def __init__(self):
        self.n_axis = None
        self.m_axis = None
        self.turn_since_start = 0
        self.main()

    def make_a_turn(self) -> None:
        """ Starts a new turn in game """
        while True:
            self.make_a_move()
            self.turn_since_start += 1

    def create_world(self) -> object:
        """ Creates a new world filled with organisms """
        self.n_axis = int(input('Podaj szerokość świata: '))
        self.m_axis = int(input('Podaj długość świata: '))
        for idx in range(self.number_of_starting_animals()):
            self.create_organism()
        # TODO Remove below prints
        World.organisms_list.insert(0, self.create_human())
        print(World.organisms_list)

    def start_menu(self) -> None:
        """ Start menu printed for player """
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

    def free_field_check(self, organism_position) -> object:
        """
        Checks if the field is empty, if not returns an object that is occupying it.
        """
        for idx in range(len(World.organisms_list)):
            if organism_position == World.organisms_list[idx].position:
                return World.organisms_list.pop(idx)

    def encounter(self, moving_organism, occupying_organism) -> None:
        """
        Triggers encounter when needed
        :param moving_organism: organism that moved onto the field
        :param occupying_organism: organism that defends the field
        """
        loser = moving_organism.collision(occupying_organism)
        if loser == moving_organism:
            World.organisms_list.append(occupying_organism)
        elif loser == occupying_organism:
            World.organisms_list.append(moving_organism)

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
            self.encounter_check(organism_list[idx])

    def encounter_check(self, organism) -> object:
        """
        Returns objects occupying the field and triggers encounter if needed
        :param organism:
        :return:
        """
        def append_new_organism(new_organism: object) -> list:
            """
            Appends new organism to a list
            Called only at organism creation
            :param new_organism: instance of a new organism
            """
            World.organisms_list.append(new_organism)

        occupying_organism = self.free_field_check(organism.position)
        if occupying_organism:
            self.encounter(organism, occupying_organism)
        else:
            append_new_organism(organism)

    def movement_queue(self) -> list:
        """
        Creates ordered by initiative list for organisms to make a move
        If initiative is equal orders organisms by their age
        """
        starting_initiative = max(World.organisms_list,
                                  key=lambda organism: organism.initiative).initiative
        final_list = []
        while starting_initiative != 0:
            final_list += sorted([animal for animal in World.organisms_list
                                  if animal.initiative == starting_initiative],
                                 key=lambda element: element.creation_time)
            starting_initiative -= 1
        # TODO remove below print
        print(final_list)
        return final_list

    def make_a_move(self) -> None:
        """
        Applies logic for movement acction.
        :return: organism object with updated position
        """
        ordered_list = self.movement_queue()
        for moving_organism in ordered_list:
            pre_move_position = moving_organism.position
            moving_organism.action()
            self.attack_occupant(moving_organism, pre_move_position)

    def attack_occupant(self, attacker: object, pre_move_position: tuple) -> None:
        """
        Checks if field was taken and if needed triggers collision method.
        :param pre_move_position: Moving organism position before the move was made
        :param attacker: instance of an object that moved onto the field.
        """
        def check_organism_type() -> None:
            """
            Checks organism type and triggers attack or multiplication
            """
            positional_list.remove(attacker)
            defender = positional_list[0]
            if type(attacker) == type(defender):
                trigger_multiplication(attacker, defender)
            else:
                trigger_attack(defender)

        def trigger_attack(defender) -> None:
            """
            Triggers organisms battle
            """
            loser = attacker.collision(defender)
            World.organisms_list.remove(loser)

        def trigger_multiplication(organism_1, organism_2) -> object:
            """
            Triggers organisms multiplication
            """
            organism_1.position = pre_move_position
            free_fields = check_area(organism_1, organism_2)
            print(free_fields)
            if free_fields:
                new_organism = organism_1.multiplication(free_fields, self, self.turn_since_start)
                # TODO Reformat below messy code
                print(f'Utworzono nowy organizm: {new_organism}\n'
                      f'Jego pozycja to: {new_organism.position}\n'
                      f'Jego Tura utowrzenia to: {new_organism.creation_time}')
                World.organisms_list.append(new_organism)
                print(f'Aktualna lista organizmów to: {World.organisms_list}')
            else:
                print('Nie ma miejsca na nowy organizm.')

        def check_area(organism_1: object, organism_2: object) -> list:
            def list_of_all_fields_around(position_1: tuple, position_2: tuple) -> list:
                """
                Creates a list of all fields around 2 objects
                """
                list_of_all_fields = []
                for organism in [position_1, position_2]:
                    list_of_all_fields += [(organism[0] + 1, organism[1]),
                                           (organism[0] - 1, organism[1]),
                                           (organism[0], organism[1] + 1),
                                           (organism[0], organism[1] - 1)]
                return list_of_all_fields

            def map_sanity_check(list_for_sanity_checking: list) -> list:
                """
                Checks if provided list does not contain fields that are out of the map range.
                :param list_for_sanity_checking:
                """
                for spot in list_for_sanity_checking:
                    if spot[0] <= 0 \
                            or spot[1] <= 0 \
                            or spot[0] > self.n_axis \
                            or spot[1] > self.m_axis:
                        list_for_sanity_checking.remove(spot)
                return list(set(list_for_sanity_checking))

            def create_final_list(list_for_empty_space_checking: list) -> list:
                """
                Creates a list of empty spaces for a new organism to be created.
                :param list_for_empty_space_checking:
                """
                def check_for_empty_field(position: tuple) -> bool:
                    """Checks if field is empty"""
                    for idx in range(len(World.organisms_list)):
                        if position == World.organisms_list[idx].position:
                            return True

                final_list = []
                for field in list_for_empty_space_checking:
                    if not check_for_empty_field(field):
                        final_list.append(field)
                return final_list

            return create_final_list(
                map_sanity_check(list_of_all_fields_around(organism_1.position,
                                                           organism_2.position)))

        positional_list = [organism for organism in World.organisms_list if
                           organism.position == attacker.position]
        if len(positional_list) > 1:
            check_organism_type()
