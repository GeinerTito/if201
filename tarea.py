class Empleado:
    def __init__(self, nombre, tarifa_por_hora):
        self.nombre = nombre
        self.tarifa_por_hora = tarifa_por_hora
        self.horas_trabajadas = 0

    def registrar_horas(self, horas):
        if horas < 0:
            print("Las horas trabajadas no pueden ser negativas.")
        else:
            self.horas_trabajadas += horas

    def calcular_sueldo(self):
        return self.horas_trabajadas * self.tarifa_por_hora

    def mostrar_informacion(self):
        sueldo_total = self.calcular_sueldo()
        print(f"Nombre del empleado: {self.nombre}")
        print(f"Tarifa por hora: ${self.tarifa_por_hora:.2f}")
        print(f"Horas trabajadas: {self.horas_trabajadas}")
        print(f"Sueldo total: ${sueldo_total:.2f}")

# Ejemplo de uso:
nombre_empleado = input("Ingrese el nombre del empleado: ")
tarifa = float(input("Ingrese la tarifa por hora del empleado: "))

empleado = Empleado(nombre_empleado, tarifa)

while True:
    try:
        horas = float(input("Ingrese las horas trabajadas (o ingrese -1 para terminar): "))
        if horas == -1:
            break
        empleado.registrar_horas(horas)
    except ValueError:
        print("Por favor, ingrese un número válido.")

empleado.mostrar_informacion()
