'''
Clase padre vehiculo, clase hija: auto 
Fecha: 10/09/2024
'''
class vehiculo:
    def __init__(self,distancia_avanzada=0):
        self.distancia_avanzada = distancia_avanzada
    def avanzar(self, velocidad=None, tiempo=None):
        if (velocidad is None and tiempo is None):
            self.distancia_avanzada += 5 
        else: 
            self.distancia_avanzada += (velocidad * tiempo)

class Auto(vehiculo):
    def __init__(self, distancia_avanzada=0, descripcion):
        super().__init__(distancia_avanzada)
        self.descripcion = descripcion
    def retroceder(self):
        self.distancia_avanzada -= 2 
    def __str__(self):
        return ('Auto (descripcion:{}), distancia_avanzada: {})'.format(self.description))

# Prueba 
auto1 = Auto(500, "Fiat")
auto1.avanzar()
print(auto1)
auto1.avanzar(20,2)
print(auto1)
auto1.retroceder()
auto1.retroceder()
print(auto1)



      

   