from Excepciones.ErrorAplicacion import ErrorAplicacion
from Excepciones.ExcepcionNoEncontrado import ExcepcionNoEncontrado

class ExcepcionIdUsuario(ExcepcionNoEncontrado):
    mensaje=ExcepcionNoEncontrado.mensaje+" : Ningun usuario que tenga ese Id"
    def __init__(self,mensaje2='Ningun usuario que tenga ese Id'):
        ExcepcionIdUsuario.mensaje=ExcepcionNoEncontrado.mensaje+" : "+mensaje2
        super().__init__(ExcepcionIdUsuario.mensaje)