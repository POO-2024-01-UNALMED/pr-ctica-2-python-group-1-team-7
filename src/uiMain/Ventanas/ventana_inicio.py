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
        posicionar(self)
        self.iconphoto(True, tk.PhotoImage(file="src//uiMain//assets//logo.png"))

        self.barra_menu = tk.Menu(self)
        self.config(menu=self.barra_menu,bg="black") 

        self.menu_inicio = tk.Menu(self.barra_menu, tearoff="off")
        self.barra_menu.add_cascade(label="Inicio", menu=self.menu_inicio)

        self.menu_inicio.add_command(
            label="Descripción", 
            command=self.descripcion_programa
        )
        self.menu_inicio.add_separator()
        self.menu_inicio.add_command(label="Salir",  command=self.destroy)

        self.p1 = tk.Frame(self, bg="gray38")
        self.p1.pack(side="left", expand=True, fill="both", pady=10, padx=(10, 5))
        self.p1.pack_propagate(False)
        self.p1.bind('<Configure>', self.redimensionar_frames)

        self.p2 = tk.Frame(self, bg="gray38")
        self.p2.pack(side="right", expand=True, fill="both", pady=10, padx=(5, 10))
        self.p2.pack_propagate(False)
        self.p2.bind('<Configure>', self.redimensionar_frames)

        self.p3 = tk.Frame(self.p1, bg='light blue')
        self.p3.pack(side="top", expand=True, fill="both", padx=10, pady=(10, 5))
        self.p3.pack_propagate(False)

        self.texto_saludo = open("src//uiMain//assets//saludo.txt", "r").read()

        self.texto_descripcion = open("src//uiMain//assets//descripcion.txt", "r").read()

        '''self.label_p3 = tk.Text(self.p3, 
            text=self.texto_saludo, 
            anchor="nw", 
            #justify="left", 
            bg='light blue',
            font=('Arial',15)
        )'''
        self.label_p3 = tk.Text(self.p3, 
                    bg='light blue',
                    font=('Arial', 15),
                    wrap='word',
                    padx=12,
                    pady=10,
                    bd=0
                )
        self.label_p3.insert('1.0', self.texto_saludo)
        self.label_p3.tag_configure('center', justify='center')
        self.label_p3.tag_add('center', '1.0', 'end')
        self.label_p3.config(state=tk.DISABLED)

        self.label_p3.pack(expand=True, fill="both")
        '''self.label_p3.bind(
            '<Configure>', 
            lambda evento: self.label_p3.config(wraplength=evento.width)
        )'''

        self.p4 = tk.Frame(self.p1, bg='LightCyan2')
        self.p4.pack(side="bottom", expand=True, fill="both", padx=10, pady=(5, 10))
        self.p4.pack_propagate(False)
        self.p4.bind('<Configure>', self.redimensionar_imagen_sistema)

        self.path_imagen_sistema = (
            "src//uiMain//assets//imagenesSistema//" 
            + self.nombre_imagenes_sistema[self.indice_imagen_sistema]
        )
        self.imagen_sistema = Image.open(self.path_imagen_sistema)
        self.imagen_sistema = ImageTk.PhotoImage(self.imagen_sistema)

        self.label_imagen_sistema = tk.Label(self.p4, image=self.imagen_sistema,bd=0)
        self.label_imagen_sistema.pack(
            side="top", expand=True, fill="both", padx=10, pady=(10, 5)
        )
        self.label_imagen_sistema.bind("<Enter>", self.cambiar_imagen_sistema)
    
        self.button_sistema = tk.Button(
            self.p4, 
            width=15,
            height=5,
            text="Ventana principal",
            bg='gray12',
            fg='white',
            font=('Calibri',12),
            command=lambda: ventana_principal.ventana_principal(self)
        )

        self.button_sistema.pack(side="bottom", expand=True, pady=(5, 10))

        self.p5 = tk.Frame(self.p2)
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
            wraplength=2,
            relief="flat",
            bg='LightCyan2',
            font=('Arial',10)
        )
        self.button_p5.pack(expand=True, fill="both",padx=1,pady=1)
        self.button_p5.bind(
            '<Configure>', lambda evento: self.button_p5.config(wraplength=evento.width)
        )
        self.button_p5.bind('<Button-1>', self.cambiar_hoja_vida_e_imagenes)
    
        self.p6 = tk.Frame(self.p2, bg='light blue')
        self.p6.pack(side="bottom", expand=True, fill="both", padx=10, pady=(5, 10))
        self.p6.pack_propagate(False)
        self.p6.bind('<Configure>', self.redimensionar_imagenes_hojas_vida)

        imagenes = []

        for archivo in os.listdir(self.path_imagenes_hoja_vida):
            imagen = Image.open(self.path_imagenes_hoja_vida + "//" + archivo)
            img = ImageTk.PhotoImage(imagen)
            imagenes.append(img)

        self.label_imagen1 = tk.Label(self.p6, image=imagenes[0],bd=0)
        self.label_imagen1.grid(row=0, column=0, padx=(15, 5), pady=(15, 5))
        
        self.label_imagen2 = tk.Label(self.p6, image=imagenes[1],bd=0)
        self.label_imagen2.grid(row=0, column=1, padx=(5, 15), pady=(15, 5))

        self.label_imagen3 = tk.Label(self.p6, image=imagenes[2],bd=0)
        self.label_imagen3.grid(row=1, column=0, padx=(15, 5), pady=(5, 15))

        self.label_imagen4 = tk.Label(self.p6, image=imagenes[3],bd=0)
        self.label_imagen4.grid(row=1, column=1, padx=(5, 15), pady=(5, 15))

        self.mainloop()

    def descripcion_programa(self):
        if (self.label_p3.get('1.0','end').strip() == self.texto_saludo):
            self.label_p3.config(state=tk.NORMAL)
            self.label_p3.delete('1.0', 'end')
            self.label_p3.insert('1.0', self.texto_descripcion) 
            self.label_p3.tag_configure('center', justify='center')
            self.label_p3.tag_add('center', '1.0', 'end')
            self.label_p3.config(font=('Arial', 12))
            self.label_p3.config(state=tk.DISABLED)
        else:
            self.label_p3.config(state=tk.NORMAL) 
            self.label_p3.delete('1.0', 'end') 
            self.label_p3.insert('1.0', self.texto_saludo)
            self.label_p3.tag_configure('center', justify='center')
            self.label_p3.tag_add('center', '1.0', 'end')
            self.label_p3.config(font=('Arial', 15))
            self.label_p3.config(state=tk.DISABLED)
    
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
            self.button_p5.config(text=self.texto_hoja_vida,font=('Arial',11))
            self.nombre = "samuel"
            self.path_imagenes_hoja_vida = ("src//uiMain//assets//hojasVida//" 
                                                + self.nombre + "//imagenes")
        else:
            self.path_texto_hoja_vida = ("src//uiMain//assets//hojasVida" 
                                            + "//santiago//hoja_vida_santiago.txt")
            self.texto_hoja_vida = open(self.path_texto_hoja_vida).read()
            self.button_p5.config(text=self.texto_hoja_vida,font=('Arial',10))
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