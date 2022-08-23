# clase Circuito
class Circuito:
    def __init__ (self, nombre, longitud='', pais='', imagen=''):
        self.nombre = nombre
        self.longitud = longitud
        self.pais = pais
        self.imagen = imagen
    
    def __str__ (self):
        return f'{self.nombre}:{self.longitud}:{self.pais}:{self.imagen}'

# clase Equipo
class Equipo:
    def __init__ (self, nombre,  historia='', pilotos='', ganados='', director='', puntaje=0, imagen=''):
        self.nombre = nombre
        self.historia = historia
        self.pilotos = pilotos
        self.ganados = ganados
        self.director = director
        self.puntaje = puntaje
        self.imagen = imagen

    def __eq__(self, nombre):
        return self.nombre == nombre 

    def __str__ (self):
        return f'{self.nombre}:{self.pilotos}:{self.historia}:{self.ganados}:{self.director}:{self.puntaje}:{self.imagen}'

# clase Piloto
class Piloto:
    def __init__ (self, nombre, edad='', pais='', equipo='', ganados='', puntaje=0, imagen=''):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.equipo = equipo
        self.ganados = ganados
        self.puntaje = puntaje
        self.imagen = imagen
    
    def __eq__(self, nombre):
        return self.nombre == nombre  

    def __str__ (self):
        return f'{self.nombre}:{self.edad}:{self.equipo}:{self.ganados}.{self.puntaje}:{self.imagen}'

# clase Calendario
class Calendario:
    def __init__ (self, nombre, fecha='', hora=''):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        
    def __str__ (self):
        return f'{self.nombre}-{self.fecha}-{self.hora}'