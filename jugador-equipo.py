import json 
from lista import Lista
from jugadores import Jugador
from equipo import Equipos

class JugadorEquipo(Lista):
    def __init__(self, jugadores: Jugador = None, equipo: Equipos = None):
        self.jugadores = jugadores
        self.equipo = equipo

        self.is_array = jugadores is None and equipo is None

        if self.is_array: # es cuando es arreglo 
            super().__init__() 

        else: # Objeto 
            self.jugadores=jugadores
            self.equipo=equipo

    def __str__(self):
        if self.is_array:
            return f"{len(self.items)} elementos"
        return f"{self.jugadores} {self.equipo}"
    
    def to_dict(self):
        if self.is_array: 
            miarreglo=[]
            for item in self.items: 
                miarreglo.append(item.to_dict())
            return miarreglo
        else: 
            return {
                "jugadores": self.jugadores.to_dict() if hasattr(self.jugadores, "to_dict") else self.jugadores,
                "equipo": self.equipo.to_dict() if hasattr(self.equipo, "to_dict") else self.equipo
            }
        
    def guardarJson(self,nombre_archivo="jugadores-equipo.json"):
        with open(f"{nombre_archivo}","w") as f:
            json.dump(self.to_dict(),f)

    def leerJson(self,nombre_archivo="jugadores-equipo.json"):
        with open(f"{nombre_archivo}","r") as f:
            data=json.load(f)
        return self.convertir_to_object(data)
    
    def convertir_to_object(self,data):
        if isinstance(data, list):
            lista = JugadorEquipo()
            lista.items = [self.convertir_to_object(d) for d in data]
            return lista
        else:
            jugador_list = Jugador()
            jugadores = jugador_list.convertir_to_object(data["jugadores"])
            equipo = Equipos(
                data["equipo"]["nombre"],
                data["equipo"]["ciudad"],
                data["equipo"]["fundacion"],
                data["equipo"]["estadio"],
                data["equipo"]["liga"],
                data["equipo"]["entrenador"]
            )
            return JugadorEquipo(jugadores, equipo)
        
if __name__=="__main__":
    import importlib
    menu_module = importlib.import_module("menu-jugador-equipo")
    MenuJugadorEquipo = menu_module.MenuJugadorEquipo
    
    menu = MenuJugadorEquipo()
    menu.menu()
    