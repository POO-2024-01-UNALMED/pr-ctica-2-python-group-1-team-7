from ErrorAplicacion import ErrorAplicacion
from ExcepcionDatosIncorrectos import ExcepcionDatosIncorrectos

class ExcepcionTelefono(ExcepcionDatosIncorrectos):
    def __init__(self,mensaje2='El telefono ingresado es incorrecto (Debe contener 10 digitos)'):
        mensaje1=ExcepcionDatosIncorrectos.mensaje
        ExcepcionTelefono.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionTelefono.mensaje)
        ExcepcionDatosIncorrectos.mensaje=mensaje1