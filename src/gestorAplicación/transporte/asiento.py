from datetime import datetime, timedelta
from gestion import Empresa, TipoAsiento
from typing import override
from concurrent.futures import ThreadPoolExecutor
import threading

class Asiento:
    def __init__(self, numero:str = "Indefinido", tipo_asiento: TipoAsiento = None):
        # Inicializa un objeto Asiento con el número y tipo de asiento dados.
        # Si no se especifica un número, se usa "Indefinido".
        # Si no se especifica un tipo, se usa None.
        self.numero = numero
        self.tipo_asiento = tipo_asiento  # Tipo de asiento
        self.reservado = False  # Estado de reserva inicial
        self.fecha_reserva = None  # Fecha de reserva inicial

    # Método para asegurarse de que los asientos se liberen en el tiempo indicado, 
    # usado en la funcionalidad 1
    @classmethod
    def chequear_asientos():
        # Utiliza hilos para programar la liberación de asientos en el futuro.
        for empresa in Empresa.get_empresas():  # Itera sobre todas las empresas
            for viaje in empresa.get_viajes():  # Itera sobre todos los 
                                                # viajes de la empresa
                for asiento in viaje.lista_asientos():  # Itera sobre todos 
                                                        # los asientos del viaje
                    if asiento.get_fecha_reserva() is not None:
                        if asiento.get_fecha_reserva() <= datetime.now():
                            asiento.liberar()  # Libera el asiento si la 
                                                # fecha de reserva ha pasado
                        else:
                            # Calcula la duración hasta la liberación
                            duration = asiento.get_fecha_reserva() - datetime.now()  
                            # Utiliza un hilo para liberar el asiento 
                            # después de la duración especificada
                            service = ThreadPoolExecutor(max_workers = 1)
                            task = threading.Timer(duration.total_seconds(), 
                                                    asiento.liberar)
                            task.start()

    # Método para reservar un asiento, usado en la funcionalidad 1, 2 y 3
    def reservar(self, fecha_reserva = None):
        # Si no se proporciona una fecha, solo marca el asiento como reservado.
        self.reservado = True
        self.fecha_reserva = fecha_reserva

    # Método para liberar un asiento, usado en la funcionalidad 1 y 3
    def liberar(self):
        # Libera el asiento, estableciendo el estado de reserva a False 
        # y la fecha de reserva a None.
        self.set_reservado(False)
        self.set_fecha_reserva(None)

    # Devuelve una representación en cadena del asiento.
    @override
    def __str__(self):
        # Muestra el número y el tipo de asiento.
        return f"{self.numero} {self.tipo_asiento}"

    # Getters y setters
    def get_numero(self):
        # Obtiene el número del asiento.
        return self.numero

    def set_numero(self, numero):
        # Establece el número del asiento.
        self.numero = numero

    def get_tipo_asiento(self):
        # Obtiene el tipo de asiento.
        return self.tipo_asiento

    def is_reservado(self):
        # Verifica si el asiento está reservado.
        # Devuelve True si está reservado, False en caso contrario.
        return self.reservado

    def set_reservado(self, reservado):
        # Establece el estado de reserva del asiento.
        self.reservado = reservado

    def get_fecha_reserva(self):
        # Obtiene la fecha de reserva del asiento.
        return self.fecha_reserva

    def set_fecha_reserva(self, fecha_reserva):
        # Establece la fecha de reserva del asiento.
        self.fecha_reserva = fecha_reserva