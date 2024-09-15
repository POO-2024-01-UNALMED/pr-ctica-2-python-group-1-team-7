from uiMain.funcionalidades.funcionalidad2 import reservar_tiquete
from uiMain.field_frame import field_frame
from uiMain import auxiliar
import tkinter as tk
from tkinter import ttk


class funcionalidad_2(tk.Frame):
    numero_frames = 1
    def __init__(self,ventana_principal, frame):
        if funcionalidad_2.numero_frames == 1:
            super().__init__(frame)
            self.pack(expand=True, fill="both")
            self.pack_propagate(False)

            self.frame_superior = tk.Frame(self)
            self.frame_superior.pack(side="top", expand=True, fill="both")
            self.frame_superior.pack_propagate(False)

            self.frame_right=tk.Frame(self.frame_superior, bg='spring green')
            self.frame_right.pack(side='right', fill="y")

            combobox_origen=ttk.Combobox(
                self.frame_right,
                values=reservar_tiquete.obtener_ubicaciones("origenes"),
                state="readonly"
            )
            combobox_origen.pack(side="top", padx=10, pady=(60, 0))
            combobox_origen.set("Seleccione el origen")          

            combobox_destino=ttk.Combobox(
                self.frame_right,
                values=reservar_tiquete.obtener_ubicaciones("destinos"),
                state="readonly"
            )
            combobox_destino.pack(side="bottom", padx=10, pady=(0, 60))
            combobox_destino.set("Seleccione el destino")   

            self.frame_centro = tk.Frame(self)
            self.frame_centro.pack(expand=True, fill="both")
            self.frame_centro.pack_propagate(False)

            scrollable_frame = auxiliar.generar_scrollbar(self.frame_centro)
            botones = auxiliar.generar_botones(self)

            self.text_viajes = tk.Text(self.frame_superior, font=(("Consolas", 11)))
            self.text_viajes.pack(expand=True, fill="both")

            botones[0].config(
                command=lambda: reservar_tiquete.mostrar_viajes(
                    self.text_viajes, 
                    combobox_origen, 
                    combobox_destino
                )
            )

            field_frame(
                scrollable_frame, 
                "CRITERIO", 
                ["Ingrese el id del viaje"], 
                "VALOR", 
                None
            ).pack(fill="x", expand=True)
        else:
            super().__init__()

        funcionalidad_2.numero_frames += 1
