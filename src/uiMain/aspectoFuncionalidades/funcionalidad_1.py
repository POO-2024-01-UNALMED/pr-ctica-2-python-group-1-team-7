""" import uiMain.FieldFrame as FieldFrame
import tkinter as tk
class funcionalidad_1(tk.Frame):
    def __init__(self,ventana,frame_interno):
        self.ventana=ventana
        self.frame_interno=frame_interno
        botones=FieldFrame.generar_botones(frame_interno)[0]

        frame_up = tk.Frame(self.frame_interno, highlightbackground="black", highlightthickness=1)
        frame_up.pack(side="top", fill="both", expand=True)

        frame_center = tk.Frame(self.frame_interno, highlightbackground="black", highlightthickness=1)
        frame_center.pack(fill="both", expand=True) """

from .field_frame import field_frame
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

            self.frame_inferior = tk.Frame(self)
            self.frame_inferior.pack(side="bottom", expand=True, fill="both")
            self.frame_inferior.pack_propagate(False)
            mensaje = tk.Label(self.frame_inferior, text="AQUÍ VA LOS RESULTADOS DE LAS CONSULTAS")
            mensaje.pack(expand=True, fill="both")

            field_frame(
                self.frame_superior,
                "CRITERIO",
                ["Código", "Nombre", "Descripción", "Ubicación"],
                "VALOR",
                None
            )
        else:
            super().__init__()

        funcionalidad_1.numero_frames += 1

