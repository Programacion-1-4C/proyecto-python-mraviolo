# importamos text para imprimir los datos de forma mas ordenada
from cgitb import text

# importamos las clases 
from entidades import * 
from informacion import *

# funcion menu
def menu ():
    # mensaje informativo para el user
    # todas las opciones que tiene para hacer
    print(
        '-------------------------------------------------------------------------\n'
        '-Hola, esta es una app que te va mostrar toda la informacion sobre la F1-\n'
        '-------------------------------------------------------------------------\n'
        '1) circuitos\n'
        '2) equipos\n'
        '3) pilotos \n'
        '4) calendario \n'
        '5) mi equipo \n'
        '6) salir'
    )

# funcion cir (circuitos)
def cir(circuitos):
    # imprimimos todos los circuitos de manera prolija usando text
    texto = ''
    for circuito in circuitos:
        texto += str(circuito.nombre) + '\n'
    return texto

def cir2(circuitos):
    # imprimimos todos los circuitos de manera prolija usando text
    texto = ''
    for circuito in circuitos:
        texto += str((circuito.nombre) + ': ' + (circuito.longitud) + ' ' + (circuito.pais)) + '\n'
    return texto

# funcion equ (equipos)
def equ (equipos):
    # imprimimos todos los equipos de manera prolija usando text
    texto = ''
    for equipo in equipos:
        texto += str(equipo.nombre) + '\n'
    return texto

def equ2 (equipos):
    # imprimimos todos los equipos de manera prolija usando text
    texto = ''
    for equipo in equipos:
        texto += str((equipo.nombre) + ': ' + '\n' + (equipo.historia)) + '\n \n'
    return texto

def equ3 (equipos):
    # imprimimos todos los equipos de manera prolija usando text
    texto = ''
    for equipo in equipos:
        texto += str((equipo.nombre) + ': ' + (equipo.pilotos)) + '\n'
    return texto

def equ4 (equipos):
    # imprimimos todos los equipos de manera prolija usando text
    texto = ''
    for equipo in equipos:
        texto += str((equipo.nombre) + ': ' + (equipo.ganados)) + '\n'
    return texto

def equ5 (equipos):
    # imprimimos todos los equipos de manera prolija usando text
    texto = ''
    for equipo in equipos:
        texto += str((equipo.nombre) + ': ' + (equipo.director)) + '\n'
    return texto  

# funcion pil (pilotos)
def pil (pilotos):
    # imprimimos todos los pilotos de manera prolija usando text
    texto = ''
    for piloto in pilotos:
        texto += str(piloto.nombre) + '\n'
    return texto

def pil2 (pilotos):
    # imprimimos todos los pilotos de manera prolija usando text
    texto = ''
    for piloto in pilotos:
        texto += str((piloto.nombre) + ': ' + (piloto.edad) + ' ' + (piloto.pais)) + '\n'
    return texto

def pil3 (pilotos):
    # imprimimos todos los pilotos de manera prolija usando text
    texto = ''
    for piloto in pilotos:
        texto += str((piloto.nombre) + ': ' + (piloto.equipo)) + '\n'
    return texto

def pil4 (pilotos):
    # imprimimos todos los pilotos de manera prolija usando text
    texto = ''
    for piloto in pilotos:
        texto += str((piloto.nombre) + ': ' + (piloto.ganados)) + '\n'
    return texto  


# funcion cal (calendario)
def cal (calendario):
    # imprimos el calendario de la F1 de manera prolija usando text
    texto = ''
    for carrera in calendario:
        texto += str(carrera) + '\n'
    return texto

# funcion mi_equipo
def mi_equipo ():
    equipo = buscar_elemento(equipos, equ)

    piloto1 = buscar_elemento(pilotos, pil)

    piloto2 = buscar_elemento(pilotos, pil)

    # calculamos el porcentaje
    porcentaje = (piloto1.puntaje + piloto2.puntaje + equipo.puntaje) / 3
    # imprimimos toda la informacion
    print(
        '-------------------------\n'
        f'equipo: {equipo.nombre}\n'
        f'piloto1: {piloto1.nombre}\n'
        f'piloto2: {piloto2.nombre}\n'
        f'puntaje: {porcentaje}\n'
        '-------------------------'
    )


def buscar_elemento(elementos, fun):
    # bucle infinito hasta que se introduzca un equipo valido
    while True:
        # pedimos al user que equipo quiere usar
        buscado = input('introduce tu equipo: ').upper()
        # analizamos si existe ese equipo
        for elemento in elementos:
            if buscado == elemento:
                # mensaje informativo indicando que se selecciono correctamente
                print(f'perfecto, has seleccionado la scuderia{buscado}')
                # salimos del bucle
                return elemento
        else:
            # mensaje informativo indicando que no existe ese equipo
            print(f'incorrecto, la scuderia introducida {buscado} no exite')
            print('los equipos disponibles son: ')
            # mostramos la lista con fun
            print(fun(elementos))
        
"""
    # pedimos al user que piloto principal quiere usar
    piloto1 = input('introduce el piloto principal: ')
    # convertimos piloto1 a mayusculas para que no salga error al buscarlo en la lista
    piloto1 = piloto1.upper()
    # bucle infinito hasta que se introduzca un piloto valido
    while True:
        # analizamos si existe ese piloto
        if piloto1 in pilotos:
            # mensaje informativo indicando que se selecciono correctamente
            print(f'perfecto, has seleccionado a {piloto1} como piloto principal')
            # salimos del bucle
            break
        else:
            # mensaje informativo indicando que no exite ese piloto
            print(f'incorrecto, el piloto {piloto1} no exite')
            print('los pilotos disponibles son: ')
            # mostramos los pilotos disponibles
            print(pil(pilotos))
            # pedimos el piloto al user de vuelta
            piloto1 = input('introduce el piloto principal: ')
            # convertimos a mayusculas el piloto1
            piloto1 = piloto1.upper()

    # pedimos al user que piloto secundario quiere usar
    piloto2 = input('introduce el piloto secundario: ')
    # convertimos piloto2 a mayusculas para que no salga error al buscarlo en la lista
    piloto2 = piloto2.upper()
    # bucle infinito hasta que se introduzca un piloto valido
    while True:
        # analizamos si existe ese piloto
        if piloto2 in pilotos:
            # mensaje informativo indicando que se selecciono correctamente
            print(f'perfecto, has seleccionado a {piloto2} como piloto principal')
            # salimos del bucle
            break
        else:
            # mensaje informativo indicando que no exite ese piloto
            print(f'incorrecto, el piloto {piloto2} no exite')
            print('los pilotos disponibles son: ')
            # mostramos los pilotos disponibles
            print(pil(pilotos))
            # pedimos el piloto al user de vuelta
            piloto2 = input('introduce el piloto principal: ')
            # convertimos a mayusculas el piloto2
            piloto2 = piloto2.upper()
"""