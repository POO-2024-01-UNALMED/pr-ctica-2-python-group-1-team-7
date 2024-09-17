class ErrorAplicacion(Exception):
    def __init__(self, mensaje='Manejo de errores de la Aplicacion'):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ExcepcionNoEncontrado(ErrorAplicacion):
    def __init__(self, mensaje='No se ha encontrado'):
        super().__init__(f"{ErrorAplicacion().mensaje} : {mensaje}")

class ExcepcionDatosIncorrectos(ErrorAplicacion):
    def __init__(self,mensaje2='Datos incorrectos ingresados'):
        super().__init__(f"{ErrorAplicacion().mensaje} : {mensaje2}")

class ExcepcionAsiento(ExcepcionNoEncontrado):
    def __init__(self,mensaje2='Ningun asiento con ese numero'):
        super().__init__(f"{ExcepcionNoEncontrado().mensaje} : {mensaje2}")

class ExcepcionCorreo(ExcepcionDatosIncorrectos):
    def __init__(self,mensaje2='El correo ingresado debe conservar la siguiente estructura: abcd123@gmail.com'):
        super().__init__(f"{ExcepcionDatosIncorrectos().mensaje} : {mensaje2}")

class ExcepcionHospedaje(ExcepcionNoEncontrado):
    def __init__(self,mensaje2='Ningun hospedaje con ese nombre'):
        super().__init__(f"{ExcepcionNoEncontrado().mensaje} : {mensaje2}")

class ExcepcionId(ExcepcionDatosIncorrectos):
    def __init__(self,mensaje2='El Id ingresado debe contener 6 digitos'):
        super().__init__(f"{ExcepcionDatosIncorrectos().mensaje} : {mensaje2}")

class ExcepcionIdUsuario(ExcepcionNoEncontrado):
    def __init__(self,mensaje2='Ningun usuario que tenga ese Id'):
        super().__init__(f"{ExcepcionNoEncontrado().mensaje} : {mensaje2}")

class ExcepcionTelefono(ExcepcionDatosIncorrectos):
    def __init__(self,mensaje2='El telefono ingresado debe contener 10 digitos'):
        super().__init__(f"{ExcepcionDatosIncorrectos().mensaje} : {mensaje2}")

class ExcepcionTiempo(ExcepcionDatosIncorrectos):
    def __init__(self,mensaje2='El tiempo se debe ingresar en el formato (X minutos,Y horas o Z dias)'):
        super().__init__(f"{ExcepcionDatosIncorrectos().mensaje} : {mensaje2}")

class ExcepcionTiquete(ExcepcionNoEncontrado):
    def __init__(self, mensaje2='Ningun tiquete con ese id'):
        super().__init__(f"{ExcepcionNoEncontrado().mensaje} : {mensaje2}")

class ExcepcionValoresVacios(ExcepcionDatosIncorrectos):
    def __init__(self,mensaje2='El valor de los siguientes campos está vacío: '):
        super().__init__(f"{ExcepcionDatosIncorrectos().mensaje} : {mensaje2}")

class ExcepcionViaje(ExcepcionNoEncontrado):
    def __init__(self, mensaje2='Ningún viaje con ese Id'):
        super().__init__(f"{ExcepcionNoEncontrado().mensaje} : {mensaje2}")

