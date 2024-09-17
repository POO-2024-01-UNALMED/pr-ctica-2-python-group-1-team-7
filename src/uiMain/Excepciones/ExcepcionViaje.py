from Excepciones.ErrorAplicacion import ErrorAplicacion
from Excepciones.ExcepcionNoEncontrado import ExcepcionNoEncontrado

class ExcepcionViaje(ExcepcionNoEncontrado):
    mensaje=ExcepcionNoEncontrado.mensaje+" : Ningun viaje con ese Id"
    def __init__(self,mensaje2='Ningun viaje con ese Id'):
        ExcepcionViaje.mensaje=ExcepcionNoEncontrado.mensaje+" : "+mensaje2
        super().__init__(ExcepcionViaje.mensaje)

