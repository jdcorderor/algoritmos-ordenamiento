# Desarrollado por Juan Diego Cordero y Nelson Guerrero.

from historial_descargas import HistorialDescargas
from reporte import Reporte

historial = HistorialDescargas()
historial.cargar_descargas_desde_json('descargas.json')
reporte = Reporte(historial)
reporte.menu_reporte()