from ErrorAplicacion import ErrorAplicacion
from ExcepcionNoEncontrado import ExcepcionNoEncontrado

class ExcepcionIdUsuario(ExcepcionNoEncontrado):
    def __init__(self,mensaje2='Ningun usuario que tenga ese Id'):
        mensaje1=ExcepcionNoEncontrado.mensaje
        ExcepcionIdUsuario.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionIdUsuario.mensaje)
        ExcepcionNoEncontrado.mensaje=mensaje1