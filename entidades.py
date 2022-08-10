class Circuito:
    def __init__(self, nombre, imagen='', descripcion=''):
        self.nombre = nombre
        self.imagen = imagen
        self.descripcion = descripcion

    def __str__(self):
        return f'{self.nombre}:{self.imagen}:{self.descripcion}'