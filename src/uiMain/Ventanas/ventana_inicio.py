from ventanas import ventana_principal
from PIL import Image, ImageTk
import tkinter as tk
import unidecode

# Normaliza la entrada eliminando acentos y caracteres especiales
def sc_input(mensaje: str):
    input_value = input(mensaje)
    return unidecode.unidecode(input_value).strip()

def salir_programa(ventana):
    ventana.destroy()

def descripcion_programa(texto_saludo, saludo):
    if (saludo.cget("text")==texto_saludo):
        saludo.config(text="Hola jejejeje \n (Darle click nuevamente a descripción para quitarla)")
    else:
        saludo.config(text=texto_saludo)

def ventana_inicio():
    ventana = tk.Tk()
    ventana.title("LussajuBus")
    ventana.geometry("700x600")

    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu) 

    menu_inicio = tk.Menu(barra_menu, tearoff="off")
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

    menu_inicio.add_command(label="Descripción",command= lambda:descripcion_programa(texto_saludo, saludo))
    menu_inicio.add_separator()
    menu_inicio.add_command(label="Salir", command= lambda: salir_programa(ventana))

    p1 = tk.Frame(ventana, highlightbackground="black", highlightthickness=2)
    p1.pack(side="left", expand=True, fill="both", pady=10, padx=(10, 5))
    p1.pack_propagate(False)

    p2 = tk.Frame(ventana, highlightbackground="black", highlightthickness=2)
    p2.pack(side="right", expand=True, fill="both", pady=10, padx=(5, 10))
    p2.pack_propagate(False)

    p3 = tk.Frame(p1, highlightbackground="black", highlightthickness=1)
    p3.pack(side="top", expand=True, fill="both", padx=10, pady=(10, 5))
    p3.pack_propagate(False)

    with open("src//uiMain//assets//saludo.txt", "r") as file:
        texto_saludo = file.read()

    etiqueta_p3 = tk.Label(p3, text=texto_saludo, anchor="nw", justify="left")
    etiqueta_p3.pack(expand=True, fill="both")
    etiqueta_p3.bind('<Configure>', lambda evento: etiqueta_p3.config(wraplength=evento.width))

    p4 = tk.Frame(p1, highlightbackground="black", highlightthickness=1, height=160)
    p4.pack(side="bottom", expand=True, fill="both", padx=10, pady=(5, 10))
    p4.pack_propagate(False)

    ingreso_sistema=tk.Button(p4,command=lambda:ventana_principal.ventana_principal(ventana))

    ingreso_sistema.pack(expand=True, fill='both')

    p5 = tk.Frame(p2, highlightbackground="black", highlightthickness=1, height=180)
    p5.pack(side="top", expand=True, fill="both", padx=10, pady=(10, 5))
    p5.pack_propagate(False)

    with open("src//uiMain//assets//saludo.txt", "r") as file:
        texto_hoja_vida = file.read()

    boton_p5 = tk.Button(p5, text=texto_hoja_vida)
    boton_p5.pack(expand=True, fill="both")

    p6 = tk.Frame(p2, highlightbackground="black", highlightthickness=1, height=160)
    p6.pack(side="bottom", expand=True, fill="both", padx=10, pady=(5, 10))
    p6.pack_propagate(False)

    p6.grid_rowconfigure(0, weight=1)
    p6.grid_columnconfigure(0, weight=1)

    foto1 = ImageTk.PhotoImage(Image.open(
        "src//uiMain//assets//download.png").resize((125, 150)))
    label_foto1 = tk.Label(p6, image=foto1)
    label_foto1.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="news")

    foto2 = ImageTk.PhotoImage(Image.open(
        "src//uiMain//assets//download.png").resize((125, 150)))
    label_foto2 = tk.Label(p6, image=foto2)
    label_foto2.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky="news")

    foto3 = ImageTk.PhotoImage(Image.open(
        "src//uiMain//assets//download.png").resize((125, 150)))
    label_foto3 = tk.Label(p6, image=foto3)
    label_foto3.grid(row=1, column=0, padx=(10, 5), pady=(5, 10), sticky="news")

    foto4 = ImageTk.PhotoImage(Image.open(
        "src//uiMain//assets//download.png").resize((125, 150)))
    label_foto4 = tk.Label(p6, image=foto4)
    label_foto4.grid(row=1, column=1, padx=(5, 10), pady=(5, 10), sticky="news")

    ventana.mainloop()