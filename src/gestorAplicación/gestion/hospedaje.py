from datetime import datetime
from typing import override
from .habitacion import Habitacion

class Hospedaje:
    def __init__(self, nombre: str = "Sin nombre", pisos: int = 0, 
                    habitaciones_piso: int = 0):
        self.nombre = nombre
        self.habitaciones: list['Habitacion'] = []  # Lista de habitaciones del hospedaje
        self.calificaciones: list[str] = []  # Lista de calificaciones como cadenas
        self.calificacion: float = 0.0  # Calificación promedio del hospedaje
        self.crear_habitaciones(3, 5)  # Llama al método para crear habitaciones 
                                        # por defecto

    # Método para crear las habitaciones de cada hospedaje y que se guarden en el arreglo 
    # de tipo Habitacion. Se llama en el constructor de cada Hospedaje
    def crear_habitaciones(self, pisos: int, habitaciones_piso: int):
        for piso in range(100, (pisos + 1) * 100, 100):
            for habitacion in range(1, habitaciones_piso + 1):
                numero_habitacion = f"{piso + habitacion}"  # Número de habitación 
                                                            # en formato string
                copia_habitacion = Habitacion(numero_habitacion)  # Crea una nueva 
                                                                   # habitación
                self.habitaciones.append(copia_habitacion)  # Agrega la habitación 
                                                            # a la lista

    # Método para buscar una habitación de un hospedaje por el número de habitación, 
    # usado en la funcionalidad 4
    def buscar_habitacion(self, numero_habitacion: str):
        for habitacion in self.habitaciones:
            if habitacion.get_numero_habitacion() == numero_habitacion:
                return habitacion  # Retorna la habitación si se encuentra
        return None  # Retorna None si no se encuentra la habitación

    # Método para verificar si un hospedaje tiene habitaciones disponibles, 
    # usado en la funcionalidad 4
    def tiene_habitaciones(self):
        for habitacion in self.habitaciones:
            if not habitacion.is_reservada():
                return True  # Retorna True si encuentra una habitación no reservada
        return False  # Retorna False si todas las habitaciones están reservadas

    # Método para saber cuántas habitaciones disponibles hay en el hospedaje, 
    # usado en la funcionalidad 4
    def habitaciones_disponibles(self):
        habitaciones_disponibles = 0
        for habitacion in self.habitaciones:
            if not habitacion.is_reservada():
                habitaciones_disponibles += 1  # Incrementa el habitaciones_disponibles 
                                                # si la habitación está disponible
        return habitaciones_disponibles  # Retorna el total de habitaciones disponibles

    # Método para reservar una habitación de un hospedaje por un período de tiempo,
    # usado en la funcionalidad 4
    def reservar_habitacion(self, numero_habitacion: str, fecha_reserva: datetime, 
                                tiquete: 'Tiquete'):
        habitacion = self.buscar_habitacion(numero_habitacion)
        if habitacion:
            habitacion.reservar(fecha_reserva)  # Reserva la habitación con 
                                                # la fecha proporcionada
            tiquete.set_hospedaje(self)  # Asocia el hospedaje con el tiquete

    # Método para liberar una habitación por el número de habitación cuando el período de 
    # tiempo de la reserva se acabe, usado en la funcionalidad 4
    def liberar_habitacion(self, numero_habitacion: str):
        habitacion = self.buscar_habitacion(numero_habitacion)
        if habitacion:
            habitacion.liberar()  # Libera la habitación

    # Representación en cadena del objeto Hospedaje
    @override
    def __str__(self):
     
        espacio_nombre = " " * (5 - len(self.nombre)) if len(self.nombre) < 5 else ""
        return (f"    {self.nombre}{espacio_nombre}      {self.calificacion} estrellas" 
                + f"     {self.habitaciones_disponibles()}")
    
    # Getters y setters 
    def get_nombre(self):
        return self.nombre  # Retorna el nombre del hospedaje

    def set_nombre(self, nombre):
        self.nombre = nombre  # Establece el nombre del hospedaje

    def get_habitaciones(self):
        return self.habitaciones  # Retorna la lista de habitaciones

    def set_habitaciones(self, habitaciones):
        self.habitaciones = habitaciones  # Establece la lista de habitaciones

    def get_calificacion(self):
        return self.calificacion  # Retorna la calificación promedio

    # Calcula y establece la calificación promedio del hospedaje
    def set_calificacion(self, calificacion):
      
        self.calificaciones.append(calificacion)  # Agrega la nueva calificación 
                                                    # a la lista
        if self.calificaciones:
            total = sum(float(c) for c in self.calificaciones)  # Calcula la suma de 
                                                                # todas las calificaciones
            self.calificacion = total / len(self.calificaciones)  # Calcula el promedio