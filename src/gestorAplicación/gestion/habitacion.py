from datetime import datetime, timedelta
from terminal import Terminal
from typing import override
import threading

class Habitacion:
    def __init__(self, numero_habitacion: str):
        self.numero_habitacion = numero_habitacion  # Número de la habitación
        self.reservada: bool = False  # Estado de reserva inicial
        self.fecha_reserva: datetime = None  # Fecha de reserva (si hay una)

    # Método que revisa todas las habitaciones y libera las que ya no están reservadas
    @classmethod
    def chequear_habitaciones(cls):
        for terminal in Terminal.get_terminales():
            for hospedaje in terminal.get_hospedajes():
                for habitacion in hospedaje.get_habitaciones():
                    if habitacion.get_fecha_reserva() is not None:
                        if habitacion.get_fecha_reserva() <= datetime.now():
                            # Libera la habitación si la fecha de reserva ha pasado
                            habitacion.liberar()
                        else:
                            # Programa la liberación de la habitación 
                            # # cuando la reserva expire
                            duracion = habitacion.get_fecha_reserva() - datetime.now()
                            minutos = int(duracion.total_seconds() // 60)
                            threading.Timer(minutos * 60, habitacion.liberar).start()

    # Método para reservar una habitación de un hospedaje por un cierto período de tiempo, 
    # usado en la funcionalidad 4
    def reservar(self, fecha_reserva: datetime):
        # Marca la habitación como reservada y establece la fecha de reserva
        self.reservada = True
        self.fecha_reserva = fecha_reserva

    # Método para liberar una habitación de un hospedaje, usado en la funcionalidad 4
    def liberar(self):
        # Marca la habitación como no reservada y elimina la fecha de reserva
        self.reservada = False
        self.fecha_reserva = None

    # Método que calcula el tiempo restante hasta que la habitación esté disponible
    def disponible_en(self):
        if self.fecha_reserva:
            ahora = datetime.now()  # Obtiene la fecha y hora actuales
            duracion = self.fecha_reserva - ahora  # Calcula la diferencia de tiempo
            dias = duracion.days
            horas, resto = divmod(duracion.seconds, 3600)  # Convierte el resto en horas 
                                                            # y minutos
            minutos, _ = divmod(resto, 60)
            return f"{dias} días {horas} horas {minutos} minutos"
        return None

    # Representa la habitación en formato de cadena
    @override
    def __str__(self):
        estado_reserva = "Sí" if self.reservada else "No"
        return (f"    {self.numero_habitacion}                      {estado_reserva}" 
                + f"            {self.disponible_en()}")
   
    # Getters y setters
    def get_numero_habitacion(self):
        return self.numero_habitacion

    def set_numero_habitacion(self, numero_habitacion):
        self.numero_habitacion = numero_habitacion

    def is_reservada(self):
        return self.reservada

    def set_reservada(self, reservada):
        self.reservada = reservada

    def get_fecha_reserva(self):
        return self.fecha_reserva

    def set_fecha_reserva(self, fecha_reserva):
        self.fecha_reserva = fecha_reserva