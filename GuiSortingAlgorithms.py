from tkinter import *
from tkinter import ttk

import random # Para evitar ingresar datos de forma manual

from insertionSort import insertion_sort
from mergeSort import merge_sort
# GUI
# Funciones interactivas de la GUI



def pepito():
    pass





def deployPrincipal():
    UI_frame_principal = Frame(root, width=600, bg='white')
    UI_frame_principal.place(in_=root, anchor="c", relx=.50, rely=.50)
    title_1 = Label(UI_frame_principal, text="Simulador de algoritmos de ordenamiento", bg='white', fg='blue', font=('Helvetica', 24), justify=CENTER)
    title_1.grid(row=0, column=0, padx=5, sticky=W)

    title_2 = Label(UI_frame_principal, text="Por inserción y por mezcla", bg='white', fg='blue', font=('Helvetica', 18), justify=CENTER)
    title_2.grid(row=1, column=0, padx=5, sticky=W)

    title_2 = Label(UI_frame_principal, text="Escoja el tipo de comparativa:", bg='white', fg='black', font=('Helvetica', 14), justify=CENTER)
    title_2.grid(row=2, column=0, padx=5, sticky=W)

    Button(UI_frame_principal, text="Gráfica", command=deployGraphMenu, bg='lightblue').grid(row=3, column=0, padx=5, pady=5)

    Button(UI_frame_principal, text="Desempeño", command=pepito, bg='red').grid(row=4, column=0, padx=5, pady=5)

# Disenio de la GUI


def deployGraphMenu():
    root.update()
    # Frames, labels, inputs, etc.
    UI_frame_menu = Frame(root, width=600, height=200, bg='grey') # Inicializar el frame
    UI_frame_menu.grid(row=0, column=0, padx=10, pady=5)

    # En el canvas se van a mostrar los algoritmos
    canvas = Canvas(root, width=600, height=380, bg='white') 
    canvas.grid(row=1, column=0, padx=10, pady=5)

# Interactuar con la GUI
    # Fila 1 del menu:
    # Mensaje:
    Label(UI_frame_menu, text="Algoritmo a ejecutar: ", bg='grey', fg='white').grid(row=0, column=0, padx=5, sticky=W)
    # Opciones de algoritmo
    algMenu = ttk.Combobox(UI_frame_menu, textvariable=selected_algorithm, values=['Algoritmo de Inserción', 'Algoritmo por Mezcla'])
    algMenu.grid(row=0, column=1, padx=5, pady=5)
    algMenu.current(0)

    speedScale = Scale(UI_frame_menu, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Velocidad")
    speedScale.grid(row=0, column=2, padx=5, pady=5)
    Button(UI_frame_menu, text="Ordenar", command=StartAlgorithm, bg='blue', fg='white', width=10).grid(row=0, column=3, padx=5, pady=5)

    # Fila 2 del menu:
    # Label(UI_frame_menu, text="Tamaño: ", bg='grey', fg='white').grid(row=1, column=0, padx=5, sticky=W)
    sizeEntry = Scale(UI_frame_menu, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Tamaño:")
    sizeEntry.grid(row=1, column=0, padx=5, pady=5, sticky=W)

    # Label(UI_frame_menu, text="Mínimo valor: ", bg='grey', fg='white').grid(row=1, column=2, padx=5, sticky=W)
    minEntry = Scale(UI_frame_menu, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Valor mínimo:")
    minEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    # Label(UI_frame_menu, text="Máximo valor: ", bg='grey', fg='white').grid(row=1, column=4, padx=5, sticky=W)
    maxEntry = Scale(UI_frame_menu, from_=11, to=100, resolution=1, orient=HORIZONTAL, label="Valor máximo:") 
    maxEntry.grid(row=1, column=2, padx=5, pady=5, sticky=W)

    Button(UI_frame_menu, text="Graficar", command=Generate, bg='white', width=10).grid(row=1, column=3, padx=5, pady=5)

    # Fila 3 del menu

def Generate():
    global data

    # Generar lista randomica a partir de los inputs
    size = int(sizeEntry.get())
    minValue = int(minEntry.get())
    maxValue = int(maxEntry.get())
    
    data = []
    for _ in range(size):
        data.append(random.randrange(minValue, maxValue+1))

    drawData(data, ['red' for x in range(len(data))]) # datap['red1', 'red2', ..., 'redN' ]

# Dibujara en pantalla cada dato, en forma de barra, de la lista a ordenar
def drawData(data, colorArray):
    canvas.delete("all")
    c_width = 600
    c_height = 380
    x_width = c_width / (len(data) + 5) 
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        # coordenadas izquierda
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # coordenadas derecha
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()

# Aqui se ejecuta el algoritmo deseado
def StartAlgorithm():
    global data
    
    # Para evitar que se usen Inputs mientras se ejecuta graficamente el algoritmo
    UI_frame_menu.focus_displayof()
    warning_message = Label(UI_frame_menu, text="Por favor, espere a que los algoritmos finalicen para interactuar con la interfaz", bg='grey', fg='white')
    warning_message.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    root.update()
    # Escoger el algoritmo:
    if algMenu.get() == "Algoritmo de Inserción":
        insertion_sort(data, drawData, speedScale.get())
    elif algMenu.get() == "Algoritmo por Mezcla":
        merge_sort(data, drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))]) 

    warning_message.destroy()
    UI_frame_menu.focus()



if __name__ == "__main__":
    # Inicializar la ventana del progama simulador
    root = Tk()
    root.title("Simulador de algoritmos de ordenamiento")
    root.geometry('625x550')
    root.resizable(width=0, height=0)
    root.config(bg='lightgrey', bd=25)

    # Variables a usar
    selected_algorithm = StringVar()
    data = []

    deployPrincipal()

    root.mainloop()