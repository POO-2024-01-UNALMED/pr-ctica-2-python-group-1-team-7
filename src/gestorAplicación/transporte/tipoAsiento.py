from enum import Enum

class TipoAsiento(Enum):
    # Definición de las constantes del enum, cada una con un color específico asociado.
    ESTANDAR = "lightyellow"        # Asiento estándar con el color rojo.
    PREMIUM = "lightgreen"     # Asiento premium con el color amarillo.
    PREFERENCIAL = "lightblue"    # Asiento preferencial con el color azul.