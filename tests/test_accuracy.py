import unittest
from src.metricas import calcular_accuracy


class TestAccuracy(unittest.TestCase):
    def test_accuracy_perfecta(self):
        self.assertEqual(calcular_accuracy([1, 0, 1], [1, 0, 1]), 1.0)

    def test_accuracy_parcial(self):
        self.assertAlmostEqual(calcular_accuracy([1, 0, 1, 1], [1, 1, 1, 0]), 0.5)

    def test_rechaza_listas_vacias(self):
        with self.assertRaises(ValueError):
            calcular_accuracy([], [])
