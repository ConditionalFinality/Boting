class Partido:
    def __init__(self, match_id, local, visitante, fecha, estadio):
            self.match_id = match_id
            self.local = local
            self.visitante = visitante
            self.fecha = fecha
            self.estadio = estadio

    def mostrar(self):
          return f'Equipo Local: {self.local.mostrar()}, Equipo Visitante: {self.visitante.mostrar()}, Fecha: {self.fecha}, Estadio: {self.estadio.mostrar()}'