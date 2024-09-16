from ErrorAplicacion import ErrorAplicacion
from ExcepcionNoEncontrado import ExcepcionNoEncontrado

class ExcepcionHospedaje(ExcepcionNoEncontrado):
    def __init__(self,mensaje2='Ningun hospedaje con ese nombre y/o ubicacion'):
        mensaje1=ExcepcionNoEncontrado.mensaje
        ExcepcionHospedaje.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionHospedaje.mensaje)
        ExcepcionNoEncontrado.mensaje=mensaje1