from uiMain.funcionalidades.funcionalidad1 import ver_viajes
from uiMain.field_frame import field_frame
from uiMain import auxiliar
import tkinter as tk

class funcionalidad_1(tk.Frame):
    numero_frames = 1
    def __init__(self,ventana_principal, frame):
        if funcionalidad_1.numero_frames == 1:
            super().__init__(frame)
            self.ventana_principal=ventana_principal

            self.pack(expand=True, fill="both")
            self.pack_propagate(False)

            self.frame_superior = tk.Frame(self)
            self.frame_superior.pack(side="top", expand=True, fill="both")
            self.frame_superior.pack_propagate(False)

            self.text_viajes = tk.Text(self.frame_superior, font=(("Calibri", 12)))
            self.text_viajes.pack(expand=True, fill="both")

            ver_viajes.mostrar_viajes(self.text_viajes)

            botones=auxiliar.generar_botones(self)

            self.frame_centro = tk.Frame(self)
            self.frame_centro.pack( expand=True, fill="both")
            self.frame_centro.pack_propagate(False)

            scrollable_frame=auxiliar.generar_scrollbar(self.frame_centro)

            f1=field_frame(
                scrollable_frame, 
                "Preguntas", 
                ["¿Desea filtrar por alguna categoría?",
                 "¿Por cuál categoría desea filtrar?",
                 "Ingrese la fecha en formato dd-mm-aaaa:",
                 "Ingrese el origen: ",
                 "Ingrese el destino: ",
                 "Ingrese la hora de salida en formato 24 horas: ",
                 "Ingrese el id del viaje: ",
                 "Ingrese la placa del vehiculo: ",
                 "¿Desea ver más detalles sobre un viaje? (si/no) ",
                 "¿Qué desea hacer?",
                 "¿Desea reservar un asiento por un cierto período de tiempo? (si/no) ",
                 "Ingrese el número del asiento: ",
                 "Ingrese otro número de asiento: ",
                 "¿Por cuánto tiempo desea reservarlo? (minutos/horas/dias)",
                 ], 
                "Respuestas del Usuario", 
                None
            )

            f1.pack(fill="x", expand=True)

            f1.ocultar_campos(["¿Por cuál categoría desea filtrar?",
                 "Ingrese la fecha en formato dd-mm-aaaa:",
                 "Ingrese el origen: ",
                 "Ingrese el destino: ",
                 "Ingrese la hora de salida en formato 24 horas: ",
                 "Ingrese el id del viaje: ",
                 "Ingrese la placa del vehiculo: ",
                 "¿Desea ver más detalles sobre un viaje? (si/no) ",
                 "¿Qué desea hacer?",
                 "¿Desea reservar un asiento por un cierto período de tiempo? (si/no) ",
                 "Ingrese el número del asiento: ",
                 "Ingrese otro número de asiento: ",
                 "¿Por cuánto tiempo desea reservarlo? (minutos/horas/dias)",
                 ])

            boton_aceptar=botones[0]

            boton_borrar=botones[1]
            boton_aceptar.bind("<Button-1>",lambda event: self.manejar_datos(event, f1))
            boton_borrar.bind("<Button-1>", lambda event: self.borrar_datos(event, f1))
            self.lista_respuestas=[]

            #logica programa
            if self.lista_respuestas:
                if self.lista_respuestas[0].strip().lower()=="si":
                    f1.activar_campo(["¿Por cuál categoría desea filtrar?"])
                    respuesta_actual= self.lista_respuestas[1].strip().lower()
                    match respuesta_actual:
                        case 1:
                            pass
                else:
                    pass
            #self.ventana_principal.volver_principal()

            
        else:
            super().__init__()

        funcionalidad_1.numero_frames += 1

    def borrar_datos(event,fieldframe:field_frame):
        for key,entry in fieldframe.entries.items():
            entry.delete(0,tk.END)

    def guardar_datos(event,fieldframe:field_frame):
        return [entry.get() for entry in fieldframe.entries.values()]

    def manejar_datos(event,self,fieldframe:field_frame):
        self.lista_respuestas = funcionalidad_1.guardar_datos(event, fieldframe)

