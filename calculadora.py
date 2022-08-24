# importamos la libreria de tkinter (interfaz)
from tkinter import *
from math import *

# funcion para escribir el numero con los botones
def escribir_botones(num):
    global operador
    operador = operador+str(num)
    input_text.set(operador)

# funcion de operacion
def operacion():
    global operador
    try:
        opera = eval(operador)
    except:
        limpiar()
        opera = 'ERROR'
    input_text.set(opera)

# funcion para limpiar la pantalla
def limpiar():
    global operador
    operador = ''
    input_text.set(operador)

#creamos la ventana
root = Tk()  
#configuracion de la calculadora
root.title('calculadora')
root.resizable(False,False)
root.geometry('392x600')

#creamos las variables para la funcion escribir_botones
input_text = StringVar()
operador = ''

#creamos las partes de la calculadora
#hacemos la salida de la calculado
salida = Entry(root,font=('arial', 20), width=23,textvariable=input_text, bd=10, justify='left', bg='powder blue').place(x=10, y=60)
 
#creamos los botones
ancho_boton = 5
alto_boton = 3

#primer fila
boton0 = Button(root, width=ancho_boton, height=alto_boton, text='0', command=lambda:escribir_botones(0)).place(x=17, y=120)
boton1 = Button(root, width=ancho_boton, height=alto_boton, text='1', command=lambda:escribir_botones(1)).place(x=107, y=120)
boton2 = Button(root, width=ancho_boton, height=alto_boton, text='2', command=lambda:escribir_botones(2)).place(x=197, y=120)
boton3 = Button(root, width=ancho_boton, height=alto_boton, text='3', command=lambda:escribir_botones(3)).place(x=287, y=120)

#seunda fila
boton4 = Button(root, width=ancho_boton, height=alto_boton, text='4', command=lambda:escribir_botones(4)).place(x=17, y=200)
boton5 = Button(root, width=ancho_boton, height=alto_boton, text='5', command=lambda:escribir_botones(5)).place(x=107, y=200)
boton6 = Button(root, width=ancho_boton, height=alto_boton, text='6', command=lambda:escribir_botones(6)).place(x=197, y=200)
boton7 = Button(root, width=ancho_boton, height=alto_boton, text='7', command=lambda:escribir_botones(7)).place(x=287, y=200)

#tercer fila
boton8 = Button(root, width=ancho_boton, height=alto_boton, text='8', command=lambda:escribir_botones(8)).place(x=17, y=280)
boton9 = Button(root, width=ancho_boton, height=alto_boton, text='9', command=lambda:escribir_botones(9)).place(x=107, y=280)
botonpi = Button(root, width=ancho_boton, height=alto_boton, text='π', command=lambda:escribir_botones('pi')).place(x=197, y=280)
botonpunto = Button(root, width=ancho_boton, height=alto_boton, text='.', command=lambda:escribir_botones('.')).place(x=287, y=280)

#cuarta fila
botonsuma = Button(root, width=ancho_boton, height=alto_boton, text='+', command=lambda:escribir_botones('+')).place(x=17, y=360)
botonresta = Button(root, width=ancho_boton, height=alto_boton, text='-', command=lambda:escribir_botones('-')).place(x=107, y=360)
botonmult = Button(root, width=ancho_boton, height=alto_boton, text='*', command=lambda:escribir_botones('*')).place(x=197, y=360)
botondiv = Button(root, width=ancho_boton, height=alto_boton, text='/', command=lambda:escribir_botones('/')).place(x=287, y=360)

#quinta fila
botonraiz = Button(root, width=ancho_boton, height=alto_boton, text='√', command=lambda:escribir_botones('sqrt')).place(x=17, y=440)
botonlimpiar = Button(root, width=ancho_boton, height=alto_boton, text='C', command=limpiar).place(x=107, y=440)
botonpotencia = Button(root, width=ancho_boton, height=alto_boton, text='EXP', command=lambda:escribir_botones('**')).place(x=197, y=440)
botonigual = Button(root, width=ancho_boton, height=alto_boton, text='=', command=operacion).place(x=287, y=440)

#sexta fila
botonparentesis1 = Button(root, width=ancho_boton, height=alto_boton, text='(', command=lambda:escribir_botones('(')).place(x=17, y=520)
botonparentesis2 = Button(root, width=ancho_boton, height=alto_boton, text=')', command=lambda:escribir_botones(')')).place(x=107, y=520)
botonporcentaje = Button(root, width=ancho_boton, height=alto_boton, text='%', command=lambda:escribir_botones('%')).place(x=197, y=520)
botonIn = Button(root, width=ancho_boton, height=alto_boton, text='In', command=lambda:escribir_botones('log')).place(x=287, y=520)

#cerramos la ventana
root.mainloop()