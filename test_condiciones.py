
import unittest
from salario import calcular_salario


class TestCondiciones(unittest.TestCase):

    # CP-CO-01: Tipo de categoria incorrecto
    def test_cp_co_01_categoria_tipo_invalido(self):
        with self.assertRaises(ValueError):
            calcular_salario(40, "1")

    # CP-CO-02: Categoria fuera del rango permitido
    def test_cp_co_02_categoria_inexistente(self):
        with self.assertRaises(ValueError):
            calcular_salario(40, 4)

    # CP-CO-03: Categoria valida
    def test_cp_co_03_categoria_valida(self):
        resultado = calcular_salario(40, 1)
        self.assertEqual(resultado, 480000)

    # CP-CO-04: Horas con tipo de dato incorrecto
    def test_cp_co_04_horas_tipo_invalido(self):
        with self.assertRaises(ValueError):
            calcular_salario("40", 1)

    # CP-CO-05: Horas negativas
    def test_cp_co_05_horas_negativas(self):
        with self.assertRaises(ValueError):
            calcular_salario(-1, 1)

    # CP-CO-06: Horas infinitas
    def test_cp_co_06_horas_infinitas(self):
        with self.assertRaises(ValueError):
            calcular_salario(float("inf"), 1)

    # CP-CO-07: Condicion de horas extras falsa
    def test_cp_co_07_sin_horas_extras(self):
        resultado = calcular_salario(39, 2)
        self.assertEqual(resultado, 663000)

    # CP-CO-08: Condicion de horas extras verdadera
    def test_cp_co_08_con_horas_extras(self):
        resultado = calcular_salario(45, 2)
        self.assertEqual(resultado, 786250)


if __name__ == "__main__":
    unittest.main()
