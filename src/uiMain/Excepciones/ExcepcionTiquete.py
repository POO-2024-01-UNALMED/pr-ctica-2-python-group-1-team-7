from Excepciones.ErrorAplicacion import ErrorAplicacion
from Excepciones.ExcepcionNoEncontrado import ExcepcionNoEncontrado

class ExcepcionTiquete(ExcepcionNoEncontrado):
    mensaje=ExcepcionNoEncontrado.mensaje+" : Ningun tiquete con ese id"
    def __init__(self,mensaje2='Ningun tiquete con ese id'):
        ExcepcionTiquete.mensaje=ExcepcionNoEncontrado.mensaje+" : "+mensaje2
        super().__init__(ExcepcionTiquete.mensaje)

