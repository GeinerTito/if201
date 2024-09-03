---
programa que usa las clases declaradas en el archivo clases
Fecha 02/09/2024
---
import clases_y_objetos as cl
#Crear objetos de clase persona 
per1 = cl.persona("Juan", 70)
per2 = cl.persona("Maria", 55) 
#Asignar valor a las propiedades 
per1.peso = 75
per2.peso = 57
per2.nombre += "Elena"
# Usar los metodods 
per1.caminar()
per2.comer()
per2.comer()
print("Nombre: {} y peso: {}",format(per2.nombre,
                                     per2.peso))
print("Nombre: {} y peso: {}",format(per2.nombre,
                                     per2.peso))