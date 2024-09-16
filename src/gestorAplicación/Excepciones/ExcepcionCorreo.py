from ErrorAplicacion import ErrorAplicacion
from ExcepcionDatosIncorrectos import ExcepcionDatosIncorrectos

class ExcepcionCorreo(ExcepcionDatosIncorrectos):
    def __init__(self,mensaje2='El correo ingresado es incorrecto (Debe conservar la siguiente estructura: abcd123@gmail.com)'):
        mensaje1=ExcepcionDatosIncorrectos.mensaje
        ExcepcionCorreo.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionCorreo.mensaje)
        ExcepcionDatosIncorrectos.mensaje=mensaje1