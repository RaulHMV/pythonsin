from team import Team
from player import Player
from CRUDContiner import CRUDContainer

class PlayerTeam(CRUDContainer):
    def __init__(self, team: Team = None, players: dict[str, Player] = None, fecha_union: str = None):
        if team is not None and players is not None:
            self.team = team
            self.players = players
            self.fecha_union = fecha_union
            self.is_dict = False  
        else:
            super().__init__()
    
    def __str__(self):
        if not self.is_dict:
            jugadores_str = ", ".join([f"{j.name} {j.apellido}" for j in self.players.values()])
            return f"Equipo: {self.team.name} | Jugadores: {jugadores_str} | Fecha: {self.fecha_union}"
        else:
            return f"PlayerTeam Container with {self.size()} teams"

if __name__ == "__main__":
    equipos = {
        "RM": Team("Real Madrid", "Madrid", 1902, "Santiago Bernabéu", "La Liga", "Carlo Ancelotti"),
        "FCB": Team("Barcelona", "Barcelona", 1899, "Camp Nou", "La Liga", "Xavi Hernández"),
        "MCI": Team("Manchester City", "Manchester", 1880, "Etihad Stadium", "Premier League", "Pep Guardiola"),
        "BM": Team("Bayern Munich", "Munich", 1900, "Allianz Arena", "Bundesliga", "Thomas Tuchel"),
        "PSG": Team("Paris Saint-Germain", "París", 1970, "Parc des Princes", "Ligue 1", "Luis Enrique")
    }


    jugadores_real_madrid = {
        "CR7": Player("Cristiano", "Ronaldo", 39, 7, "Portuguesa"),
        "VJ20": Player("Vinicius", "Junior", 24, 20, "Brasileña"),
        "LM10": Player("Luka", "Modric", 38, 10, "Croata"),
        "KB9": Player("Karim", "Benzema", 36, 9, "Francesa"),
    }

    jugadores_barcelona = {
        "LM10": Player("Lionel", "Messi", 37, 10, "Argentina"),
        "PG8": Player("Pedri", "González", 21, 8, "Española"),
        "GP6": Player("Gavi", "Páez", 19, 6, "Española")
    }


    jugadores_manchester_city = {
        "EH9": Player("Erling", "Haaland", 24, 9, "Noruega"),
        "KDB17": Player("Kevin", "De Bruyne", 32, 17, "Belga"),
        "PF47": Player("Phil", "Foden", 24, 47, "Inglesa")
    }

    jugadores_bayern_munich = {
        "JM42": Player("Jamal", "Musiala", 21, 42, "Alemana"),
        "TM25": Player("Thomas", "Müller", 34, 25, "Alemana"),
        "LS10": Player("Leroy", "Sané", 27, 10, "Alemana")
    }

    jugadores_psg = {
        "KM25": Player("Kylian", "Mbappé", 25, 9, "Francesa")
    }

    player_team1 = PlayerTeam(equipos["RM"], jugadores_real_madrid, "2021-08-31")
    player_team2 = PlayerTeam(equipos["FCB"], jugadores_barcelona, "2004-10-16")
    player_team3 = PlayerTeam(equipos["MCI"], jugadores_manchester_city, "2022-07-13")
    player_team4 = PlayerTeam(equipos["BM"], jugadores_bayern_munich, "2019-07-01")
    player_team5 = PlayerTeam(equipos["PSG"], jugadores_psg, "2023-08-01")

    players_team_collection = PlayerTeam()
    
    players_team_collection.add("RM", player_team1)
    players_team_collection.add("FCB", player_team2)
    players_team_collection.add("MCI", player_team3)
    players_team_collection.add("BM", player_team4)
    players_team_collection.add("PSG", player_team5)
    
    print("=== EQUIPOS Y JUGADORES ===")
    players_team_collection.list()
    
    print(f"\nTotal de equipos: {players_team_collection.size()}")
    
    print("\n=== OPERACIONES CRUD ===")
    
    # nuevo jugador como diccionario con clave propia
    nuevo_jugador = {"NJ10": Player("Neymar", "Jr", 32, 10, "Brasileña")}
    nuevo_equipo = PlayerTeam(
        Team("Liverpool", "Liverpool", 1892, "Anfield", "Premier League", "Jürgen Klopp"),
        nuevo_jugador,
        "2023-09-01"
    )
    
    # agregar con key propia
    if players_team_collection.add("LIV", nuevo_equipo):
        print("Liverpool agregado exitosamente!")
    
    # actualizar PSG: pasar key "PSG" y nuevo dict de jugadores (no usar suma de listas)
    psg_actualizado = PlayerTeam(
        equipos["PSG"],
        {**jugadores_psg, "MV6": Player("Marco", "Verratti", 31, 6, "Italiana")},
        "2023-08-01"
    )
    
    if players_team_collection.update("PSG", psg_actualizado):
        print("PSG actualizado con nuevo jugador!")
    
    segundo_equipo = players_team_collection.get("FCB")
    if segundo_equipo:
        print(f"\nSegundo equipo: {segundo_equipo}")
    
    print(f"\nTotal final de equipos: {len(players_team_collection)}")