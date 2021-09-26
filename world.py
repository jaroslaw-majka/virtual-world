from human import Human


class World:
    organisms_dict = {'plants': {'grass': [],
                                 'dandelion': [],
                                 'guarana': [],
                                 'wolf berries': []},
                      'animals': {'human': '',
                                  'wolf': [],
                                  'sheep': [],
                                  'fox': [],
                                  'tortoise': [],
                                  'antelope': []}}
    
    def __init__(self):
        self.n_axis = None
        self.m_axis = None
        self.turn_since_start = 0

    def make_a_turn(self):
        self.turn_since_start += 1
        # Sprawi, że organizmy wykonają swój ruch zgodnie z założeniami.
        pass

    def create_world(self):
        self.n_axis = int(input('Podaj szerokość świata: '))
        self.m_axis = int(input('Podaj długość świata: '))
        World.organisms_dict['animals']['human'] = Human(self)
        print(World.organisms_dict['animals']['human'].position)
