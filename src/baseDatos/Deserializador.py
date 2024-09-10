from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.personas.pasajero import Pasajero
from gestorAplicación.gestion.terminal import Terminal
from gestorAplicación.gestion.tiquete import Tiquete

import pickle
import os

# Definir la ruta a la carpeta temporal
ruta_temp = os.path.abspath("src\\baseDatos\\temp")

# Deserializa los objetos de diferentes clases 
# desde los archivos correspondientes en la carpeta temporal.
def deserializar():
    try:
        archivos = os.listdir(ruta_temp)
        for archivo in archivos:
            file_path = ruta_temp + "\\" + archivo
            if "empresas" in file_path:
                try:
                    # Deserializa y asigna las empresas
                    picklefile = open(file_path, "rb")
                    Empresa.set_empresas(pickle.load(picklefile))
                    picklefile.close()
                except Exception as e:
                    print(f"Error al deserializar empresas: {e}")

            elif "pasajeros" in file_path:
                try:
                    # Deserializa y asigna los pasajeros
                    picklefile = open(file_path, "rb")
                    Pasajero.set_pasajeros(pickle.load(picklefile))
                    picklefile.close()
                except Exception as e:
                    print(f"Error al deserializar pasajeros: {e}")

            elif "terminales" in file_path:
                try:
                    # Deserializa y asigna las terminales
                    picklefile = open(file_path, "rb")
                    Terminal.set_terminales(pickle.load(picklefile))
                    picklefile.close()
                except Exception as e:
                    print(f"Error al deserializar terminales: {e}")

            elif "tiquetes" in file_path:
                try:
                    # Se asigna el atributo de clase "numeros_reserva" a la clase Tiquete
                    picklefile = open(file_path, "rb")
                    Tiquete.set_numeros_reserva(
                        pickle.load(picklefile).get_numero_reserva()
                    )
                    picklefile.close()
                except Exception as e:
                    print(f"Error al deserializar tiquetes: {e}")

    except Exception as e:
        print(f"Error al deserializar archivos: {e}")
