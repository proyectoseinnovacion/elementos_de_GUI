from tkinter import *
from tkinter import scrolledtext as sc
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import pandas as pd
from PIL import Image, ImageTk

class Cuadro(Frame):
    """"""
    
    #----------------------------------------------------------------------
    def __init__(self, window, scrollable=FALSE):
        """Constructor especial de la clase Cuadro.\n
        Permite generar objetos Frame con opción de agregar scrollbar. 
        Posee métodos que permiten incorporar otros wingets de Tkinter."""

        self.scrollable = scrollable
        
        if self.scrollable:
            self.main_frame = Frame(window)
            self.main_frame.pack(side="top", fill="both", expand=True)
            self.scrollframe = ScrollFrame(self.main_frame)
            self.scrollframe.pack(side="top", fill="both", expand=True)
            # Frame que contiene objetos:
            self.z = Frame(self.scrollframe.viewPort)
            self.z.pack(side="top", fill="both", expand=True)

        else:
            # Frame que contiene objetos:
            self.z = Frame(window)
            self.z.pack()
            # Comentario

        self.lista_de_objetos = []
        self.lista_de_datos = []
   
    #----------------------------------------------------------------------
    def agregar_label(self, y, x, texto):
        """Método de la clase Cuadro. \n
        Permite agregar texto al Frame creado con la Clase Cuadro."""

        self.y= y
        self.x= x
        self.texto= texto
        self.etiqueta = Label(self.z, text= self.texto)
        self.etiqueta.grid(row= self.y, column=self.x, sticky='news', pady=4, padx=8)
        self.lista_de_objetos.append((self.etiqueta))
    
    #----------------------------------------------------------------------
    def agregar_button(self, y, x, texto, funcion):
        """Método de la clase Cuadro. \n
        Permite agregar un botón al Frame creado con la Clase Cuadro."""

        #----------------------------------------------------------------------
        def Efecto_de_boton(boton):
            """"""

            #----------------------------------------------------------------------
            def Pasar_sobre_boton(e):
                """"""
                boton['bg'] = '#b5c8e5'
        
            #----------------------------------------------------------------------
            def Dejar_boton(e):
                """"""
                boton['bg'] = "#144ca4"
        
            boton.bind('<Enter>', Pasar_sobre_boton)
            boton.bind('<Leave>', Dejar_boton)

        self.y= y
        self.x= x
        self.texto = texto
        self.funcion = funcion
        self.boton = Button(
                        self.z, 
                        text= self.texto, 
                        command=self.funcion,
                        fg = "#ffffff",
                        bg = "#144ca4",
                        relief="flat",
                        cursor="hand2"
                        )
        self.boton.grid(row= self.y, column=self.x, pady=4, padx=8)
        Efecto_de_boton(self.boton)
        self.lista_de_objetos.append((self.boton))

    #----------------------------------------------------------------------
    def agregar_imagen(self, y, x, archivo, largo, alto):
        """Método de la clase Cuadro. \n
        Permite agregar una imagen al Frame creado con la Clase Cuadro."""
        
        self.y = y
        self.x = x
        self.archivo = archivo
        self.largo = largo
        self.alto = alto
        self.ubicacion = str('images/' + self.archivo)
        self.imagen_cargada = Image.open(self.ubicacion)
        self.imagen_cargada = self.imagen_cargada.resize((self.largo, self.alto), Image.ANTIALIAS)
        self.imagen = ImageTk.PhotoImage(self.imagen_cargada)
        self.imagen_label = Label(self.z, image=self.imagen)
        self.imagen_label.grid(row = self.y, column = self.x, pady=4, padx=8)
        self.lista_de_objetos.append((self.imagen_label))

    #----------------------------------------------------------------------
    def agregar_entry(self, y, x):
        """Método de la clase Cuadro. \n
        Permite agregar una entrada de texto al Frame creado con la Clase Cuadro."""

        self.y= y
        self.x= x
        self.data = StringVar()
        self.entrada = Entry(self.z, textvariable=self.data)
        self.entrada.grid(row= self.y, column=self.x, pady=4, padx=8)
        self.lista_de_objetos.append((self.entrada))
        self.lista_de_datos.append((self.data))

    #----------------------------------------------------------------------
    def agregar_scrolltext(self, y, x):
        """Método de la clase Cuadro. \n
        Permite agregar una entrada de texto largo que posee su propio scrollbar al Frame creado con la Clase Cuadro."""

        self.y= y
        self.x= x
        self.text_area = sc.ScrolledText(self.z, 
                            wrap = WORD, 
                            width = 40, 
                            height = 5, 
                            font = ("Times New Roman",
                            11))
        self.text_area.grid(row = self.y, column = self.x, pady=4, padx=8)
        self.lista_de_objetos.append((self.text_area))
        self.lista_de_datos.append((self.text_area))

    #----------------------------------------------------------------------
    def agregar_radiobutton(self, y, x, lista):
        """Método de la clase Cuadro. \n
        Permite agregar una lista del tipo "opción múltiple" al Frame creado con la Clase Cuadro."""
        
        self.y = y
        self.x = x
        self.data = IntVar()
        self.lista = lista
        self.range_y = range(self.y, self.y + len(self.lista))
        self.tabla_lista_y_range_y = pd.DataFrame(self.lista, self.range_y)

        for i, j in zip(self.lista, self.range_y):
            self.radiobutton = Radiobutton(self.z, text= i, variable= self.data, 
            value=j+1)
            self.radiobutton.grid(row = j, column = self.x)
            self.lista_de_objetos.append((self.radiobutton))
        self.lista_de_datos.append((self.data))

    #----------------------------------------------------------------------
    def agregar_checkbutton(self, y, x, texto):
        """Método de la clase Cuadro. \n
        Permite agregar una casilla de confirmación al Frame creado con la Clase Cuadro."""

        self.y = y
        self.x = x
        self.texto = texto
        self.data = IntVar()
        self.checkbuttom = Checkbutton(self.z, text=self.texto, variable=self.data, 
            onvalue=1, offvalue=0)
        self.checkbuttom.grid(row = self.y, column = self.x)
        self.lista_de_objetos.append((self.checkbuttom))
        self.lista_de_datos.append((self.data))

    #----------------------------------------------------------------------
    def agregar_combobox(self, y, x, listadesplegable):
        """Método de la clase Cuadro. \n
        Permite agregar una lista desplegable al Frame creado con la Clase Cuadro."""
        
        self.y = y
        self.x = x
        self.listadesplegable = listadesplegable
        self.combo = ttk.Combobox(self.z, state="readonly")
        self.combo.grid(row = self.y, column = self.x, pady=4, padx=8)
        self.combo["values"] = self.listadesplegable
        self.combo.set(self.listadesplegable[0])
        self.lista_de_objetos.append((self.combo))
        self.lista_de_datos.append((self.combo))

    #----------------------------------------------------------------------
    def agregar_spinbox(self, y, x, inicio, fin, incremento, defecto):
        """Método de la clase Cuadro. \n
        Permite agregar un winget con botones para incrementar o dismunir una cantidad al Frame creado con la Clase Cuadro."""

        self.y = y
        self.x = x
        self.inicio = inicio
        self.fin = fin
        self.incremento = incremento
        self.defecto = defecto
        self.spin_box = ttk.Spinbox(self.z, from_= self.inicio, to=self.fin, increment=self.incremento, format="%.0f")
        self.spin_box.insert(0, self.defecto)
        self.spin_box["state"] = "readonly"
        self.spin_box.grid(row=self.y, column=self.x, pady=4, padx=8)
        self.lista_de_objetos.append((self.spin_box))
        self.lista_de_datos.append((self.spin_box))

    #----------------------------------------------------------------------
    def agregar_dateentry(self, y, x):
        """Método de la clase Cuadro. \n
        Permite agregar una entrada de calendario al Frame creado con la Clase Cuadro."""

        # Recordar que es importante utilizar: pyinstaller --hidden-import babel.numbers myscript.py
        # Ver: https://tkcalendar.readthedocs.io/en/stable/howtos.html 
        
        self.y = y
        self.x = x
        self.cal = DateEntry(self.z, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
        self.cal.grid(row = self.y, column = self.x, pady=4, padx=8)
        self.lista_de_objetos.append((self.cal))
        self.lista_de_datos.append((self.cal))

    #----------------------------------------------------------------------
    def agregar_rejilla(self, rejilla):
        """Método de la clase Cuadro. \n
        Permite utilizar una tupla de tuplas para incorporar diversos wingets al Frame creado con la Clase Cuadro."""

        self.rejilla = rejilla

        self.tabla = pd.DataFrame(list(self.rejilla))

        for i,row in self.tabla.iterrows():
            
            if row[0] == 'L':

                self.agregar_label(row[1], row[2], row[3])

            elif row[0] == 'I':
                
                # En este caso row[3] debe ser un archivo de imagen (p.e. png)
                self.agregar_imagen(row[1], row[2], row[3], row[4], row[5])

            elif row[0] == 'B':

                self.agregar_button(row[1], row[2], row[3], row[4])

            elif row[0] == 'E':

                self.agregar_entry(row[1], row[2])
            
            elif row[0] == 'ST':

                self.agregar_scrolltext(row[1], row[2])
            
            elif row[0] == 'R':
                
                # En este caso row[3] debe ser una lista:
                self.agregar_radiobutton(row[1], row[2], row[3])
            
            elif row[0] == 'CB':

                self.agregar_checkbutton(row[1], row[2], row[3])
            
            elif row[0] == 'CX':
                
                # En este caso row[3] debe ser una lista:
                self.agregar_combobox(row[1], row[2], row[3])
            
            elif row[0] == "SB":

                self.agregar_spinbox(row[1], row[2], row[3], row[4], row[5], row[6])

            elif row[0] == 'D':

                self.agregar_dateentry(row[1], row[2])

            else:

                print('Error, el valor de i[0] es {row[0]}')

    #----------------------------------------------------------------------
    def obtener_dato(self, n):
        """Método de la clase Cuadro. \n
        Permite recuperar la información registrada a través de los wingets agregados al Frame creado con la Clase Cuadro."""
        
        # Esta función obtiene un dato "n" de la lista que se guarda en el objeto cuadro.
        self.lista = self.lista_de_datos
        if type(self.lista[n]).__name__ == 'DateEntry':
            return self.lista[n].get_date()
        elif type(self.lista[n]).__name__ == 'ScrolledText':
            return self.lista[n].get("1.0", "end-1c")
        else:
            return self.lista[n].get()
    
    #----------------------------------------------------------------------
    def obtener_lista_de_datos(self):

        self.lista = self.lista_de_datos
        self.lista_output = []
        for i in self.lista:
            if type(i).__name__ == 'DateEntry':
                self.lista_output.append(i.get_date())
            elif type(i).__name__ == 'ScrolledText':
                self.lista_output.append(i.get("1.0", "end-1c"))
            else:
                self.lista_output.append(i.get())
        return self.lista_output

class MenuSefa():

    #----------------------------------------------------------------------
    def __init__(self, window):
        """Constructor"""

        menubar = Menu(window)
        window.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Cerrar sesión")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=window.quit)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de...")

        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)
      
class ScrollFrame(Frame):

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""

        super().__init__(parent)

        self.canvas = Canvas(self, borderwidth=0, background="Red")
        self.viewPort = Frame(self.canvas, background="Yellow")


        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.hsb = Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

        self.hsb.pack(side="bottom", fill="x")
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas_window = self.canvas.create_window((0,0), window=self.viewPort, anchor="nw",
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind("<Configure>", self.onCanvasConfigure)

        self.onFrameConfigure(None)

    #----------------------------------------------------------------------
    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    #----------------------------------------------------------------------
    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        if (event.widget.winfo_width() != event.width) and (event.widget.winfo_height()  != event.height):
            canvas_width, canvas_height = event.width, event.height
            self.canvas.itemconfig(self.canvas_window, width = canvas_width, height = canvas_height)

  
# Prueba
hola
print
