import random
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    # Lista para almacenar las placas de vehículos generadas
    placas = []

    def __init__(self, placa: str):
        # Inicializa el objeto Vehiculo con una placa específica
        self.placa = placa

    @abstractmethod
    def crear_asientos(self, filas: int):
        # Método abstracto que debe ser implementado por las subclases para definir
        # cómo se crean los asientos del vehículo. Recibe el número de filas de asientos.
        pass

    @classmethod
    def generar_placa(cls):
        # Genera una nueva placa de vehículo única
        letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        while True:
            placa = f"{random.choice(letras)}{random.choice(letras)}{random.choice(letras)}-{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
            if cls.verificar_placa(placa):
                cls.placas.append(placa)
                return placa

    @classmethod
    def verificar_placa(cls, placa: str):
        # Verifica si una placa de vehículo ya está en uso
        return placa not in cls.placas

    # Getters y setters
    @classmethod
    def set_placas(cls, placas: list[str]):
        # Establece la lista de placas generadas
        cls.placas = placas

    def get_placa(self):
        # Obtiene la placa del vehículo
        return self.placa

    def set_placa(self, placa: str):
        # Establece la placa del vehículo
        self.placa = placa