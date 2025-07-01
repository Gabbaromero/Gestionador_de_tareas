from config_loggin import registrar_accion

def agregar_tarea(tareas, descripcion, prioridad):
    tareas.append({"descripcion": descripcion, "prioridad": prioridad, "estado": "pendiente"})
    registrar_accion('Agregar Tarea', descripcion)
    if prioridad not in ['alta', 'media', 'baja']:
        raise ValueError("Prioridad no válida. Debe ser: alta, media o baja.")


def completar_tarea(tareas, id_tarea):
    tarea = tareas[id_tarea]
    tarea['estado'] = 'completada'
    registrar_accion('Completar Tarea', tarea['descripcion'])

def eliminar_tarea(tareas, id_tarea):
    tarea = tareas.pop(id_tarea)
    registrar_accion('Eliminar Tarea', tarea['descripcion'])

