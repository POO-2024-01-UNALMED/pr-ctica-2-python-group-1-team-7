from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.personas.pasajero import Pasajero
from gestorAplicación.gestion.terminal import Terminal
from gestorAplicación.gestion.tiquete import Tiquete

import pickle
import os

# Definir la ruta a la carpeta temporal
ruta_temp = os.path.abspath("src//baseDatos//temp")

#Limpia el contenido de todos los archivos en la carpeta temporal
def limpiar_archivos():
    try:
        archivos = os.listdir(ruta_temp)
        for archivo in archivos:
            file_path = ruta_temp + "//" + archivo
            open(file_path, "w").close()
    except Exception as e:
        print(f"Error al limpiar archivos: {e}")

# Serializa los objetos de diferentes clases 
# y los guarda en los archivos correspondientes.
def serializar():
    try:
        archivos = os.listdir(ruta_temp)
        for archivo in archivos:
            file_path = ruta_temp + "//" + archivo
            if "empresas" in file_path:
                try:
                    # Serializa las empresas
                    picklefile = open(file_path, "wb")
                    pickle.dump(Empresa.get_empresas(), picklefile)
                except Exception as e:
                    print(f"Error al serializar empresas: {e}")

            elif "pasajeros" in file_path:
                try:
                    # Serializa los pasajeros
                    picklefile = open(file_path, "wb")
                    pickle.dump(Pasajero.get_pasajeros(), picklefile)
                except Exception as e:
                    print(f"Error al serializar pasajeros: {e}")

            elif "terminales" in file_path:
                try:
                    # Serializa las terminales
                    picklefile = open(file_path, "wb")
                    pickle.dump(Terminal.get_terminales(), picklefile)
                except Exception as e:
                    print(f"Error al serializar terminales: {e}")

            elif "tiquetes" in file_path:
                try:
                    # Serializa el último tiquete creado para llevar 
                    # la cuenta de los números de reserva
                    picklefile = open(file_path, "wb")
                    pickle.dump(Tiquete(), picklefile)
                except Exception as e:
                    print(f"Error al serializar tiquetes: {e}")
                    
    except Exception as e:
        print(f"Error al serializar archivos: {e}")