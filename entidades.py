# clase Circuito
class Circuito:
    def __init__ (self, nombre, longitud='', pais=''):
        self.nombre = nombre
        self.longitud = longitud
        self.pais = pais
        

    def __str__ (self):
        return f'{self.nombre}:{self.longitud}'

# clase Equipo
class Equipo:
    def __init__ (self, nombre,  historia='', pilotos=''):
        self.nombre = nombre
        self.historia = historia
        self.pilotos = pilotos

    def __str__ (self):
        return f'{self.nombre}:{self.pilotos}:{self.historia}'

# clase Piloto
class Piloto:
    def __init__ (self, nombre, edad='', pais='', equipo=''):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.equipo = equipo
    
    def __str__ (self):
        return f'{self.nombre}:{self.edad}:{self.equipo}'

# clase Calendario
class Calendario:
    def __init__ (self, nombre, fecha='', hora=''):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        
    def __str__ (self):
        return f'{self.nombre}-{self.fecha}-{self.hora}'