class Terminal:
    terminales: list['Terminal'] = []

    def __init__(self, ubicacion: str):
        self.ubicacion = ubicacion.upper()
        self.hospedajes: list['Hospedaje'] = []
        Terminal.terminales.append(self)

    # Método para agregar un hospedaje a la lista de hospedajes
    def agregar_hospedaje(self, hospedaje: 'Hospedaje'):
        self.hospedajes.append(hospedaje)

    # Getters and Setters
    @classmethod
    def get_terminales(cls):
        return cls.terminales

    @classmethod
    def set_terminales(cls, terminales):
        cls.terminales = terminales

    def get_ubicacion(self):
        return self.ubicacion

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion.upper()

    def get_hospedajes(self):
        return self.hospedajes

    def set_hospedajes(self, hospedajes):
        self.hospedajes = hospedajes