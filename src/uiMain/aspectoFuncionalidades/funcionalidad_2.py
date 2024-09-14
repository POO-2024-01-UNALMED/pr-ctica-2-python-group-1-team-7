from uiMain.field_frame import field_frame
from uiMain import auxiliar
import tkinter as tk
from tkinter import ttk


class funcionalidad_2(tk.Frame):
    numero_frames = 1
    def __init__(self, frame):
        if funcionalidad_2.numero_frames == 1:
            super().__init__(frame)
            self.pack(expand=True, fill="both")
            self.pack_propagate(False)

            self.frame_superior = tk.Frame(self)
            self.frame_superior.pack(side="top", expand=True, fill="both")
            self.frame_superior.pack_propagate(False)

            self.frame_right=tk.Frame(self.frame_superior,bg='spring green')
            self.frame_right.pack(side='right', fill="both", anchor='e')

            combobox_origen=ttk.Combobox(self.frame_right,values=('Bogota','Medellin','Barranquilla'),)
            combobox_origen.set("Seleccione el origen")          
            combobox_origen.pack(side='top',padx=10,pady=(20,40),anchor='ne')

            combobox_destino=ttk.Combobox(self.frame_right,values=('Bogota','Medellin','Barranquilla'))
            combobox_destino.set("Seleccione el destino")   
            combobox_destino.pack(padx=10,pady=(40,40),anchor='ce')

            botones=auxiliar.generar_botones(self)

            self.frame_centro = tk.Frame(self)
            self.frame_centro.pack( expand=True, fill="both")
            self.frame_centro.pack_propagate(False)
            mensaje = tk.Label(self.frame_superior, text="AQUÍ VA LOS RESULTADOS DE LAS CONSULTAS 2")
            mensaje.pack(expand=True, fill="both")
            canvas = tk.Canvas(self.frame_centro,bg='lightblue')
            canvas.pack(side="left", fill="both", expand=True)

            scrollbar = tk.Scrollbar(self.frame_centro, orient="vertical", command=canvas.yview)
            scrollbar.pack(side="right", fill="y")

            canvas.configure(yscrollcommand=scrollbar.set)

            scrollable_frame = tk.Frame(canvas)
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
                )

            window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

            def on_canvas_resize(event):
                canvas.itemconfig(window, width=event.width)

            canvas.bind("<Configure>", on_canvas_resize)

            field_frame(scrollable_frame, "CRITERIO", ["Código", "Nombre", "Descripción", "Ubicación"], "VALOR", None).pack(fill="x", expand=True)
            #field_frame(field_frame,None,'Hola',None,None)
        else:
            super().__init__()

        funcionalidad_2.numero_frames += 1
