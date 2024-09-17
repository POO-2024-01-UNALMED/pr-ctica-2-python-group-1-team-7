from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.viaje import Viaje
from gestorAplicación.gestion.tiquete import Tiquete
from gestorAplicación.personas.pasajero import Pasajero
import auxiliar_excepciones as ae

from uiMain import auxiliar
import tkinter as tk
from tkinter import messagebox

class ver_viajes():
    @staticmethod
    def mostrar_viajes(frame_funcionalidad):
        for empresa in Empresa.get_empresas():
            frame_funcionalidad.text.insert(
                "end", 
                f"Viajes disponibles de la empresa {empresa.get_nombre()}\n"
            )
            frame_funcionalidad.text.insert("end", "-" * 91 + "\n")
            frame_funcionalidad.text.insert(
                "end", 
                "    FECHA          ORIGEN          DESTINO" 
                + "         HORA DE SALIDA     ID      PLACA BUS\n"
            )
            frame_funcionalidad.text.insert("end", "-" * 91 + "\n")

            for viaje in empresa.get_viajes():
                frame_funcionalidad.text.insert("end", str(viaje) + "\n")
            
            frame_funcionalidad.text.insert("end", "\n")

        frame_funcionalidad.text.config(state="disabled")
    
    @staticmethod
    def primera_pregunta(frame_funcionalidad):
        respuesta = frame_funcionalidad.field_frame.getValue(
            "¿Desea ver más detalles sobre un viaje?"
        ).lower()
        
        if respuesta == "si":
            frame_funcionalidad.field_frame.agregar_campo(
                "Ingrese el id del viaje", 
                True
            )
            return -1
        elif respuesta == "no":
            return 0
        else:
            tk.messagebox.showwarning("Advertencia","Solo se admite (si/no)")
            return 1

    @staticmethod
    def segunda_pregunta(frame_funcionalidad):
        respuesta = frame_funcionalidad.field_frame.getValue(
            "Ingrese el id del viaje"
        )

        try:
            ae.excepcion_viaje(respuesta)
            viaje = Empresa.buscar_viaje_por_id(respuesta)
            

        except:
            messagebox.showerror("Error inesperado",
                                 "Se ha producido un error inesperado pero puede continuar navegando en el programa")
            return 0
        frame_funcionalidad.text.pack_forget()

        auxiliar.asientos(frame_funcionalidad.frame_superior, viaje)

        frame_funcionalidad.field_frame.agregar_campo(
            "¿Desea reservar un asiento por un cierto período de tiempo?",
            True
        )
        return -1

    @staticmethod
    def tercera_pregunta(frame_funcionalidad):
        respuesta = frame_funcionalidad.field_frame.getValue(
            "¿Desea reservar un asiento por un cierto período de tiempo?"
        ).lower()

        if respuesta == "si":
            frame_funcionalidad.field_frame.agregar_campo(
                "Ingrese el número del asiento", 
                True
            )
            return True
        elif respuesta == "no":
            return False
        else:
            tk.messagebox.showwarning("Advertencia","Solo se admite (si/no)")
            return False

    @staticmethod
    def cuarta_pregunta(frame_funcionalidad):
        respuesta = frame_funcionalidad.field_frame.getValue(
            "Ingrese el número del asiento"
        )
        
        indice=frame_funcionalidad.field_frame.getValue(
                "Ingrese el id del viaje")
        viaje = Empresa.buscar_viaje_por_id(indice)
        ok=ae.excepcion_viaje(indice)
        if ok=="ok":
            ae.excepcion_asiento(respuesta,viaje.get_bus())
    

    
        try:
            asiento = viaje.buscar_asiento(respuesta)
            if asiento != None and not asiento.is_reservado():
                frame_funcionalidad.field_frame.agregar_campo(
                    "¿Por cuánto tiempo desea reservarlo?", 
                    True
                )
        except:
            messagebox.showerror("Error inesperado",
                                 "Se ha producido un error inesperado pero puede continuar navegando en el programa")

    @staticmethod
    def quinta_pregunta(frame_funcionalidad):
        respuesta = frame_funcionalidad.field_frame.getValue(
            "¿Por cuánto tiempo desea reservarlo?"
        ).lower()

        frame_funcionalidad.field_frame.entries[
            "¿Por cuánto tiempo desea reservarlo?"
        ].config(state="disabled")

        try:
            if respuesta[-1] == "s":
                tiempo = respuesta[0:2]
                unidad_tiempo = respuesta[3:]
            else:
                tiempo = respuesta[0]
                unidad_tiempo = respuesta[2:]
        except:
            messagebox.showerror("Error inesperado",
                                 "Se ha producido un error inesperado pero puede continuar navegando en el programa")

        frame_funcionalidad.frame_superior.winfo_children()[-1].destroy()

        frame_funcionalidad.text.config(state="normal")
        frame_funcionalidad.text.delete("1.0", "end")
        frame_funcionalidad.text.pack(expand=True, fill="both")
        frame_funcionalidad.text.insert("end", "Asiento reservado exitosamente")

