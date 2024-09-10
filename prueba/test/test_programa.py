"""
Modulo de pruebas unitarias para programa.py 
Fecha: 09/09/24 
"""
from contextlib import AbstractContextManager
from typing import Any
import unittest
from programa import suma, es_mayor  

class TestPrograma(unittest.TestCase):
    # Metodos de prueba 
    def test_suma_positivos(self):
        self.assertEqual(suma(1, 4), 5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-2, -4), -6)

    def test_suma_detro_de_un_rango(self):
        self.assertIn(suma(2,9),[1,2,4,6,7])
# Desarrollar pruebas para la funcion "es_mayor"0
    def test_verifica_si_es_mayor(self):
        self.assertTrue(es_mayor(10,5))
    def test_verifica_que_no_es_mayor(self)
        self.assertFalse(es_mayor(2,8)) 
# Desarrollar pruebas para la division de 2 numeros
    def test_division_de_positivo_con_negativo(self):
       self.assertEqual(divide(10,-2), -5)
       self.assertEqual(divide(-4,2), -2)
    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
 
if __name__ == "__main__":
  unittest.main()


