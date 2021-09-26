from human import Human


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

    def create_world(self):
        self.n_axis = int(input('Podaj szerokość świata: '))
        self.m_axis = int(input('Podaj długość świata: '))
        World.organisms_dict['animals']['human'] = Human(self, self.turn_since_start)
        # TODO Remove below prints
        print(World.organisms_dict['animals']['human'].position)
        print(World.organisms_dict)

    def start_menu(self):
        print('1. Nowa gra (swtórz nowy świat)')
        print('2. Wczytaj grę')
        print('0. Wyjdź')

    def main(self):
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
