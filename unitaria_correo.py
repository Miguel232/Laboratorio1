import unittest

class TestLeerCorreo(unittest.TestCase):

    def test_correo_valido(self):
        correo = "usuario@correo.com"
        self.assertIn("@", correo)
        self.assertIn(".", correo)

    def test_correo_invalido(self):
        correo1 = "usuariocorreo.com"
        correo2 = "usuario@correo"
        self.assertNotIn("@", correo1)
        self.assertNotIn(".", correo2)

if __name__ == "__main__":
    unittest.main()
