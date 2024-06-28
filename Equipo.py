class Equipo:
    def __init__(self, team_id, pais, codigo, grupo):
            self.team_id = team_id
            self.pais = pais
            self.codigo = codigo
            self.grupo = grupo

    def mostrar(self):
          return f'Pais: {self.pais}, Codigo FIFA: {self.codigo}, Grupo: {self.grupo}'