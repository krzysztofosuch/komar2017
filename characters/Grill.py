from characters.Character import Character
from pyxel import Pyxel


class Grill(Character):
    def __init__(self):
        super().__init__()
        self.image = Pyxel('resources/gfx/grill.pyxel', 'tmp').get_layer_image(0)
