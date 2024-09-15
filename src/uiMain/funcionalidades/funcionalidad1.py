from gestorAplicación.gestion.empresa import Empresa

class ver_viajes():
    @classmethod
    def mostrar_viajes(cls, text):
        for empresa in Empresa.get_empresas():
            text.insert(
                "end", 
                f"Viajes disponibles de la empresa {empresa.get_nombre()}\n"
            )
            text.insert("end", "-" * 91 + "\n")
            text.insert(
                "end", 
                "    FECHA          ORIGEN          DESTINO" 
                + "         HORA DE SALIDA     ID      PLACA BUS\n"
            )
            text.insert("end", "-" * 91 + "\n")

            for viaje in empresa.get_viajes():
                text.insert("end", str(viaje) + "\n")
            
            text.insert("end", "\n")

        text.config(state="disabled")

''' from datetime import datetime, timedelta
import sys
from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.transporte.tipoAsiento import TipoAsiento

def mostrar_viajes():
    for empresa in Empresa.get_empresas():
        print(f"Viajes disponibles de la empresa {empresa.get_nombre()}")

        print("-" * 92)
        print("    FECHA          ORIGEN          DESTINO         HORA DE SALIDA     ID      PLACA BUS")
        print("-" * 92)

        for viaje in empresa.get_viajes():
            print(viaje)

        print()
def ver_viajes():
    
    
    respuesta1 = input("¿Desea filtrar por alguna categoría (si/no)? ").strip().lower()
    
    if respuesta1 == "si":
        categoria = input("¿Por cuál categoría desea filtrar? ").strip().upper()
        
        viajes = []
        if categoria == "FECHA":
            fecha = input("Ingrese la fecha en formato dd-mm-aaaa: ").strip()
            try:
                nueva_fecha = datetime.strptime(fecha, "%d-%m-%Y").date()
                viajes = Empresa.buscar_viajes(nueva_fecha)
            except ValueError:
                print("Formato de fecha incorrecto")
        
        elif categoria == "ORIGEN":
            origen = input("Ingrese el origen: ").strip().upper()
            viajes = Empresa.buscar_viajes(origen, "")
        
        elif categoria == "DESTINO":
            destino = input("Ingrese el destino: ").strip().upper()
            viajes = Empresa.buscar_viajes("", destino)
        
        elif categoria == "HORA DE SALIDA":
            hora = input("Ingrese la hora de salida en formato 24 horas: ").strip()
            try:
                nueva_hora = datetime.strptime(hora, "%H:%M").time()
                viajes = Empresa.buscar_viajes(nueva_hora)
            except ValueError:
                print("Formato de hora incorrecto")
        
        elif categoria == "ID":
            id_viaje = input("Ingrese el id del viaje: ").strip()
            viajes = Empresa.buscar_viajes(id_viaje)
        
        elif categoria == "PLACA":
            placa = input("Ingrese la placa del vehiculo: ").strip()
            viajes = Empresa.buscar_viajes(placa)
        
        if not viajes:
            print("No se encontraron viajes")
        else:
            print(f"Vuelos filtrados por {categoria}")
            print("-" * 92)
            print("    FECHA          ORIGEN          DESTINO         HORA DE SALIDA     ID      PLACA BUS")
            print("-" * 92)
            for viaje in viajes:
                print(viaje)
            print()
        
        respuesta2 = input("¿Desea ver más detalles sobre un viaje? (si/no) ").strip().lower()
        
        if respuesta2 == "si":
            id_viaje = input("Ingrese el id del viaje: ").strip()
            viaje = Empresa.buscar_viaje(id_viaje)
            
            if viaje is None:
                print(f"No se encontró ningún viaje con el número de id {id_viaje}")
            else:
                if not viaje.tiene_sillas():
                    print("No hay sillas disponibles")
                    print("¿Qué desea hacer?")
                    print("1. Ver otros viajes")
                    print("2. Ir al menú principal")
                    
                    opcion = input().strip()
                    
                    if opcion == "1":
                        ver_viajes()
                else:
                    print("Asientos disponibles:")
                    tipos_asiento_fila = viaje.tipos_asiento()
                    fila = 1
                    indice = 0
                    
                    print(TipoAsiento.PREFERENCIAL)
                    print("       --")
                    
                    for asiento in viaje.lista_asientos():
                        if len(asiento.numero) == 2:
                            if asiento.is_reservado():
                                if "D" in asiento.numero:
                                    if fila == tipos_asiento_fila[indice]:
                                        print(f"{asiento.numero}   |")
                                        print("       --")
                                        print(TipoAsiento.PREMIUM if indice == 0 else TipoAsiento.ESTANDAR)
                                        print("       --")
                                        if indice < len(tipos_asiento_fila) - 1:
                                            indice += 1
                                    else:
                                        print("  " + "   |")
                                    fila += 1
                                else:
                                    print("    ")
                            else:
                                if "D" in asiento.numero:
                                    if fila == tipos_asiento_fila[indice]:
                                        print(f"{asiento.numero}   |")
                                        print("       --")
                                        print(TipoAsiento.PREMIUM if indice == 0 else TipoAsiento.ESTANDAR)
                                        print("       --")
                                        if indice < len(tipos_asiento_fila) - 1:
                                            indice += 1
                                    else:
                                        print(f"{asiento.numero}   |")
                                        print()
                                    fila += 1
                                else:
                                    print(f"{asiento.numero}  ")
                        else:
                            if asiento.is_reservado():
                                if "D" in asiento.numero:
                                    if fila == tipos_asiento_fila[indice]:
                                        print("   " + "  |")
                                        print("       --")
                                        print(TipoAsiento.PREMIUM if indice == 0 else TipoAsiento.ESTANDAR)
                                        print("       --")
                                        if indice < len(tipos_asiento_fila) - 1:
                                            indice += 1
                                    else:
                                        print("   " + "  |")
                                        print()
                                    fila += 1
                                else:
                                    print("    ")
                            else:
                                if "D" in asiento.numero:
                                    if fila == tipos_asiento_fila[indice]:
                                        print(f"{asiento.numero}  |")
                                        print("       --")
                                        print(TipoAsiento.PREMIUM if indice == 0 else TipoAsiento.ESTANDAR)
                                        print("       --")
                                        if indice < len(tipos_asiento_fila) - 1:
                                            indice += 1
                                    else:
                                        print(f"{asiento.numero}  |")
                                        print()
                                    fila += 1
                                else:
                                    print(f"{asiento.numero} ")
                    
                    print("       --")
                    print()
                    
                    respuesta3 = input("¿Desea reservar un asiento por un cierto período de tiempo? (si/no) ").strip().lower()
                    
                    if respuesta3 == "si":
                        numero_asiento = input("Ingrese el número del asiento: ").strip()
                        
                        if viaje.buscar_asiento(numero_asiento) is None or viaje.buscar_asiento(numero_asiento).is_reservado():
                            while True:
                                print("\nEl asiento no está disponible")
                                numero_asiento = input("Ingrese otro número de asiento: ").strip()
                                
                                if viaje.buscar_asiento(numero_asiento) is not None and not viaje.buscar_asiento(numero_asiento).is_reservado():
                                    break
                        
                        print("¿Por cuánto tiempo desea reservarlo? (minutos/horas/dias)")
                        tiempo = input().strip()
                        array_tiempo = tiempo.split()
                        
                        cantidad = int(array_tiempo[0])
                        fecha_reserva = None
                        fecha_viaje = datetime.combine(viaje.get_fecha(), viaje.get_hora())
                        
                        if "minutos" in tiempo.lower():
                            fecha_reserva = datetime.now() + timedelta(minutes=cantidad)
                        elif "horas" in tiempo.lower():
                            fecha_reserva = datetime.now() + timedelta(hours=cantidad)
                        elif "dias" in tiempo.lower():
                            fecha_reserva = datetime.now() + timedelta(days=cantidad)
                        else:
                            print("Tiempo no válido")
                        
                        if fecha_reserva:
                            while fecha_viaje < fecha_reserva:
                                print("La reserva debe ser antes del viaje (ó Ingrese 'E' para volver al menú principal)")
                                tiempo = input("¿Por cuánto tiempo desea reservarlo? (minutos/horas/dias)").strip()
                                
                                if tiempo.upper() == "E":
                                    break
                                
                                array_tiempo = tiempo.split()
                                cantidad = int(array_tiempo[0])
                                
                                if "minutos" in tiempo.lower():
                                    fecha_reserva = datetime.now() + timedelta(minutes=cantidad)
                                elif "horas" in tiempo.lower():
                                    fecha_reserva = datetime.now() + timedelta(hours=cantidad)
                                elif "dias" in tiempo.lower():
                                    fecha_reserva = datetime.now() + timedelta(days=cantidad)
                                else:
                                    print("Tiempo no válido")
                                    break
                            
                            if fecha_reserva:
                                viaje.reservar_asiento(numero_asiento, fecha_reserva)
                                print("Asiento reservado exitosamente")
                                # Aquí se debería implementar la lógica para liberar el asiento después del tiempo determinado
                                # Para ello, puedes utilizar threading.Timer o una tarea programada con alguna librería adecuada
                                # En esta traducción, he omitido la implementación específica
    else:
        respuesta2 = input("¿Desea ver más detalles sobre un viaje? (si/no) ").strip().lower()
        
        if respuesta2 == "si":
            id_viaje = input("Ingrese el id del viaje: ").strip()
            viaje = Empresa.buscar_viaje_por_id(id_viaje)
            
            if viaje is None:
                print(f"No se encontró ningún viaje con número de id {id_viaje}")
            else:
                if not viaje.tiene_sillas():
                    print("No hay sillas disponibles")
                    print("¿Qué desea hacer?")
                    print("1. Ver otros viajes")
                    print("2. Ir al menú principal")
                    
                    opcion = input().strip()
                    
                    if opcion == "1":
                        ver_viajes()
                else:
                    print("Asientos disponibles:")
                    tipos_asiento_fila = viaje.tipos_asiento()
                    fila = 1
                    indice = 0
                    
                    print(TipoAsiento.PREFERENCIAL)
                    print("       --")
                    
                    for asiento in viaje.lista_asientos():
                        if len(asiento.numero) == 2:
                            if asiento.is_reservado():
                                if "D" in asiento.numero:
                                    if fila == tipos_asiento_fila[indice]:
                                        print(f"{asiento.numero}   |")
                                        print("       --")
                                        print(TipoAsiento.PREMIUM if indice == 0 else TipoAsiento.ESTANDAR)
                                        print("       --")
                                        if indice < len(tipos_asiento_fila) - 1:
                                            indice += 1
                                    else:
                                        print("  " + "   |")
                                    fila += 1
                                else:
                                    print("    ")
                            else:
                                if "D" in asiento.numero:
                                    if fila == tipos_asiento_fila[indice]:
                                        print(f"{asiento.numero}   |")
                                        print("       --")
                                        print(TipoAsiento.PREMIUM if indice == 0 else TipoAsiento.ESTANDAR)
                                        print("       --")
                                        if indice < len(tipos_asiento_fila) - 1:
                                            indice += 1
                                    else:
                                        print(f"{asiento.numero}   |")
                                        print()
                                    fila += 1
                                else:
                                    print(f"{asiento.numero}  ")
                        else:
                            if asiento.is_reservado():
                                if "D" in asiento.numero:
                                    if fila == tipos_asiento_fila[indice]:
                                        print("   " + "  |")
                                        print("       --")
                                        print(TipoAsiento.PREMIUM if indice == 0 else TipoAsiento.ESTANDAR)
                                        print("       --")
                                        if indice < len(tipos_asiento_fila) - 1:
                                            indice += 1
                                    else:
                                        print("   " + "  |")
                                        print()
                                    fila += 1
                                else:
                                    print("    ")
                            else:
                                if "D" in asiento.numero:
                                    if fila == tipos_asiento_fila[indice]:
                                        print(f"{asiento.numero}  |")
                                        print("       --")
                                        print(TipoAsiento.PREMIUM if indice == 0 else TipoAsiento.ESTANDAR)
                                        print("       --")
                                        if indice < len(tipos_asiento_fila) - 1:
                                            indice += 1
                                    else:
                                        print(f"{asiento.numero}  |")
                                        print()
                                    fila += 1
                                else:
                                    print(f"{asiento.numero} ")
                    
                    print("       --")
                    print()
                    
                    respuesta3 = input("¿Desea reservar un asiento por un cierto período de tiempo? (si/no) ").strip().lower()
                    
                    if respuesta3 == "si":
                        numero_asiento = input("Ingrese el número del asiento: ").strip()
                        
                        if viaje.buscar_asiento(numero_asiento) is None or viaje.buscar_asiento(numero_asiento).is_reservado():
                            while True:
                                print("\nEl asiento no está disponible")
                                numero_asiento = input("Ingrese otro número de asiento: ").strip()
                                
                                if viaje.buscar_asiento(numero_asiento) is not None and not viaje.buscar_asiento(numero_asiento).is_reservado():
                                    break
                        
                        print("¿Por cuánto tiempo desea reservarlo? (minutos/horas/dias)")
                        tiempo = input().strip()
                        array_tiempo = tiempo.split()
                        
                        cantidad = int(array_tiempo[0])
                        fecha_reserva = None
                        fecha_viaje = datetime.combine(viaje.get_fecha(), viaje.get_hora())
                        
                        if "minutos" in tiempo.lower():
                            fecha_reserva = datetime.now() + timedelta(minutes=cantidad)
                        elif "horas" in tiempo.lower():
                            fecha_reserva = datetime.now() + timedelta(hours=cantidad)
                        elif "dias" in tiempo.lower():
                            fecha_reserva = datetime.now() + timedelta(days=cantidad)
                        else:
                            print("Tiempo no válido")
                        
                        if fecha_reserva:
                            while fecha_viaje < fecha_reserva:
                                print("La reserva debe ser antes del viaje (ó Ingrese 'E' para volver al menú principal)")
                                tiempo = input("¿Por cuánto tiempo desea reservarlo? (minutos/horas/dias)").strip()
                                
                                if tiempo.upper() == "E":
                                    break
                                
                                array_tiempo = tiempo.split()
                                cantidad = int(array_tiempo[0])
                                
                                if "minutos" in tiempo.lower():
                                    fecha_reserva = datetime.now() + timedelta(minutes=cantidad)
                                elif "horas" in tiempo.lower():
                                    fecha_reserva = datetime.now() + timedelta(hours=cantidad)
                                elif "dias" in tiempo.lower():
                                    fecha_reserva = datetime.now() + timedelta(days=cantidad)
                                else:
                                    print("Tiempo no válido")
                                    break
                            
                            if fecha_reserva:
                                viaje.reservar_asiento(numero_asiento, fecha_reserva)
                                print("Asiento reservado exitosamente")
                                # Aquí se debería implementar la lógica para liberar el asiento después del tiempo determinado
                                # Para ello, puedes utilizar threading.Timer o una tarea programada con alguna librería adecuada
                                # En esta traducción, he omitido la implementación específica
                '''