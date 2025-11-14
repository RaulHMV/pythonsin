import importlib
from jugadores import Jugador
from equipo import Equipos

jugador_equipo = importlib.import_module("jugador-equipo")
JugadorEquipo = jugador_equipo.JugadorEquipo

class MenuJugadorEquipo:
    def __init__(self):
        self.lista = JugadorEquipo()
        self.equipos_registrados = Equipos()
        self.jugadores_pool = Jugador()
        self.is_array =  self.jugadores_pool is None and self.equipos_registrados is None

        if self.is_array:
            self.cargar_datos_existentes()
    
    def cargar_datos_existentes(self):
        try:
            self.lista = self.lista.leerJson()
            print(f"Se cargaron {len(self.lista.items)} relaciones existentes.\n")
            for rel in self.lista.items:
                self.equipos_registrados.agregar(rel.equipo)
                for j in rel.jugadores.items:
                    self.jugadores_pool.agregar(j)
        except FileNotFoundError:
            print("No hay datos previos. Empezando desde cero.\n")
        except Exception as e:
            print(f"Error: {e}\n")
    
    def menu(self):
        while True:
            print("\n" + "="*40)
            print("MENU JUGADOR-EQUIPO")
            print("="*40)
            print("1. Crear nueva relacion")
            print("2. Agregar jugadores a equipo existente")
            print("3. Ver todas las relaciones")
            print("4. Editar relacion")
            print("5. Eliminar relacion")
            print("6. Guardar y salir")
            print("="*40)
            
            opcion = input("Opcion: ")
            
            if opcion == "1":
                self.crear_relacion()
            elif opcion == "2":
                self.agregar_jugadores_a_equipo()
            elif opcion == "3":
                self.ver_relaciones()
            elif opcion == "4":
                self.editar_relacion()
            elif opcion == "5":
                self.eliminar_relacion()
            elif opcion == "6":
                self.lista.guardarJson()
                print("Guardado. Adios!")
                break
            else:
                print("Opcion invalida.")
    
    def crear_relacion(self):
        print("\n--- CREAR RELACION ---")
        
        jugadores = self.seleccionar_jugadores()
        if len(jugadores.items) == 0:
            print("No agregaste jugadores.")
            return
        
        equipo = self.seleccionar_equipo()
        if equipo is None:
            return
        
        relacion_existente = None
        for rel in self.lista.items:
            if rel.equipo.nombre == equipo.nombre and rel.equipo.ciudad == equipo.ciudad:
                relacion_existente = rel
                break
        
        if relacion_existente:
            print(f"\n{equipo.nombre} ya tiene una relacion. Agregando jugadores a la relacion existente...")
            for j in jugadores.items:
                relacion_existente.jugadores.agregar(j)
            print(f"{len(jugadores.items)} jugadores agregados a {equipo.nombre}")
        else:
            relacion = JugadorEquipo(jugadores, equipo)
            self.lista.agregar(relacion)
            print(f"\n{len(jugadores.items)} jugadores asignados a {equipo.nombre}")

    def agregar_jugadores_a_equipo(self):
        print("\n--- AGREGAR JUGADORES A EQUIPO EXISTENTE ---")
        
        if len(self.lista.items) == 0:
            print("No hay equipos con relaciones. Crea una relacion primero.")
            return
        
        print("\nEquipos con relaciones:")
        for i, rel in enumerate(self.lista.items):
            print(f"{i}. {rel.equipo.nombre} - {len(rel.jugadores.items)} jugadores")
        
        idx = int(input("\nSelecciona el equipo: "))
        if idx < 0 or idx >= len(self.lista.items):
            print("Indice invalido")
            return
        
        relacion = self.lista.items[idx]
        
        print(f"\nAgregando jugadores a {relacion.equipo.nombre}")
        print("Jugadores actuales:")
        for j in relacion.jugadores.items:
            print(f"  - {j.nombre} {j.apellido} #{j.numero}")
        
        nuevos_jugadores = self.seleccionar_jugadores()
        
        for j in nuevos_jugadores.items:
            relacion.jugadores.agregar(j)
            if j not in self.jugadores_pool.items:
                self.jugadores_pool.agregar(j)
        
        print(f"\n{len(nuevos_jugadores.items)} jugadores agregados a {relacion.equipo.nombre}")
    
    def editar_relacion(self):
        print("\n--- EDITAR RELACION ---")
        
        if len(self.lista.items) == 0:
            print("No hay relaciones para editar.")
            return
        
        self.ver_relaciones()
        
        idx = int(input("\nSelecciona la relacion a editar: "))
        if idx < 1 or idx > len(self.lista.items):
            print("Indice invalido")
            return
        
        idx = idx - 1  # Ajustar porque en ver_relaciones se muestra desde 1
        relacion = self.lista.items[idx]
        
        print(f"\nEditando relacion de: {relacion.equipo.nombre}")
        print("\nQue deseas editar?")
        print("1. Cambiar equipo")
        print("2. Reemplazar todos los jugadores")
        print("3. Eliminar jugadores especificos")
        
        opcion = input("Opcion: ")
        
        if opcion == "1":
            nuevo_equipo = self.seleccionar_equipo()
            if nuevo_equipo:
                relacion.equipo = nuevo_equipo
                print("Equipo actualizado correctamente")
        
        elif opcion == "2":
            print("\nSelecciona los nuevos jugadores:")
            nuevos_jugadores = self.seleccionar_jugadores()
            if len(nuevos_jugadores.items) > 0:
                relacion.jugadores = nuevos_jugadores
                print("Jugadores reemplazados correctamente")
        
        elif opcion == "3":
            if len(relacion.jugadores.items) == 0:
                print("No hay jugadores en esta relacion.")
                return
            
            print("\nJugadores actuales:")
            for i, j in enumerate(relacion.jugadores.items):
                print(f"{i}. {j.nombre} {j.apellido} #{j.numero}")
            
            print("\nSelecciona jugadores a eliminar (numero o 'fin'):")
            while True:
                sel = input("Numero: ").strip()
                if sel.lower() == 'fin':
                    break
                try:
                    jidx = int(sel)
                    if 0 <= jidx < len(relacion.jugadores.items):
                        jugador = relacion.jugadores.items[jidx]
                        relacion.jugadores.eliminar(jidx)
                        print(f"{jugador.nombre} {jugador.apellido} eliminado")
                    else:
                        print("Indice invalido")
                except:
                    print("Invalido")
        else:
            print("Opcion invalida")
    
    def eliminar_relacion(self):
        print("\n--- ELIMINAR RELACION ---")
        
        if len(self.lista.items) == 0:
            print("No hay relaciones para eliminar.")
            return
        
        self.ver_relaciones()
        
        idx = int(input("\nSelecciona la relacion a eliminar: "))
        if idx < 1 or idx > len(self.lista.items):
            print("Indice invalido")
            return
        
        idx = idx - 1  # Ajustar porque en ver_relaciones se muestra desde 1
        relacion = self.lista.items[idx]
        
        confirmacion = input(f"Seguro que quieres eliminar la relacion de {relacion.equipo.nombre}? (s/n): ")
        
        if confirmacion.lower() == 's':
            self.lista.eliminar(idx)
            print(f"\nRelacion de {relacion.equipo.nombre} eliminada correctamente")
        else:
            print("Operacion cancelada")
    
    def seleccionar_jugadores(self):
        jugadores = Jugador()
        
        if len(self.jugadores_pool.items) > 0:
            print("\nTienes jugadores existentes. Quieres:")
            print("1. Usar existentes")
            print("2. Crear nuevos")
            opcion = input("Opcion: ")
            
            if opcion == "1":
                print("\nJugadores disponibles:")
                for i, j in enumerate(self.jugadores_pool.items):
                    print(f"{i}. {j.nombre} {j.apellido} #{j.numero}")
                
                print("\nSelecciona (numero o 'fin'):")
                while True:
                    sel = input("Numero: ").strip()
                    if sel.lower() == 'fin':
                        break
                    try:
                        idx = int(sel)
                        jugadores.agregar(self.jugadores_pool.items[idx])
                        print(f"{self.jugadores_pool.items[idx].nombre} agregado")
                    except:
                        print("Invalido")
                
                if len(jugadores.items) > 0:
                    return jugadores
        
        print("\nCrear jugadores (escribe 'fin' para terminar):")
        while True:
            nombre = input("Nombre (o 'fin'): ").strip()
            if nombre.lower() == 'fin':
                break
            
            apellido = input("Apellido: ").strip()
            edad = int(input("Edad: "))
            numero = int(input("Numero: "))
            nacionalidad = input("Nacionalidad: ").strip()
            
            nuevo = Jugador(nombre, apellido, edad, numero, nacionalidad)
            jugadores.agregar(nuevo)
            self.jugadores_pool.agregar(nuevo)
            print(f"{nombre} agregado\n")
        
        return jugadores
    
    def seleccionar_equipo(self):
        if len(self.equipos_registrados.items) > 0:
            print("\nTienes equipos existentes. Quieres:")
            print("1. Usar existente")
            print("2. Crear nuevo")
            opcion = input("Opcion: ")
            
            if opcion == "1":
                print("\nEquipos disponibles:")
                for i, e in enumerate(self.equipos_registrados.items):
                    print(f"{i}. {e.nombre} - {e.ciudad}")
                
                idx = int(input("\nSelecciona: "))
                return self.equipos_registrados.items[idx]
        
        print("\nDatos del equipo:")
        nombre = input("Nombre: ").strip()
        ciudad = input("Ciudad: ").strip()
        fundacion = int(input("Fundacion: "))
        estadio = input("Estadio: ").strip()
        liga = input("Liga: ").strip()
        entrenador = input("Entrenador: ").strip()
        
        equipo = Equipos(nombre, ciudad, fundacion, estadio, liga, entrenador)
        self.equipos_registrados.agregar(equipo)
        return equipo
    
    def ver_relaciones(self):
        print("\n--- RELACIONES ACTUALES ---")
        if len(self.lista.items) == 0:
            print("No hay relaciones.")
            return
        
        for i, rel in enumerate(self.lista.items):
            print(f"\n{i+1}. {rel.equipo.nombre} ({rel.equipo.ciudad})")
            print(f"   Jugadores: {len(rel.jugadores.items)}")
            for j in rel.jugadores.items:
                print(f"   - {j.nombre} {j.apellido} #{j.numero}")

if __name__ == "__main__":
    menu = MenuJugadorEquipo()
    menu.menu()