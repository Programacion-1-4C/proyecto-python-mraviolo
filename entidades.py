# clase Circuito
class Circuito:
    def __init__ (self, nombre, descripcion='', imagen=''):
        self.nombre = nombre
        self.imagen = imagen
        self.descripcion = descripcion

    def __str__ (self):
        return f'{self.nombre}:{self.descripcion}:{self.imagen}'

# clase Equipo
class Equipo:
    def __init__ (self, nombre,  historia='', pilotos='', imagen=''):
        self.nombre = nombre
        self.imagen = imagen
        self.historia = historia
        self.pilotos = pilotos

    def __str__ (self):
        return f'{self.nombre}:{self.pilotos}:{self.historia}:{self.imagen}'