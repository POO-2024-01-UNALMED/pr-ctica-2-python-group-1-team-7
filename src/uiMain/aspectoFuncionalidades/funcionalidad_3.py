from uiMain.funcionalidades.funcionalidad2 import reservar_tiquete
from uiMain.field_frame import field_frame
from uiMain import auxiliar
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 
import os

class funcionalidad_3(tk.Frame):
    numero_frames = 1
    def __init__(self,ventana_principal, frame):
        if funcionalidad_3.numero_frames == 1:
            super().__init__(frame)
            ventana_principal.frame_activo = self
            
            self.pack(expand=True, fill="both")
            self.pack_propagate(False)


        

            image_path = os.path.join("src", "uiMain", "assets", "download.jpg")
            if os.path.exists(image_path):
                img = Image.open(image_path)  # Usa PIL.Image.open para abrir la imagen
                self.img = ImageTk.PhotoImage(img)  # Convierte la imagen a un formato compatible con Tkinter
                self.imagen_label = tk.Label(self, image=self.img)
                self.imagen_label.pack(expand=True, fill='both')
            else:
                print("El archivo no se encuentra en la ruta especificada")
            
            '''self.frame_superior = tk.Frame(self)
            self.frame_superior.pack(side="top", expand=True, fill="both")
            self.frame_superior.pack_propagate(False)'''

            '''self.frame_right=tk.Frame(self.frame_superior, bg='lightgreen')
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

            self.field = field_frame(
                scrollable_frame, 
                "CRITERIO", 
                ["Ingrese el id del viaje"], 
                "VALOR", 
                None
            )
            self.field.pack_forget()

            self.text_viajes = tk.Text(self.frame_superior, font=(("Consolas", 11)))
            self.text_viajes.pack(expand=True, fill="both")

            self.botones[0].config(command=self.primer_paso)'''

        else:
            super().__init__()

        funcionalidad_3.numero_frames += 1
    
    def primer_paso(self):
        viajes = reservar_tiquete.mostrar_viajes(
            self.text_viajes, 
            self.combobox_origen, 
            self.combobox_destino
        )
        if len(viajes) != 0:
            self.field.pack(fill="both")
            self.botones[0].config(command=lambda: self.segundo_paso(viajes))
    
    def segundo_paso(self, viajes):
        viaje = reservar_tiquete.mostrar_asientos(
            self.frame_superior, 
            self.text_viajes, 
            self.field, 
            viajes
        )
        self.frame_right.pack_forget()
        if viaje != None:
            self.botones[0].config(command=lambda: self.tercer_paso(viaje))

    def tercer_paso(self, viaje):
        reservar_tiquete.reservar_asiento(self.field, viaje)
