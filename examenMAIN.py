import tkinter as tk
from examenAPI import ExamenApi
from examenINTERFACE import ExamenInterfaz

# Crear la ventana principal
ventana = tk.Tk()

# Instanciar la API para obtener los datos
api_service = ExamenApi("https://671be4242c842d92c381a59c.mockapi.io/Test")

# Inicializar la interfaz y pasar la ventana y el servicio API
app = ExamenInterfaz(ventana, api_service)

# Ejecutar la aplicación
ventana.mainloop()
