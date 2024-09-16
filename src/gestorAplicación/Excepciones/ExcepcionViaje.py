from ErrorAplicacion import ErrorAplicacion
from ExcepcionNoEncontrado import ExcepcionNoEncontrado

class ExcepcionViaje(ExcepcionNoEncontrado):
    def __init__(self,mensaje2='Ningun viaje con ese Id'):
        mensaje1=ExcepcionNoEncontrado.mensaje
        ExcepcionViaje.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionViaje.mensaje)
        ExcepcionNoEncontrado.mensaje=mensaje1