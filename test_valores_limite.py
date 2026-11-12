
import unittest
from salario import calcular_salario


class TestValoresLimite(unittest.TestCase):

    # Limite inferior de horas: 0

    def test_cp_vl_01_horas_menor_cero(self):
        with self.assertRaises(ValueError):
            calcular_salario(-0.01, 1)

    def test_cp_vl_02_horas_igual_cero(self):
        resultado = calcular_salario(0, 1)
        self.assertEqual(resultado, 0)

    def test_cp_vl_03_horas_mayor_cero(self):
        resultado = calcular_salario(0.01, 1)
        self.assertAlmostEqual(resultado, 120, places=2)

    # Limite entre horas normales y extras: 40

    def test_cp_vl_04_horas_menor_40(self):
        resultado = calcular_salario(39.99, 2)
        self.assertAlmostEqual(resultado, 679830, places=2)

    def test_cp_vl_05_horas_igual_40(self):
        resultado = calcular_salario(40, 2)
        self.assertEqual(resultado, 680000)

    def test_cp_vl_06_horas_mayor_40(self):
        resultado = calcular_salario(40.01, 2)
        self.assertAlmostEqual(resultado, 680212.50, places=2)

    # Limite inferior de categoria: 1

    def test_cp_vl_07_categoria_menor_1(self):
        with self.assertRaises(ValueError):
            calcular_salario(40, 0)

    def test_cp_vl_08_categoria_igual_1(self):
        resultado = calcular_salario(40, 1)
        self.assertEqual(resultado, 480000)

    def test_cp_vl_09_categoria_mayor_1(self):
        resultado = calcular_salario(40, 2)
        self.assertEqual(resultado, 680000)

    # Limite superior de categoria: 3

    def test_cp_vl_10_categoria_menor_3(self):
        resultado = calcular_salario(40, 2)
        self.assertEqual(resultado, 680000)

    def test_cp_vl_11_categoria_igual_3(self):
        resultado = calcular_salario(40, 3)
        self.assertEqual(resultado, 880000)

    def test_cp_vl_12_categoria_mayor_3(self):
        with self.assertRaises(ValueError):
            calcular_salario(40, 4)


if __name__ == "__main__":
    unittest.main()
