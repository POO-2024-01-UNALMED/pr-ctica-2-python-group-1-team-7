from Excepciones.ErrorAplicacion import ErrorAplicacion

class ExcepcionDatosIncorrectos(ErrorAplicacion):
    mensaje=ErrorAplicacion.mensaje+" : Datos incorrectos ingresados"
    def __init__(self,mensaje2='Datos incorrectos ingresados'):
        ExcepcionDatosIncorrectos.mensaje=ErrorAplicacion.mensaje+" : "+mensaje2
        super().__init__(ExcepcionDatosIncorrectos.mensaje)

