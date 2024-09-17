from Excepciones.ExcepcionId import ExcepcionId
from Excepciones.ExcepcionCorreo import ExcepcionCorreo
from Excepciones.ExcepcionTelefono import ExcepcionTelefono
from tkinter import messagebox
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
        messagebox.showwarning("Correo ingresado incorrecto",e)
    except:
        messagebox.showwarning("Correo ingresado incorrecto","El correo ingresado es incorrecto, ingréselo nuevamente")
    else:
        return "ok"
    
def excepcion_telefono(telefono):
    try:
        if len(str(telefono))!=10 or int(telefono)<0:
            raise ExcepcionTelefono()
    except ExcepcionTelefono as e:
        messagebox.showwarning("Teléfono ingresado incorrecto",e)
    except:
        messagebox.showwarning("Teléfono ingresado incorrecto","El teléfono ingresado es incorrecto, ingréselo nuevamente")
    else:
        return "ok"