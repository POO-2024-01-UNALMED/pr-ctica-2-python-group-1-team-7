import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from baseDatos import Serializador, Deserializador
from gestorAplicación.gestion.habitacion import Habitacion
from gestorAplicación.transporte.asiento import Asiento
from ventanas.ventana_inicio import ventana_inicio
import auxiliar

class Interfaz:
    @staticmethod
    def chequear_asientos_y_habitaciones():
        # Llama a los métodos estáticos para chequear asientos y habitaciones
        Asiento.chequear_asientos()
        Habitacion.chequear_habitaciones()

    def salir_del_sistema():
        print("Ten un buen viaje")
        Serializador.limpiar_archivos()
        Serializador.serializar()
        sys.exit(0)

    def main():
        #Deserializador.deserializar()
        auxiliar.instanciar_objetos()
        Interfaz.chequear_asientos_y_habitaciones()
        ventana_inicio()
       
if __name__ == "__main__":
        Interfaz.main()
       