import tkinter as tk



def mover_arriba():
    canvas.move(cuadro, -10, -10)
    canvas.move(circulo, 0, 0)

def mover_abajo():
    canvas.move(cuadro, -20, -20)
    canvas.move(circulo, 0, 0)

def mover_izquierda():
    canvas.move(cuadro, 0, 0)
    canvas.move(circulo, 0, 0)

def mover_derecha():
    canvas.move(cuadro, -30, -30)
    canvas.move(circulo, 0, 0)




ventana = tk.Tk()
ventana.title("Casita")


canvas = tk.Canvas(ventana, width=500, height=300, bg="blue")
canvas.pack()


cuadro = canvas.create_rectangle(0, 0, 150, 150, outline="black", fill="brown")

circulo = canvas.create_oval(170, 50, 270, 150, outline="yellow", fill="yellow")
circulo2 = canvas.create_oval(120, 0, 80, 150, outline="yellow", fill="yellow")

triangulo = canvas.create_polygon(100, 100, 50, 300, 150, 300, fill="green")



ventana.mainloop()