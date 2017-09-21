from characters.Character import Character
from pyxel import Pyxel


class Hollow(Character):
    unsuckable = True

    def __init__(self):
        super().__init__()
