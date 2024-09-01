from datetime import datetime, timedelta
import threading

from gestorAplicación.personas.pasajero import Pasajero
from gestorAplicación.gestion.empresa import Empresa

def hospedaje():
    print("Ingrese el número de identificación del pasajero: ", end='')
    id_pasajero = input().strip()

    while len(id_pasajero) != 6:
        print("Número de identificación (6 dígitos): ", end='')
        id_pasajero = input().strip()

    print()

    pasajero = Pasajero.buscar_pasajero(id_pasajero)

    if pasajero is None or not pasajero.get_tiquetes():
        print("El pasajero no ha reservado tiquetes para ningún viaje")
        print()
    else:
        print(f"Viajes reservados por {pasajero.get_nombre()} con número de identificación {pasajero.get_id()}")
        print("-" * 107)
        print("    FECHA          ORIGEN          DESTINO         HORA DE SALIDA     ID      PLACA BUS     ASIENTO")
        print("-" * 107)

        for tiquete in pasajero.buscar_tiquetes("validos"):
            print(f"{tiquete.get_viaje()} {tiquete.get_asiento()}")

        print()
        print("¿Desea agregar el servicio de hospedaje a algún viaje? (si/no): ", end='')
        respuesta1 = input().strip().lower()

        print()

        if respuesta1 == "si":
            print("Ingrese el id del viaje: ", end='')
            id_viaje = input().strip()
            print()

            viaje = Empresa.buscar_viaje(id_viaje)

            if viaje is None:
                print("No se encontró ningún viaje con el número de id")
                print()
            else:
                print(f"Hospedajes disponibles en {viaje.get_terminal_destino().get_ubicacion()}:")
                print("-" * 60)
                print("    NOMBRE     CALIFICACION      HABITACIONES DISPONIBLES")
                print("-" * 60)

                for hospedaje in viaje.hospedajes_disponibles():
                    print(hospedaje)

                print()
                print("Ingrese el nombre del hospedaje que desea: ", end='')
                nombre = input().strip()
                print()

                hospedaje = viaje.buscar_hospedaje(nombre)

                if hospedaje is None:
                    print(f"El hospedaje {nombre} no está disponible para este destino")
                    print()
                else:
                    print("Habitaciones disponibles:")
                    print("-" * 60)
                    print("    NUMERO DE HABITACIÓN     RESERVADA     DISPONIBLE EN")
                    print("-" * 60)

                    for habitacion in hospedaje.get_habitaciones():
                        print(habitacion)

                    print()
                    print("Ingrese el número de la habitación: ", end='')
                    numero_habitacion = input().strip()
                    print()

                    while hospedaje.buscar_habitacion(numero_habitacion) is None or \
                          hospedaje.buscar_habitacion(numero_habitacion).is_reservada():
                        print()
                        print("La habitación no está disponible")
                        print()
                        print("Ingrese otro número de habitación: ", end='')
                        numero_habitacion = input().strip()

                    print("¿Por cuánto tiempo desea quedarse? (horas/dias): ", end='')
                    tiempo = input().strip()
                    print()

                    fecha_viaje = datetime.combine(viaje.get_fecha(), viaje.get_hora())

                    array_tiempo = tiempo.split()

                    cantidad = int(array_tiempo[0])
                    fecha_reserva = None
                    ok = True

                    if "hora" in tiempo.lower():
                        fecha_reserva = fecha_viaje + timedelta(hours=cantidad)
                    elif "dia" in tiempo.lower():
                        fecha_reserva = fecha_viaje + timedelta(days=cantidad)
                    else:
                        print("Tiempo no válido")
                        print()
                        ok = False

                    if ok:
                        pasajero_tiquete = pasajero.buscar_tiquete(viaje)
                        hospedaje.reservar_habitacion(numero_habitacion, fecha_reserva, pasajero_tiquete)

                        duration = (fecha_reserva - datetime.now()).total_seconds() / 60

                        threading.Timer(duration * 60, hospedaje.liberar_habitacion(numero_habitacion)).start()

                        print(f"La habitación {numero_habitacion} en el hospedaje {hospedaje.get_nombre()} ha sido reservada correctamente")
                        print()
