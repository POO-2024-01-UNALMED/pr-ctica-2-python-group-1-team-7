from ErrorAplicacion import ErrorAplicacion
from ExcepcionDatosIncorrectos import ExcepcionDatosIncorrectos

class ExcepcionTiempo(ExcepcionDatosIncorrectos):
    def __init__(self,mensaje2='El tiempo se debe ingresar en el formato (X minutos,Y horas o Z dias)'):
        mensaje1=ExcepcionDatosIncorrectos.mensaje
        ExcepcionTiempo.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionTiempo.mensaje)
        ExcepcionDatosIncorrectos.mensaje=mensaje1