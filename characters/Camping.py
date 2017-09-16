from characters.Character import Character
from pyxel import Pyxel


class Camping(Character):
    def __init__(self):
        super().__init__()
        self.image = Pyxel('resources/gfx/przyczepa campingowa.pyxel', 'tmp').get_layer_image(0)
