import importlib
from jugadores import Jugador

class MenuJugador:
    def __init__(self,jugadores=None):


        self.lista = Jugador()
        self.cargar_datos_existentes()
    
    def cargar_datos_existentes(`self`):
        try:
            self.lista = self.lista.leerJson()
            print(f"Se cargaron {len(self.lista.items)} jugadores existentes.\n")
        except FileNotFoundError:
            print("No hay datos previos. Empezando desde cero.\n")
        except Exception as e:
            print(f"Error: {e}\n")
    
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
                self.lista.guardarJson()
                print("Guardado. Adios!")
                break
            else:
                print("Opcion invalida.")
    
    def agregar_jugador(self):
        print("\n--- AGREGAR JUGADOR ---")
        
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        edad = int(input("Edad: "))
        numero = int(input("Numero: "))
        nacionalidad = input("Nacionalidad: ").strip()
        
        jugador = Jugador(nombre, apellido, edad, numero, nacionalidad)
        self.lista.agregar(jugador)
        print(f"\n{nombre} {apellido} agregado correctamente")
    
    def ver_jugadores(self):
        print("\n--- LISTA DE JUGADORES ---")
        if len(self.lista.items) == 0:
            print("No hay jugadores registrados.")
            return
        
        for i, j in enumerate(self.lista.items):
            print(f"{i}. {j.nombre} {j.apellido} - Edad: {j.edad}, Numero: #{j.numero}, Nacionalidad: {j.nacionalidad}")
    
    def actualizar_jugador(self):
        print("\n--- ACTUALIZAR JUGADOR ---")
        
        if len(self.lista.items) == 0:
            print("No hay jugadores para actualizar.")
            return
        
        self.ver_jugadores()
        
        idx = int(input("\nSelecciona el numero del jugador a actualizar: "))
        if idx < 0 or idx >= len(self.lista.items):
            print("Indice invalido")
            return
        
        print(f"\nActualizando: {self.lista.items[idx].nombre} {self.lista.items[idx].apellido}")
        print("Ingresa los nuevos datos:")
        
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        edad = int(input("Edad: "))
        numero = int(input("Numero: "))
        nacionalidad = input("Nacionalidad: ").strip()
        
        nuevo_jugador = Jugador(nombre, apellido, edad, numero, nacionalidad)
        self.lista.actualizar(idx, nuevo_jugador)
        print(f"\nJugador actualizado correctamente")
    
    def eliminar_jugador(self):
        print("\n--- ELIMINAR JUGADOR ---")
        
        if len(self.lista.items) == 0:
            print("No hay jugadores para eliminar.")
            return
        
        self.ver_jugadores()
        
        idx = int(input("\nSelecciona el numero del jugador a eliminar: "))
        if idx < 0 or idx >= len(self.lista.items):
            print("Indice invalido")
            return
        
        jugador = self.lista.items[idx]
        confirmacion = input(f"Seguro que quieres eliminar a {jugador.nombre} {jugador.apellido}? (s/n): ")
        
        if confirmacion.lower() == 's':
            self.lista.eliminar(idx)
            print(f"\n{jugador.nombre} {jugador.apellido} eliminado correctamente")
        else:
            print("Operacion cancelada")

if __name__ == "__main__":
    menu = MenuJugador()
    menu.menu()