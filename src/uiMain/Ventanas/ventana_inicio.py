from ventanas import ventana_principal
from PIL import Image, ImageTk
import tkinter as tk
import unidecode
import os

# Normaliza la entrada eliminando acentos y caracteres especiales
def sc_input(mensaje: str):
    input_value = input(mensaje)
    return unidecode.unidecode(input_value).strip()

def descripcion_programa(etiqueta):
    with open("src//uiMain//assets//saludo.txt", "r") as file:
        texto_saludo = file.read()

    if (etiqueta.cget("text") == texto_saludo):
        etiqueta.config(
            text="Hola jejejeje \n (Darle click nuevamente a descripción para quitarla)"
        )
    else:
        etiqueta.config(text=texto_saludo)

def salir_programa(ventana):
    ventana.destroy()

def redimensionar_frames(evento):
    frame1 = evento.widget.winfo_children()[0]
    frame1.config(height=int(evento.height/3))
    frame2 = evento.widget.winfo_children()[1]
    frame2.config(height=int(evento.height*(2/3)))
 
def redimensionar_widgets_p4(evento):
    imagen = Image.open("src//uiMain//assets//download.png")
    imagen_modificada = imagen.resize((
        int((evento.width-20)), 
        int((evento.height-70))
    ))
    img = ImageTk.PhotoImage(imagen_modificada)

    label = evento.widget.winfo_children()[0]
    label.config(image=img)
    label.image=img

def cambiar_hoja_vida_e_imagenes(evento, frame):
    archivo = open("src//uiMain//assets//hojasVida//switch.txt", "r")
    switch = archivo.read()
    if switch == "0":
        nombre = "samuel"
        archivo = open("src//uiMain//assets//hojasVida//switch.txt", "w")
        archivo.write("1")
        with open(
            "src//uiMain//assets//hojasVida//samuel//hoja_vida_samuel.txt", "r"
        ) as file:
            texto_hoja_vida = file.read()
            evento.widget.config(text=texto_hoja_vida)

    elif switch == "1":
        nombre = "santiago"
        archivo = open("src//uiMain//assets//hojasVida//switch.txt", "w")
        archivo.write("0")
        with open(
            "src//uiMain//assets//hojasVida//santiago//hoja_vida_santiago.txt", "r"
        ) as file:
            texto_hoja_vida = file.read()
            evento.widget.config(text=texto_hoja_vida)

    imagenes = []

    path = "src//uiMain//assets//hojasVida//" + nombre + "//imagenes"

    frame.update()

    for archivo in os.listdir(path):
        imagen = Image.open(path + "//" + archivo)

        imagen_modificada = imagen.resize((
            int((frame.winfo_reqwidth()-40)/2), 
            int((frame.winfo_reqheight()-40)/2)
        ))

        img = ImageTk.PhotoImage(imagen_modificada)
        imagenes.append(img)

    indice = 0
    for label in frame.winfo_children():
        label.config(image=imagenes[indice])
        label.image=imagenes[indice]
        indice += 1

def redimensionar_imagenes(evento):
    imagenes = []

    archivo = open("src//uiMain//assets//hojasVida//switch.txt", "r")
    switch = archivo.read()

    if switch == "0":
        nombre = "santiago"
    elif switch == "1":
        nombre = "samuel"

    path = "src//uiMain//assets//hojasVida//" + nombre + "//imagenes"

    for archivo in os.listdir(path):
        imagen = Image.open(path + "//" + archivo)

        imagen_modificada = imagen.resize((
            int((evento.width-40)/2), 
            int((evento.height-40)/2)
        ))

        img = ImageTk.PhotoImage(imagen_modificada)
        imagenes.append(img)

    indice = 0
    for label in evento.widget.winfo_children():
        label.config(image=imagenes[indice])
        label.image=imagenes[indice]
        indice += 1

def ventana_inicio():
    ventana = tk.Tk()
    ventana.title("LussajuBus")
    ventana.geometry("700x600")

    icono = tk.PhotoImage(file="src//uiMain//assets//cubito.png")
    ventana.iconphoto(True, icono)

    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu) 

    menu_inicio = tk.Menu(barra_menu, tearoff="off")
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

    menu_inicio.add_command(
        label="Descripción", 
        command=lambda:descripcion_programa(label_p3)
    )
    menu_inicio.add_separator()
    menu_inicio.add_command(label="Salir", command=lambda: salir_programa(ventana))

    p1 = tk.Frame(ventana, highlightbackground="black", highlightthickness=2)
    p1.pack(side="left", expand=True, fill="both", pady=10, padx=(10, 5))
    p1.pack_propagate(False)
    p1.bind('<Configure>', redimensionar_frames)

    p2 = tk.Frame(ventana, highlightbackground="black", highlightthickness=2)
    p2.pack(side="right", expand=True, fill="both", pady=10, padx=(5, 10))
    p2.pack_propagate(False)
    p2.bind('<Configure>', redimensionar_frames)

    p3 = tk.Frame(p1, highlightbackground="black", highlightthickness=1)
    p3.pack(side="top", expand=True, fill="both", padx=10, pady=(10, 5))
    p3.pack_propagate(False)

    with open("src//uiMain//assets//saludo.txt", "r") as file:
        texto_saludo = file.read()

    label_p3 = tk.Label(p3, text=texto_saludo, anchor="nw", justify="left")
    label_p3.pack(expand=True, fill="both")
    label_p3.bind(
        '<Configure>', 
        lambda evento: label_p3.config(wraplength=evento.width)
    )

    p4 = tk.Frame(p1, highlightbackground="black", highlightthickness=1)
    p4.pack(side="bottom", expand=True, fill="both", padx=10, pady=(5, 10))
    p4.pack_propagate(False)
    p4.bind('<Configure>', redimensionar_widgets_p4)

    imagen_sistema = Image.open("src//uiMain//assets//download.png")
    imagen_sistema = ImageTk.PhotoImage(imagen_sistema)

    label_imagen_sistema = tk.Label(p4, image=imagen_sistema)
    label_imagen_sistema.pack(
        side="top", expand=True, fill="both", padx=10, pady=(10, 5)
    )

    button_sistema = tk.Button(
        p4, 
        width=15,
        height=5,
        text="Ventana principal",
        command=lambda:ventana_principal.ventana_principal(ventana)
    )

    button_sistema.pack(side="bottom", pady=(5, 10))

    p5 = tk.Frame(p2, highlightbackground="black", highlightthickness=1)
    p5.pack(side="top", expand=True, fill="both", padx=10, pady=(10, 5))
    p5.pack_propagate(False)
    
    with open(
        "src//uiMain//assets//hojasVida//santiago//hoja_vida_santiago.txt", "r"
    ) as file:
        texto_hoja_vida = file.read()

    button_p5 = tk.Button(p5, text=texto_hoja_vida, anchor="nw", justify="left", 
                            relief="flat")
    button_p5.pack(expand=True, fill="both")
    button_p5.bind(
        '<Configure>', lambda evento: button_p5.config(wraplength=evento.width)
    )
   
    p6 = tk.Frame(p2, highlightbackground="black", highlightthickness=1)
    p6.pack(side="bottom", expand=True, fill="both", padx=10, pady=(5, 10))
    p6.pack_propagate(False)
    p6.bind('<Configure>', redimensionar_imagenes)

    button_p5.bind('<Button-1>', lambda evento: cambiar_hoja_vida_e_imagenes(evento, p6))

    imagenes = []

    for archivo in os.listdir("src//uiMain//assets//hojasVida//santiago//imagenes"):
        imagen = Image.open(
            "src//uiMain//assets//hojasVida//santiago//imagenes//" + archivo
        )
        img = ImageTk.PhotoImage(imagen)
        imagenes.append(img)
   
    label_imagen1 = tk.Label(p6, image=imagenes[0])
    label_imagen1.grid(row=0, column=0, padx=(10, 5), pady=(10, 5))
    
    label_imagen2 = tk.Label(p6, image=imagenes[1])
    label_imagen2.grid(row=0, column=1, padx=(5, 10), pady=(10, 5))

    label_imagen3 = tk.Label(p6, image=imagenes[2])
    label_imagen3.grid(row=1, column=0, padx=(10, 5), pady=(5, 10))

    label_imagen4 = tk.Label(p6, image=imagenes[3])
    label_imagen4.grid(row=1, column=1, padx=(5, 10), pady=(5, 10))

    ventana.mainloop()