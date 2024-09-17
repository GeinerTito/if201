# Clase base Empleado
class Empleado:
    def _init_(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def calcular_bono(self):
        """
        Calcula el bono del empleado, que es el 10% del salario.
        """
        return self.salario * 0.1

# Clase derivada Gerente
class Gerente(Empleado):
    def _init_(self, nombre, edad, salario, departamento):
        super()._init_(nombre, edad, salario)
        self.departamento = departamento
    
    def calcular_bono(self):
        """
        Calcula el bono del gerente, que es el 20% del salario.
        """
        return self.salario * 0.2

# Pruebas Unitarias
import unittest

class TestSistemaGestionEmpleados(unittest.TestCase):

    def test_empleado_bono(self):
        """
        Prueba que el bono para un empleado sea el 10% del salario.
        """
        empleado = Empleado("Juan", 30, 3000)
        self.assertEqual(empleado.calcular_bono(), 300.0)

    def test_gerente_bono(self):
        """
        Prueba que el bono para un gerente sea el 20% del salario.
        """
        gerente = Gerente("Ana", 40, 5000, "Ventas")
        self.assertEqual(gerente.calcular_bono(), 1000.0)

    def test_gerente_departamento(self):
        """
        Prueba que el gerente tenga asignado correctamente el departamento.
        """
        gerente = Gerente("Carlos", 50, 6000, "Recursos Humanos")
        self.assertEqual(gerente.departamento, "Recursos Humanos")

if __name__ == '__main__':
    unittest.main(verbosity=2)