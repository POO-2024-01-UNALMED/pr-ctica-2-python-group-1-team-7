from Excepciones.ErrorAplicacion import ErrorAplicacion
from Excepciones.ExcepcionDatosIncorrectos import ExcepcionDatosIncorrectos

class ExcepcionValoresVacios(ExcepcionDatosIncorrectos):
    mensaje=ExcepcionDatosIncorrectos.mensaje+" : El valor de los siguientes campos está vacío"
    def __init__(self,mensaje2='El valor de los siguientes campos está vacío: '):
        ExcepcionValoresVacios.mensaje=ExcepcionDatosIncorrectos.mensaje+" : "+mensaje2
        super().__init__(ExcepcionValoresVacios.mensaje)


                        