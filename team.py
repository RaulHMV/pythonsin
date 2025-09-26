from CRUDContiner import CRUDContainer

class Team(CRUDContainer):
    def __init__(self, name: str = None, ciudad: str = None, fundacion: int = None, estadio: str = None, liga: str = None, entrenador: str = None):
        if name is not None and ciudad is not None:
            self.name = name
            self.ciudad = ciudad
            self.fundacion = fundacion
            self.estadio = estadio
            self.liga = liga
            self.entrenador = entrenador
            self.is_array = False  
        else:
            super().__init__()
    
    def __str__(self):
        if not self.is_array:
            return f"Equipo: {self.name}, Ciudad: {self.ciudad}, Fundación: {self.fundacion}, Estadio: {self.estadio}, Liga: {self.liga}, Entrenador: {self.entrenador}"
        else:
            return f"Team Container with {self.size()} teams"

if __name__ == "__main__":
    equipo1 = Team("Real Madrid", "Madrid", 1902, "Santiago Bernabéu", "La Liga", "Carlo Ancelotti")
    equipo2 = Team("Barcelona", "Barcelona", 1899, "Camp Nou", "La Liga", "Xavi Hernández")
    equipo3 = Team("Manchester City", "Manchester", 1880, "Etihad Stadium", "Premier League", "Pep Guardiola")
    equipo4 = Team("Bayern Munich", "Munich", 1900, "Allianz Arena", "Bundesliga", "Thomas Tuchel")
    equipo5 = Team("Paris Saint-Germain", "París", 1970, "Parc des Princes", "Ligue 1", "Luis Enrique")
    
    teams_collection = Team()
    
    teams_collection.add(equipo1)
    teams_collection.add(equipo2)
    teams_collection.add(equipo3)
    teams_collection.add(equipo4)
    teams_collection.add(equipo5)
    
    print("=== EQUIPOS ===")
    teams_collection.list()
    
    print(f"\nTotal de equipos: {teams_collection.size()}")
    
    print("\n=== OPERACIONES CRUD ===")
    
    # Agregar nuevo equipo
    nuevo_equipo = Team("Liverpool", "Liverpool", 1892, "Anfield", "Premier League", "Jürgen Klopp")
    if teams_collection.add(nuevo_equipo):
        print("Liverpool agregado exitosamente!")

    # Actualizar un equipo (cambiar entrenador del Madrid por uno gachísimo)
    madrid_actualizado = Team("Real Madrid", "Madrid", 1902, "Santiago Bernabéu", "La Liga", "Zinedine Zidane")
    if teams_collection.update(0, madrid_actualizado):
        print("Real Madrid actualizado con nuevo entrenador!")
    
    # Obtener un equipo específico
    segundo_equipo = teams_collection.get(1)
    if segundo_equipo:
        print(f"\nSegundo equipo: {segundo_equipo}")
    
    # Remover un equipo
    if teams_collection.remove(4):  # Remover PSG jijijiji
        print("PSG removido!")
    
    print(f"\nTotal final de equipos: {len(teams_collection)}")
    
    # Mostrar estado final
    print("\n=== ESTADO FINAL ===")
    teams_collection.list()