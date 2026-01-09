import socket
from pymongo import MongoClient
import json
import os
import importlib
import threading
import time

from jugadores import Jugador
from equipo import Equipos
# Dynamic import for JugadorEquipo due to hyphen in filename
jugador_equipo_module = importlib.import_module("jugador-equipo")
JugadorEquipo = jugador_equipo_module.JugadorEquipo

class Mongo:
    def __init__(self):
        self.conexion_anterior = self.hay_internet()
        self.client = None
        self.db = None
        
        if self.conexion_anterior:
            self.conectar()
        else:
            print("No hay conexión a internet, no se conectó a MongoDB.")

    def conectar(self):
        try:
            self.client = MongoClient("mongodb+srv://victroyanoooo_db_user:AFqfOnyFqrLdXpJB@cluster0.ilqoegi.mongodb.net/")
            self.db = self.client["victor_futbol"]
            print("Conexión a MongoDB establecida correctamente.")
        except Exception as e:
            print(f"Error al conectar a MongoDB: {e}")
            self.client = None
            self.db = None

    @staticmethod
    def hay_internet():
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False

    def insert_general(self, lista_obj, nameArchivo, collection, clase):
        """
        Sincroniza datos:
        - Si hay internet: Sube datos locales pendientes (si hay) a Mongo, limpia local, y descarga todo de Mongo.
        - Si no hay internet: Carga datos locales.
        """
        if self.hay_internet():
            if self.client is None:
                self.conectar()
                
            print(f"Conectado a internet. Procesando {collection}...")
            
            # Leer datos locales pendientes
            try:
                with open(nameArchivo, 'r') as f:
                    content = f.read().strip()
                    if content:
                        listData = json.loads(content)
                    else:
                        listData = []
            except (FileNotFoundError, json.JSONDecodeError):
                listData = []

            if listData:
                print(f"{nameArchivo} contiene datos pendientes. Insertando en MongoDB...")
                # Si es una lista de objetos, insertar muchos
                if isinstance(listData, list) and len(listData) > 0:
                     self.insert(collection, listData, nameArchivo)
                elif isinstance(listData, dict):
                     self.insert(collection, listData, nameArchivo)
            else:
                print(f"{nameArchivo} está vacío o limpio.")

            # Descargar todo de Mongo
            return self.find_all(collection, clase)

        else:
            print(f"Sin conexión. Cargando datos locales desde {nameArchivo}...")
            try:
                return lista_obj.leerJson(nameArchivo)
            except Exception as e:
                print(f"Error leyendo local: {e}")
                return lista_obj

    def insert(self, collection, data, nombreJSON=None):
        if self.db is None:
            self.conectar()
            if self.db is None:
                print("Error: No hay conexión a la base de datos.")
                return False

        try:
            if isinstance(data, dict):
                result = self.db[collection].insert_one(data)
                print(f"Documento insertado con ID: {result.inserted_id}")
            
            elif isinstance(data, list) and len(data) > 0:
                result = self.db[collection].insert_many(data)
                print(f"Documentos insertados con IDs: {result.inserted_ids}")
            
            if nombreJSON:
                self.limpiarJson(nombreJSON)
            
            return True
        except Exception as e:
            print(f"Error al insertar en MongoDB: {e}")
            return False

    def find_all(self, collection, clase):
        if self.db is None: return clase()
        
        data = list(self.db[collection].find({}, {"_id": 0}))
        listaClase = clase()
        
        return listaClase.convertir_to_object(data)

    def update_one(self, collection, query, new_values):
        if self.db is None:
            self.conectar()
            if self.db is None:
                return 0
        
        try:
            # Buscamos el documento para obtener su _id si no esta en query
            doc = self.db[collection].find_one(query)

            if not doc:
                print("No se encontró ningún documento que coincida con la consulta.")
                return 0
            
            filtro = {"_id": doc["_id"]}
            result = self.db[collection].update_one(filtro, {"$set": new_values})

            if result.modified_count > 0:
                print(f"Documento actualizado correctamente.")
            else:
                print(f"No se realizaron cambios.")

            return result.modified_count
        except Exception as e:
            print(f"Error al actualizar en MongoDB: {e}")
            return 0

    def delete_one(self, collection, query):
        if self.db is None:
            self.conectar()
            if self.db is None:
                return 0
        
        try:
            result = self.db[collection].delete_one(query)
            print(f"Documentos eliminados: {result.deleted_count}")
            return result.deleted_count
        except Exception as e:
            print(f"Error al eliminar en MongoDB: {e}")
            return 0

    @staticmethod
    def limpiarJson(nombreJSON):
        with open(nombreJSON, "w") as f:
            json.dump([], f)

def verificarRed(mongo):
    estado_actual = mongo.hay_internet()

    if estado_actual:
        if not mongo.conexion_anterior:
            print("✅ Conexión restaurada.")
            mongo.conectar()
        # else:
            # print("🌐 Hay internet, todo bien.")
    else:
        if mongo.conexion_anterior:
             print("❌ Se perdió la conexión a internet.")
             mongo.client = None
             mongo.db = None

    mongo.conexion_anterior = estado_actual

def ejecutar_verificacion_periodica(mongo):
    while True:
        verificarRed(mongo)
        time.sleep(5)

def iniciar_tarea_periodica(mongo):
    hilo = threading.Thread(target=ejecutar_verificacion_periodica, args=(mongo,), daemon=True)
    hilo.start()
