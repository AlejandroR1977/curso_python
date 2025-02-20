import json

class Sport:
    '''sport'''
    
    def __init__(self, name: str, players: int, league: str):
        '''constructor sport'''
        self.name = name
        if isinstance(players, int):
            self.players = players
        else:
            self.players = int(players)
        self.league = league

    def __str__(self) -> str:
        '''Representacion en string de sport'''
        return f"Sport:{self.name}, {self.players}, {self.league}"
    
    def __repr__(self):
        '''Representacion en string'''
        # Asegúrate de usar 'Sport' con mayúsculas
        return f"Sport(name = '{self.name}', players = {self.players}, league = '{self.league}')"

    def to_json(self) -> dict:
        """Convertir sport a JSON"""
        return {"name": self.name, "players": self.players, "league": self.league}

if __name__ == "__main__":
    s = Sport("Soccer", 11, "FIFA")
    print(s)
    print(repr(s))
    print(s.to_json())

    nfl = Sport("Football", 11, "NFL")
    lmp = Sport("Baseball", 9, "LMP")
    mlb = Sport("Baseball", 9, "mlb")
    lmx = Sport("Soccer", 11, "Liga MX")
    nba = Sport("basketball", 5, "NBA")

    lista_deportes = [nfl, lmp, mlb, lmx, nba, s]
    archivo_deportes = "deportes.txt"
    
    # Escribimos la representación en texto de los objetos en el archivo
    with open(archivo_deportes, "w") as file:
        for d in lista_deportes:
            file.write(repr(d) + "\n")

    sport_list = []
    
    # Leemos el archivo de deportes y convertimos la representación de texto a objeto usando eval (solo con datos seguros)
    with open(archivo_deportes, "r") as file:
        for line in file:
            # Usamos eval de manera controlada, asumiendo que los datos son seguros
            d = eval(line.strip())  # Ahora eval va a funcionar con la clase 'Sport'
            sport_list.append(d)

    print(sport_list)
    print(sport_list[0].to_json())

    # Escribimos el archivo en formato JSON
    archivo_json = "deportes.json"
    
    # Convertimos los objetos Sport a un formato JSON
    sports_json = [sport.to_json() for sport in sport_list]

    # Escribimos la lista de deportes en formato JSON
    with open(archivo_json, "w") as file:
        json.dump(sports_json, file, indent=4)

    # Leemos el archivo JSON
    sport_list_json = []
    with open(archivo_json, "r") as file:
        sport_list_json = json.load(file)
    
    print(sport_list_json)

