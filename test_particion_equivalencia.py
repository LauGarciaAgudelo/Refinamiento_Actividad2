
import unittest
from salario import calcular_salario


class TestParticionEquivalencia(unittest.TestCase):

    # CP-PE-01: Categoria 1, horas normales
    def test_cp_pe_01_categoria_1_normal(self):
        resultado = calcular_salario(35, 1)
        self.assertEqual(resultado, 420000)

    # CP-PE-02: Categoria 2, horas normales
    def test_cp_pe_02_categoria_2_normal(self):
        resultado = calcular_salario(35, 2)
        self.assertEqual(resultado, 595000)

    # CP-PE-03: Categoria 3, horas normales
    def test_cp_pe_03_categoria_3_normal(self):
        resultado = calcular_salario(35, 3)
        self.assertEqual(resultado, 770000)

    # CP-PE-04: Categoria 1, horas extras
    def test_cp_pe_04_categoria_1_extras(self):
        resultado = calcular_salario(45, 1)
        self.assertEqual(resultado, 555000)

    # CP-PE-05: Categoria 2, horas extras
    def test_cp_pe_05_categoria_2_extras(self):
        resultado = calcular_salario(45, 2)
        self.assertEqual(resultado, 786250)

    # CP-PE-06: Categoria 3, horas extras
    def test_cp_pe_06_categoria_3_extras(self):
        resultado = calcular_salario(45, 3)
        self.assertEqual(resultado, 1017500)

    # CP-PE-07: Categoria inferior al rango permitido
    def test_cp_pe_07_categoria_inferior(self):
        with self.assertRaises(ValueError):
            calcular_salario(35, 0)

    # CP-PE-08: Categoria superior al rango permitido
    def test_cp_pe_08_categoria_superior(self):
        with self.assertRaises(ValueError):
            calcular_salario(35, 4)

    # CP-PE-09: Categoria con tipo incorrecto
    def test_cp_pe_09_categoria_texto(self):
        with self.assertRaises(ValueError):
            calcular_salario(35, "2")

    # CP-PE-10: Horas negativas
    def test_cp_pe_10_horas_negativas(self):
        with self.assertRaises(ValueError):
            calcular_salario(-5, 1)

    # CP-PE-11: Horas como texto
    def test_cp_pe_11_horas_texto(self):
        with self.assertRaises(ValueError):
            calcular_salario("40", 2)

    # CP-PE-12: Horas con valor NaN
    def test_cp_pe_12_horas_nan(self):
        with self.assertRaises(ValueError):
            calcular_salario(float("nan"), 3)


if __name__ == "__main__":
    unittest.main()
