from datetime import datetime, date, time
from typing import override

class Viaje:
    ids = 1

    def __init__(self, terminal_origen: 'Terminal', terminal_destino: 'Terminal', 
                    empresa: 'Empresa' = None, fecha: date = None, 
                        hora: time = None, bus: 'Bus' = None):
        self.terminal_origen = terminal_origen
        self.terminal_destino = terminal_destino
        self.empresa = empresa
        self.fecha = fecha
        self.hora = hora
        self.bus = bus
        self.id: str = str(Viaje.ids)
        Viaje.ids += 1

    # Método para buscar un viaje por id en una lista de viajes, 
    # usado en la funcionalidad 2
    @classmethod
    def buscar_viaje(cls, viajes: list['Viaje'], id_: str):
        for viaje in viajes:
            if viaje.get_id() == id_:
                return viaje
        return None

    # Método para buscar un asiento en un viaje por el número de asiento, 
    # usado en varias funcionalidades
    def buscar_asiento(self, numero_asiento: str):
        for asiento in self.lista_asientos():
            if asiento.get_numero() == numero_asiento:
                return asiento
        return None

    # Método para buscar un hospedaje que esté disponible en el destino del viaje, 
    # usado en la funcionalidad 4
    def buscar_hospedaje(self, nombre: str):
        for hospedaje in self.hospedajes_disponibles():
            if hospedaje.get_nombre() == nombre:
                return hospedaje
        return None

    # Método para reservar un asiento en un viaje por un cierto período de tiempo o 
    # hasta que el viaje acabe, usado en varias funcionalidades
    def reservar_asiento(self, numero_asiento: str, fecha_reserva: datetime = None):
        for asiento in self.lista_asientos():
            if not asiento.is_reservado() and asiento.get_numero() == numero_asiento:
                asiento.reservar(fecha_reserva)
                break

    # Método para liberar un asiento por el número de asiento, 
    # usado en la funcionalidad 1 y 3
    def liberar_asiento(self, numero_asiento: str):
        for asiento in self.lista_asientos():
            if asiento.get_numero() == numero_asiento:
                asiento.liberar()

    # Método que devuelve la lista de asientos de un viaje, 
    # usado en varias funcionalidades
    def lista_asientos(self):
        return self.bus.get_asientos()

    # Método que devuelve una lista de tipo int, cuyos valores indican hasta que fila 
    # van cada tipo de asiento (new int[]{5, 10} significa que los asientos 
    # preferenciales van hasta la fila 5, los asientos premium van hasta la fila 10 
    # y el resto de las filas son estandar. Usado en varias funcionalidades
    def tipos_asiento(self):
        return self.bus.get_tipos_asiento()

    # Método para verificar si un viaje tiene sillas disponibles, 
    # usado en varias funcionalidades
    def tiene_sillas(self):
        for asiento in self.lista_asientos():
            if not asiento.is_reservado():
                return True
        return False

    # Método que devuelve los hospedajes disponibles de acuerdo al destino del viaje, 
    # usado en la funcionalidad 4
    def hospedajes_disponibles(self):
        return self.terminal_destino.get_hospedajes()

    # Método toString que hace calcula los espacios en blanco necesarios para que 
    # la impresión en pantalla se vea uniforme
    @override
    def __str__(self):
        origen_spaces = ' ' * max(0, 11 - len(self.terminal_origen.get_ubicacion()))
        destino_spaces = ' ' * max(0, 11 - len(self.terminal_destino.get_ubicacion()))
        id_spaces = ' ' * max(0, 3 - len(self.id))

        return (
            f"    {self.get_str_fecha()}     {self.terminal_origen.get_ubicacion()}"
            f"{origen_spaces}     {self.terminal_destino.get_ubicacion()}"
            f"{destino_spaces}     {self.hora.strftime("%H:%M")}" 
            f"              {self.id}"
            f"{id_spaces}     {self.bus.get_placa()}"
        )

    # Getters y setters         
    def get_terminal_origen(self):
        return self.terminal_origen
    
    def set_terminal_origen(self, terminal_origen):
        self.terminal_origen = terminal_origen

    def get_terminal_destino(self):
        return self.terminal_destino

    def set_terminal_origen(self, terminal_destino):
        self.terminal_destino = terminal_destino

    def get_empresa(self):
        return self.empresa

    def set_empresa(self, empresa):
        self.empresa = empresa

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    def get_hora(self):
        return self.hora

    def set_hora(self, hora):
        self.hora = hora

    def get_bus(self):
        return self.bus

    def set_bus(self, bus):
        self.bus = bus

    def get_id(self):
        return self.id

    def set_id(self, id_):
        self.id = id_

    def get_origen(self):
        return self.get_terminal_origen().get_ubicacion()

    def get_destino(self):
        return self.get_terminal_destino().get_ubicacion()

    def get_str_fecha(self):
        return self.fecha.strftime("%d-%m-%Y")