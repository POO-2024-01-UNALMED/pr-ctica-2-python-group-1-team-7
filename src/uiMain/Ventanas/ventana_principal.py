""" from datetime import datetime, time
from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.hospedaje import Hospedaje
from gestorAplicación.gestion.terminal import Terminal
from gestorAplicación.gestion.tiquete import Tiquete
from gestorAplicación.gestion.viaje import Viaje
from gestorAplicación.personas.pasajero import Pasajero
from gestorAplicación.transporte.bus import Bus """
""" import unidecode
import tkinter as tk
from tkinter import messagebox
from uiMain.aspectoFuncionalidades import funcionalidad_1
from funcionalidades.funcionalidad1 import ver_viajes
#from funcionalidad_2 import reservar_tiquete
from uiMain.funcionalidades.funcionalidad3 import gestionar_tiquetes
from uiMain.funcionalidades.funcionalidad4 import hospedaje
#from funcionalidad5 import administrador
from PIL import Image, ImageTk
from ventanas import ventana_inicio
import uiMain.FieldFrame as FieldFrame
from aspectoFuncionalidades import funcionalidad_1 """

""" # Normaliza la entrada eliminando acentos y caracteres especiales
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

    menu_procesos.add_command(label="Ver viajes",command=lambda:funcionalidad_1.funcionalidad_1(ventana,frame_interno3))
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

    #framecito=FieldFrame("CRITERIO",["Código", "Nombre", "Descripción", "Ubicación"],"VALOR",None)

    ventana.mainloop() """

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from .aspectoFuncionalidades.funcionalidad_1 import funcionalidad_1

class ventana_principal(tk.Tk):
    def __init__(self, ventana):
        super().__init__()
        self.title("LussajuBus")
        self.geometry("800x500")

        self.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_ambas_ventanas(ventana))

        self.barra_menu = tk.Menu(self)
        self.config(menu=self.barra_menu) 

        self.menu_archivo = tk.Menu(self.barra_menu, tearoff="off")
        self.barra_menu.add_cascade(label="Archivo", menu=self.menu_archivo)

        self.menu_archivo.add_command(
            label="Aplicación", 
            command=lambda: self.info_aplicacion()
        )
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(
            label="Salir", 
            command=lambda: self.cerrar_ventana(ventana)
        )

        self.menu_procesos = tk.Menu(self.barra_menu, tearoff="off")
        self.barra_menu.add_cascade(
            label="Procesos y Consultas", 
            menu=self.menu_procesos
        )

        self.menu_procesos.add_command(
            label="Ver viajes",
            command=lambda: funcionalidad_1(self.frame_interno3)
        )
        self.menu_procesos.add_separator()
        self.menu_procesos.add_command(label="Reservar tiquete")
        self.menu_procesos.add_separator()
        self.menu_procesos.add_command(label="Gestionar tiquetes")
        self.menu_procesos.add_separator()
        self.menu_procesos.add_command(label="Servicio de hospedaje")
        self.menu_procesos.add_separator()
        self.menu_procesos.add_command(label="Administrador")

        self.menu_ayuda = tk.Menu(self.barra_menu, tearoff="off")
        self.barra_menu.add_cascade(label="Ayuda", menu=self.menu_ayuda)
        self.menu_ayuda.add_command(label="Acerca de", command=lambda: self.acerca_de())
        
        self.frame_ventana = tk.Frame(self, highlightbackground="black", 
                                        highlightthickness=2)
        self.frame_ventana.pack(padx=(20, 20), pady=(20, 20), fill="both", expand=True)

        self.nombre_proceso_consulta="Bienvenido a la ventana principal"

        self.label_nombre=tk.Label(
            self.frame_ventana,
            text=self.nombre_proceso_consulta,font=("Arial",15)
        )
        self.label_nombre.pack(side="top", anchor="n", pady=10)

        self.frame_interno1=tk.Frame(self.frame_ventana,highlightbackground="black", 
                                        highlightthickness=1)
        self.frame_interno1.pack(fill="both", expand=True)

        self.texto_descripcion="Aquí va la descripción de la funcionalidad\n...\n..."

        self.label_descripcion=tk.Label(
            self.frame_interno1,
            text=self.texto_descripcion,
            font=("Arial",10)
        )
        self.label_descripcion.pack(side="top", anchor="n", pady=10)

        self.frame_interno2=tk.Frame(self.frame_interno1,highlightbackground="black", 
                                        highlightthickness=1)
        self.frame_interno2.pack(fill="both", expand=True)

        self.frame_interno3=tk.Frame(self.frame_interno2,highlightbackground="black", 
                                        highlightthickness=1)
        self.frame_interno3.pack(pady=10,padx=100,fill="both", expand=True)
        self.frame_interno3.pack_propagate(False)

        self.mainloop()

    def cerrar_ambas_ventanas(self, ventana):
        self.destroy()
        ventana.destroy()

    def cerrar_ventana(self, ventana):
        self.destroy()
        ventana.deiconify()

    def info_aplicacion(self):
        messagebox.showinfo("Acerca de la Aplicación" 
                                + "Esta aplicación permite al usuario ....")

    def acerca_de(self):
        messagebox.showinfo("Autores" + "Autores de la aplicación:\n\n-" 
                                + "Santiago Cardona Franco \n- Samuel Hernández Duque")


