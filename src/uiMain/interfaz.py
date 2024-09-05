import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from baseDatos import Serializador, Deserializador
from gestorAplicación.gestion.habitacion import Habitacion
from gestorAplicación.transporte.asiento import Asiento
import funcionalidad_1
import funcionalidad_2
import funcionalidad_3
import funcionalidad_4
import funcionalidad_5
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

        auxiliar.ventanas()
        """
        opcion = ""

        while opcion != "6":
            print("MENU PRINCIPAL")
            print()
            print("¿Qué operación desea realizar?")
            print()
            print("1. Ver viajes disponibles")
            print("2. Reservar tiquete")
            print("3. Gestionar tiquetes")
            print("4. Agregar servicio de hospedaje")
            print("5. Opciones de administrador")
            print("6. Salir")
            print()
            opcion = sc_input("Ingrese el número de la operación: ")
            print()

            match opcion:
                case "1":
                    funcionalidad_1.ver_viajes()
                case "2":
                    funcionalidad_2.reservar_tiquete()
                case "3":
                    funcionalidad_3.gestionar_tiquetes()
                case "4":
                    funcionalidad_4.hospedaje()
                case "5":
                    print("Bienvenido Administrador")
                    funcionalidad_5.administrador()
                case "6":
                    sc_input.salir_del_sistema()
                case _:
                    print("Opción no válida")
                    print()
        """
if __name__ == "__main__":
        Interfaz.main()
       