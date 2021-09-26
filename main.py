from world import World
from human import Human


if __name__ == '__main__':
    world1 = World()
    world1.create_world()
    print(f'World 1 dims: {world1.m_axis} x {world1.n_axis}')
    organism0 = Human(world1)
    print(f'Humans position is: {organism0.position}')
    organism0.action()

# Myślę, żeby zapisywać dane w dict, będę mógł zagnieździć w nim organizmy danego typu
# wraz z informacjami dotyczacymi każdego z nich (wiek, położenie)
    # Zrobiłbym to w takiej kolejności world >
#       info dot world (wymiary, tury od startu) >
#           organizmy >
#               zwierzęta, rośliny

# sprawdzenie czy pole jest puste zrobię po prostu za pomocą sprawdzenia,
# czy dany tuple (położenie x, y) znajduje się w dict.
