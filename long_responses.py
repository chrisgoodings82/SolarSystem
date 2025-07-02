import random
from enum import Enum

class Action(Enum):
    NONE = 0
    DISPLAY = 1
    RESPONSE = 2
    QUERY = 3
    COMPARE = 4

class Detail(Enum):
    NONE = 0
    ALL = 1
    FACT = 2

class Fact(Enum):
    NONE = 0
    MASS = 1
    DISTANCE = 2
    SATELLITES = 3
    MOONS = 4
    RADIUS = 5
    ALL = 6

class Planet(Enum):
    NONE = 0
    MERCURY = 1
    VENUS = 2
    EARTH = 3
    MARS = 4
    JUPITER = 5
    SATURN = 6
    URANUS = 7
    NEPTUNE = 8
    ALL = 9


R_PLUTO = "Pluto, once considered the ninth planet, is now classified as a dwarf planet. It is located in the Kuiper Belt, a region beyond Neptune, and is known for its icy surface and five moons, the largest being Charon."


def unknown():
    response = ['Could you please re-phrase that?',
                'I\'m not quite sure what you mean...',
                'Hmmm, that is a tough one... could you try a different question, please?'][random.randrange(3)]
    return response