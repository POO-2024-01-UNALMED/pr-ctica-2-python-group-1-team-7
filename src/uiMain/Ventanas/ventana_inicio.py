from uiMain.auxiliar import posicionar
from ventanas import ventana_principal
from PIL import Image, ImageTk
import tkinter as tk
import unidecode
import os

class ventana_inicio(tk.Tk):
    def __init__(self):
        self.nombre_imagenes_sistema = os.listdir("src//uiMain//assets//imagenesSistema")
        self.indice_imagen_sistema = 0
        self.nombre = "santiago"
        self.path_imagenes_hoja_vida = ("src//uiMain//assets//hojasVida//" 
                                        + self.nombre + "//imagenes")

        super().__init__()
        self.title("LussajuBus")
        posicionar(self, "1000", "700")
        self.iconphoto(True, tk.PhotoImage(file="src//uiMain//assets//cubito.png"))

        self.barra_menu = tk.Menu(self)
        self.config(menu=self.barra_menu) 

        self.menu_inicio = tk.Menu(self.barra_menu, tearoff="off")
        self.barra_menu.add_cascade(label="Inicio", menu=self.menu_inicio)

        self.menu_inicio.add_command(
            label="Descripción", 
            command=self.descripcion_programa
        )
        self.menu_inicio.add_separator()
        self.menu_inicio.add_command(label="Salir",  command=self.destroy)

        self.p1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.p1.pack(side="left", expand=True, fill="both", pady=10, padx=(10, 5))
        self.p1.pack_propagate(False)
        self.p1.bind('<Configure>', self.redimensionar_frames)

        self.p2 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.p2.pack(side="right", expand=True, fill="both", pady=10, padx=(5, 10))
        self.p2.pack_propagate(False)
        self.p2.bind('<Configure>', self.redimensionar_frames)

        self.p3 = tk.Frame(self.p1, highlightbackground="black", highlightthickness=1)
        self.p3.pack(side="top", expand=True, fill="both", padx=10, pady=(10, 5))
        self.p3.pack_propagate(False)

        self.texto_saludo = open("src//uiMain//assets//saludo.txt", "r").read()

        self.label_p3 = tk.Label(self.p3, 
            text=self.texto_saludo, 
            anchor="nw", 
            justify="left"
        )
        self.label_p3.pack(expand=True, fill="both")
        self.label_p3.bind(
            '<Configure>', 
            lambda evento: self.label_p3.config(wraplength=evento.width)
        )

        self.p4 = tk.Frame(self.p1, highlightbackground="black", highlightthickness=1)
        self.p4.pack(side="bottom", expand=True, fill="both", padx=10, pady=(5, 10))
        self.p4.pack_propagate(False)
        self.p4.bind('<Configure>', self.redimensionar_imagen_sistema)

        self.path_imagen_sistema = (
            "src//uiMain//assets//imagenesSistema//" 
            + self.nombre_imagenes_sistema[self.indice_imagen_sistema]
        )
        self.imagen_sistema = Image.open(self.path_imagen_sistema)
        self.imagen_sistema = ImageTk.PhotoImage(self.imagen_sistema)

        self.label_imagen_sistema = tk.Label(self.p4, image=self.imagen_sistema)
        self.label_imagen_sistema.pack(
            side="top", expand=True, fill="both", padx=10, pady=(10, 5)
        )
        self.label_imagen_sistema.bind("<Enter>", self.cambiar_imagen_sistema)
    
        self.button_sistema = tk.Button(
            self.p4, 
            width=15,
            height=5,
            text="Ventana principal",
            command=lambda: ventana_principal.ventana_principal(self)
        )

        self.button_sistema.pack(side="bottom", pady=(5, 10))

        self.p5 = tk.Frame(self.p2, highlightbackground="black", highlightthickness=1)
        self.p5.pack(side="top", expand=True, fill="both", padx=10, pady=(10, 5))
        self.p5.pack_propagate(False)

        self.path_texto_hoja_vida = ("src//uiMain//assets//hojasVida" 
                                        + "//santiago//hoja_vida_santiago.txt")
        self.texto_hoja_vida = open(self.path_texto_hoja_vida).read()

        self.button_p5 = tk.Button(
            self.p5, 
            text=self.texto_hoja_vida, 
            anchor="nw", 
            justify="left", 
            relief="flat"
        )
        self.button_p5.pack(expand=True, fill="both")
        self.button_p5.bind(
            '<Configure>', lambda evento: self.button_p5.config(wraplength=evento.width)
        )
        self.button_p5.bind('<Button-1>', self.cambiar_hoja_vida_e_imagenes)
    
        self.p6 = tk.Frame(self.p2, highlightbackground="black", highlightthickness=1)
        self.p6.pack(side="bottom", expand=True, fill="both", padx=10, pady=(5, 10))
        self.p6.pack_propagate(False)
        self.p6.bind('<Configure>', self.redimensionar_imagenes_hojas_vida)

        imagenes = []

        for archivo in os.listdir(self.path_imagenes_hoja_vida):
            imagen = Image.open(self.path_imagenes_hoja_vida + "//" + archivo)
            img = ImageTk.PhotoImage(imagen)
            imagenes.append(img)

        self.label_imagen1 = tk.Label(self.p6, image=imagenes[0])
        self.label_imagen1.grid(row=0, column=0, padx=(10, 5), pady=(10, 5))
        
        self.label_imagen2 = tk.Label(self.p6, image=imagenes[1])
        self.label_imagen2.grid(row=0, column=1, padx=(5, 10), pady=(10, 5))

        self.label_imagen3 = tk.Label(self.p6, image=imagenes[2])
        self.label_imagen3.grid(row=1, column=0, padx=(10, 5), pady=(5, 10))

        self.label_imagen4 = tk.Label(self.p6, image=imagenes[3])
        self.label_imagen4.grid(row=1, column=1, padx=(5, 10), pady=(5, 10))

        self.mainloop()

    def descripcion_programa(self):
        if (self.label_p3.cget("text") == self.texto_saludo):
            self.label_p3.config(
                text="Hola jejejeje" + "\n" 
                    + "(Darle click nuevamente a descripción para quitarla)"
            )
        else:
            self.label_p3.config(text=self.texto_saludo)
    
    def redimensionar_frames(self, evento):
        frame1 = evento.widget.winfo_children()[0]
        frame1.config(height=int(evento.height/3))
        frame2 = evento.widget.winfo_children()[1]
        frame2.config(height=int(evento.height*(2/3)))
    
    def redimensionar_imagen_sistema(self, evento):
        self.p4.update()

        self.imagen_sistema = Image.open(self.path_imagen_sistema)
        self.imagen_sistema = self.imagen_sistema.resize((
            int((self.p4.winfo_width()-20)), 
            int((self.p4.winfo_height()-70))
        ))
        self.imagen_sistema = ImageTk.PhotoImage(self.imagen_sistema)

        self.label_imagen_sistema.config(image=self.imagen_sistema)
        self.label_imagen_sistema.image=self.imagen_sistema

    def cambiar_imagen_sistema(self, evento):
        if self.indice_imagen_sistema == 4:
            self.indice_imagen_sistema = 0
        else:
            self.indice_imagen_sistema += 1

        self.path_imagen_sistema = (
            "src//uiMain//assets//imagenesSistema//" 
            + self.nombre_imagenes_sistema[self.indice_imagen_sistema]
        )
        
        self.redimensionar_imagen_sistema(None)
    
    def cambiar_hoja_vida_e_imagenes(self, evento):
        if "santiago" in self.path_texto_hoja_vida:
            self.path_texto_hoja_vida = ("src//uiMain//assets//hojasVida" 
                                            + "//samuel//hoja_vida_samuel.txt")
            self.texto_hoja_vida = open(self.path_texto_hoja_vida).read()
            self.button_p5.config(text=self.texto_hoja_vida)
            self.nombre = "samuel"
            self.path_imagenes_hoja_vida = ("src//uiMain//assets//hojasVida//" 
                                                + self.nombre + "//imagenes")
        else:
            self.path_texto_hoja_vida = ("src//uiMain//assets//hojasVida" 
                                            + "//santiago//hoja_vida_santiago.txt")
            self.texto_hoja_vida = open(self.path_texto_hoja_vida).read()
            self.button_p5.config(text=self.texto_hoja_vida)
            self.nombre = "santiago"
            self.path_imagenes_hoja_vida = ("src//uiMain//assets//hojasVida//" 
                                                + self.nombre + "//imagenes")

        self.redimensionar_imagenes_hojas_vida(None)

    def redimensionar_imagenes_hojas_vida(self, evento):
        imagenes = []
        for archivo in os.listdir(self.path_imagenes_hoja_vida):
            imagen = Image.open(self.path_imagenes_hoja_vida + "//" + archivo)

            imagen_modificada = imagen.resize((
                int((self.p6.winfo_width()-40)/2), 
                int((self.p6.winfo_height()-40)/2)
            ))

            img = ImageTk.PhotoImage(imagen_modificada)
            imagenes.append(img)

        indice = 0
        for label in self.p6.winfo_children():
            label.config(image=imagenes[indice])
            label.image=imagenes[indice]
            indice += 1