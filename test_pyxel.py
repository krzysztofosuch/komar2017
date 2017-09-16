import unittest, pyxel


class PyxelTestCase(unittest.TestCase):
    def test_create_pyxel(self):
        pyxel.Pyxel('resources/test/DemoDoc.pyxel', 'tmp')

    def test_create_animated(self):
        p = pyxel.Pyxel('resources/gfx/Latanie.pyxel', 'tmp')
        pyxel.AnimatedPyxel(p)

if __name__ == '__main__':
    unittest.main()
