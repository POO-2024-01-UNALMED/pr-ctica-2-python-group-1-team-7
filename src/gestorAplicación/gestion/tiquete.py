from typing import override

class Tiquete:
    numeros_reserva = 1000000  # Contador para generar números de reserva únicos

    def __init__(self, pasajero: 'Pasajero', viaje: 'Viaje', asiento: 'Asiento', 
                    hospedaje: 'Hospedaje' = None):
        # Inicializa un nuevo tiquete con los datos proporcionados
        self.pasajero = pasajero  # El pasajero asociado con el tiquete
        self.viaje = viaje  # El viaje asociado con el tiquete
        self.asiento = asiento  # El asiento reservado
        self.hospedaje = hospedaje  # Información de hospedaje, si aplica
        self.numero_reserva = str(Tiquete.numeros_reserva)  # Asigna un número de 
                                                            # reserva único
        Tiquete.numeros_reserva += 1  # Incrementa el contador de números de reserva

    # Método para cambiar el asiento de un pasajero en un viaje por otro asiento, 
    # usado en la funcionalidad 3
    def cambiar_asiento(self, nuevo_asiento: 'Asiento'):
        self.liberar_asiento()  # Libera el asiento actual
        self.viaje.reservar_asiento(nuevo_asiento.get_numero, None)  # Reserva el 
                                                                        # nuevo asiento
        self.asiento = nuevo_asiento  # Actualiza el asiento en el tiquete

    # Método para que un pasajero pueda cambiar de viaje, usado en la funcionalidad 3
    def cambiar_viaje(self, nuevo_viaje: 'Viaje', numero_asiento: str):
        self.liberar_asiento()  # Libera el asiento actual
        self.viaje = nuevo_viaje  # Asigna el nuevo viaje al tiquete
        self.asiento = nuevo_viaje.buscar_asiento(numero_asiento)  # Encuentra y asigna
                                                                    # el nuevo asiento
        nuevo_viaje.reservar_asiento(numero_asiento, None)  # Reserva el nuevo asiento 
                                                            # en el nuevo viaje

    # Método para que un asiento se libere después de un cierto período de tiempol, 
    # usado en la funcionalidad 1
    def liberar_asiento(self):
        self.viaje = Empresa.buscar_viaje(self.viaje.get_id)  # Actualiza el viaje 
                                                                # del tiquete
        self.viaje.liberar_asiento(self.asiento.get_numero)  # Libera el asiento 
                                                                # en el viaje

    # Representa el tiquete como una cadena con formato específico
    @override
    def __str__(self): 
        # Calcula los espacios necesarios para el nombre
        nombre_espacios = 9 - len(self.pasajero.nombre)  

        # Calcula los espacios para el asiento
        asiento_espacios = 16 - len(f"{self.asiento.numero} {self.asiento.tipo_asiento}")  
    
        # Espacios para el nombre y el asiento
        espacio_nombre = ' ' * nombre_espacios if nombre_espacios > 0 else ''
        espacio_asiento = ' ' * asiento_espacios if asiento_espacios > 0 else ''

        # Devuelve una cadena formateada con la información del tiquete
        return (f"    {self.numero_reserva}               {self.pasajero.nombre}"
                f"{espacio_nombre}     {self.asiento}{espacio_asiento}    "
                f"{self.viaje.str_fecha} {self.viaje.hora}     {self.viaje.id}")

    # Getters y setters
    @classmethod
    def get_numeros_reserva(cls):
        # Devuelve el contador actual de números de reserva
        return cls.numeros_reserva

    @classmethod
    def set_numeros_reserva(cls, numeros_reserva):
        # Establece el contador de números de reserva a un valor específico
        cls.numeros_reserva = numeros_reserva

    def get_pasajero(self):
        # Devuelve el pasajero asociado con el tiquete
        return self.pasajero

    def set_pasajero(self, pasajero):
        # Establece el pasajero asociado con el tiquete
        self.pasajero = pasajero

    def get_viaje(self):
        # Devuelve el viaje asociado con el tiquete
        return self.viaje

    def set_viaje(self, viaje):
        # Establece el viaje asociado con el tiquete
        self.viaje = viaje

    def get_asiento(self):
        # Devuelve el asiento asociado con el tiquete
        return self.asiento

    def set_asiento(self, asiento):
        # Establece el asiento asociado con el tiquete
        self.asiento = asiento

    def get_hospedaje(self):
        # Devuelve la información de hospedaje asociada con el tiquete
        return self.hospedaje

    def set_hospedaje(self, hospedaje):
        # Establece la información de hospedaje asociada con el tiquete
        self.hospedaje = hospedaje

    def get_numero_reserva(self):
        # Devuelve el número de reserva del tiquete
        return self.numero_reserva

    def set_numero_reserva(self, numero_reserva):
        # Establece el número de reserva del tiquete
        self.numero_reserva = numero_reserva