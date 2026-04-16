"""
ProTravel - Día 1: Mi primer programa orientado a objetos
Objetivo: Calcular ingresos del día
"""

class Tour:
    def __init__(self, nombre, precio):
        self.nombre =nombre
        self.precio = precio
        self.reservas_hoy = 0


    def agregar_reserva(self):
        self.reservas_hoy += 1
        print(f"Reserva agregada para {self.nombre}.")
    
    def ingresos_del_dia(self):
        return self.precio * self.reservas_hoy
    
tour_canal = Tour("Canal de Panama", 175)
tour_amador = Tour("Amador", 50)
tour_playa = Tour("Playa Bonita", 175)

tour_canal.agregar_reserva()
tour_canal.agregar_reserva()
tour_amador.agregar_reserva()
tour_playa.agregar_reserva()

#Calcular ingresos del día
print("\nIngresos del día:")
print(f"{tour_canal.nombre}: ${tour_canal.ingresos_del_dia()}")
print(f"{tour_amador.nombre}: ${tour_amador.ingresos_del_dia()}")
print(f"{tour_playa.nombre}: ${tour_playa.ingresos_del_dia()}")


