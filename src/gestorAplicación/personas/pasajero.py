from datetime import date
from gestorAplicacion.gestion import Empresa, Tiquete, Viaje
from gestorAplicacion.personas.persona import Persona


class Pasajero(Persona):
    pasajeros = []

    def __init__(self, nombre="Sin nombre", idPasajero="0", telefono="0000000000", correo="No tiene"):
        super().__init__(nombre, idPasajero, telefono, correo)
        self.tiquetes = []
        Pasajero.pasajeros.append(self)

    @staticmethod
    def buscarPasajero(idPasajero):
        for pasajero in Pasajero.pasajeros:
            if pasajero.getId() == idPasajero:
                return pasajero
        return None

    @staticmethod
    def buscarPasajeroPorNombre(nombre, idPasajero):
        for pasajero in Pasajero.pasajeros:
            if pasajero.nombre == nombre and pasajero.id is not None:
                if pasajero.id == idPasajero:
                    return pasajero
        return None

    def buscarTiquetes(self, tipoTiquetes):
        tiquetesValidos = []
        tiquetesVencidos = []

        for tiquete in self.tiquetes:
            tiquete.setViaje(Empresa.buscarViaje(tiquete.getViaje().getId()))
            if tipoTiquetes == "validos" and tiquete.getViaje().getFecha() > date.today():
                tiquetesValidos.append(tiquete)
            elif tipoTiquetes == "vencidos" and tiquete.getViaje().getFecha() < date.today():
                tiquetesVencidos.append(tiquete)

        if tipoTiquetes == "validos":
            return tiquetesValidos
        elif tipoTiquetes == "vencidos":
            return tiquetesVencidos
        else:
            return None

    def buscarTiquetePorViaje(self, viaje):
        for tiquete in self.tiquetes:
            tiquete.setViaje(Empresa.buscarViaje(viaje.getId()))
            if tiquete.getViaje() == viaje:
                return tiquete
        return None

    def buscarTiquetePorReserva(self, numeroReserva):
        for tiquete in self.tiquetes:
            if tiquete.getNumeroReserva() == numeroReserva:
                return tiquete
        return None

    def cancelarTiquete(self, tiquete):
        for _tiquete in self.tiquetes:
            if _tiquete == tiquete:
                _tiquete.liberarAsiento()
                self.tiquetes.remove(_tiquete)
                break

    def agregarTiquete(self, tiquete):
        self.tiquetes.append(tiquete)

    def getTiquetes(self):
        return self.tiquetes

    def setTiquetes(self, tiquetes):
        self.tiquetes = tiquetes

    @staticmethod
    def getPasajeros():
        return Pasajero.pasajeros

    @staticmethod
    def setPasajeros(pasajeros):
        Pasajero.pasajeros = pasajeros

    @staticmethod
    def eliminarPasajeroPorNombre(nombre, idPasajero):
        pasajero = Pasajero.buscarPasajeroPorNombre(nombre, idPasajero)
        if pasajero:
            Pasajero.pasajeros.remove(pasajero)

    @staticmethod
    def eliminarPasajeroPorId(idPasajero):
        pasajero = Pasajero.buscarPasajero(idPasajero)
        if pasajero:
            Pasajero.pasajeros.remove(pasajero)

    def __str__(self):
        return f"     {self.getNombre()}        {self.getId()}        {self.getTelefono()}           {self.getCorreo()}     "
