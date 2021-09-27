from human import Human
from wolf import Wolf


class World:
    organisms_dict = {'plants': {'grass': [],
                                 'dandelion': [],
                                 'guarana': [],
                                 'wolf berries': []},
                      'animals': {'wolf': [],
                                  'sheep': [],
                                  'fox': [],
                                  'tortoise': [],
                                  'antelope': []}}
    
    def __init__(self):
        self.n_axis = None
        self.m_axis = None
        self.turn_since_start = 0
        self.main()

    def make_a_turn(self):
        # Sprawi, że organizmy wykonają swój ruch zgodnie z założeniami.
        while True:
            Human.action(World.organisms_dict['animals']['human'])
            self.turn_since_start += 1

    def create_world(self) -> object:
        """
        Creates a new world filled with organisms
        """
        self.n_axis = int(input('Podaj szerokość świata: '))
        self.m_axis = int(input('Podaj długość świata: '))
        self.create_human()
        self.create_wolf()
        # TODO Remove below prints
        print(f"Human: {World.organisms_dict['animals']['human'].position}")
        print(f"Wolf: {World.organisms_dict['animals']['wolf'][0].position}")
        print(World.organisms_dict)

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
        World.organisms_dict['animals']['human'] = Human(self, self.turn_since_start)

    def number_of_starting_animals(self) -> int:
        """
        Calculates number of animals of same species to be created at the world creation
        """
        return self.n_axis * self.m_axis // 100

    def create_wolf(self) -> object:
        """
        Creates object of Wolf class
        """
        World.organisms_dict['animals']['wolf'].append(Wolf(self, self.turn_since_start))
