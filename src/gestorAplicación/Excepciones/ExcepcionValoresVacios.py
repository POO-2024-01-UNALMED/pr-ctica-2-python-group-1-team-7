from ErrorAplicacion import ErrorAplicacion
from ExcepcionDatosIncorrectos import ExcepcionDatosIncorrectos

class ExcepcionValoresVacios(ExcepcionDatosIncorrectos):
    def __init__(self,mensaje2='El valor de los siguientes campos está vacío: '):
        mensaje1=ExcepcionDatosIncorrectos.mensaje
        ExcepcionValoresVacios.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionValoresVacios.mensaje)
        ExcepcionDatosIncorrectos.mensaje=mensaje1