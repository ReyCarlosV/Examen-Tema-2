import requests

# Clase para manejar la conexión a la API
class ExamenApi:
    def __init__(self, url):
        self.url = url

    def obtener_todos_los_registros(self):
        try:
            respuesta = requests.get(self.url)
            if respuesta.status_code == 200:
                registros = respuesta.json()
                return registros if registros else []
            else:
                return []
        except Exception as e:
            print(f"Error al obtener los datos: {e}")
            return []
