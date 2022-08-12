# importamos text para imprimir los datos de forma mas ordenada
from cgitb import text

# diccionario con todos los equipos y sus pilotos
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

# lista con todos los pilotos 
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

# lista con todos los equipos 
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

# lista con todos los circuitos
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

# funcion pil_equ (equipos y pilotos)
def pil_equ (equipos_pilotos):
    # imprimimos todos los equipos con sus pilotos de manera prolija usando text
    texto = ''
    for piloto_equipo in equipos_pilotos:
        texto += str(piloto_equipo) + '\n'
    return texto

# funcion cir (circuitos)
def cir(circuitos):
    # imprimimos todos los circuitos de manera prolija usando text
    texto = ''
    for circuito in circuitos:
        texto += str(circuito) + '\n'
    return texto

# funcion equ (equipos)
def equ (equipos):
    # imprimimos todos los equipos de manera prolija usando text
    texto = ''
    for equipo in equipos:
        texto += str(equipo) + '\n'
    return texto

# funcion pil (pilotos)
def pil (pilotos):
    # imprimimos todos los pilotos de manera prolija usando text
    texto = ''
    for piloto in pilotos:
        texto += str(piloto) + '\n'
    return texto

# funcion cal (calendario)
def cal ():
    pass

# funcion mi_equipo
def mi_equipo ():
        # pedimos al user que equipo quiere usar
        equipo = input('introduce tu equipo: ')
        # convertimos equipo a mayusculas para que no salga error al buscarlo en la lista
        equipo = equipo.upper()
        # bucle infinito hasta que se introduzca un equipo valido
        while True:
            # analizamos si existe ese equipo
            if equipo in equipos:
                # mensaje informativo indicando que se selecciono correctamente
                print(f'perfecto, has seleccionado la scuderia{equipo}')
                # salimos del bucle
                break
            else:
                # mensaje informativo indicando que no existe ese equipo
                print(f'incorrecto, la scuderia introducida {equipo} no exite')
                # mostramos los equipos disponibles
                print(equ(equipos))
                # pedimos el equipo al user de vuelta
                equipo = input('introduce tu equipo: ')
                # convertimos a mayusculas el equipo
                equipo = equipo.upper()

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
                # mostramos los pilotos disponibles
                print(pil(pilotos))
                # pedimos el piloto al user de vuelta
                piloto2 = input('introduce el piloto principal: ')
                # convertimos a mayusculas el piloto2
                piloto2 = piloto2.upper()

        # imprimimos toda la informacion
        print(
            '-------------------------\n'
            f'equipo: {equipo}\n'
            f'piloto1: {piloto1}\n'
            f'piloto2: {piloto2}\n'
            '-------------------------'
        )