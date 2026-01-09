import importlib
from jugadores import Jugador
from mongo import Mongo, iniciar_tarea_periodica

class MenuJugador(Jugador):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mongo = Mongo()
        iniciar_tarea_periodica(self.mongo)

        if self.is_array:
            self.cargar_datos_existentes()
    
    def cargar_datos_existentes(self):
        try:
            # Usamos insert_general para sincronizar
            # insert_general(lista_obj, nameArchivo, collection, clase)
            # Devuelve un objeto Jugador con los items cargados
            data = self.mongo.insert_general(self, "jugadores.json", "jugadores", Jugador)
            self.items = data.items
            print(f"Se cargaron {len(self.items)} jugadores existentes.\n")
        except Exception as e:
            print(f"Error cargando datos: {e}\n")
            # Fallback a local si falla algo critico en mongo
            try:
                data = self.leerJson()
                self.items = data.items
            except:
                pass
    
    def menu(self):
        while True:
            print("\n" + "="*40)
            print("MENU JUGADORES")
            print("="*40)
            print("1. Agregar jugador")
            print("2. Ver todos los jugadores")
            print("3. Actualizar jugador")
            print("4. Eliminar jugador")
            print("5. Guardar y salir")
            print("="*40)
            
            opcion = input("Opcion: ")
            
            if opcion == "1":
                self.agregar_jugador()
            elif opcion == "2":
                self.ver_jugadores()
            elif opcion == "3":
                self.actualizar_jugador()
            elif opcion == "4":
                self.eliminar_jugador()
            elif opcion == "5":
                self.guardarJson()
                print("Guardado. Adios!")
                break
            else:
                print("Opcion invalida.")
    
    def agregar_jugador(self):
        print("\n--- AGREGAR JUGADOR ---")
        
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        while True:
            try:
                edad = int(input("Edad: "))
                break
            except ValueError:
                print("Por favor ingresa un numero valido para la edad.")
        
        while True:
            try:
                numero = int(input("Numero: "))
                break
            except ValueError:
                print("Por favor ingresa un numero valido para el numero.")
        nacionalidad = input("Nacionalidad: ").strip()
        
        jugador = Jugador(nombre, apellido, edad, numero, nacionalidad)
        self.agregar(jugador)
        
        if self.mongo.hay_internet():
            self.mongo.insert("jugadores", jugador.to_dict())
        else:
            self.guardarJson()
            
        print(f"\n{nombre} {apellido} agregado correctamente")
    
    def ver_jugadores(self):
        print("\n--- LISTA DE JUGADORES ---")
        if len(self.items) == 0:
            print("No hay jugadores registrados.")
            return
        
        for i, j in enumerate(self.items):
            print(f"{i}. {j.nombre} {j.apellido} - Edad: {j.edad}, Numero: #{j.numero}, Nacionalidad: {j.nacionalidad}")
    
    def actualizar_jugador(self):
        print("\n--- ACTUALIZAR JUGADOR ---")
        
        if len(self.items) == 0:
            print("No hay jugadores para actualizar.")
            return
        
        self.ver_jugadores()
        
        idx = int(input("\nSelecciona el numero del jugador a actualizar: "))
        if idx < 0 or idx >= len(self.items):
            print("Indice invalido")
            return
        
        print(f"\nActualizando: {self.items[idx].nombre} {self.items[idx].apellido}")
        print("Ingresa los nuevos datos:")
        
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        while True:
            try:
                edad = int(input("Edad: "))
                break
            except ValueError:
                print("Por favor ingresa un numero valido para la edad.")
        
        while True:
            try:
                numero = int(input("Numero: "))
                break
            except ValueError:
                print("Por favor ingresa un numero valido para el numero.")
        nacionalidad = input("Nacionalidad: ").strip()
        
        nuevo_jugador = Jugador(nombre, apellido, edad, numero, nacionalidad)
        
        jugador_anterior = self.items[idx]
        query = jugador_anterior.to_dict()
        
        self.actualizar(idx, nuevo_jugador)
        
        if self.mongo.hay_internet():
            self.mongo.update_one("jugadores", query, nuevo_jugador.to_dict())
        else:
            self.guardarJson()
            
        print(f"\nJugador actualizado correctamente")
    
    def eliminar_jugador(self):
        print("\n--- ELIMINAR JUGADOR ---")
        
        if len(self.items) == 0:
            print("No hay jugadores para eliminar.")
            return
        
        self.ver_jugadores()
        
        idx = int(input("\nSelecciona el numero del jugador a eliminar: "))
        if idx < 0 or idx >= len(self.items):
            print("Indice invalido")
            return
        
        jugador = self.items[idx]
        confirmacion = input(f"Seguro que quieres eliminar a {jugador.nombre} {jugador.apellido}? (s/n): ")
        
        if confirmacion.lower() == 's':
            query = jugador.to_dict()
            self.eliminar(idx)
            
            if self.mongo.hay_internet():
                self.mongo.delete_one("jugadores", query)
            else:
                self.guardarJson()
                
            print(f"\n{jugador.nombre} {jugador.apellido} eliminado correctamente")
        else:
            print("Operacion cancelada")

if __name__ == "__main__":
    menu = MenuJugador()
    menu.menu()