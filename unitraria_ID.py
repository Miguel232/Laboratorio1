import unittest

class TestLeerIdentificacion(unittest.TestCase):

    def test_identificacion_valida(self):
        identificacion = "1234567890"
        self.assertEqual(len(identificacion), 10)
        self.assertTrue(identificacion.isdigit())

    def test_identificacion_menos_digitos(self):
        identificacion = "12345"
        self.assertNotEqual(len(identificacion), 10)

    def test_identificacion_mas_digitos(self):
        identificacion = "1234567890123"
        self.assertNotEqual(len(identificacion), 10)

    def test_identificacion_con_letras(self):
        identificacion = "1234A67890"
        self.assertFalse(identificacion.isdigit())

if __name__ == "__main__":
    unittest.main()
