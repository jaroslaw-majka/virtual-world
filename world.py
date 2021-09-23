class World:
    # klasa zarządzająca rozgrywką i organizmami na planszy
    def __init__(self):
        self.n_axis = None
        self.m_axis = None

    def make_a_turn(self):
        # Sprawi, że organizmy wykonają swój ruch zgodnie z założeniami.
        pass

    def create_world(self):
        self.n_axis = int(input('Podaj szerokość świata: '))
        self.m_axis = int(input('Podaj długość świata: '))
