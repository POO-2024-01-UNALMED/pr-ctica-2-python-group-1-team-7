from ErrorAplicacion import ErrorAplicacion

class ExcepcionNoEncontrado(ErrorAplicacion):
    def __init__(self,mensaje2='No se ha encontrado'):
        mensaje1=ErrorAplicacion.mensaje
        ExcepcionNoEncontrado.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionNoEncontrado.mensaje)
        ErrorAplicacion.mensaje=mensaje1