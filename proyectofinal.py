
# IMPORTAMOS 
# Importamos la biblioteca de Tkinter que sirve para crear interfaces gráficas 
# Podemos crear ventanas, botones para hacer clik,menus etc.

import tkinter as tk
from tkinter import messagebox
import random




# DECLARAMOS UN CONJUNTO DE PALABRAS DE DONDE SE SELECIONARÁ DE MANERA ALEATORIA CUALQUIER 
# PALABRA PARA COMENZAR EL JUEGO DEL AHORCADO
# Con la función random.choice elegir una palabra de manera aleatoria del conjunto palabras
# Definimos cuantos intentos tendrá el jugador para adivinar la palabra

palabras = {"PLATANO", "FRESA", "NARANJA", "NARANJA", "JICAMA", "SANDIA", "MELON"}
palabra_secreta = random.choice(list(palabras))
letras_adivinadas = []
intentos = 6




# ESTRUCTURA DEL JUEGO

def abrir_ventana_edicion():
    # Crear ventana secundaria
    ventana_edicion = tk.Toplevel(ventana)
    ventana_edicion.title("Editar mensaje")
    ventana_edicion.geometry("300x100")
    
    # Cuadro de texto
    tk.Label(ventana_edicion, text="Ingresa tu nombre:").pack(pady=5)
    entrada_nombre = tk.Entry(ventana_edicion, width=25)
    entrada_nombre.pack(pady=5)
    entrada_nombre.focus()
    
    # Botón para actualizar
    tk.Button(
        ventana_edicion,
        text="Actualizar",
        command=lambda: actualizar_mensaje(entrada_nombre.get(), ventana_edicion)
    ).pack(pady=5)

def actualizar_mensaje(nombre, ventana):
    if nombre.strip():  # Verificar que no esté vacío
        etiqueta.config(text=f"Hola {nombre.strip()} \n bienvenido al Juego del \n Ahorcado")
    ventana.destroy()  # Cerrar ventana de edición






def clickBotonPista():
    messagebox.showwarning("Pista", "Son Nombres de Frutas Tropicales")


def actualizar_pantalla():
    """Actualiza la palabra mostrada en guiones."""
    display = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            display += letra + " "
        else:
            display += "_ "
    etiqueta_palabra.config(text=display)

def verificar_letra():
    global intentos

    letra = entrada_letra.get().upper()
    entrada_letra.delete(0, tk.END)

    # Validaciones
    if len(letra) != 1 or not letra.isalpha():
        messagebox.showwarning("Error", "Introduce una sola letra válida.")
        return

    if letra in letras_adivinadas:
        messagebox.showinfo("Aviso", "Ya probaste esa letra.")
        return

    letras_adivinadas.append(letra)

    # Verificar si está en la palabra
    if letra in palabra_secreta:
        actualizar_pantalla()
        if all(l in letras_adivinadas for l in palabra_secreta):
            messagebox.showinfo("¡Ganaste!", f"Adivinaste la palabra: {palabra_secreta}")
    else:
        intentos -= 1
        etiqueta_intentos.config(text=f"Intentos restantes: {intentos}")

        if intentos == 0:
            messagebox.showerror("Derrota", f"Perdiste. La palabra era: {palabra_secreta}")




#   INTERFAZ DELJUEGO

ventana = tk.Tk()
ventana.title("Juego del Ahorcado")
ventana.geometry("500x500")
ventana.config(bg="lightblue")


# Etiqueta con mensaje inicial
etiqueta = tk.Label(
    ventana, 
    text="Cambia tu nombre \n para comenzar el juego", 
    font=("Patchwork Stitchlings", 9),
    pady=50
)
etiqueta.pack()

# Botón para abrir editor
tk.Button(
    ventana,
    text="Cambiar nombre",
    command=abrir_ventana_edicion
).pack()




botonPista = tk.Button(ventana, command=clickBotonPista, text="¿Quieres una pista antes de Jugar?, Da clik aqui")
botonPista.pack(pady=11)
# Palabra oculta
etiqueta_palabra = tk.Label(ventana, text="_ _ _ _ _", font=("Eyesis", 35))
etiqueta_palabra.pack(pady=20)
# Entrada de letra
tk.Label(ventana, text="Ingresa una letra:").pack()
entrada_letra = tk.Entry(ventana, font=("Sabotase", 35), width=5)
entrada_letra.pack(pady=5)
# Botón para verificar
boton_verificar = tk.Button(ventana, text="Probar letra", command=verificar_letra)
boton_verificar.pack(pady=10)
# Intentos
etiqueta_intentos = tk.Label(ventana, text=f"Intentos restantes: {intentos}")
etiqueta_intentos.pack()




actualizar_pantalla()
ventana.mainloop()

