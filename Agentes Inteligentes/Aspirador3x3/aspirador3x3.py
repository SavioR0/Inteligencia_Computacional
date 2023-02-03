from enum import Enum


class states(Enum):
    C = "Clean"
    D = "Dirty"


class actions(Enum):
    R = "right"
    L = "left"
    U = "up"
    D = "down"


class Aspirador3x3 ():

    def __init__(self, initial, goal=(states.C, states.C, states.C, states.C, states.C, states.C, states.C, states.C, states.C)):
        print("Entrou no construtor")
        super().__init__(initial, goal)
