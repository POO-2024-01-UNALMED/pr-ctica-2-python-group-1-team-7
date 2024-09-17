from Excepciones.ErrorAplicacion import ErrorAplicacion
from Excepciones.ExcepcionDatosIncorrectos import ExcepcionDatosIncorrectos

class ExcepcionTelefono(ExcepcionDatosIncorrectos):
    mensaje=ExcepcionDatosIncorrectos.mensaje+" : El telefono ingresado debe contener 10 digitos"
    def __init__(self,mensaje2='El telefono ingresado debe contener 10 digitos'):
        ExcepcionTelefono.mensaje=ExcepcionDatosIncorrectos.mensaje+" : "+mensaje2
        super().__init__(ExcepcionTelefono.mensaje)
