from CRUD import CRUDContainer

class Player(CRUDContainer):
    def __init__(self, name: str = None, apellido: str = None, edad: int = None, numero: int = None, nacionalidad: str = None):
        if name is not None and apellido is not None:
            self.name = name
            self.apellido = apellido
            self.edad = edad
            self.numero = numero
            self.nacionalidad = nacionalidad
            self.is_array = False 
        else:
            super().__init__()
    
    def __str__(self):
        if not self.is_array:
            return f"Jugador: {self.name} {self.apellido}, Edad: {self.edad}, Numero: {self.numero}, Nacionalidad: {self.nacionalidad}"
        else:
            return f"Player Container with {self.size()} players"
    
if __name__ == "__main__":
    jugador1 = Player("Cristiano", "Ronaldo", 39, 7, "Portuguesa")
    jugador2 = Player("Lionel", "Messi", 37, 10, "Argentina")
    jugador3 = Player("Kylian", "Mbappé", 25, 9, "Francesa")
    jugador4 = Player("Erling", "Haaland", 24, 9, "Noruega")
    jugador5 = Player("Vinicius", "Junior", 24, 20, "Brasileña")
    
    players_collection = Player()
    
    players_collection.add(jugador1)
    players_collection.add(jugador2)
    players_collection.add(jugador3)
    players_collection.add(jugador4)
    players_collection.add(jugador5)
    
    # Mostrar todos los jugadores
    print("=== JUGADORES ===")
    players_collection.list()
    
    print(f"\nTotal de jugadores: {players_collection.size()}")
    
    # Ejemplo de operaciones CRUD
    print("\n=== OPERACIONES CRUD ===")
    
    # Agregar al neimar pro
    nuevo_jugador = Player("Neymar", "Jr", 32, 10, "Brasileña")
    if players_collection.add(nuevo_jugador):
        print("Neymar agregado exitosamente!")
    
    # Actualizar un jugador (cambiar datos de uno existente)
    messi_actualizado = Player("Lionel", "Messi", 37, 10, "Argentina")  
    if players_collection.update(1, messi_actualizado):
        print("Messi actualizado!")
    
    # Obtener un jugador específico
    tercer_jugador = players_collection.get(2)
    if tercer_jugador:
        print(f"\nTercer jugador: {tercer_jugador}")
    
    # Remover al CR7 kchau
    if players_collection.remove(0):
        print("Primer jugador removido!")
    
    print(f"\nTotal final de jugadores: {len(players_collection)}")
    
    # Mostrar estado final........
    print("\n=== ESTADO FINAL ===")
    players_collection.list()