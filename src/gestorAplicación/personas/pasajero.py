from datetime import date
from gestor_aplicacion.gestion import Empresa, Tiquete, Viaje
from gestor_aplicacion.personas.persona import Persona


class Pasajero(Persona):
    pasajeros = []

    def __init__(self, nombre="Sin nombre", id_pasajero="0", telefono="0000000000", correo="No tiene"):
        super().__init__(nombre, id_pasajero, telefono, correo)
        self.tiquetes = []
        Pasajero.pasajeros.append(self)

    @staticmethod
    def buscar_pasajero(id_pasajero):
        for pasajero in Pasajero.pasajeros:
            if pasajero.get_id() == id_pasajero:
                return pasajero
        return None

    @staticmethod
    def buscar_pasajero_por_nombre(nombre, id_pasajero):
        for pasajero in Pasajero.pasajeros:
            if pasajero.nombre == nombre and pasajero.id is not None:
                if pasajero.id == id_pasajero:
                    return pasajero
        return None

    def buscar_tiquetes(self, tipo_tiquetes):
        tiquetes_validos = []
        tiquetes_vencidos = []

        for tiquete in self.tiquetes:
            tiquete.set_viaje(Empresa.buscar_viaje(tiquete.get_viaje().get_id()))
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
        for tiquete in self.tiquetes:
            tiquete.set_viaje(Empresa.buscar_viaje(viaje.get_id()))
            if tiquete.get_viaje() == viaje:
                return tiquete
        return None

    def buscar_tiquete_por_reserva(self, numero_reserva):
        for tiquete in self.tiquetes:
            if tiquete.get_numero_reserva() == numero_reserva:
                return tiquete
        return None

    def cancelar_tiquete(self, tiquete):
        for _tiquete in self.tiquetes:
            if _tiquete == tiquete:
                _tiquete.liberar_asiento()
                self.tiquetes.remove(_tiquete)
                break

    def agregar_tiquete(self, tiquete):
        self.tiquetes.append(tiquete)

    def get_tiquetes(self):
        return self.tiquetes

    def set_tiquetes(self, tiquetes):
        self.tiquetes = tiquetes

    @staticmethod
    def get_pasajeros():
        return Pasajero.pasajeros

    @staticmethod
    def set_pasajeros(pasajeros):
        Pasajero.pasajeros = pasajeros

    @staticmethod
    def eliminar_pasajero_por_nombre(nombre, id_pasajero):
        pasajero = Pasajero.buscar_pasajero_por_nombre(nombre, id_pasajero)
        if pasajero:
            Pasajero.pasajeros.remove(pasajero)

    @staticmethod
    def eliminar_pasajero_por_id(id_pasajero):
        pasajero = Pasajero.buscar_pasajero(id_pasajero)
        if pasajero:
            Pasajero.pasajeros.remove(pasajero)

    def __str__(self):
        return f"     {self.get_nombre()}        {self.get_id()}        {self.get_telefono()}           {self.get_correo()}     "