from datetime import datetime, timedelta
from gestor_aplicacion.gestion import Empresa, TipoAsiento
from concurrent.futures import ThreadPoolExecutor
import threading

class Asiento:
    asientos = []

    def __init__(self, numero="Indefinido", tipo_asiento=None):
        self.numero = numero
        self.reservado = False
        self.fecha_reserva = None
        self.tipo_asiento = tipo_asiento
        Asiento.asientos.append(self)

    @staticmethod
    def chequear_asientos():
        for empresa in Empresa.get_empresas():
            for viaje in empresa.get_viajes():
                for asiento in viaje.lista_asientos():
                    if asiento.get_fecha_reserva() is not None:
                        if asiento.get_fecha_reserva() <= datetime.now():
                            asiento.liberar()
                        else:
                            duration = asiento.get_fecha_reserva() - datetime.now()
                            service = ThreadPoolExecutor(max_workers=1)
                            task = threading.Timer(duration.total_seconds(), asiento.liberar)
                            task.start()

    @staticmethod
    def buscar_asiento(numero, tipo):
        for asiento in Asiento.asientos:
            if asiento.get_numero() is not None and asiento.get_tipo_asiento() is not None:
                if asiento.get_numero() == numero and asiento.get_tipo_asiento() == TipoAsiento[tipo]:
                    return asiento
        return None

    def reservar(self, fecha_reserva=None):
        self.reservado = True
        self.fecha_reserva = fecha_reserva

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def is_reservado(self):
        return self.reservado

    def set_reservado(self, reservado):
        self.reservado = reservado

    def get_fecha_reserva(self):
        return self.fecha_reserva

    def set_fecha_reserva(self, fecha_reserva):
        self.fecha_reserva = fecha_reserva

    def __str__(self):
        return f"{self.numero} {self.tipo_asiento}"

    def get_tipo_asiento(self):
        return self.tipo_asiento

    def liberar(self):
        self.set_reservado(False)
        self.set_fecha_reserva(None)

    @staticmethod
    def get_asientos():
        return Asiento.asientos

    @staticmethod
    def set_asientos(asientos):
        Asiento.asientos = asientos