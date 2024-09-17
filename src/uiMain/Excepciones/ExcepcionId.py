from Excepciones.ErrorAplicacion import ErrorAplicacion
from Excepciones.ExcepcionDatosIncorrectos import ExcepcionDatosIncorrectos

class ExcepcionId(ExcepcionDatosIncorrectos):
    mensaje=ExcepcionDatosIncorrectos.mensaje+" : El Id ingresado debe contener 6 digitos"
    def __init__(self,mensaje2='El Id ingresado debe contener 6 digitos'):
        ExcepcionId.mensaje=ExcepcionDatosIncorrectos.mensaje+" : "+mensaje2
        super().__init__(ExcepcionId.mensaje)
