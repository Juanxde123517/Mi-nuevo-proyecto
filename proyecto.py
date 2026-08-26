import json
from datetime import datetime

#Class Tarea
class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento= fecha_vencimiento
        self.completado = False #Hasta que nosotros no le demos una indicación de que está completado, debe mantenerse en falso (sin completar)

    def marcar_completada(self):
        self.completado = True

    def editar_tarea(self, nuevo_titulo, nueva_descripcion, nueva_fecha):
        self.nuevo_titulo = nuevo_titulo
        self.nueva_descripcion = nueva_descripcion
        self.fecha_vencimiento = nueva_fecha

#Class Usuario
class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.nombre_usuario = contraseña
        self.tareas = []

    def agregar_tareas(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, titulo_tarea):
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo_tarea]
        #Recorre toda la lista de tareas hasta llegar a la tarea que tenga el titulo igual al ingresado

    def obtener_tareas(Self):
        return self.tareas
        