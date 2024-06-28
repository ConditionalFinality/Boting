class Estadio:
        def __init__(self, stadium_id, nombre, ubicacion, capacidad, restaurantes):
            self.stadium_id = stadium_id
            self.nombre = nombre
            self.ubicacion = ubicacion
            self.capacidad = capacidad
            self.restaurantes = restaurantes

        def mostrar(self):
            return f'Nombre: {self.nombre}, Ubicación: {self.ubicacion}'