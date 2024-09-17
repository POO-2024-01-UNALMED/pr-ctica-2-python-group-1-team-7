import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from baseDatos import Serializador, Deserializador
from src.gestorAplicación.gestion.habitacion import Habitacion
from src.gestorAplicación.transporte.asiento import Asiento
from src.uiMain.ventanas.ventana_inicio import ventana_inicio

from src.gestorAplicación.personas.pasajero import Pasajero
from src.gestorAplicación.gestion.empresa import Empresa
from src.gestorAplicación.gestion.viaje import Viaje
from src.gestorAplicación.gestion.terminal import Terminal
from src.gestorAplicación.gestion.hospedaje import Hospedaje
from src.gestorAplicación.transporte.bus import Bus

import auxiliar
import auxiliar_excepciones as ae

class Interfaz:
    @staticmethod
    def chequear_asientos_y_habitaciones():
        # Llama a los métodos estáticos para chequear asientos y habitaciones
        Asiento.chequear_asientos()
        Habitacion.chequear_habitaciones()

    def salir_del_sistema():
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
        