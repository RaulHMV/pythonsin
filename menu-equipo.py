import importlib
from equipo import Equipos
from mongo import Mongo, iniciar_tarea_periodica

class MenuEquipo(Equipos):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mongo = Mongo()
        iniciar_tarea_periodica(self.mongo)

        if self.is_array:
            self.cargar_datos_existentes()
    
    def cargar_datos_existentes(self):
        try:
            data = self.mongo.insert_general(self, "equipos.json", "equipos", Equipos)
            self.items = data.items
            print(f"Se cargaron {len(self.items)} equipos existentes.\n")
        except Exception as e:
            print(f"Error cargando datos: {e}\n")
            try:
                data = self.leerJson()
                self.items = data.items
            except:
                pass
    
    def menu(self):
        while True:
            print("\n" + "="*40)
            print("MENU EQUIPOS")
            print("="*40)
            print("1. Agregar equipo")
            print("2. Ver todos los equipos")
            print("3. Actualizar equipo")
            print("4. Eliminar equipo")
            print("5. Guardar y salir")
            print("="*40)
            
            opcion = input("Opcion: ")
            
            if opcion == "1":
                self.agregar_equipo()
            elif opcion == "2":
                self.ver_equipos()
            elif opcion == "3":
                self.actualizar_equipo()
            elif opcion == "4":
                self.eliminar_equipo()
            elif opcion == "5":
                self.guardarJson()
                print("Guardado. Adios!")
                break
            else:
                print("Opcion invalida.")
    
    def agregar_equipo(self):
        print("\n--- AGREGAR EQUIPO ---")
        
        nombre = input("Nombre: ").strip()
        ciudad = input("Ciudad: ").strip()
        while True:
            try:
                fundacion = int(input("Fundacion: "))
                break
            except ValueError:
                print("Por favor ingresa un año valido.")
        estadio = input("Estadio: ").strip()
        liga = input("Liga: ").strip()
        entrenador = input("Entrenador: ").strip()
        
        equipo = Equipos(nombre, ciudad, fundacion, estadio, liga, entrenador)
        self.agregar(equipo)
        
        if self.mongo.hay_internet():
            self.mongo.insert("equipos", equipo.to_dict())
        else:
            self.guardarJson()
            
        print(f"\n{nombre} agregado correctamente")
    
    def ver_equipos(self):
        print("\n--- LISTA DE EQUIPOS ---")
        if len(self.items) == 0:
            print("No hay equipos registrados.")
            return
        
        for i, e in enumerate(self.items):
            print(f"{i}. {e.nombre} - Ciudad: {e.ciudad}, Fundacion: {e.fundacion}, Estadio: {e.estadio}, Liga: {e.liga}, DT: {e.entrenador}")
    
    def actualizar_equipo(self):
        print("\n--- ACTUALIZAR EQUIPO ---")
        
        if len(self.items) == 0:
            print("No hay equipos para actualizar.")
            return
        
        self.ver_equipos()
        
        idx = int(input("\nSelecciona el numero del equipo a actualizar: "))
        if idx < 0 or idx >= len(self.items):
            print("Indice invalido")
            return
        
        print(f"\nActualizando: {self.items[idx].nombre}")
        print("Ingresa los nuevos datos:")
        
        nombre = input("Nombre: ").strip()
        ciudad = input("Ciudad: ").strip()
        while True:
            try:
                fundacion = int(input("Fundacion: "))
                break
            except ValueError:
                print("Por favor ingresa un año valido.")
        estadio = input("Estadio: ").strip()
        liga = input("Liga: ").strip()
        entrenador = input("Entrenador: ").strip()
        
        nuevo_equipo = Equipos(nombre, ciudad, fundacion, estadio, liga, entrenador)
        
        equipo_anterior = self.items[idx]
        query = equipo_anterior.to_dict()
        
        self.actualizar(idx, nuevo_equipo)
        
        if self.mongo.hay_internet():
            self.mongo.update_one("equipos", query, nuevo_equipo.to_dict())
        else:
            self.guardarJson()
            
        print(f"\nEquipo actualizado correctamente")
    
    def eliminar_equipo(self):
        print("\n--- ELIMINAR EQUIPO ---")
        
        if len(self.items) == 0:
            print("No hay equipos para eliminar.")
            return
        
        self.ver_equipos()
        
        idx = int(input("\nSelecciona el numero del equipo a eliminar: "))
        if idx < 0 or idx >= len(self.items):
            print("Indice invalido")
            return
        
        equipo = self.items[idx]
        confirmacion = input(f"Seguro que quieres eliminar a {equipo.nombre}? (s/n): ")
        
        if confirmacion.lower() == 's':
            query = equipo.to_dict()
            self.eliminar(idx)
            
            if self.mongo.hay_internet():
                self.mongo.delete_one("equipos", query)
            else:
                self.guardarJson()
                
            print(f"\n{equipo.nombre} eliminado correctamente")
        else:
            print("Operacion cancelada")

if __name__ == "__main__":
    menu = MenuEquipo()
    menu.menu()