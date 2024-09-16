from ErrorAplicacion import ErrorAplicacion
from ExcepcionNoEncontrado import ExcepcionNoEncontrado

class ExcepcionAsiento(ExcepcionNoEncontrado):
    def __init__(self,mensaje2='Ningun asiento con ese numero'):
        mensaje1=ExcepcionNoEncontrado.mensaje
        ExcepcionAsiento.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionAsiento.mensaje)
        ExcepcionNoEncontrado.mensaje=mensaje1