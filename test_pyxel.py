import unittest, pyxel


class PyxelTestCase(unittest.TestCase):
    def test_create_pyxel(self):
        pyxel_demo_doc = pyxel.Pyxel('resources/test/DemoDoc.pyxel', 'tmp')

if __name__ == '__main__':
    unittest.main()
