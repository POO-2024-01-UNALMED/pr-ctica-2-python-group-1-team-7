from uiMain.funcionalidades.funcionalidad1 import ver_viajes
from uiMain.field_frame import field_frame
#from uiMain.ventanas.ventana_principal import ventana_principal

from uiMain import auxiliar
import tkinter as tk

class funcionalidad_1(tk.Frame):
    numero_frames = 1
    def __init__(self,ventana_principal:tk.Tk, frame):
        if funcionalidad_1.numero_frames == 1:
            super().__init__(frame)
            self.ventana_principal=ventana_principal
            self.ventana_principal.frame_activo = self

            self.pack(expand=True, fill="both")
            self.pack_propagate(False)

            self.frame_superior = tk.Frame(self)
            self.frame_superior.pack(side="top", expand=True, fill="both")
            self.frame_superior.pack_propagate(False)

            self.frame_centro = tk.Frame(self)
            self.frame_centro.pack( expand=True, fill="both")
            self.frame_centro.pack_propagate(False)

            scrollable_frame = auxiliar.generar_scrollbar(self.frame_centro)

            self.botones = auxiliar.generar_botones(self)
            self.boton_aceptar = self.botones[0]
            self.boton_borrar = self.botones[1]

            self.field_frame = field_frame(
                scrollable_frame, 
                "Consultas", 
                ["¿Desea ver más detalles sobre un viaje?"], 
                "Respuestas del usuario", 
                None
            )

            self.text = tk.Text(self.frame_superior, font=(("Consolas", 11)))
            self.text.pack(expand=True, fill="both")

            self.boton_aceptar.config(command=self.primer_paso)
            self.boton_borrar.config(command=self.field_frame.clear_entries)

            ver_viajes.mostrar_viajes(self)
        else:
            super().__init__()

        funcionalidad_1.numero_frames += 1
    
    def primer_paso(self):
        boolean = ver_viajes.primera_pregunta(self)
        if boolean:
            self.boton_aceptar.config(command=self.segundo_paso)
        else:
            self.ventana_principal.volver_principal(self.ventana_principal)

    def segundo_paso(self):
        ver_viajes.segunda_pregunta(self)
        self.boton_aceptar.config(command=self.tercer_paso)

    def tercer_paso(self):
        boolean = ver_viajes.tercera_pregunta(self)
        if boolean:
            self.boton_aceptar.config(command=self.cuarto_paso)
        else:
            self.ventana_principal.volver_principal(self.ventana_principal)

    def cuarto_paso(self):
        ver_viajes.cuarta_pregunta(self)
        self.boton_aceptar.config(command=self.quinto_paso)

    def quinto_paso(self):
        ver_viajes.quinta_pregunta(self)
        self.boton_aceptar.config(state="disabled")
        self.boton_borrar.config(state="disabled")
