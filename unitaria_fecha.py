import unittest
from datetime import datetime

class TestLeerFecha(unittest.TestCase):

    def test_fecha_valida(self):
        fecha_str = "15/08/2000"
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.assertEqual(fecha.day, 15)
        self.assertEqual(fecha.month, 8)
        self.assertEqual(fecha.year, 2000)

    def test_formato_invalido(self):
        fecha_str = "2000-08-15"
        with self.assertRaises(ValueError):
            datetime.strptime(fecha_str, "%d/%m/%Y")

    def test_fecha_invalida(self):
        fecha_str = "31/02/2020"
        with self.assertRaises(ValueError):
            datetime.strptime(fecha_str, "%d/%m/%Y")

if __name__ == "__main__":
    unittest.main()
