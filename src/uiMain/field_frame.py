import tkinter as tk

class field_frame(tk.Frame):
    def __init__(
        self, 
        parent, 
        tituloCriterios, 
        criterios, 
        tituloValores, 
        valores = None, 
        habilitado = None
    ):
        super().__init__(parent, bg='lightblue')
        self.pack(fill="both")

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
            frame_tituloCriterios=tk.Frame(
                self,
                highlightbackground="blue", 
                highlightthickness=2
            )
            frame_tituloCriterios.grid(row=0,column=0,sticky='news',padx=10,pady=10)
            label=tk.Label(frame_tituloCriterios,text=self.tituloCriterios)
            label.pack()
        if self.tituloValores!=None:
            frame_tituloValores=tk.Frame(
                self,
                highlightbackground="blue", 
                highlightthickness=2
            )
            frame_tituloValores.grid(row=0,column=1,sticky='news',padx=10,pady=10)
            label=tk.Label(frame_tituloValores,text=self.tituloValores)
            label.pack()

        if self.criterios != None:
            for criterio in self.criterios:
                label = tk.Label(self, text=str(criterio))
                label.grid(
                    row=self.criterios.index(criterio)+1, 
                    column=0, 
                    sticky='news', 
                    padx=10, 
                    pady=10
                )
                self.labels[criterio] = label

                entry = tk.Entry(self)
                entry.grid(
                    row=self.criterios.index(criterio)+1, 
                    column=1, 
                    sticky='news', 
                    padx=10, 
                    pady=10
                )
                self.entries[criterio] = entry
 
    def activar_campo(self, lista_criterios):
        for criterio in lista_criterios:
            if criterio in self.labels and criterio in self.entries:
                self.labels[criterio].grid(
                    row=self.criterios.index(criterio)+1, 
                    column=0, 
                    sticky='news', 
                    padx=10, 
                    pady=10
                )
                self.entries[criterio].grid(
                    row=self.criterios.index(criterio)+1, 
                    column=1, 
                    sticky='news', 
                    padx=10, 
                    pady=10
                )

    def ocultar_campos(self, lista_criterios):
        for criterio in lista_criterios:
            if criterio in self.labels and criterio in self.entries:
                self.labels[criterio].grid_forget()
                self.entries[criterio].grid_forget()
    
    def agregar_campo(self, criterio, desabilitar_anterior):
        if desabilitar_anterior:
            self.labels[list(self.labels.keys())[-1]].config(state="disabled")
        label = tk.Label(self, text=criterio)
        label.grid(
            row=len(self.labels)+1, 
            column=0, 
            sticky='news', 
            padx=10, 
            pady=10
        )
        self.labels[criterio] = label
        
        if desabilitar_anterior:
            self.entries[list(self.entries.keys())[-1]].config(state="disabled")
        entry = tk.Entry(self)
        entry.grid(
            row=len(self.entries)+1, 
            column=1, 
            sticky='news', 
            padx=10, 
            pady=10
        )
        self.entries[criterio] = entry

    
    def getValue(self, criterio):
        return self.entries[criterio].get()

