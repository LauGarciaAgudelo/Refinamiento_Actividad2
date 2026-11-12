
import unittest
from salario import calcular_salario


class TestCalcularSalario(unittest.TestCase):

    def test_40_horas_categoria_1(self):
        resultado = calcular_salario(40, 1)
        self.assertEqual(resultado, 480000)

    def test_45_horas_categoria_2(self):
        resultado = calcular_salario(45, 2)
        self.assertEqual(resultado, 786250)

    def test_35_horas_categoria_3(self):
        resultado = calcular_salario(35, 3)
        self.assertEqual(resultado, 770000)

    def test_41_horas_categoria_1(self):
        resultado = calcular_salario(41, 1)
        self.assertEqual(resultado, 495000)

    def test_cero_horas(self):
        resultado = calcular_salario(0, 2)
        self.assertEqual(resultado, 0)

    def test_horas_negativas(self):
        with self.assertRaises(ValueError):
            calcular_salario(-5, 1)

    def test_categoria_invalida(self):
        with self.assertRaises(ValueError):
            calcular_salario(40, 4)


if __name__ == "__main__":
    unittest.main()
