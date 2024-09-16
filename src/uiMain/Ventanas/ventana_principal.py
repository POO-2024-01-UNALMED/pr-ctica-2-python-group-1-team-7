from uiMain.aspectoFuncionalidades.funcionalidad_1 import funcionalidad_1
from uiMain.aspectoFuncionalidades.funcionalidad_2 import funcionalidad_2
from uiMain.auxiliar import posicionar
import os

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ventana_principal(tk.Tk):
    def __init__(self, ventana):
        super().__init__()
        ventana.withdraw()
        self.title("LussajuBus")
        posicionar(self)
        self.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_ambas_ventanas(ventana))

        self.barra_menu = tk.Menu(self)
        self.config(menu=self.barra_menu,bg='black') 

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
            command=lambda:self.generador_funcionalidades(1))
        self.menu_procesos.add_separator()
        self.menu_procesos.add_command(
            label="Reservar tiquete",
            command=lambda:self.generador_funcionalidades(2)
        )
        self.menu_procesos.add_separator()
        self.menu_procesos.add_command(label="Gestionar tiquetes")
        self.menu_procesos.add_separator()
        self.menu_procesos.add_command(label="Servicio de hospedaje")
        self.menu_procesos.add_separator()
        self.menu_procesos.add_command(label="Administrador")

        self.menu_ayuda = tk.Menu(self.barra_menu, tearoff="off")
        self.barra_menu.add_cascade(label="Ayuda", menu=self.menu_ayuda)
        self.menu_ayuda.add_command(label="Acerca de", command=lambda: self.acerca_de())
        
        self.frame_ventana = tk.Frame(self,bg='light blue')
        self.frame_ventana.pack(padx=(20, 20), pady=(20, 20), fill="both", expand=True)

        self.nombre_proceso_consulta="Bienvenido a la ventana principal"

        self.label_nombre=tk.Label(
            self.frame_ventana,
            text=self.nombre_proceso_consulta,font=("Arial",15),bg='light blue'
        )
        self.label_nombre.pack(side="top", anchor="n", pady=10)

        self.frame_interno1=tk.Frame(self.frame_ventana,bg='LightCyan2')
        self.frame_interno1.pack(fill="both", expand=True)

        self.texto_descripcion="Aquí va la descripción de la funcionalidad\n...\n..."

        self.label_descripcion=tk.Label(
            self.frame_interno1,
            text=self.texto_descripcion,
            font=("Arial",10),
            bg='LightCyan2'
        )
        self.label_descripcion.pack(side="top", anchor="n", pady=10)

        self.frame_interno2=tk.Frame(self.frame_interno1,bg='gray38')
        self.frame_interno2.pack(fill="both", expand=True)

        self.frame_interno3=tk.Frame(self.frame_interno2,bg='white')
        self.frame_interno3.pack(pady=10,padx=100,fill="both", expand=True)
        self.frame_interno3.pack_propagate(False)

        """ imagen = tk.PhotoImage(file="src//uiMain//assets//logo.png")
        self.imagen_label = tk.Label(self.frame_interno3, image=imagen)
        self.imagen_label.image = imagen
        self.imagen_label.pack(expand=True, fill='both')  """

        self.frame_activo = None

        self.mainloop()

    def cerrar_ambas_ventanas(self, ventana):
        self.destroy()
        ventana.destroy()

    def cerrar_ventana(self, ventana):
        self.reiniciar_contador_frames()
        self.destroy()
        ventana.deiconify()
        posicionar(ventana)

    def reiniciar_contador_frames(self):
        funcionalidad_1.numero_frames=1
        funcionalidad_2.numero_frames=1
        #funcionalidad_3.numero_frames=1
        #funcionalidad_4.numero_frames=1
        #funcionalidad_5.numero_frames=1

    def generador_funcionalidades(self, funcionalidad):
        self.reiniciar_contador_frames()
        if self.frame_activo:
            self.frame_activo.pack_forget()
        match funcionalidad:
            case 1:
                self.configurar_nombre_descripcion(
                    "FUNCIONALIDAD 1", 
                    "descripción funcionalidad 1\n...\n..."
                )
                self.frame_activo = funcionalidad_1(self,self.frame_interno3)
            case 2:
                self.configurar_nombre_descripcion(
                    "FUNCIONALIDAD 2", 
                    "descripción funcionalidad 2\n...\n..."
                )
                self.frame_activo = funcionalidad_2(self,self.frame_interno3)
            case 3:
                self.configurar_nombre_descripcion(
                    "FUNCIONALIDAD 3", 
                    "descripción funcionalidad 3\n...\n..."
                )
                #self.frame_activo = funcionalidad_3(self,self.frame_interno3)
            case 4:
                self.configurar_nombre_descripcion(
                    "FUNCIONALIDAD 4", 
                    "descripción funcionalidad 4\n...\n..."
                )
                #self.frame_activo = funcionalidad_4(self,self.frame_interno3)
            case 5:
                self.configurar_nombre_descripcion(
                    "FUNCIONALIDAD 5", 
                    "descripción funcionalidad 5\n...\n..."
                )
                #self.frame_activo = funcionalidad_5(self,self.frame_interno3)

    def info_aplicacion(self):
        messagebox.showinfo(
            "Acerca de la Aplicación" , 
            "Esta aplicación permite al usuario tener el control de un sistema" 
            + " de transporte terrestre en Colombia, en el cuál podrá gestionar" 
            + " y consultar información relacionada con los viajes, tiquetes, buses," 
            + " hospedajes y otros datos relevantes que ayudan a fortalecer" 
            + " la industria del transporte Nacional"
        )

    def acerca_de(self):
        messagebox.showinfo(
            "Autores" , 
            "Autores de la aplicación:\n\n-" 
            + "Santiago Cardona Franco \n- Samuel Hernández Duque"
        )
        
    def configurar_nombre_descripcion(self,nombre,descripcion):
        self.nombre_proceso_consulta=nombre
        self.texto_descripcion=descripcion
        self.label_nombre.config(text=self.nombre_proceso_consulta)
        self.label_descripcion.config(text=self.texto_descripcion)

    def volver_principal(self):
        decision=messagebox.askyesno(
            "Diálogo de confirmación",
            "¿Desea volver al menú principal?"
        )
        if decision:
            ventana_principal(self)

    
