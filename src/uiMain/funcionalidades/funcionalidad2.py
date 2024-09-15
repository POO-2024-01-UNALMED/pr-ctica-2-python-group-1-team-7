from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.viaje import Viaje
from uiMain import auxiliar
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
            field_frame.getValue("Ingrese el id del viaje")
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
            field_frame.agregar_campo("Ingrese el número del asiento")

            auxiliar.asientos(frame_superior, viaje)

        return viaje
    
    @classmethod
    def reservar_asiento(cls, field_frame, viaje):
        print("hola")
    
        viaje.buscar_asiento(field_frame.getValue("Ingrese el número del asiento"))

"""  numero_asiento = sc_input("Ingrese el número del asiento: ").strip()

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
print()  """

