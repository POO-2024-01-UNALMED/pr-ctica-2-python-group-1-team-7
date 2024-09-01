import os
import pickle
from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.terminal import Terminal
from gestorAplicación.gestion.tiquete import Tiquete
from gestorAplicación.personas.pasajero import Pasajero

# Definir la ruta a la carpeta temporal
ruta_temp = os.path.join(os.getcwd(), "src", "baseDatos", "temp")

def limpiar_archivos():
    """
    Limpia el contenido de todos los archivos en la carpeta temporal.
    """
    try:
        docs = os.listdir(ruta_temp)
        for doc in docs:
            file_path = os.path.join(ruta_temp, doc)
            if os.path.isfile(file_path):
                with open(file_path, 'w') as file:
                    # Limpia el contenido del archivo
                    pass
    except Exception as e:
        print(f"Error al limpiar archivos: {e}")

def serializar():
    """
    Serializa los objetos de diferentes clases y los guarda en los archivos correspondientes.
    """
    try:
        docs = os.listdir(ruta_temp)
        for doc in docs:
            file_path = os.path.join(ruta_temp, doc)
            if "empresas" in file_path:
                try:
                    with open(file_path, 'wb') as file:
                        # Serializa las empresas
                        pickle.dump(Empresa.get_empresas(), file)
                except Exception as e:
                    print(f"Error al serializar empresas: {e}")

            elif "pasajeros" in file_path:
                try:
                    with open(file_path, 'wb') as file:
                        # Serializa los pasajeros
                        pickle.dump(Pasajero.get_pasajeros(), file)
                except Exception as e:
                    print(f"Error al serializar pasajeros: {e}")

            elif "terminales" in file_path:
                try:
                    with open(file_path, 'wb') as file:
                        # Serializa las terminales
                        pickle.dump(Terminal.get_terminales(), file)
                except Exception as e:
                    print(f"Error al serializar terminales: {e}")

            elif "tiquetes" in file_path:
                try:
                    with open(file_path, 'wb') as file:
                        # Serializa los tiquetes (aquí se asume que se serializa un objeto de Tiquete)
                        pickle.dump(Tiquete(), file)
                except Exception as e:
                    print(f"Error al serializar tiquetes: {e}")

    except Exception as e:
        print(f"Error al serializar archivos: {e}")