from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.viaje import Viaje
from gestorAplicación.gestion.tiquete import Tiquete
from gestorAplicación.personas.pasajero import Pasajero
import auxiliar_excepciones as ae

from uiMain import auxiliar
import tkinter as tk

class reservar_tiquete():
    @staticmethod
    def obtener_ubicaciones(tipo):
        ubicaciones = []
        for empresa in Empresa.get_empresas():
            for viaje in empresa.get_viajes():
                if tipo == "origenes":
                    ubicaciones.append(viaje.get_terminal_origen().get_ubicacion())
                elif tipo == "destinos":
                    ubicaciones.append(viaje.get_terminal_destino().get_ubicacion())
        return list(set(ubicaciones))

    @staticmethod
    def mostrar_viajes(text, combobox_origen, combobox_destino):
        text.config(state="normal")
        text.delete("1.0", "end")
        origen = combobox_origen.get()
        destino = combobox_destino.get()

        viajes = Empresa.buscar_viajes_por_origen_destino(origen, destino)

        '''        for viaje in viajes:
            if (ae.excepcion_viaje(viaje.get_id()))=="ok":
                print("ok")'''

        if not viajes:
            ae.excepcion_viaje('99999')
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

    @staticmethod
    def mostrar_asientos(frame_superior, text, field_frame, viajes):
        text.config(state="normal")
        text.delete("1.0", "end")
        try:
            viaje = Viaje.buscar_viaje(
                viajes, 
                field_frame.getValue("Ingrese el id del viaje")
            )
            
            if not viaje:
                ae.excepcion_viaje("9999999")

                text.insert(
                    "end", 
                    f"No se encontró ningún viaje con número de id {id}" 
                    + " disponible para reservar\n"
                )
            else:
                text.pack_forget()
                field_frame.agregar_campo("Ingrese el número del asiento", True)
                auxiliar.asientos(frame_superior, viaje)
        except:
            pass

        return viaje
    
    @staticmethod
    def reservar_asiento(field_frame, viaje):
        try:
            numero_asiento = field_frame.getValue("Ingrese el número del asiento")

            asiento = viaje.buscar_asiento(numero_asiento)
            if asiento != None and not asiento.is_reservado():
                ae.excepcion_asiento(numero_asiento,viaje.get_bus())
                viaje.reservar_asiento(numero_asiento, None)
                field_frame.agregar_campo("Nombre", True)
                field_frame.agregar_campo("Id", False)
                field_frame.agregar_campo("Correo", False)
                field_frame.agregar_campo("Teléfono", False)  
                return asiento
            else:
                ae.excepcion_asiento(numero_asiento,viaje.get_bus())
                return None  
        except:
            pass
       
    @staticmethod
    def imprimir_tiquete(frame_superior, field_frame, viaje, asiento):
        try:
            frame_superior.winfo_children()[1].destroy()

            text = frame_superior.winfo_children()[0]
            text.tag_configure("center", justify='center')
            text.tag_add("center", 1.0, "end")
            text.pack(expand=True, fill="both")

            atributos = []
            for criterio in list(field_frame.labels.keys())[-4:]:
                field_frame.entries[criterio].config(state="disabled")
                atributos.append(field_frame.getValue(criterio))

            pasajero = Pasajero(atributos[0], atributos[1], atributos[2], atributos[3])
            tiquete = Tiquete(pasajero, viaje, asiento)
            pasajero.agregar_tiquete(tiquete)
            
            text.insert("end", "Tiquete reservado exitosamente\n", "center")
            text.insert("end", "-" * 34 + "\n")
            text.insert("end", f"Tiquete No. {tiquete.get_numero_reserva()}" + "\n")
            text.insert("end", "-" * 34 + "\n")
            text.insert("end", f"Nombre del pasajero: {atributos[0]}" + "\n")
            text.insert("end", f"Id del pasajero: {atributos[1]}" + "\n")
            text.insert("end", f"Teléfono: {atributos[2]}" + "\n")
            text.insert("end", f"Correo: {atributos[3]}" + "\n")
            text.insert("end", f"Asiento: {asiento}" + "\n")
            text.insert("end", f"Empresa: {viaje.get_empresa().get_nombre()}" + "\n")
            text.insert("end", f"Placa del bus: {viaje.get_bus().get_placa()}" + "\n")
            text.insert("end", f"Id del viaje: {viaje.get_id()}" + "\n")
            text.insert(
                "end", 
                f"Fecha y hora: {viaje.get_fecha()} {viaje.get_hora().strftime("%H:%M")}" 
                + "\n"
            )
            text.insert(
                "end", 
                f"Origen: {viaje.get_terminal_origen().get_ubicacion()}" 
                + "\n"
            )
            text.insert(
                "end", 
                f"Destino: {viaje.get_terminal_destino().get_ubicacion()}" 
                + "\n"
            )
            text.insert("end", "-" * 34 + "\n")
        except:
            pass