class ErrorAplicacion(Exception):
    def __init__(self, mensaje='Manejo de errores de la Aplicacion'):
        ErrorAplicacion.mensaje=mensaje
        super().__init__(mensaje)