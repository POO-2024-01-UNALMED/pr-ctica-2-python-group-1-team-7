from datetime import datetime
from typing import List
from typing import override
from transporte.asiento import Asiento
from habitacion import Habitacion

class Hospedaje:
    # Lista estática para almacenar todos los hospedajes
    hospedajes: List['Hospedaje'] = []

    def __init__(self, nombre="Sin nombre", ubicacion="Sin ubicación"):
        # Inicializa los atributos del hospedaje
        self.nombre = nombre
        self.ubicacion = ubicacion.upper()  # Convierte la ubicación a mayúsculas
        self.habitaciones: List['Habitacion'] = []  # Lista de habitaciones del hospedaje
        self.calificaciones: List[str] = []  # Lista de calificaciones como cadenas
        self.calificacion = 0.0  # Calificación promedio del hospedaje
        self.terminal = None  # Terminal asociado al hospedaje
        Hospedaje.hospedajes.append(self)  # Agrega el nuevo hospedaje a la lista estática
        self.crear_habitaciones(3, 5)  # Llama al método para crear habitaciones por defecto

    def crear_habitaciones(self, pisos, habitaciones_piso):
        # Crea habitaciones para el hospedaje
        for piso in range(100, pisos * 100 + 1, 100):
            for habitacion in range(1, habitaciones_piso + 1):
                numero_habitacion = f"{piso + habitacion}"  # Número de habitación en formato string
                copia_habitacion = Habitacion(numero_habitacion)  # Crea una nueva habitación
                self.habitaciones.append(copia_habitacion)  # Agrega la habitación a la lista
                copia_habitacion.set_hospedaje(self)  # Asocia la habitación con el hospedaje

    def tiene_habitaciones(self):
        # Verifica si hay al menos una habitación disponible
        for habitacion in self.habitaciones:
            if not habitacion.is_reservada():
                return True  # Retorna True si encuentra una habitación no reservada
        return False  # Retorna False si todas las habitaciones están reservadas

    def buscar_habitacion(self, numero_habitacion):
        # Busca una habitación por su número
        for habitacion in self.habitaciones:
            if habitacion.get_numero_habitacion() == numero_habitacion:
                return habitacion  # Retorna la habitación si se encuentra
        return None  # Retorna None si no se encuentra la habitación

    def habitaciones_disponibles(self):
        # Cuenta el número de habitaciones disponibles
        contador = 0
        for habitacion in self.habitaciones:
            if not habitacion.is_reservada():
                contador += 1  # Incrementa el contador si la habitación está disponible
        return contador  # Retorna el total de habitaciones disponibles

    def reservar_habitacion(self, numero_habitacion: str, fecha_reserva: datetime, tiquete: 'Tiquete'):
        # Reserva una habitación para un tiquete
        habitacion = self.buscar_habitacion(numero_habitacion)
        if habitacion:
            habitacion.reservar(fecha_reserva)  # Reserva la habitación con la fecha proporcionada
            tiquete.set_hospedaje(self)  # Asocia el hospedaje con el tiquete

    @staticmethod
    def buscar_hospedaje(nombre: str, ubicacion: str):
        # Busca un hospedaje por nombre y ubicación
        ubicacion = ubicacion.upper()
        for hospedaje in Hospedaje.hospedajes:
            if hospedaje.nombre == nombre and hospedaje.ubicacion == ubicacion:
                return hospedaje  # Retorna el hospedaje si se encuentra
        return None  # Retorna None si no se encuentra el hospedaje

    def liberar_habitacion(self, numero_habitacion: str):
        # Libera una habitación por su número
        habitacion = self.buscar_habitacion(numero_habitacion)
        if habitacion:
            habitacion.liberar()  # Libera la habitación

    @override
    def __str__(self):
        # Representación en cadena del objeto Hospedaje
        espacio_nombre = " " * (5 - len(self.nombre)) if len(self.nombre) < 5 else ""
        return f"    {self.nombre}{espacio_nombre}      {self.calificacion} estrellas     {self.habitaciones_disponibles()}"

    def get_nombre(self):
        return self.nombre  # Retorna el nombre del hospedaje

    def set_nombre(self, nombre: str):
        self.nombre = nombre  # Establece el nombre del hospedaje

    def get_habitaciones(self):
        return self.habitaciones  # Retorna la lista de habitaciones

    def set_habitaciones(self, habitaciones: List[Habitacion]):
        self.habitaciones = habitaciones  # Establece la lista de habitaciones

    def get_calificacion(self):
        return self.calificacion  # Retorna la calificación promedio

    def set_calificacion(self, calificacion: str):
        # Calcula y establece la calificación promedio del hospedaje
        self.calificaciones.append(calificacion)  # Agrega la nueva calificación a la lista
        if self.calificaciones:
            total = sum(float(c) for c in self.calificaciones)  # Calcula la suma de todas las calificaciones
            self.calificacion = total / len(self.calificaciones)  # Calcula el promedio

    def get_ubicacion(self):
        return self.ubicacion  # Retorna la ubicación del hospedaje

    def set_ubicacion(self, ubicacion: str):
        self.ubicacion = ubicacion.upper()  # Establece la ubicación en mayúsculas

    @staticmethod
    def eliminar_hospedaje(nombre: str, ubicacion: str):
        # Elimina un hospedaje por nombre y ubicación
        ubicacion = ubicacion.upper()
        hospedaje = Hospedaje.buscar_hospedaje(nombre, ubicacion)
        if hospedaje:
            Hospedaje.hospedajes.remove(hospedaje)  # Elimina el hospedaje de la lista estática

    def eliminar_habitacion(self, numero: str):
        # Elimina una habitación por su número
        habitacion = self.buscar_habitacion(numero)
        if habitacion:
            self.habitaciones.remove(habitacion)  # Elimina la habitación de la lista

    def set_terminal(self, terminal):
        self.terminal = terminal  # Establece el terminal asociado

    def get_terminal(self):
        return self.terminal  # Retorna el terminal asociado

    @staticmethod
    def get_hospedajes():
        return Hospedaje.hospedajes  # Retorna la lista de todos los hospedajes