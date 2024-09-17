from Excepciones.ErrorAplicacion import ErrorAplicacion
from ExcepcionDatosIncorrectos import ExcepcionDatosIncorrectos

class ExcepcionTiempo(ExcepcionDatosIncorrectos):
    mensaje=ExcepcionDatosIncorrectos.mensaje+" : El tiempo se debe ingresar en el formato (X minutos,Y horas o Z dias)"
    def __init__(self,mensaje2='El tiempo se debe ingresar en el formato (X minutos,Y horas o Z dias)'):
        ExcepcionTiempo.mensaje=ExcepcionDatosIncorrectos.mensaje+" : "+mensaje2
        super().__init__(ExcepcionTiempo.mensaje)

            