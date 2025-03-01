# Desarrollado por Juan Diego Cordero y Nelson Guerrero.

import json
from descarga import Descarga

class HistorialDescargas:
    def __init__(self):
        self.cola_descargas = []
        self.historial_completadas = []

    def cargar_descargas_desde_json(self, archivo_json):
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
            for descarga_data in datos:
                descarga = Descarga(
                    url=descarga_data['url'],
                    tamano=descarga_data['tamano'],
                    fecha_inicio=descarga_data['fecha_inicio'],
                    estado=descarga_data['estado']
                )
                if descarga.estado == 'completada':
                    self.historial_completadas.append(descarga)
                elif descarga.estado == 'pendiente' or descarga.estado == 'en_progreso':
                    self.cola_descargas.append(descarga)
        print("Descargas cargadas correctamente desde el archivo JSON.")

    def mostrar_descargas(self):
        print("\nDescargas en la cola (pendientes y en progreso):")
        for descarga in self.cola_descargas:
            print(f"{descarga.url} - {descarga.tamano} - {descarga.fecha_inicio} - {descarga.estado}")
        
        print("\nDescargas completadas:")
        for descarga in self.historial_completadas:
            print(f"{descarga.url} - {descarga.tamano} - {descarga.fecha_inicio} - {descarga.estado}")