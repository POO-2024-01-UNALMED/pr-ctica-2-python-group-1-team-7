import tkinter as tk

def generar_botones(frame_contenedor):
    frame_down = tk.Frame(frame_contenedor, highlightbackground="black", highlightthickness=1)
    frame_down.pack(side="bottom", fill="x")

    botones_frame = tk.Frame(frame_down, highlightbackground="black", highlightthickness=1)
    botones_frame.pack(side="bottom",anchor='s',pady=5)

    boton_aceptar = tk.Button(botones_frame, text="Aceptar", font=("Arial", 10), width=8, height=1)
    boton_aceptar.pack(side='left',anchor='s', padx=7)

    boton_borrar = tk.Button(botones_frame, text="Borrar", font=("Arial", 10), width=8, height=1)
    boton_borrar.pack(side='left',anchor='s', padx=7)

    return (boton_aceptar,boton_borrar)

class FieldFrame(tk.Frame):
    def __init__(self,tituloCriterios,criterios,tituloValores,valores,habilitado=None):
        super().__init__()
        self.tituloCriterios=tituloCriterios
        self.criterios=criterios
        self.tituloValores=tituloValores
        self.valores=valores
        self.habilitado=habilitado
        frame=tk.Frame(highlightbackground="black", highlightthickness=1)
        if self.tituloCriterios!=None:
            frame_tituloCriterios=tk.Frame(frame,highlightbackground="black", highlightthickness=1)
            frame_tituloCriterios.grid(row=0,column=0)
            label=tk.Label(frame_tituloCriterios,txt=self.tituloCriterios)
            label.pack()
        if self.tituloValores!=None:
            frame_tituloValores=tk.Frame(frame,highlightbackground="black", highlightthickness=1)
            frame_tituloValores.grid(row=0,column=1)
            label=tk.Label(frame_tituloValores,txt=self.tituloValores)
            label.pack()
        if self.criterios!=None:
            for criterio in self.criterios:
                label=tk.Label(frame,text=str(criterio))
                label.grid(row=self.criterios.index(criterio)+1,column=0)
            if self.valores!=None:
                for valor in self.valores:
                    if habilitado!=None:
                        if self.criterios[self.valores.index(valor)] in self.habilitado:
                            editado="disabled"
                        else:
                            editado="normal"
                    else:
                        editado="normal"
                    if valor==None:
                        entry=tk.Entry(frame,state=editado)
                        entry.grid(row=self.valores.index(valor)+1,column=1)
                    else:
                        entry=tk.Entry(frame,state=editado,textvariable=tk.StringVar(frame,value=valor))
                        entry.grid(row=self.valores.index(valor)+1,column=1)
            else:
                for criterio in self.criterios:
                    if habilitado!=None:
                        if criterio in self.habilitado:
                            editado="disabled"
                        else:
                            editado="normal"
                    else: 
                        editado="normal"
                    entry=tk.Entry(frame,state=editado)
                    entry.grid(row=self.criterios.index(criterio)+1,column=1)
    
    def getValue(self,criterio):
        #Lanzar un exception error si no encuentra el criterior
        if criterio in self.criterios:
            return self.valores[self.criterios.index(criterio)]