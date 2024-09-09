from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.personas.pasajero import Pasajero

def administrador():
    print("¿Qué desea modificar?\n")
    print("1. Empresas")
    print("2. Hospedajes")
    print("3. Terminales")
    print("4. Viajes")
    print("5. Personal")
    print("6. Buses")
    print("7. Volver\n")
    
    respuesta1 = input("Ingrese el número de la operación: ").strip()
    print()
    
    if respuesta1 == "1":
        print("Ingrese una opción\n")
        print("1. Agregar")
        print("2. Ver")
        print("3. Eliminar")
        print("4. Volver\n")

        empresas = input().strip()
        print()

        if empresas == "1":
            print("¿Qué desea agregar?\n")
            print("1. Empresa")
            print("2. Conductores a una empresa")
            print("3. Volver\n")

            empresas_agregar = input().strip()
            print()

            if empresas_agregar == "1":
                nombre = input("Introduzca el nombre de la empresa: ").strip()
                empresa = Empresa.buscar_empresa(nombre)
                if empresa is not None:
                    print("La empresa ya existe\n")
                    accion = input("¿Desea realizar alguna acción más como administrador? (si/no): ").strip().lower()
                    if accion == "si":
                        administrador()
                    return

                Empresa(nombre)
                print("\nEmpresa creada exitosamente\n")
                accion = input("¿Desea realizar alguna acción más como administrador? (si/no): ").strip().lower()
                if accion == "si":
                    administrador()

            elif empresas_agregar == "2":'''
                id_conductor = input("Introduzca el número de identificación del conductor: ").strip()
                while len(id_conductor) != 6:
                    id_conductor = input("Número de identificación (6 dígitos): ").strip()
                
                print()
                nombre = input("Introduzca el nombre de la empresa: ").strip()
                print()

                if Conductor.buscar_conductor(id_conductor) is None:
                    print("No se ha encontrado a ningún conductor con ese ID\n")
                    accion = input("¿Desea realizar alguna acción más como administrador? (si/no): ").strip().lower()
                    if accion == "si":
                        administrador()
                    return

                empresa = Empresa.buscar_empresa(nombre)
                if empresa is not None:
                    empresa.añadir_conductor(Conductor.buscar_conductor(id_conductor))
                else:
                    print(f"No se ha encontrado la empresa {nombre}\n")
                    accion = input("¿Desea realizar alguna acción más como administrador? (si/no): ").strip().lower()
                    if accion == "si":
                        administrador()
                    return

                print(f"Conductor {Conductor.buscar_conductor(id_conductor).get_nombre()} asignado correctamente a la empresa {nombre}\n")
                accion = input("¿Desea realizar alguna acción más como administrador? (si/no): ").strip().lower()
                if accion == "si":
                    administrador()'''

        elif empresas == "2":
            print("¿Qué desea ver?\n")
            print("1. Empresa")
            print("2. Volver\n")

            empresas_ver = input().strip()
            print()

            if empresas_ver == "1":
                print("Lista de empresas actuales")
                print("-" * 28)
                print("    Nombre de la empresa")
                print("-" * 28)

                for empresa in Empresa.get_empresas():
                    print(f"          {empresa.get_nombre()}")
                
                print()
                accion = input("¿Desea realizar alguna acción más como administrador? (si/no): ").strip().lower()
                if accion == "si":
                    administrador()

        elif empresas == "3":
            print("¿Qué desea eliminar?\n")
            print("1. Empresa")
            print("2. Conductores de una empresa")
            print("3. Volver\n")

            empresas_eliminar = input().strip()
            print()

            if empresas_eliminar == "1":
                nombre = input("Ingrese el nombre de la empresa a eliminar: ").strip()
                empresa = Empresa.buscar_empresa(nombre)
                if empresa is None:
                    print(f"\nNo se ha encontrado la empresa {nombre}\n")
                    accion = input("¿Desea realizar alguna acción más como administrador? (si/no): ").strip().lower()
                    if accion == "si":
                        administrador()
                    return

                Empresa.eliminar_empresa(nombre)
                print(f"\nEmpresa {nombre} eliminada exitosamente\n")
                accion = input("¿Desea realizar alguna acción más como administrador? (si/no): ").strip().lower()
                if accion == "si":
                    administrador()

            elif empresas_eliminar == "2":
                id_conductor = input("Introduzca el número de identificación del conductor: ").strip()
                while len(id_conductor) != 6:
                    id_conductor = input("Número de identificación (6 dígitos): ").strip()

                print()
                nombre = input("Introduzca el nombre de la empresa: ").strip()
                print()
'''
                if Conductor.buscar_conductor(id_conductor) is None:
                    print("No se ha encontrado a ningún conductor con ese ID\n")
                    accion = input("¿Desea realizar alguna acción más como administrador? (si/no): ").strip().lower()
                    if accion == "si":
                        administrador()
                    return

                empresa = Empresa.buscar_empresa(nombre)
                if empresa is not None:
                    empresa.eliminar_conductor(Conductor.buscar_conductor(id_conductor))
                    print(f"Conductor con ID {id_conductor} eliminado correctamente de la empresa {empresa.get_nombre()}\n")
                    accion = input("¿Desea realizar alguna acción más como administrador? (si/no): ").strip().lower()
                    if accion == "si":
                        administrador()
                else:
                    print(f"No se ha encontrado la empresa {nombre}\n")
                    accion = input("¿Desea realizar alguna acción más como administrador? (si/no): ").strip().lower()
                    if accion == "si":
                        administrador()'''
    if respuesta1 == "2":
            print("Ingrese una opción\n")
            print("1. Agregar")
            print("2. Ver")
            print("3. Eliminar")
            print("4. Volver\n")

            hospedajes = input().strip()

            if hospedajes == "1":
                print("¿Qué desea agregar?\n")
                print("1. Hospedaje")
                print("2. Habitaciones a un hospedaje")
                print("3. Calificación a un hospedaje")
                print("4. Volver\n")

                hospedajes_agregar = input().strip()

                if hospedajes_agregar == "1":
                    print("Ingrese el nombre del hospedaje")
                    nombre = input().strip()
                    print("Ingrese la ubicación del hospedaje")
                    ubicacion = input().strip()

                    if buscarHospedaje(nombre, ubicacion) is not None:
                        print("El hospedaje ya existe\n")
                        print("Desea realizar alguna acción más cómo administrador (si/no)")
                        accion = input().strip().lower()
                        if accion == "si":
                            administrador()
                        break

                    Hospedaje(nombre, ubicacion)
                    print("Hospedaje creado exitosamente\n")
                    print("Desea realizar alguna acción más cómo administrador (si/no)")
                    accion = input().strip().lower()
                    if accion == "si":
                        administrador()
                    break

                if hospedajes_agregar == "2":
                    print("Ingrese el nombre del hospedaje")
                    nombre = input().strip()
                    print("Ingrese la ubicación del hospedaje")
                    ubicacion = input().strip()

                    hospedaje = Hospedaje.buscarHospedaje(nombre, ubicacion)

                    if hospedaje is None:
                        print("El hospedaje no existe\n")
                        print("Desea realizar alguna acción más cómo administrador (si/no)")
                        accion = input().strip().lower()
                        if accion == "si":
                            administrador()
                        break

                    print("Ingrese la cantidad de pisos (Sólo números enteros)")
                    pisos = int(input().strip())
                    print("Ingrese las habitaciones por piso (Sólo números enteros)")
                    habitaciones = int(input().strip())

                    hospedaje.crearHabitaciones(pisos, habitaciones)
                    print("Habitaciones agregadas correctamente\n")
                    print("Desea realizar alguna acción más cómo administrador (si/no)")
                    accion = input().strip().lower()
                    if accion == "si":
                        administrador()
                    break

                if hospedajes_agregar == "3":
                    print("Ingrese el nombre del hospedaje")
                    nombre = input().strip()
                    print("Ingrese la ubicación del hospedaje")
                    ubicacion = input().strip()

                    hospedaje = Hospedaje.buscarHospedaje(nombre, ubicacion)

                    if hospedaje is None:
                        print("El hospedaje no existe\n")
                        print("Desea realizar alguna acción más cómo administrador (si/no)")
                        accion = input().strip().lower()
                        if accion == "si":
                            administrador()
                        break

                    print("Agregue su calificación del hospedaje del 1 al 5 (Sólo números enteros)")
                    calificar = input().strip()

                    hospedaje.setCalificacion(calificar)
                    print("Calificación agregada correctamente\n")
                    print("Desea realizar alguna acción más cómo administrador (si/no)")
                    accion = input().strip().lower()
                    if accion == "si":
                        administrador()
                    break

                administrador()

            if hospedajes == "2":
                print("¿Qué desea ver?\n")
                print("1. Hospedajes")
                print("2. Volver\n")

                hospedajes_ver = input().strip()

                if hospedajes_ver == "1":
                    print("Lista de hospedajes actuales")
                    print("-" * 56)
                    print("    Nombre         Ubicación         Calificación")
                    print("-" * 56)

                    for hospedaje in Hospedaje.getHospedajes():
                        if hospedaje is not None:
                            print(f"    {hospedaje.nombre}             {hospedaje.ubicacion}            {hospedaje.calificacion}\n")

                    print("Desea realizar alguna acción más cómo administrador (si/no)")
                    accion = input().strip().lower()
                    if accion == "si":
                        administrador()
                    break

                administrador()

            if hospedajes == "3":
                print("¿Qué desea eliminar?\n")
                print("1. Hospedaje")
                print("2. Habitaciones de un hospedaje")
                print("3. Volver\n")

                hospedajes_eliminar = input().strip()

                if hospedajes_eliminar == "1":
                    print("Ingrese el nombre del hospedaje a eliminar")
                    nombre = input().strip()
                    print("Ingrese la ubicación del hospedaje a eliminar")
                    ubicacion = input().strip()

                    hospedaje = Hospedaje.buscarHospedaje(nombre, ubicacion)
                    if hospedaje is None:
                        print(f"No se ha encontrado el hospedaje {nombre}\n")
                        print("Desea realizar alguna acción más cómo administrador (si/no)")
                        accion = input().strip().lower()
                        if accion == "si":
                            administrador()
                        break

                    Hospedaje.eliminarHospedaje(nombre, ubicacion)
                    print(f"Hospedaje {nombre} eliminado exitosamente\n")
                    print("Desea realizar alguna acción más cómo administrador (si/no)")
                    accion = input().strip().lower()
                    if accion == "si":
                        administrador()
                    break

                if hospedajes_eliminar == "2":
                    print("Ingrese el nombre del hospedaje a eliminar")
                    nombre = input().strip()
                    print("Ingrese la ubicación del hospedaje a eliminar")
                    ubicacion = input().strip()

                    hospedaje = Hospedaje.buscarHospedaje(nombre, ubicacion)
                    if hospedaje is None:
                        print(f"No se ha encontrado el hospedaje {nombre}\n")
                        print("Desea realizar alguna acción más cómo administrador (si/no)")
                        accion = input().strip().lower()
                        if accion == "si":
                            administrador()
                        break

                    print("Ingrese el número de la habitación")
                    habitacion = input().strip()

                    if hospedaje.buscarHabitacion(habitacion) is None:
                        print(f"No se ha encontrado la habitación {habitacion}\n")
                        print("Desea realizar alguna acción más cómo administrador (si/no)")
                        accion = input().strip().lower()
                        if accion == "si":
                            administrador()
                        break

                    hospedaje.eliminarHabitacion(habitacion)
                    print(f"Habitación {habitacion} eliminada exitosamente\n")
                    print("Desea realizar alguna acción más cómo administrador (si/no)")
                    accion = input().strip().lower()
                    if accion == "si":
                        administrador()
                    break

                brea

    if respuesta1 == "4":
            administrador()
            break

        if opcion == "3":
            print("Ingrese una opción\n")
            print("1. Agregar")
            print("2. Ver")
            print("3. Eliminar")
            print("4. Volver\n")

            terminales = input().strip()

            if terminales == "1":
                print("¿Qué desea agregar?\n")
                print("1. Terminal")
                print("2. Empresa a una terminal")
                print("3. Volver\n")

                terminales_agregar = input().strip()

                if terminales_agregar == "1":
                    print("Ingrese el nombre de la terminal")
                    nombre = input().strip()

                    print("Ingrese la ubicación de la terminal")
                    ubicacion = input().strip()

                    terminal = Terminal.buscarTerminal(nombre, ubicacion)
                    if terminal is not None:
                        print("La terminal ya existe\n")
                        print("Desea realizar alguna acción más cómo administrador (si/no)")
                        accion = input().strip().lower()
                        if accion == "si":
                            administrador()
                        break

                    Terminal(nombre, ubicacion)
                    print("Terminal creada exitosamente\n")
                    print("Desea realizar alguna acción más cómo administrador (si/no)")
                    accion = input().strip().lower()
                    if accion == "si":
                        administrador()
                    break

                if terminales_agregar == "2":
                    print("Ingrese el nombre de la empresa")
                    nombre_emp = input().strip()

                    print("Ingrese el nombre de la terminal")
                    nombre_ter = input().strip()

                    print("Ingrese la ubicación de la terminal")
                    ubicacion = input().strip()

                    terminal = Terminal.buscarTerminal(nombre_ter, ubicacion)
                    empresa = Empresa.buscarEmpresa(nombre_emp)

                    if terminal is None or empresa is None:
                        print(f"No se ha encontrado la terminal {nombre_ter} ó la empresa {nombre_emp}\n")
                        print("Desea realizar alguna acción más cómo administrador (si/no)")
                        accion = input().strip().lower()
                        if accion == "si":
                            administrador()
                        break

                    terminal.agregarEmpresa(empresa)
                    print(f"Empresa {nombre_emp} ha sido vinculada a la terminal {nombre_ter}\n")
                    print("Desea realizar alguna acción más cómo administrador (si/no)")
                    accion = input().strip().lower()
                    if accion == "si":
                        administrador()
                    break

                administrador()

            if terminales == "2":
                print("¿Qué desea ver?\n")
                print("1. Terminales")
                print("2. Volver\n")

                terminales_ver = input().strip()

                if terminales_ver == "1":
                    print("Lista de terminales")
                    print("-" * 35)
                    print("    Nombre           Ubicación")
                    print("-" * 35)

                    for terminal in Terminal.getTerminales():
                        if terminal is not None:
                            print(f"    {terminal.nombre}             {terminal.ubicacion}")

                        print()

                    print("Desea realizar alguna acción más cómo administrador (si/no)")
                    accion = input().strip().lower()
                    if accion == "si":
                        administrador()
                    break

                administrador()

            if terminales == "3":
                print("¿Qué desea eliminar?\n")
                print("1. Terminal")
                print("2. Empresa de una terminal")
                print("3. Volver\n")

                terminales_eliminar = input().strip()

                if terminales_eliminar == "1":
                    print("Ingrese el nombre de la terminal a eliminar")
                    nombre = input().strip()
                    print("Ingrese la ubicación de la terminal a eliminar")
                    ubicacion = input().strip()
                    terminal = Terminal.buscarTerminal(nombre, ubicacion)
                    if terminal is None:
                        print(f"No se ha encontrado la terminal {nombre} en {ubicacion}\n")
                        print("Desea realizar alguna acción más cómo administrador (si/no)")
                        accion = input().strip().lower()
                        if accion == "si":
                            administrador()
                        break

                    Terminal.eliminarTerminal(nombre, ubicacion)
                    print(f"Terminal {nombre} en {ubicacion} ha sido eliminada exitosamente\n")
                    print("Desea realizar alguna acción más cómo administrador (si/no)")
                    accion = input().strip().lower()
                    if accion == "si":
                        administrador()
                    break

                if terminales_eliminar == "2":
                    print("Ingrese el nombre de la terminal")
                    nombre_ter = input().strip()
                    print("Ingrese la ubicación de la terminal")
                    ubicacion = input().strip()

                    terminal = Terminal.buscarTerminal(nombre_ter, ubicacion)
                    if terminal is None:
                        print(f"No se ha encontrado la terminal {nombre_ter} en {ubicacion}\n")
                        print("Desea realizar alguna acción más cómo administrador (si/no)")
                        accion = input().strip().lower()
                        if accion == "si":
                            administrador()
                        break

                    print("Ingrese el nombre de la Empresa")
                    nombre_emp = input().strip()

                    if Empresa.buscarEmpresa(nombre_emp) is None:
                        print(f"No se ha encontrado la empresa {nombre_emp}\n")
                        print("Desea realizar alguna acción más cómo administrador (si/no)")
                        accion = input().strip().lower()
                        if accion == "si":
                            administrador()
                        break

                    terminal.eliminarEmpresa(nombre_emp)
                    print(f"Empresa {nombre_emp} eliminada exitosamente\n")
                    print("Desea realizar alguna acción más cómo administrador (si/no)")
                    accion = input().strip().lower()
                    if accion == "si":
                        administrador()
                    break

                administrador()

            if opcion == "4":
                administrador()
            break





