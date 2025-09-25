import unittest

class TestLeerGenero(unittest.TestCase):

    def test_genero_valido(self):
        for genero in ["M", "F"]:
            self.assertIn(genero, ["M", "F"])

    def test_genero_invalido(self):
        self.assertNotIn("X", ["M", "F"])
        self.assertNotIn("H", ["M", "F"])
        self.assertNotIn("1", ["M", "F"])

if __name__ == "__main__":
    unittest.main()
