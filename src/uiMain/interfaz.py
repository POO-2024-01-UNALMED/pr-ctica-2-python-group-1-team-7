import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from baseDatos import Serializador, Deserializador
from gestorAplicación.gestion.habitacion import Habitacion
from gestorAplicación.transporte.asiento import Asiento
import uiMain.funcionalidades.funcionalidad1 as funcionalidad1
import uiMain.funcionalidades.funcionalidad2 as funcionalidad2
import uiMain.funcionalidades.funcionalidad3 as funcionalidad3
import uiMain.funcionalidades.funcionalidad4 as funcionalidad4
#from uiMain.Ventanas import ventana_inicio
#import uiMain.Ventanas.ventana_principal
import uiMain.ventanas.ventana_inicio
#import funcionalidad5
import auxiliar
from auxiliar import sc_input


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
        uiMain.ventanas.ventana_inicio.ventana_inicio()
       
if __name__ == "__main__":
        Interfaz.main()
       