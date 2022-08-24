# importamos la clases
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
    Piloto('CARLOS SAINZ', '27', 'España, Madrid', 'Ferrari', '(1) victoria / (12) podios / (1) pole / (0) campeonatos', 8),
    Piloto('CHARLES LECRECR', '24', 'Monaco, Montecarlo', 'Ferrari', '(5) victoria / (18) podios / (16) pole / (0) campeonatos', 9),
    Piloto('MAX VERSTAPPEN', '24', 'Belgica, Hasselt', 'Red Bull', '(28) victoria / (70) podios / (16) pole / (1) campeonatos', 10),
    Piloto('SERGIO PEREZ', '32', 'Mexico, Guadalajara', 'Red Bull', '(3) victoria / (21) podios / (1) pole / (0) campeonatos', 9),
    Piloto('LEWIS HAMILTON', '37', 'Reino Unido, Stevenage', 'Mercedes', '(103) victoria / (188) podios / (103) pole / (7) campeonatos', 10),
    Piloto('GEORGE RUSSEL', '24', 'Reino Unido, Kings Lynn', 'Mercedes', '(0) victoria / (6) podios / (1) pole / (0) campeonatos', 6),
    Piloto('LANDO NORRIS', '22', 'Reino Unido, Bristol', 'McLaren', '(0) victoria / (6) podios / (1) pole / (0) campeonatos', 6),
    Piloto('DANIEL RICCIARDO', '33', 'Australia, Perth', 'McLaren', '(8) victoria / (32) podios / (3) pole / (0) campeonatos', 8),
    Piloto('ALEX ALBON', '26', 'Reino Unido, Londres', 'Williams', '(0) victoria / (2) podios / (0) pole / (0) campeonatos', 3),
    Piloto('NICOLAS LATIFI', '27', 'Canada, Montreal', 'Williams', '(0) victoria / (0) podios / (0) pole / (0) campeonatos', 1),
    Piloto('MICK SCHUMACHER', '23', 'Suiza, Genolier', 'Haas', '(0) victoria / (0) podios / (0) pole / (0) campeonatos', 6),
    Piloto('KEVIN MAGNUSSEN', '29', 'Dinamarca, Roskilde', 'Hass', '(0) victoria / (1) podios / (0) pole / (0) campeonatos', 7),
    Piloto('FERNANDO ALONSO', '41', 'España, Oviedo', 'Alpine', '(32) victoria / (98) podios / (22) pole / (2) campeonatos', 10),
    Piloto('ESTEBAN OCON', '25', 'Francia, Evreux', 'Alpine', '(1) victoria / (2) podios / (0) pole / (0) campeonatos', 5),
    Piloto('PIERRE GASLY', '26', 'Francia, Ruan', 'Alpha Tauri', '(1) victoria / (3) podios / (0) pole / (0) campeonatos', 6),
    Piloto('YUKI TSUNODA', '22', 'Japon, Sagamihara', 'Alpha Tauri', '(0) victoria / (0) podios / (0) pole / (0) campeonatos', 4),
    Piloto('VALTERI BOTTAS', '32', 'Finlandia, Nastola', 'Alfa Romeo', '(10) victoria / (67) podios / (20) pole / (0) campeonatos', 9),
    Piloto('GUANYU ZHOU', '23', 'China, Shanghai', 'Alfa Romeo', '(0) victoria / (0) podios / (0) pole / (0) campeonatos', 4),
    Piloto('SEBASTIAN VETTEL', '35', 'Alemania, Happenheim', 'Aston Martin', '(53) victoria / (122) podios / (57) pole / (4) campeonatos', 10),
    Piloto('LANCE STROLL', '23', 'Canada, Montreal', 'Aston Martin', '(0) victoria / (3) podios / (1) pole / (0) campeonatos', 4)
]

# lista con todos los equipos 
equipos = [
    Equipo('FERRARI', 'La primera participación de Ferrari en Fórmula 1 fue en el Gran Premio de Mónaco de 1950, con el Tipo 125 F1. Ferrari es considerado uno de los cuatro grandes equipos de Fórmula 1. Ha contado con muchos de los pilotos más destacados de la historia de la Fórmula 1 como Michael Schumacher, Niki Lauda, Juan Manuel Fangio,Alberto Ascari, Alain Prost, Nigel Mansell, Carlos Reutemann, Gilles Villeneuve, Kimi Räikkönen, Sebastian Vettel y Fernando Alonso', 'Charles Lecrecr / Carlos Sainz', '(16) constructores / (15) pilotos / (773) podios / (240) victorias', 'Mattia Binotto', 10),
    Equipo('RED BULL', 'Red Bull Racing es una escudería austriaca de Fórmula 1 con base en Milton Keynes (Inglaterra), propiedad de la empresa de bebidas energéticas Red Bull. La compañía adquirió la escudería Jaguar Racing por cerca de 110 millones de dólares cuando la propietaria anterior de este equipo, Ford Motor Company, anunció su retirada de la máxima categoría del automovilismo. La empresa Red Bull posee un equipo filial de Fórmula 1, Scuderia AlphaTauri (conocida hasta 2019 como Scuderia Toro Rosso), con sede en Faenza (Italia), desde el que los jóvenes pilotos dan posteriormente el salto al primer equipo. Compite desde 2005 y en sus dos primeras temporadas corrió con licencia británica.', 'Max Verstappen / Sergio Perez', '(4) constructores / (5) pilotos / (221) podios / (84) victorias', 'Christian Horner', 9),
    Equipo('MERCEDES', 'Mercedes-Benz es una de las automotrices más exitosas de la Fórmula 1, considerada uno de los cuatro equipos con mejores resultados, junto con Williams, Ferrari y McLaren. Participó inicialmente como constructor en Fórmula 1 en 1954 y 1955, y volvió a hacerlo desde 2010 hasta la actualidad.', 'Lewis Hamilton / George Russel', '(8) constructores / (9) pilotos / (263) podios / (124) victorias', 'Torger Christian Wolff', 9),
    Equipo('MCLAREN', 'McLaren Racing Limited, conocida generalmente como McLaren, es una escudería británica de automovilismo con sede en Woking (Surrey, Inglaterra), fundada en 1963 por Bruce McLaren. Es considerado uno de los cuatro grandes equipos de Fórmula 1. ', 'Lando Norris / Daniel Ricciardo', '(12) constructores / (8) pilotos / (489) podios / (183) victorias', 'Zak Brown', 8),
    Equipo('WILLIAMS', 'Williams Grand Prix Engineering, comúnmente conocido como Williams, es un equipo de Fórmula 1 creado en 1977 por Frank Williams y Patrick Head. Es considerado uno de los cuatro grandes equipos de Fórmula 1, junto con Ferrari, McLaren y Mercedes. Ha ganado 9 campeonatos de constructores y 7 campeonatos de pilotos.', 'Nicolas Latifi / Alex Albon', '(9) constructores / (7) pilotos / (302) podios / (114) victorias', 'Simon Roberts', 3),
    Equipo('HAAS', 'Haas es la escudería más joven de la parrilla. Se constituyó en 2014 y empezó a competir en 2016. Debutó con un acuerdo de colaboración técnica con Dallara -que produjo su primer chasis- y Ferrari -que les permitió aprovechar algunos de sus componentes y recursos tecnológicos.', 'Kevin Magnussen / Mich Schumacher', '(0) constructores / (0) pilotos / (0) podios / (0) victorias', 'Guenther Steiner', 5),
    Equipo('ALPINE', 'Es propiedad de Renault, que compitió en la categoría reina bajo ese nombre hasta 2020. La marca Alpine, de coches deportivos y de competición, la fundó Jean Rédélé en 1955. La compañía cosechó una gran éxito con la comercialización del cupé deportivo A110, lanzado en 1961.', 'Fernando Alonso / Esteban Ocon', '(0) constructores / (0) pilotos / (2) podios / (1) victorias', 'Otmar Szafnauer', 6),
    Equipo('ALPHA TAURI', ' Es una escudería de Fórmula 1 que surgió a finales de 2005, después de la compra de la escudería Minardi por parte de Red Bull. Actuaba como equipo filial del equipo Red Bull Racing, formando jóvenes promesas para dar el salto a la escudería "madre"', 'Pierre Gasly / Tuki Tsunoda', '(0) constructores / (0) pilotos / (2) podios / (1) victorias', 'Franz Tost', 5),
    Equipo('ALFA ROMEO', 'Alfa Romeo ha participado como una escudería de Fórmula 1 en diferentes periodos. Antes de su retorno como equipo constructor en 2019, tras renombrar la estructura de Sauber y asumir la licencia suiza, participó en los campeonatos de las temporadas 1950, 1951 y entre 1979 y 1985 como escudería italiana.', 'Valteri Bottas / Guanyu Zhou', '(0) constructores / (2) pilotos / (26) podios / (10) victorias', 'Frédéric Vasseur', 6),
    Equipo('ASTON MARTIN', 'Aston Martin es una escudería británica de Fórmula 1 que a finales de 2020 regresó a la parrilla, gracias a que Lawrence Stroll invirtió en Aston Martin £182 millones de libras, lo cual le proporcionó el 20 % de las acciones del fabricante, con tal movimiento decide usar la imagen de Aston Martin para convertir a partir de 2021 al equipo Racing Point en Aston Martin F1 Team. Actualmente tiene su base en Silverstone, Reino Unido', 'Sebastian Vettel / Lance Stroll', '(0) constructores / (0) pilotos / (1) podios / (0) victorias', 'Mike Krack', 5)
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
