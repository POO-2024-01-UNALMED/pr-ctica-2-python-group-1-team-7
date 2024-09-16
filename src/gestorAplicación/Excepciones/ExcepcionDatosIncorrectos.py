from ErrorAplicacion import ErrorAplicacion

class ExcepcionDatosIncorrectos(ErrorAplicacion):
    def __init__(self,mensaje2='Datos incorrectos ingresados'):
        mensaje1=ErrorAplicacion.mensaje
        ExcepcionDatosIncorrectos.mensaje=mensaje1+" : "+mensaje2
        super().__init__(ExcepcionDatosIncorrectos.mensaje)
        ErrorAplicacion.mensaje=mensaje1