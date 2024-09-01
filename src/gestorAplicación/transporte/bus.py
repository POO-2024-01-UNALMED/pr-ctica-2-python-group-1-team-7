from vehiculo import Vehiculo
from asiento import Asiento
from tipoAsiento import TipoAsiento

class Bus(Vehiculo):
    def __init__(self, filas: int, tipos_asiento_fila: list[int]):
        # Inicializa el Bus con un número de filas y un esquema de tipos de asiento.
        # Inicializa la lista de asientos vacía
        self.tipos_asiento_fila = tipos_asiento_fila
        self.asientos:list[Asiento] = []
        # Crea los asientos para el bus
        self.crear_asientos(filas)
        # Genera una placa única para el bus
        self.placa = Vehiculo.generar_placa()
    
    # Método para crear los asientos al llamar al constructor
    def crear_asientos(self, filas: int):
        # Crea los asientos del bus basándose en el número de filas y el esquema de tipos de asiento.
        letras = "ABCD"  # Letras que representan las columnas de los asientos

        for fila in range(1, filas + 1):
            for letra in letras:
                numero_asiento = f"{fila}{letra}"  # Genera el número del asiento
                # Determina el tipo de asiento según el número de fila
                if fila <= self.tipos_asiento_fila[0]:
                    tipo = TipoAsiento.PREFERENCIAL
                elif fila <= self.tipos_asiento_fila[1]:
                    tipo = TipoAsiento.PREMIUM
                else:
                    tipo = TipoAsiento.ESTANDAR
                # Crea y agrega el asiento a la lista de asientos
                self.asientos.append(Asiento(numero_asiento, tipo))

    # Getters y setters
    def get_tipos_asiento(self):
        # Devuelve el esquema de tipos de asiento
        return self.tipos_asiento_fila

    def set_tipos_asiento(self, tipos_asiento: list[int]):
        # Establece el esquema de tipos de asiento
        self.tipos_asiento_fila = tipos_asiento

    def get_asientos(self):
        # Devuelve la lista de asientos del bus
        return self.asientos

    def set_asientos(self, asientos: list[Asiento]):
        # Establece la lista de asientos del bus
        self.asientos = asientos

    def get_placa(self):
        # Devuelve la placa del bus
        return self.placa

    def set_placa(self, placa: str):
        # Establece la placa del bus
        self.placa = placa