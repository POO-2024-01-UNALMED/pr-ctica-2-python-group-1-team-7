from datetime import datetime, time
from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.hospedaje import Hospedaje
from gestorAplicación.gestion.terminal import Terminal
from gestorAplicación.gestion.tiquete import Tiquete
from gestorAplicación.gestion.viaje import Viaje
from gestorAplicación.personas.pasajero import Pasajero
from gestorAplicación.transporte.bus import Bus
import unidecode
import tkinter as tk
from tkinter import messagebox
from funcionalidades.funcionalidad1 import ver_viajes
#from funcionalidad_2 import reservar_tiquete
from uiMain.funcionalidades.funcionalidad3 import gestionar_tiquetes
from uiMain.funcionalidades.funcionalidad4 import hospedaje
#from funcionalidad5 import administrador
from PIL import Image, ImageTk
from ventanas import ventana_inicio

class FieldFrame(tk.Frame):
    def __init__(self,tituloCriterios,criterios,tituloValores,valores,habilitado):
        self.tituloCriterios=tituloCriterios
        self.criterios=criterios
        self.tituloValores=tituloValores
        self.valores=valores
        self.habilitado=habilitado

    def getValue(self,criterio):
        #Lanzar un exception error si no encuentra el criterior
        if criterio in self.criterios:
            return self.valores[criterio.index()]

# Normaliza la entrada eliminando acentos y caracteres especiales
def sc_input(mensaje: str):
    input_value = input(mensaje)
    return unidecode.unidecode(input_value).strip()

def cerrar_ventana(ventana2, ventana1):
    ventana2.destroy()
    ventana1.deiconify()

def cerrar_ambas_ventanas(ventana, ventana1):
    ventana.destroy()
    ventana1.destroy()

def info_aplicacion():
    messagebox.showinfo("Acerca de la Aplicación", "Esta aplicación permite al usuario ....")

def acerca_de():
    messagebox.showinfo("Autores", "Autores de la aplicación:\n\n- Santiago Cardona Franco \n- Samuel Hernández Duque")

def funcionalidad_1(ventana,frame_interno3):

    frame_down = tk.Frame(frame_interno3, highlightbackground="black", highlightthickness=1)
    frame_down.pack(side="bottom", fill="x")

    botones_frame = tk.Frame(frame_down, highlightbackground="black", highlightthickness=1)
    botones_frame.pack(side="bottom",anchor='s',pady=5)

    boton_aceptar = tk.Button(botones_frame, text="Aceptar", font=("Arial", 10), width=8, height=1)
    boton_aceptar.pack(side='left',anchor='s', padx=7)

    boton_borrar = tk.Button(botones_frame, text="Borrar", font=("Arial", 10), width=8, height=1)
    boton_borrar.pack(side='left',anchor='s', padx=7)

    frame_up = tk.Frame(frame_interno3, highlightbackground="black", highlightthickness=1)
    frame_up.pack(side="top", fill="both", expand=True)

    frame_center = tk.Frame(frame_interno3, highlightbackground="black", highlightthickness=1)
    frame_center.pack(fill="both", expand=True)


def ventana_principal(ventana1):
    ventana1.withdraw()
    ventana = tk.Tk()
    ventana.title("LussajuBus")
    ventana.geometry("800x500")

    ventana.protocol("WM_DELETE_WINDOW",lambda:cerrar_ambas_ventanas(ventana1, ventana))

    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu) 

    menu_archivo = tk.Menu(barra_menu, tearoff="off")
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

    menu_archivo.add_command(label="Aplicación", command=lambda: info_aplicacion())
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=lambda:cerrar_ventana(ventana,ventana1))

    menu_procesos = tk.Menu(barra_menu, tearoff="off")
    barra_menu.add_cascade(label="Procesos y Consultas", menu=menu_procesos)

    menu_procesos.add_command(label="Ver viajes",command=lambda: funcionalidad_1(ventana,frame_interno3))
    menu_procesos.add_separator()
    menu_procesos.add_command(label="Reservar tiquete")
    menu_procesos.add_separator()
    menu_procesos.add_command(label="Gestionar tiquetes")
    menu_procesos.add_separator()
    menu_procesos.add_command(label="Servicio de hospedaje")
    menu_procesos.add_separator()
    menu_procesos.add_command(label="Administrador")

    menu_ayuda = tk.Menu(barra_menu, tearoff="off")
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
    menu_ayuda.add_command(label="Acerca de", command=lambda:acerca_de())
      
    frame_ventana = tk.Frame(ventana, highlightbackground="black", 
                                    highlightthickness=2)
    frame_ventana.pack(padx=(20, 20), pady=(20, 20), fill="both", expand=True)

    nombre_proceso_consulta="Bienvenido a la ventana principal"

    label_nombre=tk.Label(frame_ventana,text=nombre_proceso_consulta,font=("Arial",15))
    label_nombre.pack(side="top", anchor="n", pady=10)

    frame_interno1=tk.Frame(frame_ventana,highlightbackground="black", 
                                    highlightthickness=1)
    frame_interno1.pack(fill="both", expand=True)

    texto_descripcion="Aquí va la descripción de la funcionalidad\n...\n..."

    label_descripcion=tk.Label(frame_interno1,text=texto_descripcion,font=("Arial",10))
    label_descripcion.pack(side="top", anchor="n", pady=10)

    frame_interno2=tk.Frame(frame_interno1,highlightbackground="black", 
                                    highlightthickness=1)
    frame_interno2.pack(fill="both", expand=True)

    frame_interno3=tk.Frame(frame_interno2,highlightbackground="black", 
                                    highlightthickness=1)
    frame_interno3.pack(pady=10,padx=100,fill="both", expand=True)

    ventana.mainloop()
