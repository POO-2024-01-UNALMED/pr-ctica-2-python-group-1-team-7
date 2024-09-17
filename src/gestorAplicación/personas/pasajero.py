from datetime import date
from typing import override
from ..gestion.empresa import Empresa
from .persona import Persona

class Pasajero(Persona):
    pasajeros: list['Pasajero'] = []  # Lista estática para almacenar todos los pasajeros

    def __init__(self, nombre="Sin nombre", id_pasajero="0", telefono="0000000000", 
                    correo="No tiene"):
        # Inicializa un objeto Pasajero con nombre, id, teléfono y correo opcionales.
        # Llama al constructor de la clase base Persona.
        super().__init__(nombre, id_pasajero, telefono, correo)
        self.tiquetes = []  # Lista para almacenar los tiquetes del pasajero
        Pasajero.pasajeros.append(self)  # Agrega el pasajero a la lista de pasajeros

    # Método para buscar un pasajero por id, usado en varias funcionalidades
    @classmethod
    def buscar_pasajero(cls, id_pasajero: str):
        # Devuelve el pasajero encontrado o None si no se encuentra.
        for pasajero in cls.pasajeros:
            if pasajero.get_id() == id_pasajero:
                return pasajero
        return None

    # Método para buscar los tiquetes válidos y vencidos asociados con un pasajero,
    # usado en la funcionalidad 3
    def buscar_tiquetes(self, tipo_tiquetes: str):
        # Devuelve una lista de tiquetes válidos o vencidos.
        tiquetes_validos = []
        tiquetes_vencidos = []

        for tiquete in self.tiquetes:
            # Actualiza la información del viaje
            tiquete.set_viaje(Empresa.buscar_viaje(tiquete.get_viaje().get_id())) 
            if tipo_tiquetes == "validos" and (tiquete.get_viaje().get_fecha() 
                                                > date.today()):
                tiquetes_validos.append(tiquete)
            elif tipo_tiquetes == "vencidos" and (tiquete.get_viaje().get_fecha() 
                                                    < date.today()):
                tiquetes_vencidos.append(tiquete)

        if tipo_tiquetes == "validos":
            return tiquetes_validos
        elif tipo_tiquetes == "vencidos":
            return tiquetes_vencidos
        else:
            return None

    #  Método para buscar un tiquete de acuerdo al viaje, usado en la funcionalidad 3
    def buscar_tiquete_por_viaje(self, viaje):
        # Devuelve el tiquete encontrado o None si no se encuentra.
        for tiquete in self.tiquetes:
            # Actualiza la información del viaje
            tiquete.set_viaje(Empresa.buscar_viaje(tiquete.get_viaje().get_id()))  
            if tiquete.get_viaje() == viaje:
                return tiquete
        return None

    # Método para buscar un tiquete de acuerdo al numero de reserva, 
    # usado en la funcionalidad 3
    def buscar_tiquete_por_reserva(self, numero_reserva: str):
        # Devuelve el tiquete encontrado o None si no se encuentra.
        for tiquete in self.tiquetes:
            if tiquete.get_numero_reserva() == numero_reserva:
                return tiquete
        return None

    # Método para agregar un tiquete, usado en la funcionalidad 2
    def agregar_tiquete(self, tiquete):
        self.tiquetes.append(tiquete)   

    # Método que cancela un tiquete específico liberando el asiento y 
    # eliminando el tiquete de la lista.
    def cancelar_tiquete(self, tiquete):
        for _tiquete in self.tiquetes:
            if _tiquete == tiquete:
                _tiquete.liberar_asiento()  # Libera el asiento asociado
                self.tiquetes.remove(_tiquete)  # Elimina el tiquete de la lista
                break

    # Devuelve una representación en cadena del pasajero.
    @override
    def __str__(self):
        # Muestra el nombre, ID, teléfono y correo del pasajero.
        return (f"     {self.get_nombre()}        {self.get_id()}        " + 
                f"{self.get_telefono()}           {self.get_correo()}     ")
    
    # Getters y setters
    @classmethod
    def get_pasajeros(cls):
        # Obtiene la lista de todos los pasajeros.
        return cls.pasajeros

    @classmethod
    def set_pasajeros(cls, pasajeros):
        # Establece la lista de todos los pasajeros.
        cls.pasajeros = pasajeros
        
    def get_tiquetes(self):
        # Obtiene la lista de tiquetes del pasajero.
        return self.tiquetes

    def set_tiquetes(self, tiquetes):
        # Establece la lista de tiquetes del pasajero.
        self.tiquetes = tiquetes