from Athlete import Athlete
from Sport import Sport
from Team import Team

class Game:
    '''Clase game: Juego entre 2 equipos'''
    sports_dict = {
        'LMP': [x for x in range(0, 11)],
        'NBA': [x for x in range(70, 121)],
        'NFL': [x for x in range(3, 56)],
        'LMX': [x for x in range(0, 9)],
        'MLB': [x for x in range(0, 11)]
    }

    def __init__(self, A: Team, B: Team) -> None:
        '''Constructor Game'''
        self.A = A
        self.B = B
        self.score = {A.name: 0, B.name: 0}

    def play(self):
        '''Juego simulado entre equipos'''
        for s in Game.sports_dict.values():  # Se referencia correctamente sports_dict
            print(s)

if __name__ == "__main__":
    dt = ['Jordan', 'Johnson', 'Pipen', 'Bird', 'Kobe']
    cz = ['Bjovik', 'Czack', 'Pfeizer', 'Leonard', 'Kempfe']
    
    players_a = [Athlete(x) for x in dt]
    players_b = [Athlete(x) for x in cz]
    
    basketball = Sport("NBA", 5, "DreamTeam")
    
    # Se agregan los jugadores a cada equipo
    t = Team("Dream Team", basketball, players_a)
    c = Team("Czeck Republic", basketball, players_b)
    
    game = Game(t, c)
    game.play()


