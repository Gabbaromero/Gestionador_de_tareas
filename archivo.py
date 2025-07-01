import json
import os

def cargar_tareas(archivo='tareas.json'):
    if not os.path.exists(archivo):
        return []  
    
    with open(archivo, 'r') as f:
        return json.load(f)

def guardar_tareas(tareas, archivo='tareas.json'):
    with open(archivo, 'w') as f:
        json.dump(tareas, f)