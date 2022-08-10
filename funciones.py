from cgitb import text

from entidades import Circuito


equipos_pilotos = { 
                'FERRARI':'CARLOS SAINZ''CHARLES LECRECR', 
                'RED BULL':'MAX VERSTAPPEN''SERGIO PEREZ', 
                'MERCEDES': 'LEWIS HAMILTON''JORGE RUSSEL',
                'MCLARES': 'LANDO NORRIS''DANIEL RICCIARDO',
                'WILLIAMS': 'ALEX ALBON''NICOLAS LATIFI',
                'HAAS': 'MICK SCHUMACHER''KEVIN MAGNUSSEN',
                'ALPINE': 'FERNANDO ALONSO''ESTEBAN OCON',
                'ALPHA TAURI': 'PIERRE GASLY''YUKI TSUNODA', 
                'ALFA ROMEO': 'VALTERI BOTTAS''GUANYU SHOU',
                'ASTON MARTIN': 'SEBASTIAN VETTEL''LANCE STROLL'
                }

pilotos = [
    'CARLOS SAINZ',
    'CHARLES LECRECR',
    'MAX VERSTAPPEN',
    'SERGIO PEREZ',
    'LEWIS HAMILTON',
    'JORGE RUSSEL',
    'LANDO NORRIS',
    'DANIEL RICCIARDO',
    'ALEX ALBON',
    'NICOLAS LATIFI',
    'MICK SCHUMACHER',
    'KEVIN MAGNUSSEN',
    'FERNANDO ALONSO',
    'ESTEBAN OCON',
    'PIERRE GASLY',
    'YUKI TSUNODA',
    'VALTERI BOTTAS',
    'GUANYU SHOU',
    'SEBASTIAN VETTEL',
    'LANCE STROLL'
    ]

equipos = [
    'FERRARI',
    'RED BULL',
    'MERCEDES',
    'MCLAREN',
    'WILLIAMS',
    'HAAS',
    'ALPINE',
    'ALPHA TAURI',
    'ALFA ROMEO',
    'ASTON MARTIN'
    ]

circuitos = [
    'BAHRAIN'
    'JEDDAH',
    'ALBERT PARK',
    'IMOLA',
    'MIAMI',
    'CATALUÑA',
    'MONACO',
    'BAKU',
    'VILLENEUVE',
    'SILVERTONE',
    'RED BULL RING',
    'PAUL RICARD',
    'HUNGARORING',
    'SPA FRANCORCHAMPS',
    'ZANDVOORT',
    'MONZA',
    'MARINA BAY',
    'SAZUKA',
    'THE AMERICAS',
    'HERMANOS RODRIGUEZ',
    'JORGE CARLOS PACE',
    'YAS MARINA'
    ]

def menu ():
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

def pil_equ (equipos_pilotos):
    texto = ''
    for piloto_equipo in equipos_pilotos:
        texto += str(piloto_equipo) + '\n'
    return texto


def cir(circuitos):
    texto = ''
    for circuito in circuitos:
        texto += str(circuito) + '\n'
    return texto

def equ (equipos):
    texto = ''
    for equipo in equipos:
        texto += str(equipo) + '\n'
    return texto

def pil (pilotos):
    texto = ''
    for piloto in pilotos:
        texto += str(piloto) + '\n'
    return texto

def cal ():
    pass

def mi_equipo ():

        equipo = input('introduce tu equipo: ')
        equipo = equipo.upper()
        while True:
            if equipo in equipos:
                print(f'perfecto, has seleccionado la scuderia{equipo}')
                break
            else:
                print(f'incorrecto, la scuderia introducida {equipo} no exite')
                print(equ(equipos))
                equipo = input('introduce tu equipo: ')
                equipo = equipo.upper()

        piloto1 = input('introduce el piloto principal: ')
        piloto1 = piloto1.upper()

        while True:
            if piloto1 in pilotos:
                print(f'perfecto, has seleccionado a {piloto1} como piloto principal')
                break
            else:
                print(f'incorrecto, el piloto {piloto1} no exite')
                print(pil(pilotos))
                piloto1 = input('introduce el piloto principal: ')
                piloto1 = piloto1.upper()
        
        piloto2 = input('introduce el piloto secundario: ')
        piloto2 = piloto2.upper()

        while True:
            if piloto2 in pilotos:
                print(f'perfecto, has seleccionado a {piloto2} como piloto principal')
                break
            else:
                print(f'incorrecto, el piloto {piloto2} no exite')
                print(pil(pilotos))
                piloto2 = input('introduce el piloto principal: ')
                piloto2 = piloto2.upper()

        print(
            '-------------------------\n'
            f'equipo: {equipo}\n'
            f'piloto1: {piloto1}\n'
            f'piloto2: {piloto2}\n'
            '-------------------------'
        )