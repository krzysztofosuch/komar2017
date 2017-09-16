from characters.Character import Character
from pyxel import Pyxel


class Campfire(Character):
    unsuckable = True

    def __init__(self):
        super().__init__()
        self.image = Pyxel('resources/gfx/ognisko.pyxel', 'tmp').get_layer_image(0)
