from datetime import datetime, timedelta
from typing import List, Optional
import threading
from typing import override
from personas.persona import Persona
from transporte.asiento import Asiento
from hospedaje import Hospedaje

class Habitacion:
    # Lista de todas las instancias de Habitacion
    habitaciones: List['Habitacion'] = []

    def __init__(self, numero_habitacion: str, hospedaje=None, ubicacion: str = ""):
        self.numero_habitacion = numero_habitacion  # Número de la habitación
        self.hospedaje = hospedaje  # Hospedaje al que pertenece la habitación
        self.ubicacion = ubicacion.upper()  # Ubicación de la habitación en mayúsculas
        self.reservada = False  # Estado de reserva inicial
        self.fecha_reserva: Optional[datetime] = None  # Fecha de reserva (si hay una)
        Habitacion.habitaciones.append(self)  # Añade la habitación a la lista de habitaciones

    def reservar(self, fecha_reserva: datetime):
        # Marca la habitación como reservada y establece la fecha de reserva
        self.reservada = True
        self.fecha_reserva = fecha_reserva

    def liberar(self):
        # Marca la habitación como no reservada y elimina la fecha de reserva
        self.reservada = False
        self.fecha_reserva = None

    def disponible_en(self):
        # Calcula el tiempo restante hasta que la habitación esté disponible
        if self.fecha_reserva:
            ahora = datetime.now()  # Obtiene la fecha y hora actuales
            duracion = self.fecha_reserva - ahora  # Calcula la diferencia de tiempo
            dias = duracion.days
            horas, resto = divmod(duracion.seconds, 3600)  # Convierte el resto en horas y minutos
            minutos, _ = divmod(resto, 60)
            return f"{dias} días {horas} horas {minutos} minutos"
        return None

    @override
    def __str__(self):
        # Representa la habitación en formato de cadena
        estado_reserva = "Sí" if self.reservada else "No"
        return f"    {self.numero_habitacion}                      {estado_reserva}            {self.disponible_en()}"

    def get_hospedaje(self):
        return self.hospedaje

    def set_hospedaje(self, hospedaje):
        self.hospedaje = hospedaje

    def get_numero_habitacion(self):
        return self.numero_habitacion

    def set_numero_habitacion(self, numero_habitacion):
        self.numero_habitacion = numero_habitacion

    def is_reservada(self):
        return self.reservada

    def set_reservada(self, reservada):
        self.reservada = reservada

    def get_ubicacion(self):
        return self.ubicacion

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion.upper()

    def get_fecha_reserva(self) -> Optional[datetime]:
        return self.fecha_reserva

    def set_fecha_reserva(self, fecha_reserva: datetime):
        self.fecha_reserva = fecha_reserva

    @staticmethod
    def get_habitaciones():
        return Habitacion.habitaciones

    @staticmethod
    def set_habitaciones(habitaciones: List['Habitacion']):
        Habitacion.habitaciones = habitaciones

    @staticmethod
    def chequear_habitaciones():
        # Revisa todas las habitaciones y libera las que ya no están reservadas
        for terminal in Terminal.get_terminales():
            for hospedaje in terminal.get_hospedajes():
                for habitacion in hospedaje.get_habitaciones():
                    if habitacion.get_fecha_reserva() is not None:
                        if habitacion.get_fecha_reserva() <= datetime.now():
                            # Libera la habitación si la fecha de reserva ha pasado
                            habitacion.liberar()
                        else:
                            # Programa la liberación de la habitación cuando la reserva expire
                            duracion = habitacion.get_fecha_reserva() - datetime.now()
                            minutos = int(duracion.total_seconds() // 60)
                            threading.Timer(minutos * 60, habitacion.liberar).start()

