# mateo raviolo
# importamos las funciones
from funciones import *
from tkinter import Tk

# bucle infinito para ejecutar el programa
while True:
    # llamamos a la funcion menu
    menu()

    # pedimos al user que quiere hacer
    operacion = int(input('>>> '))
 
    # analizamos la operacion
    # opcion 1
    if operacion == 1:
        # imprimimos todos los circuitos
        # llamamos a la funcion cir
        print(cir(circuitos))
        # opciones de circuitos
        print(
            '1) ver descripcion\n'
            '2) ver imagen\n'
            '3) volver\n'
        )
 
        # pedimos al user si quiere hacer alguna de esas operaciones
        operacion = int(input('>>> '))
 
        # opcion 1
        if operacion == 1:
            print(cir2(circuitos))
 
        # opcion 2
        elif operacion == 2:
            print('no se ha cargado una imagen')

        # opcion 3
        elif operacion == 3:
            pass

    # opcion 2
    elif operacion == 2:
        # imprimimos todos los equipos 
        # llamamos a la funcion equ
        print(equ(equipos))
        # opciones de equipos
        print(
            '1) ver historia de los equipos\n'
            '2) ver pilotos del equipo\n'
            '3) ver campeonatos ganados\n'
            '4) ver director \n'
            '5) ver imagen\n'
            '6) volver\n'
        )
 
        # pedimos al user si quiere hacer alguna de esas operaciones
        operacion = int(input('>>> '))
 
        # opcion 1
        if operacion == 1:
            print(equ2(equipos))
 
        # opcion 2
        elif operacion == 2:
            print(equ3(equipos))
 
        # opcion 3
        elif operacion == 3:
            print(equ4(equipos))
 
        # opcion 4
        elif operacion == 4:
            print(equ5(equipos))
 
        # opcion 5
        elif operacion == 5:
            print('no se ha cargado una imagen')

        # opcion 6
        elif operacion == 6:
            pass
            

    # opcion 3
    elif operacion == 3:
        # imprimimos todos los pilotos
        # llamamos a la funcion pil
        print(pil(pilotos))
        # opciones de pilotos
        print(
            '1) ver informacion personal del piloto\n'
            '2) ver escuderias a las que pertenecen\n'
            '3) ver su estadisticas\n'
            '4) ver imagen\n'
            '5) volver\n'
        )
 
        # pedimos al user si quiere hacer alguna de esas operaciones
        operacion = int(input('>>> '))
 
        # opcion 1
        if operacion == 1:
            print(pil2(pilotos))
 
        # opcion 2
        elif operacion == 2:
            print(pil3(pilotos))
 
        # opcion 3
        elif operacion == 3:
            print(pil4(pilotos))
 
        # opcion 4
        elif operacion == 4:
            print('no se ha cargado una imagen')

        # opcion 5
        elif operacion == 5:
            pass

    # opcion 4
    elif operacion == 4:
        # imprimimos el calendario de la F1
        # llamamos a la funcion cal
        print(cal(calendario))
    
    # opcion 5
    elif operacion == 5:
        # mensaje informativo
        print('necesitamos que ingreses un equipo, piloto1 y piloto2')
        print(
            '-------------------------\n'
            f'equipo: \n'
            f'piloto1: \n'
            f'piloto2: \n'
            '-------------------------'
        )
        # llamamos a la funcion mi_equipo
        print(mi_equipo())

    # opcion 6
    elif operacion == 6:
        # cerramos el programa
        break
    
    # ninguna de las opciones
    else:
        # mensaje de opcion no disponible para el user
        print('valor incorrecto')