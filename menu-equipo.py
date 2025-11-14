import importlib
from equipo import Equipos

class MenuEquipo:
    def __init__(self):
        self.lista = Equipos()
        self.cargar_datos_existentes()
    
    def cargar_datos_existentes(self):
        try:
            self.lista = self.lista.leerJson()
            print(f"Se cargaron {len(self.lista.items)} equipos existentes.\n")
        except FileNotFoundError:
            print("No hay datos previos. Empezando desde cero.\n")
        except Exception as e:
            print(f"Error: {e}\n")
    
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
                self.lista.guardarJson()
                print("Guardado. Adios!")
                break
            else:
                print("Opcion invalida.")
    
    def agregar_equipo(self):
        print("\n--- AGREGAR EQUIPO ---")
        
        nombre = input("Nombre: ").strip()
        ciudad = input("Ciudad: ").strip()
        fundacion = int(input("Fundacion: "))
        estadio = input("Estadio: ").strip()
        liga = input("Liga: ").strip()
        entrenador = input("Entrenador: ").strip()
        
        equipo = Equipos(nombre, ciudad, fundacion, estadio, liga, entrenador)
        self.lista.agregar(equipo)
        print(f"\n{nombre} agregado correctamente")
    
    def ver_equipos(self):
        print("\n--- LISTA DE EQUIPOS ---")
        if len(self.lista.items) == 0:
            print("No hay equipos registrados.")
            return
        
        for i, e in enumerate(self.lista.items):
            print(f"{i}. {e.nombre} - Ciudad: {e.ciudad}, Fundacion: {e.fundacion}, Estadio: {e.estadio}, Liga: {e.liga}, DT: {e.entrenador}")
    
    def actualizar_equipo(self):
        print("\n--- ACTUALIZAR EQUIPO ---")
        
        if len(self.lista.items) == 0:
            print("No hay equipos para actualizar.")
            return
        
        self.ver_equipos()
        
        idx = int(input("\nSelecciona el numero del equipo a actualizar: "))
        if idx < 0 or idx >= len(self.lista.items):
            print("Indice invalido")
            return
        
        print(f"\nActualizando: {self.lista.items[idx].nombre}")
        print("Ingresa los nuevos datos:")
        
        nombre = input("Nombre: ").strip()
        ciudad = input("Ciudad: ").strip()
        fundacion = int(input("Fundacion: "))
        estadio = input("Estadio: ").strip()
        liga = input("Liga: ").strip()
        entrenador = input("Entrenador: ").strip()
        
        nuevo_equipo = Equipos(nombre, ciudad, fundacion, estadio, liga, entrenador)
        self.lista.actualizar(idx, nuevo_equipo)
        print(f"\nEquipo actualizado correctamente")
    
    def eliminar_equipo(self):
        print("\n--- ELIMINAR EQUIPO ---")
        
        if len(self.lista.items) == 0:
            print("No hay equipos para eliminar.")
            return
        
        self.ver_equipos()
        
        idx = int(input("\nSelecciona el numero del equipo a eliminar: "))
        if idx < 0 or idx >= len(self.lista.items):
            print("Indice invalido")
            return
        
        equipo = self.lista.items[idx]
        confirmacion = input(f"Seguro que quieres eliminar a {equipo.nombre}? (s/n): ")
        
        if confirmacion.lower() == 's':
            self.lista.eliminar(idx)
            print(f"\n{equipo.nombre} eliminado correctamente")
        else:
            print("Operacion cancelada")

if __name__ == "__main__":
    menu = MenuEquipo()
    menu.menu()