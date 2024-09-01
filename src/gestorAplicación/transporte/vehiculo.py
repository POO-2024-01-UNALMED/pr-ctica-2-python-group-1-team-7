import random
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    placas = []

    def __init__(self, placa: str):
        self.placa = placa

    @abstractmethod
    def crear_asientos(self, filas: int):
        pass

    @classmethod
    def generar_placa(cls):
        letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        while True:
            r1 = random.choice(letras)
            r2 = random.choice(letras)
            r3 = random.choice(letras)
            r4 = str(random.randint(0, 9))
            r5 = str(random.randint(0, 9))
            r6 = str(random.randint(0, 9))
            placa = f"{r1}{r2}{r3}-{r4}{r5}{r6}"

            if cls.verificar_placa(placa):
                cls.placas.append(placa)
                return placa

    @classmethod
    def verificar_placa(cls, placa: str):
        return placa not in cls.placas

    # Getters y setters
    @classmethod
    def get_placas(cls):
        return cls.placas

    @classmethod
    def set_placas(cls,placas: list[str]):
        cls.placas = placas

    def get_placa(self):
        return self.placa

    def set_placa(self, placa: str):
        self.placa = placa