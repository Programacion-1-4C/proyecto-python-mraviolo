# importamos text para imprimir los datos de forma mas ordenada
from cgitb import text

# importamos las clases 
from entidades import * 

# diccionario con el calendario de la F1
calendario = [
    Calendario('BAHRAIN','20/03/2022', '12:00 AM'),
    Calendario('JEDDAH', '27/03/2022', '14:00 PM'),
    Calendario('ALBERT PARK', '10/04/2022', '02:00 AM'),
    Calendario('IMOLA', '24/04/2022', '10:00 AM'),
    Calendario('MIAMI', '08/05/2022', '16:30 PM'),
    Calendario('CATALUÑA', '22/05/2022', '10:00 AM'),
    Calendario('MONACO', '29/05/2022', '10:00 AM'),
    Calendario('BAKU', '12/06/2022', '08:00 AM'),
    Calendario('VILLENEUVE', '19/06/2022', '15:00 PM'),
    Calendario('SILVERTONE', '03/07/2022', '11:00 AM'),
    Calendario('RED BULL RING', '10/07/2022', '10:00 AM'),
    Calendario('PAUL RICARD', '24/07/2022', '10:00 AM'),
    Calendario('HUNGARORING', '31/07/2022', '10:00 AM'),
    Calendario('SPA FRANCORCHAMPS', '28/08/2022', '10:00 AM'),
    Calendario('ZANDVOORT', '04/09/2022', '10:00 AM'),
    Calendario('MONZA', '11/09/2022', '10:00 AM'),
    Calendario('MARINA BAY', '02/10/2022', '09:00 AM'),
    Calendario('SAZUKA', '09/10/2022', '02:00 AM'),
    Calendario('THE AMERICAS', '23/10/2022', '16:00 PM'),
    Calendario('HERMANOS RODRIGUEZ', '30/10/2022', '15:00 PM'),
    Calendario('JORGE CARLOS PACE', '13/11/2022', '15:00 PM'),
    Calendario('YAS MARINA', '20/11/2022', '10:00 AM')
]

# lista con todos los pilotos 
pilotos = [
    Piloto('CARLOS SAINZ', '27', 'España, Madrid', 'Ferrari'),
    Piloto('CHARLES LECRECR', '24', 'Monaco, Montecarlo', 'Ferrari'),
    Piloto('MAX VERSTAPPEN', '24', 'Belgica, Hasselt', 'Red Bull'),
    Piloto('SERGIO PEREZ', '32', 'Mexico, Guadalajara', 'Red Bull'),
    Piloto('LEWIS HAMILTON', '37', 'Reino Unido, Stevenage', 'Mercedes'),
    Piloto('GEORGE RUSSEL', '24', 'Reino Unido, Kings Lynn', 'Mercedes'),
    Piloto('LANDO NORRIS', '22', 'Reino Unido, Bristol', 'McLaren'),
    Piloto('DANIEL RICCIARDO', '33', 'Australia, Perth', 'McLaren'),
    Piloto('ALEX ALBON', '26', 'Reino Unido, Londres', 'Williams'),
    Piloto('NICOLAS LATIFI', '27', 'Canada, Montreal', 'Williams'),
    Piloto('MICK SCHUMACHER', '23', 'Suiza, Genolier', 'Haas'),
    Piloto('KEVIN MAGNUSSEN', '29', 'Dinamarca, Roskilde', 'Hass'),
    Piloto('FERNANDO ALONSO', '41', 'España, Oviedo', 'Alpine'),
    Piloto('ESTEBAN OCON', '25', 'Francia, Evreux', 'Alpine'),
    Piloto('PIERRE GASLY', '26', 'Francia, Ruan', 'Alpha Tauri'),
    Piloto('YUKI TSUNODA', '22', 'Japon, Sagamihara', 'Alpha Tauri'),
    Piloto('VALTERI BOTTAS', '32', 'Finlandia, Nastola', 'Alfa Romeo'),
    Piloto('GUANYU ZHOU', '23', 'China, Shanghai', 'Alfa Romeo'),
    Piloto('SEBASTIAN VETTEL', '35', 'Alemania, Happenheim', 'Aston Martin'),
    Piloto('LANCE STROLL', '23', 'Canada, Montreal', 'Aston Martin')
]

# lista con todos los equipos 
equipos = [
    Equipo('FERRARI', '', 'Charles Lecrecr / Carlos Sainz'),
    Equipo('RED BULL', '', 'Max Verstappen / Sergio Perez'),
    Equipo('MERCEDES', '', 'Lewis Hamilton / George Russel'),
    Equipo('MCLAREN', '', 'Lando Norris / Daniel Ricciardo'),
    Equipo('WILLIAMS', '', 'Nicolas Latifi / Alex Albon'),
    Equipo('HAAS', '', 'Kevin Magnussen / Mich Schumacher'),
    Equipo('ALPINE', '', 'Fernando Alonso / Esteban Ocon'),
    Equipo('ALPHA TAURI', '', 'Pierre Gasly / Tuki Tsunoda'),
    Equipo('ALFA ROMEO', '', 'Valteri Bottas / Guanyu Zhou'),
    Equipo('ASTON MARTIN', '', 'Sebastian Vettel / Lance Stroll')
]

# lista con todos los circuitos
circuitos = [
    Circuito('BAHRAIN', '5,412 km', 'Bahrain'),
    Circuito('JEDDAH', '6.175 km', 'Arabia Saudi'),
    Circuito('ALBERT PARK', '5.303 km', 'Australia'),
    Circuito('IMOLA', '4,909 km', 'Italia'),
    Circuito('MIAMI', '5,400 km', 'Estados Unidos'),
    Circuito('CATALUÑA', '4,675 km', 'España'),
    Circuito('MONACO', '3,337 km', 'Monaco'),
    Circuito('BAKU', '6,003 km', 'Azerbaiyan'),
    Circuito('VILLENEUVE', '4,361 km', 'Canada'),
    Circuito('SILVERTONE', ' 5.901 km', 'Reino Unido'),
    Circuito('RED BULL RING', '4,318 km', 'Austria'),
    Circuito('PAUL RICARD', '5,842 km', 'Francia'),
    Circuito('HUNGARORING', '4,381 km', 'Hungria'),
    Circuito('SPA FRANCORCHAMPS', '7.004 km', 'Belgica'),
    Circuito('ZANDVOORT', '4,307 km', 'Paises Bajos'),
    Circuito('MONZA', '5,793 km', 'Italia'),
    Circuito('MARINA BAY', '5,065 km', 'Singapur'),
    Circuito('SAZUKA', '5,807 km', 'Japon'),
    Circuito('THE AMERICAS', '5,513 km', 'Estados Unidos'),
    Circuito('HERMANOS RODRIGUEZ', '4,304 km', 'Mexico'),
    Circuito('JORGE CARLOS PACE', '4.309 metros', 'Brasil'),
    Circuito('YAS MARINA', '5,281 km', 'Abu Dabi')
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
        texto += str((equipo.nombre) + ': ' + (equipo.historia)) + '\n'
    return texto

def equ3 (equipos):
    # imprimimos todos los equipos de manera prolija usando text
    texto = ''
    for equipo in equipos:
        texto += str((equipo.nombre) + ': ' + (equipo.pilotos)) + '\n'
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
        texto += str((piloto.nombre) +  ': ' + (piloto.edad) + ' ' + (piloto.pais)) + '\n'
    return texto

def pil3 (pilotos):
    # imprimimos todos los pilotos de manera prolija usando text
    texto = ''
    for piloto in pilotos:
        texto += str((piloto.nombre) + ': ' + (piloto.equipo)) + '\n'
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