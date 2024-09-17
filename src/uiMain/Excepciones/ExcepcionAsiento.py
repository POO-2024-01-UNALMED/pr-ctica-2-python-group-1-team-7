from Excepciones.ErrorAplicacion import ErrorAplicacion
from Excepciones.ExcepcionNoEncontrado import ExcepcionNoEncontrado

class ExcepcionAsiento(ExcepcionNoEncontrado):
    mensaje=ExcepcionNoEncontrado.mensaje+" : Ningun asiento con ese numero"
    def __init__(self,mensaje2='Ningun asiento con ese numero'):
        ExcepcionAsiento.mensaje=ExcepcionNoEncontrado.mensaje+" : "+mensaje2
        super().__init__(ExcepcionAsiento.mensaje)