from archivo import cargar_tareas, guardar_tareas
from config_loggin import config_logging
from errores import verificar_id
from tareas import agregar_tarea, completar_tarea, eliminar_tarea

def mostrar_menu():
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Eliminar tarea")
    print("4. Mostrar tareas")
    print("5. Salir")

def main():
    config_logging()
    tareas = cargar_tareas()
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")
        
        if opcion == '1':
            descripcion = input("Descripcion de la tarea: ")
            prioridad = input("Prioridad (alta/media/baja): ")
            agregar_tarea(tareas, descripcion, prioridad)

        elif opcion == '2':
            id_tarea = input("ID de la tarea a completar: ")
            if id_tarea.isdigit():
                id_tarea = int(id_tarea)
                try:
                    verificar_id(tareas, id_tarea)
                    completar_tarea(tareas, id_tarea)
                except IndexError as e:
                    print(e)
            else:
                print("Por favor, ingresa un numero valido.")

        elif opcion == '3':
            try:
                id_tarea = int(input("ID de la tarea a eliminar: "))
                verificar_id(tareas, id_tarea)
                eliminar_tarea(tareas, id_tarea)
            except (IndexError, ValueError) as e:
                print(f"Error: {e}")

        elif opcion == '4':
            for idx, tarea in enumerate(tareas):
                print(f"{idx}. {tarea['descripcion']} - {tarea['estado']} - {tarea['prioridad']}")

        elif opcion == '5':
            guardar_tareas(tareas)
            break

        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    main()