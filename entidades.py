# clase Circuito
class Circuito:
    def __init__ (self, nombre, longitud='', pais=''):
        self.nombre = nombre
        self.longitud = longitud
        self.pais = pais
        

    def __str__ (self):
        return f'{self.nombre}:{self.longitud}:{self.pais}'

# clase Equipo
class Equipo:
    def __init__ (self, nombre,  historia='', pilotos='', ganados='', director=''):
        self.nombre = nombre
        self.historia = historia
        self.pilotos = pilotos
        self.ganados = ganados
        self.director = director

    def __str__ (self):
        return f'{self.nombre}:{self.pilotos}:{self.historia}:{self.ganados}:{self.director}'

# clase Piloto
class Piloto:
    def __init__ (self, nombre, edad='', pais='', equipo='', ganados=''):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.equipo = equipo
        self.ganados = ganados
    
    def __str__ (self):
        return f'{self.nombre}:{self.edad}:{self.equipo}:{self.ganados}'

# clase Calendario
class Calendario:
    def __init__ (self, nombre, fecha='', hora=''):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        
    def __str__ (self):
        return f'{self.nombre}-{self.fecha}-{self.hora}'