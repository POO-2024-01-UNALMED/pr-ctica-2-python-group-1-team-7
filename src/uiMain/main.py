import re
from datetime import datetime, date, time, timedelta
from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor
import unicodedata
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from baseDatos import Deserializador, Serializador
from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.habitacion import Habitacion
from gestorAplicación.gestion.hospedaje import Hospedaje
from gestorAplicación.gestion.terminal import Terminal
from gestorAplicación.gestion.tiquete import Tiquete
from gestorAplicación.gestion.viaje import Viaje
from gestorAplicación.personas.persona import Persona
from gestorAplicación.personas.pasajero import Pasajero
from gestorAplicación.transporte.asiento import Asiento
from gestorAplicación.transporte.bus import Bus
from gestorAplicación.transporte.tipoAsiento import TipoAsiento
from gestorAplicación.transporte.vehiculo import Vehiculo
import funcionalidad_1
import funcionalidad_2
import funcionalidad_3
import funcionalidad_4
import funcionalidad_5


class Interfaz:
    sc = input  # Usamos la funcion input como entrada de datos

    @staticmethod
    def input():
        input_value = Interfaz.sc()
        # Normaliza la entrada eliminando acentos y caracteres especiales
        return unicodedata.normalize('NFD', input_value).encode('ascii', 'ignore').decode('ascii')

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
        # Deserializador.deserializar()
        Interfaz.chequear_asientos_y_habitaciones()

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
            opcion = input("Ingrese el número de la operación: ")
            print()

            if opcion == "1":
                funcionalidad_1.ver_viajes()
            elif opcion == "2":
                funcionalidad_2.reservar_tiquete()
            elif opcion == "3":
                funcionalidad_3.gestionar_tiquetes()
            elif opcion == "4":
                funcionalidad_4.hospedaje()
            elif opcion == "5":
                print("Bienvenido Administrador")
                funcionalidad_5.administrador()
            elif opcion == "6":
                Interfaz.salir_del_sistema()
            else:
                print("Opción no válida")
                print()

if __name__ == "__main__":
        Interfaz.main()