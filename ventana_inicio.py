import tkinter as tk

# Crea la ventana_inicio principal
ventana_inicio = tk.Tk()
ventana_inicio.geometry("500x900")
ventana_inicio.title("Resident Evil")
ventana_inicio.config(background="#C4C4C4")

#imagen circulos y logo
imagen_circulo = tk.PhotoImage (file = "img\circulos_inicio.png")
imagen_logo = tk.PhotoImage (file = "img\logo2.png")

# colocar imagenes
lienzo = tk.Canvas(ventana_inicio, width=500, height=8000, background="#C4C4C4", borderwidth = 0)
lienzo.create_image(250, 75, image = imagen_circulo)
lienzo.create_image(250, 300, image = imagen_logo)
lienzo.pack()


# imagenes de los botones
imagen_principiante = tk.PhotoImage (file = "img\principiante_buton.png")
imagen_avanzado = tk.PhotoImage (file = "img\dificil_buton.png") #es el la imagen del nivel avanzado se cambia el nombre a la imagen por que "\a" es algo resrvado del lenguaje

# Crea los botones
boton_principiante = tk.Button(ventana_inicio, image=imagen_principiante, borderwidth = 0)
boton_avanzado = tk.Button(ventana_inicio, image=imagen_avanzado, borderwidth = 0)

# Coloca los botones
boton_principiante.place(x=250, y=650, anchor="center")
boton_avanzado.place(x=250, y=750, anchor="center")

# Eventos de los botones
def evento_boton_principiante():
    ventana_inicio_principiante = tk.Toplevel(ventana_inicio)
    ventana_inicio_principiante.title("Principiante")
    texto = "El modo principiante es el modo más fácil del juego. Está diseñado para jugadores que están aprendiendo los conceptos básicos de Resident Evil. En este modo, los enemigos son más débiles y los recursos son más abundantes."
    label = tk.Label(ventana_inicio_principiante, text=texto)
    label.pack()

def evento_boton_avanzado():
    ventana_inicio_avanzado = tk.Toplevel(ventana_inicio)
    ventana_inicio_avanzado.title("Avanzado")
    texto = "El modo avanzado es el modo más difícil del juego. Está diseñado para jugadores experimentados que buscan un desafío. En este modo, los enemigos son más fuertes y los recursos son más escasos."
    label = tk.Label(ventana_inicio_avanzado, text=texto)
    label.pack()

# Asigna los eventos a los botones
boton_principiante.config(command=evento_boton_principiante, background="#C4C4C4")
boton_avanzado.config(command=evento_boton_avanzado, background="#C4C4C4")

# Inicia la aplicación
ventana_inicio.mainloop()
