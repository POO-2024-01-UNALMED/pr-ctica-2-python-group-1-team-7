class Persona:
    def __init__(self, nombre: str = "", id_: str = "", telefono: str = None, 
                    correo: str = None):
        self.nombre = nombre
        self.id = id_
        self.telefono = telefono
        self.correo = correo

    def buscar_tiquete_por_reserva(self, numero_reserva: str):
        return None

    def buscar_tiquetes(self, tipo_tiquetes: str):
        return None

    def agregar_tiquete(self, tiquete: 'Tiquete'):
        pass

    def cancelar_tiquete(self, tiquete: 'Tiquete'):
        pass

    # Getters and Setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):
        self.correo = correo