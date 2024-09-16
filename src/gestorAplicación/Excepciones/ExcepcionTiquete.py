from ErrorAplicacion import ErrorAplicacion
from ExcepcionNoEncontrado import ExcepcionNoEncontrado

class ExcepcionTiquete(ExcepcionNoEncontrado):
    def __init__(self,mensaje2='Ningun tiquete con ese id'):
        mensaje1=ExcepcionNoEncontrado.mensaje
        ExcepcionTiquete.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionTiquete.mensaje)
        ExcepcionNoEncontrado.mensaje=mensaje1