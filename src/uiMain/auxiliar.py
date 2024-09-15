from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.hospedaje import Hospedaje
from gestorAplicación.gestion.terminal import Terminal
from gestorAplicación.gestion.tiquete import Tiquete
from gestorAplicación.gestion.viaje import Viaje
from gestorAplicación.personas.pasajero import Pasajero
from gestorAplicación.transporte.bus import Bus
from uiMain.field_frame import field_frame

from datetime import datetime, time
import unidecode
import tkinter as tk

# Normaliza la entrada eliminando acentos y caracteres especiales
def sc_input(mensaje: str):
    input_value = input(mensaje)
    return unidecode.unidecode(input_value).strip()

def posicionar(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (int(width)/2))
        y_cordinate = int((screen_height/2) - (int(height)/2))

        window.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate-100}")
        
def generar_botones(frame_contenedor):
    frame_inferior = tk.Frame(frame_contenedor, bg='lightblue')
    frame_inferior.pack(side="bottom", fill="x")

    frame_botones = tk.Frame(frame_inferior, bg='lightblue')
    frame_botones.pack(pady=5)

    boton_aceptar = tk.Button(
        frame_botones, 
        text="Aceptar", 
        font=("Calibri", 10), 
        width=8, 
        height=1
    )
    boton_aceptar.pack(side='left', padx=7)

    boton_borrar = tk.Button(
        frame_botones, 
        text="Borrar", 
        font=("Arial", 10), 
        width=8, 
        height=1
    )
    boton_borrar.pack(side='right', padx=7)

    return (boton_aceptar, boton_borrar)

def generar_scrollbar(frame):
    canvas = tk.Canvas(frame, bg='lightblue')
    canvas.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = tk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def on_canvas_resize(event):
        canvas.itemconfig(window, width=event.width)

    canvas.bind("<Configure>", on_canvas_resize)
    
    print(f"Scrollable frame creado: {scrollable_frame}")
    return scrollable_frame

def borrar_datos(event,fieldframe:field_frame):
    for valor in fieldframe.valores:
        if valor in fieldframe.entries:
            fieldframe.entries[valor].config(text="")

def instanciar_objetos():
    # Crear instancias de Terminal
    medellin = Terminal("MEDELLIN")
    bogota = Terminal("BOGOTA")
    cali = Terminal("CALI")
    bucaramanga = Terminal("BUCARAMANGA")
    pereira = Terminal("PEREIRA")
    santa_marta = Terminal("SANTA MARTA")
    cartagena = Terminal("CARTAGENA")
    tolima = Terminal("TOLIMA")

    # Crear instancias de Empresa
    swift = Empresa("Swift")
    zoom = Empresa("Zoom")
    jet = Empresa("Jet")
    cruis = Empresa("Cruis")

    # Crear instancias de Bus
    bus1 = Bus(14, [3, 4])
    bus2 = Bus(13, [2, 6])
    bus3 = Bus(10, [2, 7])
    bus4 = Bus(15, [5, 9])
    bus5 = Bus(9, [3, 4])
    bus6 = Bus(14, [5, 10])
    bus7 = Bus(13, [3, 4])
    bus8 = Bus(11, [5, 8])

    # Crear instancias de Viaje
    viaje1 = Viaje(medellin, bogota)
    viaje2 = Viaje(cali, bogota)
    viaje3 = Viaje(medellin, cali)
    viaje4 = Viaje(pereira, santa_marta)
    viaje5 = Viaje(cartagena, tolima)
    viaje6 = Viaje(bucaramanga, medellin)
    viaje7 = Viaje(pereira, cali)
    viaje8 = Viaje(bogota, santa_marta)

    # Crear instancias de Hospedaje
    pod = Hospedaje("Pod", 3, 4)
    nest = Hospedaje("Nest", 4, 5)
    oasis = Hospedaje("Oasis", 3, 6)
    haven = Hospedaje("Haven", 2, 5)
    zen = Hospedaje("Zen", 4, 4)
    den = Hospedaje("Den", 2, 7)
    pad = Hospedaje("Pad", 4, 6)
    hub = Hospedaje("Hub", 4, 3)

    # Crear instancias de Pasajero
    pasajero1 = Pasajero("Samuel", "123456")
    pasajero2 = Pasajero("Santiago", "654321")
    pasajero3 = Pasajero("Juan", "123321")
    pasajero4 = Pasajero("Camilo", "100123")

    # Asignar empresas a viajes
    viaje1.set_empresa(zoom)
    viaje2.set_empresa(zoom)
    viaje3.set_empresa(swift)
    viaje4.set_empresa(swift)
    viaje5.set_empresa(cruis)
    viaje6.set_empresa(cruis)
    viaje7.set_empresa(jet)
    viaje8.set_empresa(jet)

    # Asignar buses a viajes
    viaje1.set_bus(bus1)
    viaje2.set_bus(bus2)
    viaje3.set_bus(bus3)
    viaje4.set_bus(bus4)
    viaje5.set_bus(bus5)
    viaje6.set_bus(bus6)
    viaje7.set_bus(bus7)
    viaje8.set_bus(bus8)

    # Asignar fechas a viajes
    viaje1.set_fecha(datetime.strptime("2025-08-21", "%Y-%m-%d").date())
    viaje2.set_fecha(datetime.strptime("2026-05-23", "%Y-%m-%d").date())
    viaje3.set_fecha(datetime.strptime("2025-09-15", "%Y-%m-%d").date())
    viaje4.set_fecha(datetime.strptime("2025-12-21", "%Y-%m-%d").date())
    viaje5.set_fecha(datetime.strptime("2024-10-22", "%Y-%m-%d").date())
    viaje6.set_fecha(datetime.strptime("2024-12-26", "%Y-%m-%d").date())
    viaje7.set_fecha(datetime.strptime("2026-07-25", "%Y-%m-%d").date())
    viaje8.set_fecha(datetime.strptime("2024-07-29", "%Y-%m-%d").date())

    # Asignar horas a viajes
    viaje1.set_hora(time(15, 0))
    viaje2.set_hora(time(16, 0))
    viaje3.set_hora(time(13, 0))
    viaje4.set_hora(time(12, 0))
    viaje5.set_hora(time(9, 0))
    viaje6.set_hora(time(8, 30))
    viaje7.set_hora(time(20, 10))
    viaje8.set_hora(time(17, 0))

    # Agregar viajes a empresas
    zoom.get_viajes().extend([viaje1, viaje2])
    swift.get_viajes().extend([viaje3, viaje4])
    cruis.get_viajes().extend([viaje5, viaje6])
    jet.get_viajes().extend([viaje7, viaje8])

    # Agregar hospedajes a terminales
    medellin.get_hospedajes().append(pod)
    bogota.get_hospedajes().append(nest)
    cali.get_hospedajes().append(den)
    bucaramanga.get_hospedajes().append(zen)
    pereira.get_hospedajes().append(haven)
    santa_marta.get_hospedajes().append(hub)
    cartagena.get_hospedajes().append(oasis)
    tolima.get_hospedajes().append(pad)

    # Crear y agregar tiquetes a pasajeros
    pasajero1.agregar_tiquete(Tiquete(pasajero1, viaje1, viaje1.buscar_asiento("12A")))
    pasajero2.agregar_tiquete(Tiquete(pasajero2, viaje2, viaje2.buscar_asiento("11D")))
    pasajero3.agregar_tiquete(Tiquete(pasajero3, viaje3, viaje3.buscar_asiento("5A")))
    pasajero4.agregar_tiquete(Tiquete(pasajero4, viaje4, viaje4.buscar_asiento("10B")))
    pasajero1.agregar_tiquete(Tiquete(pasajero1, viaje5, viaje5.buscar_asiento("6B")))
    pasajero2.agregar_tiquete(Tiquete(pasajero2, viaje6, viaje6.buscar_asiento("9A")))
    pasajero3.agregar_tiquete(Tiquete(pasajero3, viaje7, viaje7.buscar_asiento("11D")))
    pasajero4.agregar_tiquete(Tiquete(pasajero4, viaje8, viaje8.buscar_asiento("10C")))

    # Reservar asientos en los viajes
    viaje1.reservar_asiento(viaje1.buscar_asiento("12A").numero, None)
    viaje2.reservar_asiento(viaje2.buscar_asiento("11D").numero, None)
    viaje3.reservar_asiento(viaje3.buscar_asiento("5A").numero, None)
    viaje4.reservar_asiento(viaje4.buscar_asiento("10B").numero, None)
    viaje5.reservar_asiento(viaje5.buscar_asiento("6B").numero, None)
    viaje6.reservar_asiento(viaje6.buscar_asiento("9A").numero, None)
    viaje7.reservar_asiento(viaje7.buscar_asiento("11D").numero, None)
    viaje8.reservar_asiento(viaje8.buscar_asiento("10C").numero, None)

