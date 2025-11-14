
import json
from lista import Lista 

class Equipos(Lista):
    def __init__(self, nombre: str = None, ciudad: str = None, fundacion: int = None, estadio: str = None, liga: str = None, entrenador: str = None):

        self.is_array = nombre is None and ciudad is None and fundacion is None and estadio is None and liga is None and entrenador is None

        if self.is_array: # es cuando es arreglo
            super().__init__()
        else: # Objeto
            self.nombre=nombre
            self.ciudad=ciudad
            self.fundacion=fundacion
            self.estadio=estadio
            self.liga=liga
            self.entrenador=entrenador

    def __str__(self):
        if self.is_array:
            return f"{len(self.items)} elementos"
        return f"{self.nombre} {self.ciudad} {self.fundacion} {self.estadio} {self.liga} {self.entrenador}"
    
    def to_dict(self):
        if self.is_array: 
            miarreglo=[]
            for item in self.items: 
                miarreglo.append(item.to_dict())
            return miarreglo
        else: 
            return {
                "nombre":self.nombre,
                "ciudad":self.ciudad,
                "fundacion":self.fundacion,
                "estadio":self.estadio,
                "liga":self.liga,
                "entrenador":self.entrenador
            }
    def guardarJson(self,nombre_archivo="equipos.json"):
            with open(f"{nombre_archivo}","w") as f:
                json.dump(self.to_dict(),f)

    def leerJson(self,nombre_archivo="equipos.json"):
        with open(f"{nombre_archivo}","r") as f:
            data=json.load(f)
        return self.convertir_to_object(data)

    def convertir_to_object(self,data):
        if isinstance(data,list): 
            lista=Equipos()
            lista.items=[self.convertir_to_object(d) for d in data] 
            return lista 
        else:
            return Equipos(data["nombre"], data["ciudad"], data["fundacion"], data["estadio"], data["liga"], data["entrenador"])
            
if __name__=="__main__":
    import importlib
    menu_module = importlib.import_module("menu-equipo")
    MenuEquipo = menu_module.MenuEquipo
    
    menu = MenuEquipo()
    menu.menu()