from funciones import *
from tkinter import *   

while True:

    menu()

    operacion = int(input('>>> '))

    if operacion == 1:
        print(cir(circuitos))
        print(
            '1) ver imagen del circuito\n'
            '2) ver infomacion del circuito'
        )
        operacion = int(input('>>> '))
        if operacion == 1:
            pass
        elif operacion == 2:
            pass

    elif operacion == 2:
        print(equ(equipos))
        print(
            '1) ver historia de la escuderia\n'
            '2) ver los pilotos que pertenecen a la escuderia'
        )
        operacion = int(input('>>> '))
        if operacion == 1:
            pass
        elif operacion == 2:
            print(pil_equ(equipos_pilotos))

    elif operacion == 3:
        print(pil(pilotos))
        print(
            '1) ver informacion personal del piloto\n'
            '2) ver escuderias a las que pertenecen'
        )
        operacion = int(input('>>> '))
        if operacion == 1:
            pass
        elif operacion == 2:
            print(pil_equ(equipos_pilotos))

    elif operacion == 4:
        pass
    
    elif operacion == 5:
        print(mi_equipo())
    
    elif operacion == 6:
        break
    
    else:
        print('valor incorrecto')