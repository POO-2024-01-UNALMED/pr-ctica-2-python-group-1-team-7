from datetime import datetime, timedelta
from gestion import Empresa, TipoAsiento
from concurrent.futures import ThreadPoolExecutor
import threading

class Asiento:
    asientos:list['Asiento'] = []  # Lista estática para almacenar todos los asientos

    def __init__(self, numero="Indefinido", tipo_asiento=None):
        # Inicializa un objeto Asiento con el número y tipo de asiento dados.
        # Si no se especifica un número, se usa "Indefinido".
        # Si no se especifica un tipo, se usa None.
        self.numero = numero
        self.reservado = False  # Estado de reserva inicial
        self.fecha_reserva = None  # Fecha de reserva inicial
        self.tipo_asiento = tipo_asiento  # Tipo de asiento
        Asiento.asientos.append(self)  # Agrega el asiento a la lista de asientos

    @staticmethod
    def chequear_asientos():
        # Verifica y libera asientos cuyo tiempo de reserva ha expirado.
        # Utiliza hilos para programar la liberación de asientos en el futuro.
        for empresa in Empresa.get_empresas():  # Itera sobre todas las empresas
            for viaje in empresa.get_viajes():  # Itera sobre todos los viajes de la empresa
                for asiento in viaje.lista_asientos():  # Itera sobre todos los asientos del viaje
                    if asiento.get_fecha_reserva() is not None:
                        if asiento.get_fecha_reserva() <= datetime.now():
                            asiento.liberar()  # Libera el asiento si la fecha de reserva ha pasado
                        else:
                            duration = asiento.get_fecha_reserva() - datetime.now()  # Calcula la duración hasta la liberación
                            # Utiliza un hilo para liberar el asiento después de la duración especificada
                            service = ThreadPoolExecutor(max_workers=1)
                            task = threading.Timer(duration.total_seconds(), asiento.liberar)
                            task.start()

    @staticmethod
    def buscar_asiento(numero, tipo):
        # Busca un asiento por su número y tipo.
        # Devuelve el asiento encontrado o None si no se encuentra.
        for asiento in Asiento.asientos:  # Itera sobre todos los asientos
            if asiento.get_numero() is not None and asiento.get_tipo_asiento() is not None:
                if asiento.get_numero() == numero and asiento.get_tipo_asiento() == TipoAsiento[tipo]:
                    return asiento
        return None

    def reservar(self, fecha_reserva=None):
        # Reserva el asiento para una fecha dada.
        # Si no se proporciona una fecha, solo marca el asiento como reservado.
        self.reservado = True
        self.fecha_reserva = fecha_reserva

    def get_numero(self):
        # Obtiene el número del asiento.
        return self.numero

    def set_numero(self, numero):
        # Establece el número del asiento.
        self.numero = numero

    def is_reservado(self):
        # Verifica si el asiento está reservado.
        # Devuelve True si está reservado, False en caso contrario.
        return self.reservado

    def set_reservado(self, reservado):
        # Establece el estado de reserva del asiento.
        self.reservado = reservado

    def get_fecha_reserva(self):
        # Obtiene la fecha de reserva del asiento.
        return self.fecha_reserva

    def set_fecha_reserva(self, fecha_reserva):
        # Establece la fecha de reserva del asiento.
        self.fecha_reserva = fecha_reserva

    def __str__(self):
        # Devuelve una representación en cadena del asiento.
        # Muestra el número y el tipo de asiento.
        return f"{self.numero} {self.tipo_asiento}"

    def get_tipo_asiento(self):
        # Obtiene el tipo de asiento.
        return self.tipo_asiento

    def liberar(self):
        # Libera el asiento, estableciendo el estado de reserva a False y la fecha de reserva a None.
        self.set_reservado(False)
        self.set_fecha_reserva(None)

    @staticmethod
    def get_asientos():
        # Obtiene la lista de todos los asientos.
        return Asiento.asientos

    @staticmethod
    def set_asientos(asientos):
        # Establece la lista de todos los asientos.
        Asiento.asientos = asientos