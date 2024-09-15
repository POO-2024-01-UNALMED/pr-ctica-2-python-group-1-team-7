from datetime import datetime, time, date

class Empresa:
    empresas: list['Empresa'] = []

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.viajes = []
        Empresa.empresas.append(self)

    # Método para buscar viajes por fecha, usado en el filtro de la funcionalidad 1
    @classmethod
    def buscar_viajes_por_fecha(cls, fecha: date):
        viajes = []
        for empresa in cls.empresas:
            for viaje in empresa.get_viajes():
                if viaje.get_fecha() == fecha:
                    viajes.append(viaje)
        return viajes

    # Método para buscar viajes por origen y destino, usado en la funcionalidad 1 y 2
    @classmethod
    def buscar_viajes_por_origen_destino(cls, origen: str, destino: str):
        viajes = []
        if (destino == ""):
            for empresa in cls.empresas:
                for viaje in empresa.get_viajes():
                    if viaje.get_origen() == origen:
                        viajes.append(viaje)
        elif (origen == ""):
            for empresa in cls.empresas:
                for viaje in empresa.get_viajes():
                    if viaje.get_destino() == destino:
                        viajes.append(viaje)
        else:
            for empresa in cls.empresas:
                for viaje in empresa.get_viajes():
                    if viaje.tiene_sillas():
                        if (
                            viaje.get_origen() == origen 
                            and viaje.get_destino() == destino 
                            and datetime.now() < datetime.combine(
                                viaje.get_fecha(), 
                                viaje.get_hora()
                            )
                        ):
                            viajes.append(viaje)
        return viajes

    # Método para buscar viajes por hora, usado en el filtro de la funcionalidad 1
    @classmethod
    def buscar_viajes_por_hora(cls, hora: time):
        viajes = []
        for empresa in cls.empresas:
            for viaje in empresa.get_viajes():
                if viaje.get_hora() == hora:
                    viajes.append(viaje)
        return viajes

    # Método para buscar un viaje por id, usado en varias funcionalidades
    @classmethod
    def buscar_viaje_por_id(cls, id_: str):
        for empresa in cls.empresas:
            for viaje in empresa.get_viajes():
                if viaje.get_id() == id_:
                    return viaje
        return None

    # Método para agregar un viaje a la lista de viajes
    def agregar_viaje(self, viaje: 'Viaje'):
        self.get_viajes.append(viaje)

    # Getters y setters 
    @classmethod
    def get_empresas(cls):
        return cls.empresas

    @classmethod
    def set_empresas(cls, empresas):
        cls.empresas = empresas

    def get_viajes(self):
        return self.viajes

    def set_viajes(self, viajes):
        self.viajes = viajes

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre