import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from baseDatos import Serializador, Deserializador
from gestorAplicación.gestion.habitacion import Habitacion
from gestorAplicación.transporte.asiento import Asiento
from ventanas.ventana_inicio import ventana_inicio

from gestorAplicación.personas.pasajero import Pasajero
from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.viaje import Viaje
from gestorAplicación.gestion.terminal import Terminal
from gestorAplicación.gestion.hospedaje import Hospedaje
from gestorAplicación.transporte.bus import Bus

import auxiliar
import auxiliar_excepciones as ae

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
       