import json 
from lista import Lista 

class Jugador(Lista):
    def __init__(self, nombre: str = None, apellido: str = None, edad: int = None, numero: int = None, nacionalidad: str = None):

        self.is_array= nombre is None and apellido is None and edad is None and numero is None and nacionalidad is None

        if self.is_array: # es cuando es arreglo 
            super().__init__()
            
        else: # Objeto 
            self.nombre=nombre
            self.apellido=apellido
            self.edad=edad
            self.numero=numero
            self.nacionalidad=nacionalidad

    def __str__(self):
        if self.is_array:
            return f"{len(self.items)} elementos"
        return f"{self.nombre} {self.apellido} {self.edad} {self.numero} {self.nacionalidad}"
    def to_dict(self):
        if self.is_array: 
            miarreglo=[]
            for item in self.items: 
                miarreglo.append(item.to_dict())
            return miarreglo
        else: 
            return {
                "nombre":self.nombre,
                "edad":self.edad,
                "apellido":self.apellido,
                "numero":self.numero,
                "nacionalidad":self.nacionalidad
            }

    def guardarJson(self,nombre_archivo="jugadores.json"):
        with open(f"{nombre_archivo}","w") as f:
            json.dump(self.to_dict(),f)

    def leerJson(self,nombre_archivo="jugadores.json"):
        with open(f"{nombre_archivo}","r") as f:
            data=json.load(f)
        return self.convertir_to_object(data)

    def convertir_to_object(self,data):
        if isinstance(data,list): 
            lista=Jugador()
            lista.items=[self.convertir_to_object(d) for d in data] 
            return lista 
        else:
            return Jugador(data["nombre"], data["apellido"], data["edad"], data["numero"], data["nacionalidad"])
            
if __name__=="__main__":
    import importlib
    menu_module = importlib.import_module("menu-jugador")
    MenuJugador = menu_module.MenuJugador
    
    menu = MenuJugador()
    menu.menu()
    