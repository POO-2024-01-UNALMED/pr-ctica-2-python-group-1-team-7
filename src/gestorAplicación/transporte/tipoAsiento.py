from enum import Enum

class TipoAsiento(Enum):
    # Definición de las constantes del enum, cada una con un color específico asociado.
    ESTANDAR = "Rojo"        # Asiento estándar con el color rojo.
    PREMIUM = "Amarillo"     # Asiento premium con el color amarillo.
    PREFERENCIAL = "Azul"    # Asiento preferencial con el color azul.