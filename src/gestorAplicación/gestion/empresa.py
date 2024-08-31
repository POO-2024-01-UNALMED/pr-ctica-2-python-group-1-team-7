from datetime import datetime, time, date
from viaje import Viaje

class Empresa:
    empresas = []

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.viajes = []
        Empresa.empresas.append(self)

    # Método para buscar viajes por fecha, usado en el filtro de la funcionalidad 1
    @classmethod
    def buscar_viajes_por_fecha(fecha: date):
        viajes = []
        for empresa in Empresa.empresas:
            for viaje in empresa.get_viajes():
                if viaje.get_fecha() == fecha:
                    viajes.append(viaje)
        return viajes

    # Método para buscar viajes por origen y destino, usado en la funcionalidad 1 y 2
    @classmethod
    def buscar_viajes_por_origen_destino(origen: str, destino: str):
        viajes = []
        if (destino == ""):
            for empresa in Empresa.empresas:
                for viaje in empresa.get_viajes():
                    if viaje.get_origen == origen:
                        viajes.append(viaje)
        elif (origen == ""):
            for empresa in Empresa.empresas:
                for viaje in empresa.get_viajes():
                    if viaje.get_destino == destino:
                        viajes.append(viaje)
        else:
            for empresa in Empresa.empresas:
                for viaje in empresa.get_viajes():
                    if viaje.tiene_sillas():
                        if (viaje.get_origen == origen 
                                and viaje.get_destino == destino 
                                and datetime.now() 
                                    < datetime.combine(viaje.get_fecha(), 
                                                        viaje.get_hora())):
                            viajes.append(viaje)
        return viajes

    # Método para buscar viajes por hora, usado en el filtro de la funcionalidad 1
    @classmethod
    def buscar_viajes_por_hora(hora: time):
        viajes = []
        for empresa in Empresa.empresas:
            for viaje in empresa.get_viajes():
                if viaje.get_hora() == hora:
                    viajes.append(viaje)
        return viajes

    # Método para buscar un viaje por id, usado en varias funcionalidades
    @classmethod
    def buscar_viaje_por_id(id_: str):
        for empresa in Empresa.empresas:
            for viaje in empresa.get_viajes():
                if viaje.get_id() == id_:
                    return viaje
        return None

    # Getters y setters 
    @classmethod
    def get_empresas():
        return Empresa.empresas

    @classmethod
    def set_empresas(empresas):
        Empresa.empresas = empresas

    def get_viajes(self):
        return self.viajes

    def set_viajes(self, viajes):
        self.viajes = viajes

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre