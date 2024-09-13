import uiMain.FieldFrame as FieldFrame
import tkinter as tk
class funcionalidad_1(tk.Frame):
    def __init__(self,ventana,frame_interno):
        self.ventana=ventana
        self.frame_interno=frame_interno
        botones=FieldFrame.generar_botones(frame_interno)[0]

        frame_up = tk.Frame(self.frame_interno, highlightbackground="black", highlightthickness=1)
        frame_up.pack(side="top", fill="both", expand=True)

        frame_center = tk.Frame(self.frame_interno, highlightbackground="black", highlightthickness=1)
        frame_center.pack(fill="both", expand=True)
