# importamos las funciones
from funciones import *

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
            '1) ver imagen del circuito\n'
            '2) ver infomacion del circuito\n'
            '3) volver'
        )
        # pedimos al user si quiere hacer alguna de esas operaciones
        operacion = int(input('>>> '))
        # opcion 1
        if operacion == 1:
            pass
        # opcion 2
        elif operacion == 2:
            pass

    # opcion 2
    elif operacion == 2:
        # imprimimos todos los equipos 
        # llamamos a la funcion equ
        print(equ(equipos))
        # opciones de equipos
        print(
            '1) ver historia de la escuderia\n'
            '2) ver los pilotos que pertenecen a la escuderia\n'
            '3) volver'
        )
        # pedimos al user si quiere hacer alguna de esas operaciones
        operacion = int(input('>>> '))
        # opcion 1
        if operacion == 1:
            pass
        # opcion 2
        elif operacion == 2:
            # imprimimos los equipos con sus respectivos pilotos
            # llamamos la funcion pil_equ
            print(pil_equ(equipos_pilotos))

    # opcion 3
    elif operacion == 3:
        # imprimimos todos los pilotos
        # llamamos a la funcion pil
        print(pil(pilotos))
        # opciones de pilotos
        print(
            '1) ver informacion personal del piloto\n'
            '2) ver escuderias a las que pertenecen\n'
            '3) volver'
        )
        # pedimos al user si quiere hacer alguna de esas operaciones
        operacion = int(input('>>> '))
        # opcion 1
        if operacion == 1:
            pass
        # opcion 2
        elif operacion == 2:
            # imprimimos los pilotos con sus respectivos equipos
            # llamamos a la funcion pil_equ
            print(pil_equ(equipos_pilotos))

    # opcion 4
    elif operacion == 4:
        # imprimimos el calendario de la F1
        # llamamos a la funcion cal
        print(cal(calendario))
    
    # opcion 5
    elif operacion == 5:
        # imprimimos su equipo armado por el
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