from characters.Character import Character
from pyxel import Pyxel


class Hollow(Character):
    unsuckable = True

    def __init__(self):
        super().__init__()
        self.image = Pyxel('resources/gfx/dziupla_woda.pyxel', 'tmp').get_layer_image(0)
