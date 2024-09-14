from uiMain.funcionalidades.funcionalidad1 import ver_viajes
from uiMain.field_frame import field_frame
from uiMain import auxiliar
import tkinter as tk

class funcionalidad_1(tk.Frame):
    numero_frames = 1
    def __init__(self, frame):
        if funcionalidad_1.numero_frames == 1:
            super().__init__(frame)
            self.pack(expand=True, fill="both")
            self.pack_propagate(False)

            self.frame_superior = tk.Frame(self)
            self.frame_superior.pack(side="top", expand=True, fill="both")
            self.frame_superior.pack_propagate(False)

            self.text_viajes = tk.Text(self.frame_superior, font=(("Calibri", 12)))
            self.text_viajes.pack(expand=True, fill="both")

            ver_viajes.mostrar_viajes(self.text_viajes)

            """ field_frame(
                scrollable_frame, "CRITERIO", 
                ["¿Desea filtrar por alguna categoría?"], 
                "VALOR", 
                None
            ).pack(fill="x", expand=True) """

            botones = auxiliar.generar_botones(self)

            self.frame_centro = tk.Frame(self)
            self.frame_centro.pack(expand=True, fill="both")
            self.frame_centro.pack_propagate(False)

            canvas = tk.Canvas(self.frame_centro, bg='lightblue')
            canvas.pack(fill="both", expand=True)

            scrollbar = tk.Scrollbar(
                self.frame_centro, 
                orient="vertical", 
                command=canvas.yview
            )
            scrollbar.pack(side="right", fill="y")

            canvas.configure(yscrollcommand=scrollbar.set)

            scrollable_frame = tk.Frame(canvas)
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            window = canvas.create_window(
                (0, 0), 
                window=scrollable_frame, 
                anchor="nw"
            )

            def on_canvas_resize(event):
                canvas.itemconfig(window, width=event.width)

            canvas.bind("<Configure>", on_canvas_resize)

            f1=field_frame(
                scrollable_frame, 
                "CRITERIO", 
                ["¿Desea filtrar por alguna categoría?","a","b"], 
                "VALOR", 
                None
            )

            f1.pack(fill="x", expand=True)
            f1.ocultar_campos(["a","b"])

            #field_frame(self.frame_centro,None,["¿Por cuál categoría desea filtrar?"],None,None).pack(side='bottom',fill='x',expand=True)
        else:
            super().__init__()

        funcionalidad_1.numero_frames += 1

