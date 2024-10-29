import requests

class getRecord:
    def __init__(self, url):
        self.url = url

    def obtener_todos_los_registros(self):
        try:
            # Hacer una solicitud GET a la API
            respuesta = requests.get(self.url)
            # Verificar si la solicitud fue exitosa
            if respuesta.status_code == 200:
                registros = respuesta.json()
                # Retornar todos los registros
                return registros if registros else []
            else:
                return []
        except Exception as e:
            print(f"Error al obtener los datos: {e}")
            return []
