from uiMain.funcionalidades.funcionalidad3 import gestionar_tiquetes
from uiMain.field_frame import field_frame
from uiMain import auxiliar
import tkinter as tk

class funcionalidad_3(tk.Frame):
    numero_frames = 1
    def __init__(self,ventana_principal, frame):
        if funcionalidad_3.numero_frames == 1:
            super().__init__(frame)
            self.ventana_principal = ventana_principal
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
                ["Ingrese el número de identificación del pasajero"], 
                "Respuestas del usuario", 
                None
            )

            self.text = tk.Text(self.frame_superior, font=(("Consolas", 11)))
            self.text.pack(expand=True, fill="both")

            self.boton_aceptar.config(command=self.primer_paso)
            self.boton_borrar.config(command=self.field_frame.clear_entries)
        else:
            super().__init__()

        funcionalidad_3.numero_frames += 1
    
    def primer_paso(self):
        try:
            gestionar_tiquetes.mostrar_tiquetes(self)
        except:
            pass
        else:
            self.boton_aceptar.config(command=self.segundo_paso)

    def segundo_paso(self):
        try:
            gestionar_tiquetes.primera_pregunta(self)
        except:
            pass
        else:
            self.boton_aceptar.config(command=self.tercer_paso)

    def tercer_paso(self):
        try:
            gestionar_tiquetes.seleccionar_tiquete(self)
        except:
            pass
        else:
            self.boton_aceptar.config(command=self.cuarto_paso)

    def cuarto_paso(self):
        try:
            gestionar_tiquetes.decision(self)
        except:
            pass
        else:
            self.boton_aceptar.config(command=self.quinto_paso)

    def quinto_paso(self):
        try:
            gestionar_tiquetes.modificar(self, self.ventana_principal)
        except:
            pass
        else:
            self.boton_aceptar.config(command=self.sexto_paso)

    def sexto_paso(self):
        try:
            gestionar_tiquetes.modificar_continuacion(self)
        except:
            pass

