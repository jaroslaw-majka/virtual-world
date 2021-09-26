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
        pass

    def collision(self):
        # Człowiek będzie posiadał specjalną umiejętność, którą można aktywować
        # która będzie wpływała na sposób działania tej metody przez 5 tur
        # potem ta umiejętność przez kolejnych 5 tur będzie nieaktywna
        pass
