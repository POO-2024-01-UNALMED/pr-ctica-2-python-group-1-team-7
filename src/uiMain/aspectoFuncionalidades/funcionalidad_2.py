from uiMain.funcionalidades.funcionalidad2 import reservar_tiquete
from uiMain.field_frame import field_frame
from uiMain import auxiliar
import tkinter as tk
from tkinter import ttk
import auxiliar_excepciones as ae

class funcionalidad_2(tk.Frame):
    numero_frames = 1
    def __init__(self,ventana_principal, frame):
        if funcionalidad_2.numero_frames == 1:
            super().__init__(frame)
            ventana_principal.frame_activo = self

            self.pack(expand=True, fill="both")
            self.pack_propagate(False)
        
            self.frame_superior = tk.Frame(self)
            self.frame_superior.pack(side="top", expand=True, fill="both")
            self.frame_superior.pack_propagate(False)

            self.frame_right=tk.Frame(self.frame_superior, bg='LightCyan2')
            self.frame_right.pack(side='right', fill="y")

            self.combobox_origen=ttk.Combobox(
                self.frame_right,
                values=reservar_tiquete.obtener_ubicaciones("origenes"),
                state="readonly"
            )
            self.combobox_origen.pack(side="top", padx=10, pady=(60, 0))
            self.combobox_origen.set("Seleccione el origen")          

            self.combobox_destino=ttk.Combobox(
                self.frame_right,
                values=reservar_tiquete.obtener_ubicaciones("destinos"),
                state="readonly"
            )
            self.combobox_destino.pack(side="bottom", padx=10, pady=(0, 60))
            self.combobox_destino.set("Seleccione el destino")   

            self.frame_centro = tk.Frame(self)
            self.frame_centro.pack(expand=True, fill="both")
            self.frame_centro.pack_propagate(False)

            scrollable_frame = auxiliar.generar_scrollbar(self.frame_centro)

            self.botones = auxiliar.generar_botones(self)
            self.boton_aceptar = self.botones[0]
            self.boton_borrar = self.botones[1]

            self.field = field_frame(
                scrollable_frame, 
                "Consultas", 
                ["Ingrese el id del viaje"], 
                "Respuestas del usuario", 
                None
            )
            self.field.pack_forget()

            self.text_viajes = tk.Text(self.frame_superior, font=(("Consolas", 11)))
            self.text_viajes.pack(expand=True, fill="both")

            self.boton_aceptar.config(command=self.primer_paso)
            self.boton_borrar.config(command=self.field.clear_entries)
        else:
            super().__init__()

        funcionalidad_2.numero_frames += 1
    
    def primer_paso(self):
        viajes = reservar_tiquete.mostrar_viajes(
            self.text_viajes, 
            self.combobox_origen, 
            self.combobox_destino
        )
        if len(viajes) != 0:
            self.field.pack(fill="both")
            self.boton_aceptar.config(command=lambda: self.segundo_paso(viajes))
    
    def segundo_paso(self, viajes):
        viaje = reservar_tiquete.mostrar_asientos(
            self.frame_superior, 
            self.text_viajes, 
            self.field, 
            viajes
        )
        self.frame_right.destroy()
        if viaje != None:
            self.boton_aceptar.config(command=lambda: self.tercer_paso(viaje))
        else:
            self.segundo_paso(self, viajes)

    def tercer_paso(self, viaje):
        asiento = reservar_tiquete.reservar_asiento(self.field, viaje)
        if asiento != None:
            self.boton_aceptar.config(command=lambda: self.cuarto_paso(viaje, asiento))

    def cuarto_paso(self, viaje, asiento):
        if (ae.excepcion_id(self.field.entries["Id"].get())!="ok" or 
            ae.excepcion_telefono(self.field.entries["Teléfono"].get())!="ok" or
            ae.excepcion_correo(self.field.entries["Correo"].get())!="ok"):
            self.cuarto_paso(self, viaje, asiento)
            
        else:
            reservar_tiquete.imprimir_tiquete(
            self.frame_superior, 
            self.field, 
            viaje, 
            asiento)
            self.boton_aceptar.config(state="disabled")
            self.boton_borrar.config(state="disabled")
