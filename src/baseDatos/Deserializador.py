import os
import pickle
from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.terminal import Terminal
from gestorAplicación.gestion.tiquete import Tiquete
from gestorAplicación.personas.pasajero import Pasajero

# Definir la ruta a la carpeta temporal
ruta_temp = os.path.join(os.getcwd(), "src", "baseDatos", "temp")

def deserializar():
    """
    Deserializa los objetos de diferentes clases desde los archivos correspondientes en la carpeta temporal.
    """
    try:
        docs = os.listdir(ruta_temp)
        for doc in docs:
            file_path = os.path.join(ruta_temp, doc)
            if "empresas" in file_path:
                try:
                    with open(file_path, 'rb') as file:
                        # Deserializa y asigna las empresas
                        empresas = pickle.load(file)
                        Empresa.set_empresas(empresas)
                except Exception as e:
                    print(f"Error al deserializar empresas: {e}")

            elif "pasajeros" in file_path:
                try:
                    with open(file_path, 'rb') as file:
                        # Deserializa y asigna los pasajeros
                        pasajeros = pickle.load(file)
                        Pasajero.set_pasajeros(pasajeros)
                except Exception as e:
                    print(f"Error al deserializar pasajeros: {e}")

            elif "terminales" in file_path:
                try:
                    with open(file_path, 'rb') as file:
                        # Deserializa y asigna las terminales
                        terminales = pickle.load(file)
                        Terminal.set_terminales(terminales)
                except Exception as e:
                    print(f"Error al deserializar terminales: {e}")

            elif "tiquetes" in file_path:
                try:
                    with open(file_path, 'rb') as file:
                        # Deserializa un objeto de Tiquete
                        tiquete = pickle.load(file)
                        # Se asume que Tiquete tiene un método para asignar el número de reserva
                        Tiquete.set_numeros_reserva(int(tiquete.get_numero_reserva()))
                except Exception as e:
                    print(f"Error al deserializar tiquetes: {e}")

    except Exception as e:
        print(f"Error al deserializar archivos: {e}")
