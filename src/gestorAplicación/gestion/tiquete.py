from typing import List, override
import datetime
from gestion.empresa import Empresa
from personas.pasajero import Pasajero
from personas.persona import Persona
from transporte.asiento import Asiento

class Tiquete:
    # Lista estática para almacenar todos los tiquetes
    tiquetes: List['Tiquete'] = []
    numeros_reserva = 1000000  # Contador para generar números de reserva únicos

    def __init__(self, pasajero=None, viaje=None, asiento=None, hospedaje=None):
        # Inicializa un nuevo tiquete con los datos proporcionados
        self.numero_reserva = str(Tiquete.numeros_reserva)  # Asigna un número de reserva único
        self.pasajero = pasajero  # El pasajero asociado con el tiquete
        self.viaje = viaje  # El viaje asociado con el tiquete
        self.asiento = asiento  # El asiento reservado
        self.hospedaje = hospedaje  # Información de hospedaje, si aplica
        Tiquete.tiquetes.append(self)  # Agrega el tiquete a la lista de tiquetes
        Tiquete.numeros_reserva += 1  # Incrementa el contador de números de reserva

    def cambiar_asiento(self, nuevo_asiento):
        # Cambia el asiento reservado para el tiquete
        self.liberar_asiento()  # Libera el asiento actual
        self.viaje.reservar_asiento(nuevo_asiento.numero, None)  # Reserva el nuevo asiento
        self.asiento = nuevo_asiento  # Actualiza el asiento en el tiquete

    def cambiar_viaje(self, nuevo_viaje, numero_asiento):
        # Cambia el viaje asociado con el tiquete
        self.liberar_asiento()  # Libera el asiento actual
        self.viaje = nuevo_viaje  # Asigna el nuevo viaje al tiquete
        self.asiento = nuevo_viaje.buscar_asiento(numero_asiento)  # Encuentra y asigna el nuevo asiento
        nuevo_viaje.reservar_asiento(numero_asiento, None)  # Reserva el nuevo asiento en el nuevo viaje

    def liberar_asiento(self):
        # Libera el asiento en el viaje actual
        viaje = Empresa.buscar_viaje(self.viaje.id)  # Busca el viaje actual usando su ID
        self.viaje = viaje  # Actualiza el viaje del tiquete
        self.viaje.liberar_asiento(self.asiento.numero)  # Libera el asiento en el viaje

    @staticmethod
    def buscar_tiquete(pasajero, viaje, asiento, hospedaje):
        # Busca un tiquete específico en la lista de tiquetes
        for tiquete in Tiquete.tiquetes:
            if (tiquete.pasajero == pasajero and
                tiquete.viaje == viaje and
                tiquete.asiento == asiento and
                tiquete.hospedaje == hospedaje):
                return tiquete  # Devuelve el tiquete si coincide con los parámetros
        return None  # Retorna None si no se encuentra el tiquete

    @override
    def __str__(self):
        # Representa el tiquete como una cadena con formato específico
        nombre_espacios = 9 - len(self.pasajero.nombre)  # Calcula los espacios necesarios para el nombre
        asiento_espacios = 16 - len(f"{self.asiento.numero} {self.asiento.tipo_asiento}")  # Calcula los espacios para el asiento

        # Espacios para el nombre y el asiento
        espacio_nombre = ' ' * nombre_espacios if nombre_espacios > 0 else ''
        espacio_asiento = ' ' * asiento_espacios if asiento_espacios > 0 else ''

        # Devuelve una cadena formateada con la información del tiquete
        return (f"    {self.numero_reserva}               {self.pasajero.nombre}"
                f"{espacio_nombre}     {self.asiento}{espacio_asiento}    "
                f"{self.viaje.str_fecha} {self.viaje.hora}     {self.viaje.id}")

    @staticmethod
    def get_numeros_reserva():
        # Devuelve el contador actual de números de reserva
        return Tiquete.numeros_reserva

    @staticmethod
    def set_numeros_reserva(numeros_reserva):
        # Establece el contador de números de reserva a un valor específico
        Tiquete.numeros_reserva = numeros_reserva

    def get_viaje(self):
        # Devuelve el viaje asociado con el tiquete
        return self.viaje

    def set_viaje(self, viaje):
        # Establece el viaje asociado con el tiquete
        self.viaje = viaje

    def get_pasajero(self):
        # Devuelve el pasajero asociado con el tiquete
        return self.pasajero

    def set_pasajero(self, pasajero):
        # Establece el pasajero asociado con el tiquete
        self.pasajero = pasajero

    def get_asiento(self):
        # Devuelve el asiento asociado con el tiquete
        return self.asiento

    def set_asiento(self, asiento):
        # Establece el asiento asociado con el tiquete
        self.asiento = asiento

    def get_numero_reserva(self):
        # Devuelve el número de reserva del tiquete
        return self.numero_reserva

    def set_numero_reserva(self, numero_reserva):
        # Establece el número de reserva del tiquete
        self.numero_reserva = numero_reserva

    @staticmethod
    def get_tiquetes():
        # Devuelve la lista de todos los tiquetes
        return Tiquete.tiquetes

    def get_hospedaje(self):
        # Devuelve la información de hospedaje asociada con el tiquete
        return self.hospedaje

    def set_hospedaje(self, hospedaje):
        # Establece la información de hospedaje asociada con el tiquete
        self.hospedaje = hospedaje