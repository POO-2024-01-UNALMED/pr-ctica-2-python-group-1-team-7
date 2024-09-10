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
#from funcionalidad1 import ver_viajes
#from funcionalidad_2 import reservar_tiquete
from uiMain.funcionalidades.funcionalidad3 import gestionar_tiquetes
from uiMain.funcionalidades.funcionalidad4 import hospedaje
#from funcionalidad5 import administrador
from PIL import Image, ImageTk
from ventanas import ventana_inicio

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

    menu_procesos.add_command(label="Ver viajes")
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

    ventana.mainloop()
