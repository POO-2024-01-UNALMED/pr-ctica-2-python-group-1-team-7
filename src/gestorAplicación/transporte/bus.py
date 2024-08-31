import vehiculo
import asiento

class Bus(vehiculo.Vehiculo):
    def __init__(self, filas: int, tipos_asiento_fila: list[int]):
        self.tipos_asiento_fila = tipos_asiento_fila
        self.asientos = self.crear_asientos(filas)
        self.placa = vehiculo.Vehiculo.generar_placa()
    
    # Método para crear los asientos al llamar al constructor
    def crear_asientos(self, filas: int):
        letras = "ABCD"

        for fila in range(1, filas + 1):
            for letra in letras:
                numero_asiento = f"{fila}{letra}"
                if fila <= self.tipos_asiento_fila[0]:
                    tipo = TipoAsiento.PREFERENCIAL
                elif fila <= self.tipos_asiento_fila[1]:
                    tipo = TipoAsiento.PREMIUM
                else:
                    tipo = TipoAsiento.ESTANDAR
                self.asientos.append(asiento.Asiento(numero_asiento, tipo))

    # Getters y setters
    def get_tipos_asiento(self):
        return self.tipos_asiento_fila

    def set_tipos_asiento(self, tipos_asiento: list[int]):
        self.tipos_asiento_fila = tipos_asiento

    def get_asientos(self):
        return self.asientos

    def set_asientos(self, asientos: list[Asiento]):
        self.asientos = asientos

    def get_placa(self):
        return self.placa

    def set_placa(self, placa: str):
        self.placa = placa

    