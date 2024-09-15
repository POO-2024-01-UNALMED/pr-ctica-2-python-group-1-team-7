from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.viaje import Viaje
import tkinter as tk

class reservar_tiquete():
    @classmethod
    def obtener_ubicaciones(cls, tipo):
        ubicaciones = []
        for empresa in Empresa.get_empresas():
            for viaje in empresa.get_viajes():
                if tipo == "origenes":
                    ubicaciones.append(viaje.get_terminal_origen().get_ubicacion())
                elif tipo == "destinos":
                    ubicaciones.append(viaje.get_terminal_destino().get_ubicacion())
        return list(set(ubicaciones))

    @classmethod
    def mostrar_viajes(cls, text, combobox_origen, combobox_destino):
        text.config(state="normal")
        text.delete("1.0", "end")
        origen = combobox_origen.get()
        destino = combobox_destino.get()
        viajes = Empresa.buscar_viajes_por_origen_destino(origen, destino)

        if not viajes:
            text.insert(
                "end", 
                "No se encontraron viajes disponibles para reservar\n"
            )
        else:
            text.insert(
                "end", 
                "Estos son los viajes disponibles para la ruta " 
                + f"{origen.upper()} --> {destino.upper()}:\n"
            )

            for viaje in viajes:
                text.insert("end", "-" * 91 + "\n")
                text.insert(
                    "end", 
                    "    FECHA          ORIGEN          DESTINO" 
                    + "         HORA DE SALIDA     ID      PLACA BUS\n"
                )
                text.insert("end", "-" * 91 + "\n")
                text.insert("end", str(viaje) + "\n")
                text.insert("end", "\n")
        text.config(state="disabled")
        return viajes

    @classmethod
    def mostrar_asientos(cls, frame_superior, text, field_frame, viajes):
        text.config(state="normal")
        text.delete("1.0", "end")
        viaje = Viaje.buscar_viaje(
            viajes, 
            field_frame.entries["Ingrese el id del viaje"].get()
        )

        if not viaje:
            text.insert(
                "end", 
                f"No se encontró ningún viaje con número de id {id}" 
                + " disponible para reservar\n"
            )
        else:
            text.pack_forget()
            field_frame.entries["Ingrese el id del viaje"].config(state="disabled")
            
            frame_principal = tk.Frame(frame_superior)
            frame_principal.place(relx=0.5, rely=0.5, anchor="center")

            frame_asientos = tk.Frame(frame_principal)
            frame_asientos.pack(side="left", padx=(50, 10), pady=20)

            frame_tipos_asiento = tk.Frame(frame_principal)
            frame_tipos_asiento.pack(side="right", padx=(10, 50), pady=50)

            label_preferencial = tk.Label(
                frame_tipos_asiento, 
                bg="lightblue", 
                text="Preferencial"
            )
            label_preferencial.grid(row=0, column=0)

            label_premium = tk.Label(
                frame_tipos_asiento, 
                bg="lightgreen", 
                text="Premium"
            )
            label_premium.grid(row=1, column=0)

            label_estandar = tk.Label(
                frame_tipos_asiento, 
                bg="lightyellow", 
                text="Estándar"
            )
            label_estandar.grid(row=2, column=0)

            letras = "DCBA"
            for i in range(15):
                for j in range(4):
                    if i + 1 <= 5:
                        tk.Label(
                            frame_asientos, 
                            bg="lightblue", 
                            text=str(i+1) + letras[j] + " ", 
                            font="Consolas"
                        ).grid(row=j, column=i)
                    elif i + 1 < 10:
                        tk.Label(
                            frame_asientos, 
                            bg="lightgreen", 
                            text=str(i+1) + letras[j] + " ", 
                            font="Consolas"
                        ).grid(row=j, column=i)
                    else:
                        tk.Label(
                            frame_asientos, 
                            bg="lightyellow", 
                            text=str(i+1) + letras[j], 
                            font="Consolas"
                        ).grid(row=j, column=i)

""" 
from gestorAplicación.gestion.empresa import Empresa
from auxiliar import sc_input
import re

def reservar_tiquete():
    origen = sc_input("Ingrese el origen: ").strip()
    destino = sc_input("Ingrese el destino: ").strip()

    viajes = Empresa.buscar_viajes_por_origen_destino(origen.upper(), destino.upper())

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

        id = sc_input("Ingrese el id del viaje: ").strip()

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

            numero_asiento = sc_input("Ingrese el número del asiento: ").strip()

            while True:
                asiento = viaje.buscar_asiento(numero_asiento)
                if asiento is None or asiento.is_reservado():
                    print("\nEl asiento no está disponible\n")
                    numero_asiento = sc_input("Ingrese otro número de asiento: ").strip()
                else:
                    break

            viaje.reservar_asiento(numero_asiento, None)

            print("Ingrese sus datos:\n")

            nombre = sc_input("Nombre completo: ").strip()
            id_pasajero = sc_input("Número de identificación (6 dígitos): ").strip()

            while len(id_pasajero) != 6:
                id_pasajero = sc_input("Número de identificación (6 dígitos): ").strip()

            pasajero = Pasajero.buscar_pasajero(id_pasajero)

            if not pasajero:
                telefono = sc_input("Teléfono: ").strip()
                while not re.match(r'^\d{10}$', telefono):
                    print("Teléfono inválido\nEl teléfono debe contener 10 dígitos\n")
                    telefono = sc_input("Teléfono: ").strip()

                correo = sc_input("Correo electrónico: ").strip()
                while not re.match(r'^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$', correo):
                    print("Correo inválido\nEl correo debe tener la estructura (abcde@xyz.com)\n")
                    correo = sc_input("Correo electrónico: ").strip()

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
"""
