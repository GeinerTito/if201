"""
Definicion de funciones que seran sometidas a 
Pruebas unitarias
Fecha: 09/09/2024
"""
def suma(x, y):
    return x + y 

def es_mayor(x, y):
    return(x > y)

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("No se puede dividir por 0")
    return (x / y)