import re

def input():
    # This is a placeholder for the input function.
    # You may replace it with your custom implementation or use the built-in input() in actual usage.
    return ""

def reservar_tiquete():
    origen = input("Ingrese el origen: ").strip()
    destino = input("Ingrese el destino: ").strip()

    viajes = Empresa.buscar_viajes_origen_destino(origen.upper(), destino.upper())

    if not viajes:
        print("No se encontraron viajes disponibles para reservar\n")
    else:
        print(f"Estos son los viajes disponibles para la ruta {origen.upper()} --> {destino.upper()}:")
        
        for viaje in viajes:
            print("-" * 92)
            print("    FECHA          ORIGEN          DESTINO         HORA DE SALIDA     ID      PLACA BUS")
            print("-" * 92)
            print(viaje)
            print()

        id = input("Ingrese el id del viaje: ").strip()

        viaje = Viaje.buscar_viaje(viajes, id)

        if not viaje:
            print(f"No se encontró ningún viaje con número de id {id} disponible para reservar\n")
        else:
            print("Asientos disponibles:\n")

            tipos_asiento_fila = viaje.tipos_asiento()
            fila = 1
            indice = 0

            print(TipoAsiento.PREFERENCIAL)
            print("	       --")

            for asiento in viaje.lista_asientos():
                if len(asiento.get_numero()) == 2:
                    if asiento.is_reservado():
                        if "D" in asiento.get_numero():
                            if fila == tipos_asiento_fila[indice]:
                                print(f"{asiento.get_numero()}   |")
                                print("	       --")
                                if indice == 0:
                                    print(TipoAsiento.PREMIUM)
                                else:
                                    print(TipoAsiento.ESTANDAR)
                                print("	       --")
                                if indice < len(tipos_asiento_fila) - 1:
                                    indice += 1
                            else:
                                print("   |")
                            fila += 1
                        else:
                            print("    ", end="")
                    else:
                        if "D" in asiento.get_numero():
                            if fila == tipos_asiento_fila[indice]:
                                print(f"{asiento.get_numero()}   |")
                                print("	       --")
                                if indice == 0:
                                    print(TipoAsiento.PREMIUM)
                                else:
                                    print(TipoAsiento.ESTANDAR)
                                print("	       --")
                                if indice < len(tipos_asiento_fila) - 1:
                                    indice += 1
                            else:
                                print(f"{asiento.get_numero()}   |")
                                print()
                            fila += 1
                        else:
                            print(f"{asiento.get_numero()}  ", end="")
                else:
                    if asiento.is_reservado():
                        if "D" in asiento.get_numero():
                            if fila == tipos_asiento_fila[indice]:
                                print("   |")
                                print("	       --")
                                if indice == 0:
                                    print(TipoAsiento.PREMIUM)
                                else:
                                    print(TipoAsiento.ESTANDAR)
                                print("	       --")
                                if indice < len(tipos_asiento_fila) - 1:
                                    indice += 1
                            else:
                                print("   |")
                                print()
                            fila += 1
                        else:
                            print("    ", end="")
                    else:
                        if "D" in asiento.get_numero():
                            if fila == tipos_asiento_fila[indice]:
                                print(f"{asiento.get_numero()}  |")
                                print("	       --")
                                if indice == 0:
                                    print(TipoAsiento.PREMIUM)
                                else:
                                    print(TipoAsiento.ESTANDAR)
                                print("	       --")
                                if indice < len(tipos_asiento_fila) - 1:
                                    indice += 1
                            else:
                                print(f"{asiento.get_numero()}  |")
                                print()
                            fila += 1
                        else:
                            print(f"{asiento.get_numero()} ", end="")

            print("	       --\n")

            numero_asiento = input("Ingrese el número del asiento: ").strip()

            while True:
                asiento = viaje.buscar_asiento(numero_asiento)
                if asiento is None or asiento.is_reservado():
                    print("\nEl asiento no está disponible\n")
                    numero_asiento = input("Ingrese otro número de asiento: ").strip()
                else:
                    break

            viaje.reservar_asiento(numero_asiento, None)

            print("Ingrese sus datos:\n")

            nombre = input("Nombre completo: ").strip()
            id_pasajero = input("Número de identificación (6 dígitos): ").strip()

            while len(id_pasajero) != 6:
                id_pasajero = input("Número de identificación (6 dígitos): ").strip()

            pasajero = Pasajero.buscar_pasajero(id_pasajero)

            if not pasajero:
                telefono = input("Teléfono: ").strip()
                while not re.match(r'^\d{10}$', telefono):
                    print("Teléfono inválido\nEl teléfono debe contener 10 dígitos\n")
                    telefono = input("Teléfono: ").strip()

                correo = input("Correo electrónico: ").strip()
                while not re.match(r'^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$', correo):
                    print("Correo inválido\nEl correo debe tener la estructura (abcde@xyz.com)\n")
                    correo = input("Correo electrónico: ").strip()

                pasajero = Pasajero(nombre, id_pasajero, telefono, correo)

            asiento = viaje.buscar_asiento(numero_asiento)
            tiquete = Tiquete(pasajero, viaje, asiento)
            pasajero.agregar_tiquete(tiquete)

            print("Tiquete reservado exitosamente\n")
            print("-" * 34)
            print(f"    Tiquete No. {tiquete.get_numero_reserva()}")
            print("-" * 34)
            print(f"Nombre del pasajero: {nombre}")
            print(f"Id del pasajero: {id_pasajero}")
            print(f"Teléfono: {pasajero.get_telefono()}")
            print(f"Correo: {pasajero.get_correo()}")
            print(f"Asiento: {asiento}")
            print(f"Empresa: {viaje.get_empresa().get_nombre()}")
            print(f"Placa del bus: {viaje.get_bus().get_placa()}")
            print(f"Id del viaje: {viaje.get_id()}")
            print(f"Fecha y hora: {viaje.get_fecha()} {viaje.get_hora()}")
            print(f"Origen: {viaje.get_terminal_origen().get_ubicacion()}")
            print(f"Destino: {viaje.get_terminal_destino().get_ubicacion()}")
            print("-" * 34)
            print()
