from datetime import date
from typing import override
from gestion import Empresa, Tiquete, Viaje
from personas.persona import Persona

class Pasajero(Persona):
    pasajeros:list['Pasajero'] = []  # Lista estática para almacenar todos los pasajeros

    def __init__(self, nombre="Sin nombre", id_pasajero="0", telefono="0000000000", correo="No tiene"):
        # Inicializa un objeto Pasajero con nombre, id, teléfono y correo opcionales.
        # Llama al constructor de la clase base Persona.
        super().__init__(nombre, id_pasajero, telefono, correo)
        self.tiquetes = []  # Lista para almacenar los tiquetes del pasajero
        Pasajero.pasajeros.append(self)  # Agrega el pasajero a la lista de pasajeros

    @staticmethod
    def buscar_pasajero(id_pasajero):
        # Busca un pasajero por su ID.
        # Devuelve el pasajero encontrado o None si no se encuentra.
        for pasajero in Pasajero.pasajeros:
            if pasajero.get_id() == id_pasajero:
                return pasajero
        return None

    @staticmethod
    def buscar_pasajero_por_nombre(nombre, id_pasajero):
        # Busca un pasajero por su nombre y ID.
        # Devuelve el pasajero encontrado o None si no se encuentra.
        for pasajero in Pasajero.pasajeros:
            if pasajero.nombre == nombre and pasajero.id is not None:
                if pasajero.id == id_pasajero:
                    return pasajero
        return None

    def buscar_tiquetes(self, tipo_tiquetes):
        # Busca tiquetes válidos o vencidos según el tipo especificado.
        # Devuelve una lista de tiquetes válidos o vencidos.
        tiquetes_validos = []
        tiquetes_vencidos = []

        for tiquete in self.tiquetes:
            tiquete.set_viaje(Empresa.buscar_viaje(tiquete.get_viaje().get_id()))  # Actualiza la información del viaje
            if tipo_tiquetes == "validos" and tiquete.get_viaje().get_fecha() > date.today():
                tiquetes_validos.append(tiquete)
            elif tipo_tiquetes == "vencidos" and tiquete.get_viaje().get_fecha() < date.today():
                tiquetes_vencidos.append(tiquete)

        if tipo_tiquetes == "validos":
            return tiquetes_validos
        elif tipo_tiquetes == "vencidos":
            return tiquetes_vencidos
        else:
            return None

    def buscar_tiquete_por_viaje(self, viaje):
        # Busca un tiquete específico asociado con un viaje dado.
        # Devuelve el tiquete encontrado o None si no se encuentra.
        for tiquete in self.tiquetes:
            tiquete.set_viaje(Empresa.buscar_viaje(viaje.get_id()))  # Actualiza la información del viaje
            if tiquete.get_viaje() == viaje:
                return tiquete
        return None

    def buscar_tiquete_por_reserva(self, numero_reserva):
        # Busca un tiquete por su número de reserva.
        # Devuelve el tiquete encontrado o None si no se encuentra.
        for tiquete in self.tiquetes:
            if tiquete.get_numero_reserva() == numero_reserva:
                return tiquete
        return None

    def cancelar_tiquete(self, tiquete):
        # Cancela un tiquete específico liberando el asiento y eliminando el tiquete de la lista.
        for _tiquete in self.tiquetes:
            if _tiquete == tiquete:
                _tiquete.liberar_asiento()  # Libera el asiento asociado
                self.tiquetes.remove(_tiquete)  # Elimina el tiquete de la lista
                break

    def agregar_tiquete(self, tiquete):
        # Agrega un tiquete a la lista de tiquetes del pasajero.
        self.tiquetes.append(tiquete)

    def get_tiquetes(self):
        # Obtiene la lista de tiquetes del pasajero.
        return self.tiquetes

    def set_tiquetes(self, tiquetes):
        # Establece la lista de tiquetes del pasajero.
        self.tiquetes = tiquetes

    @staticmethod
    def get_pasajeros():
        # Obtiene la lista de todos los pasajeros.
        return Pasajero.pasajeros

    @staticmethod
    def set_pasajeros(pasajeros):
        # Establece la lista de todos los pasajeros.
        Pasajero.pasajeros = pasajeros

    @staticmethod
    def eliminar_pasajero_por_nombre(nombre, id_pasajero):
        # Elimina un pasajero de la lista por su nombre y ID.
        pasajero = Pasajero.buscar_pasajero_por_nombre(nombre, id_pasajero)
        if pasajero:
            Pasajero.pasajeros.remove(pasajero)

    @staticmethod
    def eliminar_pasajero_por_id(id_pasajero):
        # Elimina un pasajero de la lista por su ID.
        pasajero = Pasajero.buscar_pasajero(id_pasajero)
        if pasajero:
            Pasajero.pasajeros.remove(pasajero)

    @override
    def __str__(self):
        # Devuelve una representación en cadena del pasajero.
        # Muestra el nombre, ID, teléfono y correo del pasajero.
        return f"     {self.get_nombre()}        {self.get_id()}        {self.get_telefono()}           {self.get_correo()}     "