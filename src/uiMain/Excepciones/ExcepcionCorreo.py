from Excepciones.ErrorAplicacion import ErrorAplicacion
from Excepciones.ExcepcionDatosIncorrectos import ExcepcionDatosIncorrectos

class ExcepcionCorreo(ExcepcionDatosIncorrectos):
    mensaje=ExcepcionDatosIncorrectos.mensaje+" : El correo ingresado debe conservar la siguiente estructura: abcd123@gmail.com"
    def __init__(self,mensaje2='El correo ingresado debe conservar la siguiente estructura: abcd123@gmail.com'):
        ExcepcionCorreo.mensaje=ExcepcionDatosIncorrectos.mensaje+" : "+mensaje2
        super().__init__(ExcepcionCorreo.mensaje)