from gestorAplicación.personas.pasajero import Pasajero
import uiMain.auxiliar_excepciones as exepciones
from uiMain import auxiliar

import tkinter as tk

class gestionar_tiquetes():
    PASAJERO = None
    TIQUETES_VALIDOS = None
    TIQUETES_VENCIDOS = None
    TIQUETE = None

    @classmethod
    def mostrar_tiquetes(cls, frame_funcionalidad):
        numero_identificacion = frame_funcionalidad.field_frame.getValue(
            "Ingrese el número de identificación del pasajero"
        )

        if (
            exepciones.excepcion_id(numero_identificacion) == "ok" 
            and exepciones.excepcion_id_usuario(numero_identificacion) == "ok"
        ):
            pasajero = Pasajero.buscar_pasajero(numero_identificacion)
            
            tiquetes_validos = pasajero.buscar_tiquetes("validos")
            tiquetes_vencidos = pasajero.buscar_tiquetes("vencidos")

            if(len(tiquetes_validos) != 0):
                frame_funcionalidad.text.insert(
                    "end", 
                    f"Tiquetes válidos\n"
                )
                frame_funcionalidad.text.insert("end", "-" * 93 + "\n")
                frame_funcionalidad.text.insert(
                    "end", 
                    "    NUMERO DE RESERVA     NOMBRE        ASIENTO"
                    + "             FECHA DEL VIAJE      ID VIAJE     \n"
                )
                frame_funcionalidad.text.insert("end", "-" * 93 + "\n")

                for tiquete in tiquetes_validos:
                    frame_funcionalidad.text.insert("end", str(tiquete) + "\n")

                frame_funcionalidad.text.insert("end", "\n")

            if(len(tiquetes_vencidos) != 0):
                frame_funcionalidad.text.insert(
                        "end", 
                        f"Tiquetes vencidos\n"
                )
                frame_funcionalidad.text.insert("end", "-" * 93 + "\n")
                frame_funcionalidad.text.insert(
                    "end", 
                    "    NUMERO DE RESERVA     NOMBRE        ASIENTO"
                    + "             FECHA DEL VIAJE      ID VIAJE     \n"
                )
                frame_funcionalidad.text.insert("end", "-" * 93 + "\n")

                for tiquete in tiquetes_vencidos:
                    frame_funcionalidad.text.insert("end", str(tiquete) + "\n")

                frame_funcionalidad.text.insert("end", "\n")
            
            frame_funcionalidad.text.config(state="disabled")

            frame_funcionalidad.field_frame.agregar_campo(
                "¿Desea escoger algún tiquete?", 
                True
            )

            cls.PASAJERO = pasajero
            cls.TIQUETES_VALIDOS = tiquetes_validos
            cls.TIQUETES_VENCIDOS = tiquetes_vencidos
        else:
            raise Exception

    @staticmethod
    def primera_pregunta(frame_funcionalidad):
        respuesta = frame_funcionalidad.field_frame.getValue(
            "¿Desea escoger algún tiquete?"
        ).lower()

        if respuesta == "si":
            frame_funcionalidad.field_frame.agregar_campo(
                "Escoja el tiquete ingresando el número de reserva", 
                True
            )
        elif respuesta == "no":
            pass
        else:
            tk.messagebox.showwarning("Advertencia","Solo se admite (si/no)")
            raise Exception

    @classmethod
    def seleccionar_tiquete(cls, frame_funcionalidad):
        numero_tiquete = frame_funcionalidad.field_frame.getValue(
            "Escoja el tiquete ingresando el número de reserva"
        )

        if exepciones.excepcion_tiquete(numero_tiquete) == "ok":
            tiquete = cls.PASAJERO.buscar_tiquete_por_reserva(numero_tiquete)

            if tiquete in cls.TIQUETES_VENCIDOS:
                frame_funcionalidad.text.config(state="normal")
                frame_funcionalidad.text.delete("1.0", "end")
                frame_funcionalidad.text.insert("end", "-" * 93 + "\n")
                frame_funcionalidad.text.insert(
                    "end", 
                    "    NUMERO DE RESERVA     NOMBRE        ASIENTO"
                    + "             FECHA DEL VIAJE      ID VIAJE     \n"
                )
                frame_funcionalidad.text.insert("end", "-" * 93 + "\n")
                frame_funcionalidad.text.insert("end", str(tiquete))
                frame_funcionalidad.text.config(state="disabled")
            elif tiquete in cls.TIQUETES_VALIDOS:
                frame_funcionalidad.field_frame.agregar_campo(
                    "¿Desea cancelarlo o modificarlo?", 
                    True
                )
                cls.TIQUETE = tiquete
            else:
                raise Exception
        else:
            raise Exception
    
    @classmethod
    def decision(cls, frame_funcionalidad):
        decision = frame_funcionalidad.field_frame.getValue(
            "¿Desea cancelarlo o modificarlo?"
        ).lower()

        if decision == "cancelarlo":
            frame_funcionalidad.text.config(state="normal")
            frame_funcionalidad.text.delete("1.0", "end")
            frame_funcionalidad.text.insert("end", "Tiquete cancelado exitosamente")
            frame_funcionalidad.text.config(state="disabled")
            frame_funcionalidad.boton_aceptar.config(state="disabled")
            frame_funcionalidad.boton_borrar.config(state="disabled")
            frame_funcionalidad.field_frame.entries[
                "¿Desea cancelarlo o modificarlo?"
            ].config(state="disabled")
            cls.PASAJERO.cancelar_tiquete(cls.TIQUETE)
        elif decision == "modificarlo":
            frame_funcionalidad.field_frame.agregar_campo(
                "¿Desea cambiar de asiento o de viaje?", 
                True
            )
        else:
            tk.messagebox.showwarning(
                "Advertencia",
                "Solo se admite (cancerlarlo/modificarlo)"
            )
            raise Exception
    
    @classmethod
    def modificar(cls, frame_funcionalidad, ventana_principal):
        respuesta = decision = frame_funcionalidad.field_frame.getValue(
            "¿Desea cambiar de asiento o de viaje?"
        ).lower()

        if respuesta == "asiento":
            if not cls.TIQUETE.get_viaje().tiene_sillas():
                tk.messagebox.showwarning(
                    "Advertencia",
                    "No hay más asientos disponibles. Escoja otra opción"
                )
                raise Exception
            else:
                frame_funcionalidad.text.pack_forget()
                auxiliar.asientos(
                    frame_funcionalidad.frame_superior, 
                    cls.TIQUETE.get_viaje()
                )
                frame_funcionalidad.field_frame.agregar_campo(
                    "Ingrese el número del asiento", 
                    True
                )
        elif respuesta == "viaje":
            cls.TIQUETE.liberar_asiento()
            frame_funcionalidad.destroy()
            ventana_principal.generador_funcionalidades(2)
            raise Exception
        else:
            tk.messagebox.showwarning("Advertencia","Solo se admite (asiento/viaje)")
            raise Exception

    @classmethod
    def modificar_continuacion(cls, frame_funcionalidad):
        try:
            numero_asiento = frame_funcionalidad.field_frame.getValue(
                "Ingrese el número del asiento"
            )

            if exepciones.excepcion_asiento(
                numero_asiento, 
                cls.TIQUETE.get_viaje().get_bus()
            ) == "ok":
                cls.TIQUETE.cambiar_asiento(
                    cls.TIQUETE.get_viaje().buscar_asiento(numero_asiento)
                )

                frame_funcionalidad.frame_superior.winfo_children()[-1].destroy()

                frame_funcionalidad.text.config(state="normal")
                frame_funcionalidad.text.delete("1.0", "end")

                frame_funcionalidad.text.tag_configure("center", justify='center')
                frame_funcionalidad.text.tag_add("center", 1.0, "end")
                frame_funcionalidad.text.pack(expand=True, fill="both")
                
                frame_funcionalidad.text.insert(
                    "end", 
                    "Tiquete reservado exitosamente\n", "center"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    "-" * 34 + "\n"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    f"Tiquete No. {cls.TIQUETE.get_numero_reserva()}" + "\n"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    "-" * 34 + "\n"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    f"Nombre del pasajero: {cls.PASAJERO.get_nombre()}" + "\n"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    f"Id del pasajero: {cls.PASAJERO.get_id()}" + "\n"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    f"Asiento: {cls.TIQUETE.get_asiento()}" + "\n"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    f"Empresa: {cls.TIQUETE.get_viaje().get_empresa().get_nombre()}" 
                    + "\n"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    f"Placa del bus: {cls.TIQUETE.get_viaje().get_bus().get_placa()}" 
                    + "\n"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    f"Id del viaje: {cls.TIQUETE.get_viaje().get_id()}" + "\n"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    f"Fecha y hora: {cls.TIQUETE.get_viaje().get_fecha()} " 
                    + f"{cls.TIQUETE.get_viaje().get_hora().strftime("%H:%M")}" 
                    + "\n"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    f"Origen: {cls.TIQUETE.get_viaje().get_origen()}" 
                    + "\n"
                )
                frame_funcionalidad.text.insert(
                    "end", 
                    f"Destino: {cls.TIQUETE.get_viaje().get_destino()}" 
                    + "\n"
                )

                frame_funcionalidad.text.insert("end", "-" * 34 + "\n")
                frame_funcionalidad.text.config(state="disabled")

                frame_funcionalidad.field_frame.entries[
                    "Ingrese el número del asiento"
                ].config(state="disabled")

                frame_funcionalidad.boton_aceptar.config(state="disabled")
                frame_funcionalidad.boton_borrar.config(state="disabled")
            else:
                raise Exception
        except Exception as e:
                print(e)
        


