""" import tkinter as tk

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
            return self.valores[self.criterios.index(criterio)] """



'''self.frame_izquierda = tk.Frame(self)
        self.frame_izquierda.grid(side="left", expand=True, fill="both")
        self.frame_derecha = tk.Frame(self)
        self.frame_derecha.pack(side="right", expand=True, fill="both")

        self.label_titulo_criterios = tk.Label(self.frame_izquierda, text=tituloCriterios)
        self.label_titulo_criterios.pack(expand=True, fill="x", pady=10)

        for text_label in self.criterios:
            label = tk.Label(self.frame_izquierda, text=text_label)
            label.pack(expand=True, fill="x")

        self.label_titulo_valores = tk.Label(self.frame_derecha, text=tituloValores)
        self.label_titulo_valores.pack(expand=True, fill="x", pady=10)

        for i in range(4):
            entry = tk.Entry(self.frame_derecha)
            entry.pack(expand=True, fill="x", padx=40)

    def getValue(self,criterio):
        #Lanzar un exception error si no encuentra el criterior
        if criterio in self.criterios:
            return self.valores[self.criterios.index(criterio)]

        self.label_titulo_criterios = tk.Label(self.frame_izquierda, text=tituloCriterios)
        self.label_titulo_criterios.grid(row=0,column=0, pady=10)

        for text_label in self.criterios:
            label = tk.Label(self.frame_izquierda, text=text_label)
            label.pack(expand=True, fill="x")

        self.label_titulo_valores = tk.Label(self.frame_derecha, text=tituloValores)
        self.label_titulo_valores.pack(expand=True, fill="x", pady=10)

        for i in range(4):
            entry = tk.Entry(self.frame_derecha)
            entry.pack(expand=True, fill="x", padx=40)'''
import tkinter as tk

class field_frame(tk.Frame):
    def __init__(self, parent, tituloCriterios, criterios, tituloValores, valores, habilitado=None):
        super().__init__(parent, bg='lightblue')
        self.pack(expand=True, fill="both")
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores
        self.habilitado = habilitado

        self.labels = {}
        self.entries = {}

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        if self.tituloCriterios!=None:
            frame_tituloCriterios=tk.Frame(self,highlightbackground="blue", highlightthickness=2)
            frame_tituloCriterios.grid(row=0,column=0,sticky='news',padx=10,pady=10)
            label=tk.Label(frame_tituloCriterios,text=self.tituloCriterios)
            label.pack()
        if self.tituloValores!=None:
            frame_tituloValores=tk.Frame(self,highlightbackground="blue", highlightthickness=2)
            frame_tituloValores.grid(row=0,column=1,sticky='news',padx=10,pady=10)
            label=tk.Label(frame_tituloValores,text=self.tituloValores)
            label.pack()

        if self.criterios!=None:
            for criterio in self.criterios:
                label = tk.Label(self, text=str(criterio))
                label.grid(row=self.criterios.index(criterio)+1, column=0, sticky='news', padx=10, pady=10)
                self.labels[criterio] = label

                entry = tk.Entry(self)
                entry.grid(row=self.criterios.index(criterio)+1, column=1, sticky='news', padx=10, pady=10)
                self.entries[criterio] = entry


    def activar_campo(self, lista_criterios):
        for criterio in lista_criterios:
            if criterio in self.labels and criterio in self.entries:
                self.labels[criterio].grid(row=self.criterios.index(criterio)+1, column=0, sticky='news', padx=10, pady=10)
                self.entries[criterio].grid(row=self.criterios.index(criterio)+1, column=1, sticky='news', padx=10, pady=10)

    def ocultar_campos(self, lista_criterios):
        for criterio in lista_criterios:
            if criterio in self.labels and criterio in self.entries:
                self.labels[criterio].grid_forget()
                self.entries[criterio].grid_forget()

    

        '''
        if self.criterios!=None:
            for criterio in self.criterios:
                label=tk.Label(self,text=str(criterio))
                label.grid(row=self.criterios.index(criterio)+1,column=0,sticky='news',padx=10,pady=10)
                self.label.append()
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
                        entry=tk.Entry(self,state=editado)
                        entry.grid(row=self.valores.index(valor)+1,column=1,sticky='news',padx=10,pady=10)
                    else:
                        entry=tk.Entry(self,state=editado,textvariable=tk.StringVar(self,value=valor))
                        entry.grid(row=self.valores.index(valor)+1,column=1,sticky='news',padx=10,pady=10)
            else:
                for criterio in self.criterios:
                    if habilitado!=None:
                        if criterio in self.habilitado:
                            editado="disabled"
                        else:
                            editado="normal"
                    else: 
                        editado="normal"
                    entry=tk.Entry(self,state=editado)
                    entry.grid(row=self.criterios.index(criterio)+1,column=1,sticky='news',padx=10,pady=10)

    def getValue(self,criterio):
        #Lanzar un exception error si no encuentra el criterior
        if criterio in self.criterios:
            return self.valores[self.criterios.index(criterio)]
        
    def activar_campo(self,lista_criterios):
        for criterio in lista_criterios:
            if criterio in self.criterios:
                indice=self.criterios.index(criterio)+1
                label=self.grid_slaves(row=indice,column=0)
                label[0].grid(row=self.criterios.index(criterio)+1,column=0,sticky='news',padx=10,pady=10)
                entry=self.grid_slaves(row=indice,column=1)
                entry[0].grid(row=self.criterios.index(criterio)+1,column=1,sticky='news',padx=10,pady=10)
    
    def ocultar_campos(self,lista_criterios):
        for criterio in lista_criterios:
            if criterio in self.criterios:
                indice=self.criterios.index(criterio)+1
                label=self.grid_slaves(row=indice,column=0)
                label[0].grid_forget()
                entry=self.grid_slaves(row=indice,column=1)
                entry[0].grid_forget()
'''
        
    