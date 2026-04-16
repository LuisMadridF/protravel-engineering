# Leccion 01
# Day 01
"""Engineer (donde vas):"""

from dataclasses import dataclass
from typing import List
from datetime import datetime


"""La Diferencia Entre Programador y Engineer
Programador (donde estás):"""

tour = 120
persons = 4
total = tour * persons
print(total)

@dataclass
class Tour:
    """Representa un tour disponible en ProTravel."""
    id : str
    nombre : str
    precio_base : float
    capacidad_maxima: int

    def calcular_precio(self,num_personas: int, fecha: datetime) -> float:
        """
        Calcula el precio considerando temporada alta o baja.
        
        args:
            num_personas : cantidad de personas
            fecha : fecha de la reserva

        """

