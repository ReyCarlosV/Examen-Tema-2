import tkinter as tk
from examenAPI import ExamenApi
from examenINTERFACE import ExamenInterfaz

# Clase para ejecutar el programa
class ExamenMain:
    def __init__(self):
        ventana = tk.Tk()
        api_service = ExamenApi("https://671be4242c842d92c381a59c.mockapi.io/Test")
        ExamenInterfaz(ventana, api_service)
        ventana.mainloop()

# Ejecutar el programa
if __name__ == "__main__":
    ExamenMain()
