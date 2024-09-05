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

# Normaliza la entrada eliminando acentos y caracteres especiales
def sc_input(mensaje: str):
    input_value = input(mensaje)
    return unidecode.unidecode(input_value).strip()

def ventanas():
    ventana = tk.Tk()
    ventana.title("LussajuBus")
    ventana.geometry("500x500")
    ventana.configure(background='lightgray')

    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu) 

    menu_archivo = tk.Menu(barra_menu, tearoff="off")
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

    menu_archivo.add_command(label="Aplicación")
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir")

    menu_procesos = tk.Menu(barra_menu, tearoff="off")
    barra_menu.add_cascade(label="Procesos y Consultas", menu=menu_procesos)

    menu_ayuda = tk.Menu(barra_menu, tearoff="off")
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
      
    """ frame_principal = tk.Frame(ventana, highlightbackground="black", 
                                    highlightthickness=1)
    frame_principal.pack(padx=(15, 15), pady=(30, 15), fill="both", expand=True) """

    #frameMenu = tk.Frame(frame_principal, bg="blue")
    
    ventana.mainloop()


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

