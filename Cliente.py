class Cliente:
    def __init__(self, nombre, cedula, edad, partido, vip):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.partido = partido
        self.vip = vip
        
    def mostrar(self): 
        return f'Nombre del Cliente: {self.nombre}, Cédula: {self.cedula}, Edad: {self.edad}'