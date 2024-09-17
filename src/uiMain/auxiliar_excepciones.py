from Excepciones.ExcepcionId import ExcepcionId
from Excepciones.ExcepcionCorreo import ExcepcionCorreo
from Excepciones.ExcepcionTelefono import ExcepcionTelefono
from Excepciones.ExcepcionTiempo import ExcepcionTiempo
from Excepciones.ExcepcionIdUsuario import ExcepcionIdUsuario
from Excepciones.ExcepcionViaje import ExcepcionViaje
from Excepciones.ExcepcionTiquete import ExcepcionTiquete
from Excepciones.ExcepcionHospedaje import ExcepcionHospedaje
from Excepciones.ExcepcionAsiento import ExcepcionAsiento
from Excepciones.ExcepcionValoresVacios import ExcepcionValoresVacios

from field_frame import field_frame

from gestorAplicación.gestion.empresa import Empresa
from gestorAplicación.gestion.viaje import Viaje
from gestorAplicación.gestion.tiquete import Tiquete
from gestorAplicación.personas.pasajero import Pasajero
from gestorAplicación.gestion.terminal import Terminal
from gestorAplicación.gestion.hospedaje import Hospedaje
from gestorAplicación.transporte.bus import Bus

from tkinter import messagebox
import tkinter as tk
import re

def excepcion_id(id):
    try:
        if len(str(id))!=6 or int(id)<0:
            raise ExcepcionId()
    except ExcepcionId as e:
        messagebox.showwarning("Id de usuario incorrecto",e)
    except:
        messagebox.showwarning("Id de usuario incorrecto","El id de usuario debe ser un número")
    else:
        return "ok"
        
def excepcion_correo(correo):
    try:
        patron=r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron,correo):
            raise ExcepcionCorreo()
    except ExcepcionCorreo as e:
        messagebox.showwarning("Correo ingresado incorrectamente",e)
    except:
        messagebox.showwarning("Correo ingresado incorrectamente","El correo ingresado es incorrecto, ingréselo nuevamente")
    else:
        return "ok"
    
def excepcion_telefono(telefono):
    try:
        if len(str(telefono))!=10 or int(telefono)<0:
            raise ExcepcionTelefono()
    except ExcepcionTelefono as e:
        messagebox.showwarning("Teléfono ingresado incorrectamente",e)
    except:
        messagebox.showwarning("Teléfono ingresado incorrectamente","El teléfono ingresado es incorrecto, ingréselo nuevamente")
    else:
        return "ok"
    
def excepcion_tiempo(tiempo):
    try:
        patron=r'^[0-9]+ (días?|horas?|minutos?)$'
        if not re.match(patron,tiempo):
            raise ExcepcionTiempo()
    except ExcepcionTiempo as e:
        messagebox.showwarning("Tiempo ingresado incorrectamente",e)
    except:
        messagebox.showwarning("Tiempo ingresado incorrectamente","El tiempo ingresado es incorrecto, ingréselo nuevamente")
    else:
        return "ok"
    
def excepcion_id_usuario(id):
    ok=excepcion_id(id)
    try:
        if ok=="ok":
            ok=False
            for pasajero in Pasajero.pasajeros:
                if str(pasajero.get_id())==str(id):
                    ok=True
            if ok==False:
                raise ExcepcionIdUsuario()
            
    except ExcepcionId as e:
        messagebox.showwarning("Id de usuario incorrecto",e)
    except ExcepcionIdUsuario as e:
        messagebox.showwarning("Id de usuario incorrecto",e)
    except:
        messagebox.showwarning("Id de usuario incorrecto","El id de usuario debe ser un número")
    else:
        return "ok"
    
def excepcion_viaje(id):
    try:
        ok=False
        for empresa in Empresa.get_empresas():
            for viaje in empresa.get_viajes():
                if str(viaje.get_id())==str(id):
                    ok=True
        if ok==False:
            raise ExcepcionViaje()
    except ExcepcionViaje as e:
        messagebox.showwarning("Id de viaje incorrecto",e)
    except:
        messagebox.showwarning("Id de viaje incorrecto","El id de empresa debe ser un número")
    else:
        return "ok"
    
def excepcion_tiquete(numero_reserva):
    try:
        int(numero_reserva)
        ok=False
        for pasajero in Pasajero.get_pasajeros():
            for tiquete in pasajero.get_tiquetes():
                if str(tiquete.get_numero_reserva())==str(numero_reserva):
                    ok=True
        if ok==False:
            raise ExcepcionTiquete()
    except ExcepcionTiquete as e:
        messagebox.showwarning("Número de reserva de tiquete incorrecto",e)
    except:
        messagebox.showwarning("Número de reserva de tiquete incorrecto","El número de reserva del tiquete debe ser un número")
    else:
        return "ok"
    
def excepcion_hospedaje(nombre):
    try:
        ok=False
        for terminal in Terminal.get_terminales():
             for hospedaje in terminal.get_hospedajes():
                  if hospedaje.get_nombre()==str(nombre):
                      ok=True
        if ok==False:
            raise ExcepcionHospedaje()
    except ExcepcionHospedaje as e:
        messagebox.showwarning("Nombre de hospedaje incorrecto",e)
    except:
        messagebox.showwarning("Nombre de hospedaje incorrecto","El nombre del hospedaje debe ser una cadena de caracteres")
    else:
        return "ok"
    
def excepcion_asiento(numero,bus:Bus):
    try:
        ok=False
        for asiento in bus.get_asientos():
            if str(asiento.get_numero())==str(numero):
                ok=True
        if ok==False:
            raise ExcepcionAsiento()
    except ExcepcionAsiento as e:
        messagebox.showwarning("Número de asiento incorrecto o asiento ocupado",e)
    except:
        messagebox.showwarning("Número de asiento incorrecto o asiento ocupado",
                               "El numero del asiento no se ha puesto correctamente, ingréselo nuevamente")
    else:
        return "ok"
    
def valores_vacios(field:field_frame):
    try:
        ok=True
        lista=[]
        value:tk.Entry
        for key,value in field.entries.items():
            if (value.get()==""):
                ok=False
                lista.append(field.labels[key])
        if ok==False:
            raise ExcepcionValoresVacios()
    except ExcepcionValoresVacios as e:
        messagebox.showwarning("No se han llenado todos los campos",e+lista)
    except:
        messagebox.showwarning("No se han llenado todos los campos",
                                "Debe diligenciar todos los campos para poder continuar")
    else:
        return "ok"
    