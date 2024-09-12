'''
clase empleado, nombrado, parcial 
Fecha: 12/08/2024
'''
class Empleado:
    def __init__(self, nombre="sin nombre")
        self.nombre = nombre 
    def calcular(self):
        pass 
    def __str__(self):
        return 'Empleado (nombre: {})' .format(self.nombre)
    
class Nombrado(Empleado):
    def __init__(self, nombre, sueldo):
        super(). __init(nombre) # asignar valores a la clase superior 
        self.suelo = sueldo
    def calcular(self, sueldo=None):
        if sueldo is None: 
            return self.sueldo 
        else:
            self.sueldo = sueldo 
            return self.sueldo 

class Parcial(Empleado):
    def __init__(self, nombre, horas_tranajadas=None, tarifa_hora=None):
        super(). __init__(nombre)
        if horas_tranajadas is not None:
            self.horas_tranajadas = horas_tranajadas
        if tarifa_hora is not None:
            self.tarifa_hora = tarifa_hora
    def calcular(self, horas_trabajadas=None, tarifa_hora=None):
        if horas trabajadas is not None: 
           self.horas_tranajadas = horas_trabajadas
        if tarifa_hora is not None:
            self.tarifa_hora = tarifa_hora
        return self.horas_tranajadas * self.tarifa_hora
    def __str__(self):
        return 'Parcial (nombre: {}, horas_trabajadas: {}, tarifa_horas: {})'.format(self.nombre, self.sueldo)

# Prueba 
emp1 = Empleado()
emp2 = Empleado('Juan')
print (emp1)
print (emp2)
nomb1 = Nombrado('Andres',200)
nomb1 = Nombrado('Rosa', 100)
print(nomb1)
print(nomb2)
Parc1 = Parcial("Maria")
Parc2 = Parcial("Carlos")
Parc1.horas_trabajadas = 40
Parc2.horas_tranajadas = 50
Parc1.tarifa_hora = 25
Parc2.tarifa_hora = 24
print(Parc1)
print(Parc2)
print ("Para el empleado parcial: {}, el sueldo es: {}".format(Parc1.nombre, Parc1.calcular()))
print ("Para el empleado parcial: {}, el sueldo es: {}".format(Parc2.nombre, Parc2.calcular()))