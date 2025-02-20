'''
Clase Team: Equipo
'''
from Athlete import Athlete
from Sport import Sport
class Team:
    """Clase para representar un equipo"""
    def __init__(self, name:str, sport:Sport, players:list):
        """Constructor de la clase Team"""
        self.name = name
        self.sport = sport
        self.players = players
        