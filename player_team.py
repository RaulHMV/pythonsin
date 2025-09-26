from team import Team
from player import Player
from CRUDContiner import CRUDContainer

class PlayerTeam(CRUDContainer):
    def __init__(self, team: Team = None, players: list[Player] = None, fecha_union: str = None):
        if team is not None and players is not None:
            self.team = team
            self.players = players
            self.fecha_union = fecha_union
            self.is_array = False  
        else:
            super().__init__()
    
    def __str__(self):
        if not self.is_array:
            jugadores_str = ", ".join([f"{j.name} {j.apellido}" for j in self.players])
            return f"Equipo: {self.team.name} | Jugadores: {jugadores_str} | Fecha: {self.fecha_union}"
        else:
            return f"PlayerTeam Container with {self.size()} teams"

if __name__ == "__main__":
    equipos = [
        Team("Real Madrid", "Madrid", 1902, "Santiago Bernabéu", "La Liga", "Carlo Ancelotti"),
        Team("Barcelona", "Barcelona", 1899, "Camp Nou", "La Liga", "Xavi Hernández"),
        Team("Manchester City", "Manchester", 1880, "Etihad Stadium", "Premier League", "Pep Guardiola"),
        Team("Bayern Munich", "Munich", 1900, "Allianz Arena", "Bundesliga", "Thomas Tuchel"),
        Team("Paris Saint-Germain", "París", 1970, "Parc des Princes", "Ligue 1", "Luis Enrique")
    ]
    
    jugadores_real_madrid = [
        Player("Cristiano", "Ronaldo", 39, 7, "Portuguesa"),
        Player("Vinicius", "Junior", 24, 20, "Brasileña"),
        Player("Luka", "Modric", 38, 10, "Croata"),
        Player("Karim", "Benzema", 36, 9, "Francesa")
    ]
    
    jugadores_barcelona = [
        Player("Lionel", "Messi", 37, 10, "Argentina"),
        Player("Pedri", "González", 21, 8, "Española"),
        Player("Gavi", "Páez", 19, 6, "Española")
    ]
    
    jugadores_manchester_city = [
        Player("Erling", "Haaland", 24, 9, "Noruega"),
        Player("Kevin", "De Bruyne", 32, 17, "Belga"),
        Player("Phil", "Foden", 24, 47, "Inglesa")
    ]
    
    jugadores_bayern_munich = [
        Player("Jamal", "Musiala", 21, 42, "Alemana"),
        Player("Thomas", "Müller", 34, 25, "Alemana"),
        Player("Leroy", "Sané", 27, 10, "Alemana")
    ]
    
    jugadores_psg = [
        Player("Kylian", "Mbappé", 25, 9, "Francesa")
    ]
    
    player_team1 = PlayerTeam(equipos[0], jugadores_real_madrid, "2021-08-31")
    player_team2 = PlayerTeam(equipos[1], jugadores_barcelona, "2004-10-16")
    player_team3 = PlayerTeam(equipos[2], jugadores_manchester_city, "2022-07-13")
    player_team4 = PlayerTeam(equipos[3], jugadores_bayern_munich, "2019-07-01")
    player_team5 = PlayerTeam(equipos[4], jugadores_psg, "2023-08-01")
    
    players_team_collection = PlayerTeam()
    
    players_team_collection.add(player_team1)
    players_team_collection.add(player_team2)
    players_team_collection.add(player_team3)
    players_team_collection.add(player_team4)
    players_team_collection.add(player_team5)
    
    print("=== EQUIPOS Y JUGADORES ===")
    players_team_collection.list()
    
    print(f"\nTotal de equipos: {players_team_collection.size()}")
    
    print("\n=== OPERACIONES CRUD ===")
    

    nuevo_jugador = [Player("Neymar", "Jr", 32, 10, "Brasileña")]
    nuevo_equipo = PlayerTeam(
        Team("Liverpool", "Liverpool", 1892, "Anfield", "Premier League", "Jürgen Klopp"),
        nuevo_jugador,
        "2023-09-01"
    )
    
    if players_team_collection.add(nuevo_equipo):
        print("Liverpool agregado exitosamente!")
    
    psg_actualizado = PlayerTeam(
        equipos[4],
        jugadores_psg + [Player("Marco", "Verratti", 31, 6, "Italiana")],
        "2023-08-01"
    )
    
    if players_team_collection.update(4, psg_actualizado):
        print("PSG actualizado con nuevo jugador!")
    
    segundo_equipo = players_team_collection.get(1)
    if segundo_equipo:
        print(f"\nSegundo equipo: {segundo_equipo}")
    
    print(f"\nTotal final de equipos: {len(players_team_collection)}")