

def gestionar_tiquetes():
    id_pasajero = input("Ingrese el número de identificación del pasajero: ")

    while len(id_pasajero) != 6:
        print("Número de identificación (6 dígitos): ")
        id_pasajero = input()

    print()

    pasajero = Pasajero.buscar_pasajero(id_pasajero)

    if pasajero is None or not pasajero.get_tiquetes():
        print("No hay tiquetes asociados con el número de identificación\n")
    else:
        tiquetes_validos = pasajero.buscar_tiquetes("validos")
        tiquetes_vencidos = pasajero.buscar_tiquetes("vencidos")

        if tiquetes_validos:
            print("Tiquetes válidos")
            print("-" * 93)
            print("    NUMERO DE RESERVA     NOMBRE        ASIENTO             FECHA DEL VIAJE      ID VIAJE     ")
            print("-" * 93)

            for tiquete in tiquetes_validos:
                print(tiquete)

            print()

        if tiquetes_vencidos:
            print("Tiquetes vencidos")
            print("-" * 93)
            print("    NUMERO DE RESERVA     NOMBRE        ASIENTO             FECHA DEL VIAJE      ID VIAJE     ")
            print("-" * 93)

            for tiquete in tiquetes_vencidos:
                print(tiquete)

            print()

        respuesta1 = input("¿Desea escoger algún tiquete? (si/no): ").lower()
        print()

        if respuesta1 == "si":
            numero_reserva = input("Escoja el tiquete ingresando el número de reserva: ")
            print()

            if pasajero.buscar_tiquete(numero_reserva) is None:
                print(f"No se encontró ningún tiquete con el número de reserva {numero_reserva}\n")
            else:
                for tiquete in tiquetes_vencidos:
                    if tiquete.get_numero_reserva() == numero_reserva:
                        print("Detalles del viaje")
                        print("-" * 92)
                        print("    FECHA          ORIGEN          DESTINO         HORA DE SALIDA     ID      PLACA BUS")
                        print("-" * 92)
                        print(tiquete.get_viaje())
                        print("\nDetalles del tiquete")
                        print("-" * 93)
                        print("    NUMERO DE RESERVA     NOMBRE        ASIENTO             FECHA DEL VIAJE      ID VIAJE     ")
                        print("-" * 93)
                        print(tiquete)
                        print()
                        break

                for tiquete in tiquetes_validos:
                    if tiquete.get_numero_reserva() == numero_reserva:
                        print("¿Qué desea hacer?\n")
                        print("1. Cancelarlo")
                        print("2. Modificarlo")
                        respuesta2 = input("Ingrese el número de la operación: ")
                        print()

                        if respuesta2 == "1":
                            pasajero.cancelar_tiquete(tiquete)
                            print("Tiquete cancelado exitosamente\n")
                        else:
                            print("¿Qué desea hacer?\n")
                            print("1. Cambiar de asiento")
                            print("2. Elegir otro viaje")
                            respuesta3 = input("Ingrese el número de la operación: ")
                            print()

                            if respuesta3 == "1":
                                viaje = tiquete.get_viaje()

                                if not viaje.tiene_sillas():
                                    print("No hay más asientos disponibles\n")
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
                                                            print("	       --")
                                                        else:
                                                            print(TipoAsiento.ESTANDAR)
                                                            print("	       --")

                                                        if indice < len(tipos_asiento_fila) - 1:
                                                            indice += 1
                                                    else:
                                                        print("  " + "   |")
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
                                                            print("	       --")
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
                                                        print("   " + "  |")
                                                        print("	       --")

                                                        if indice == 0:
                                                            print(TipoAsiento.PREMIUM)
                                                            print("	       --")
                                                        else:
                                                            print(TipoAsiento.ESTANDAR)
                                                            print("	       --")

                                                        if indice < len(tipos_asiento_fila) - 1:
                                                            indice += 1
                                                    else:
                                                        print("   " + "  |")
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
                                                            print("	       --")
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
                                    numero_asiento = input("Ingrese el número del asiento: ")

                                    while viaje.buscar_asiento(numero_asiento) is None or viaje.buscar_asiento(numero_asiento).is_reservado():
                                        print("\nEl asiento no está disponible\n")
                                        numero_asiento = input("Ingrese otro número de asiento: ")

                                    tiquete.cambiar_asiento(viaje.buscar_asiento(numero_asiento))

                            elif respuesta3 == "2":
                                origen = input("Ingrese el origen: ")
                                print()
                                destino = input("Ingrese el destino: ")
                                print()

                                print(f"Estos son los viajes disponibles para la ruta {origen.upper()} --> {destino.upper()}:")
                                print("-" * 92)
                                print("    FECHA          ORIGEN          DESTINO         HORA DE SALIDA     ID      PLACA BUS")
                                print("-" * 92)

                                for viaje in Empresa.buscar_viajes(origen.upper(), destino.upper()):
                                    print(viaje)

                                print()
                                id_viaje = input("Ingrese el id del viaje: ")
                                print()

                                viaje = Empresa.buscar_viaje(id_viaje)

                                if not viaje.lista_asientos():
                                    print("No hay más asientos disponibles")
                                    break

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
                                                        print("	       --")
                                                    else:
                                                        print(TipoAsiento.ESTANDAR)
                                                        print("	       --")

                                                    if indice < len(tipos_asiento_fila) - 1:
                                                        indice += 1
                                                else:
                                                    print("  " + "   |")
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
                                                        print("	       --")
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
                                                    print("   " + "  |")
                                                    print("	       --")

                                                    if indice == 0:
                                                        print(TipoAsiento.PREMIUM)
                                                        print("	       --")
                                                    else:
                                                        print(TipoAsiento.ESTANDAR)
                                                        print("	       --")

                                                    if indice < len(tipos_asiento_fila) - 1:
                                                        indice += 1
                                                else:
                                                    print("   " + "  |")
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
                                                        print("	       --")
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
                                numero_asiento = input("Ingrese el número del asiento: ")

                                while viaje.buscar_asiento(numero_asiento) is None or viaje.buscar_asiento(numero_asiento).is_reservado():
                                    print("\nEl asiento no está disponible\n")
                                    numero_asiento = input("Ingrese otro número de asiento: ")

                                tiquete.cambiar_viaje(viaje, viaje.buscar_asiento(numero_asiento))
                                pasajero.cancelar_tiquete(tiquete)

