import tkinter as tk

# Crea la ventana_inicio principal
ventana_inicio = tk.Tk()
ventana_inicio.geometry("500x800")
ventana_inicio.title("Resident Evil")

# Crea los botones
boton_principiante = tk.Button(ventana_inicio, text="Principiante")
boton_avanzado = tk.Button(ventana_inicio, text="Avanzado")

# Coloca los botones
boton_principiante.pack()
boton_avanzado.pack()

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
boton_principiante.config(command=evento_boton_principiante)
boton_avanzado.config(command=evento_boton_avanzado)

# Inicia la aplicación
ventana_inicio.mainloop()
