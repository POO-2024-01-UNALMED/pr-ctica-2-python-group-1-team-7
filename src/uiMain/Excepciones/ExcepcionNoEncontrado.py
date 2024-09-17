from Excepciones.ErrorAplicacion import ErrorAplicacion

class ExcepcionNoEncontrado(ErrorAplicacion):
    mensaje=ErrorAplicacion.mensaje+" : No se ha encontrado"
    def __init__(self,mensaje2='No se ha encontrado'):
        ExcepcionNoEncontrado.mensaje=ErrorAplicacion.mensaje+" : "+mensaje2
        super().__init__(ExcepcionNoEncontrado.mensaje)
