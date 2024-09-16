from ErrorAplicacion import ErrorAplicacion
from ExcepcionDatosIncorrectos import ExcepcionDatosIncorrectos

class ExcepcionId(ExcepcionDatosIncorrectos):
    def __init__(self,mensaje2='El Id ingresado debe contener 6 digitos'):
        mensaje1=ExcepcionDatosIncorrectos.mensaje
        ExcepcionId.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionId.mensaje)
        ExcepcionDatosIncorrectos.mensaje=mensaje1