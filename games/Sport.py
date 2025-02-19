class Sport:
    '''sport'''
    
    def __init__(self, name:str, players:int, league:str):
        '''constructor sport'''
        self.name = name
        if isinstance(players,int):
            self.players = players
        else:
            self.players = int(players)(players)
        self.league = league

    def __str__(self)->str:
        '''Representacion en string de sport'''
        return f"Sport:{self.name}, {self.players}, {self.league}"
    
    def __repr__(self):
        '''Representacion en string'''
        return f"sport(name = '{self.name}', players = {self.players}, league = {self.league}')"
    
    def to_json(self)->dict:
        """Convertir sport a JSON"""
        return {"name": self.name, "players": self.players, "league": self.league}
    
    if __name__ == "__main__":
        nfl = Sport("Football", 11, "NFL")
        print(nfl)
        print(repr(nfl))
        print(nfl.to_json())
        lmp = Sport("Baseball", "9", "LMP")
        print(lmp)
        print(repr(lmp))
        print(lmp.to_json())