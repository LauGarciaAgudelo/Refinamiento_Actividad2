
import unittest
from salario import calcular_salario


class TestCaminoBasico(unittest.TestCase):

    # P1: Categoria con tipo de dato incorrecto
    def test_cp_cb_01_categoria_no_entera(self):
        with self.assertRaises(ValueError):
            calcular_salario(40, "1")

    # P2: Categoria entera fuera de las permitidas
    def test_cp_cb_02_categoria_inexistente(self):
        with self.assertRaises(ValueError):
            calcular_salario(40, 4)

    # P3: Horas con tipo de dato incorrecto
    def test_cp_cb_03_horas_no_numericas(self):
        with self.assertRaises(ValueError):
            calcular_salario("40", 1)

    # P4: Horas negativas
    def test_cp_cb_04_horas_negativas(self):
        with self.assertRaises(ValueError):
            calcular_salario(-1, 1)

    # P5: Horas infinitas
    def test_cp_cb_05_horas_infinitas(self):
        with self.assertRaises(ValueError):
            calcular_salario(float("inf"), 1)

    # P6: Horas normales
    def test_cp_cb_06_salario_normal(self):
        resultado = calcular_salario(40, 1)
        self.assertEqual(resultado, 480000)

    # P7: Horas extras
    def test_cp_cb_07_salario_extra(self):
        resultado = calcular_salario(45, 2)
        self.assertEqual(resultado, 786250)


if __name__ == "__main__":
    unittest.main()
