"""   
Programa que usa las clases declaradas en el archivo clases.py
Fecha: 02/09/24   
"""
class personas: 
    #def _init_(self,nombre, peso):
      #  self.nombre = nombre
      # self.peso = peso
    def __init__(self, args):
         if len(args) == 0:
            self.nombre = 'sin nombre'
            self.peso = 0
         else:
             self.nombre = args[0]
             self.peso = args[1]
             #Lo de arriba es un constructor con numeros 
    def caminar (self, args):
         if len(args) > 0:
             self.peso -= args{0} / 0.0
        else: 
             self.peso -= 0.5
    def comer (self):
        self.peso += 1
    def __str__(self):
         return 'persona (nombre: {}, peso: {})',format(self.nombre, self.peso
         )

"""
Nueva clase: Atleta
"""
class Atleta (personas): 
     estatura = 0.0
     def calcular_inc (self):
          return self.peso 
    

