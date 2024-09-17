from Excepciones.ErrorAplicacion import ErrorAplicacion
from Excepciones.ExcepcionNoEncontrado import ExcepcionNoEncontrado

class ExcepcionHospedaje(ExcepcionNoEncontrado):
    mensaje=ExcepcionNoEncontrado.mensaje+" : Ningun hospedaje con ese nombre y/o ubicacion"
    def __init__(self,mensaje2='Ningun hospedaje con ese nombre y/o ubicacion'):
        ExcepcionHospedaje.mensaje=ExcepcionNoEncontrado.mensaje+" : "+mensaje2
        super().__init__(ExcepcionHospedaje.mensaje)