import tkinter as tk
from tkinter import simpledialog, messagebox
from examenTABLE import ExamenTabla

# Clase para la interfaz de usuario y los botones
class ExamenInterfaz:
    def __init__(self, ventana, api_service):
        self.ventana = ventana
        self.api_service = api_service
        self.ventana.title("Registros de Deportistas")
        self.ventana.geometry("1000x320")
        self.ventana.resizable(False, False)

        # Crear una instancia de la tabla
        self.tabla = ExamenTabla(ventana)

        # Botón para actualizar los datos
        self.boton_actualizar = tk.Button(ventana, text="Actualizar", command=self.mostrar_registros)
        self.boton_actualizar.pack(side="left", padx=10, pady=10)

        # Botón para buscar un registro específico
        self.boton_buscar = tk.Button(ventana, text="Buscar Registro", command=self.buscar_registro)
        self.boton_buscar.pack(side="left", padx=10, pady=10)

        # Mostrar los registros al iniciar la aplicación
        self.mostrar_registros()

    def mostrar_registros(self):
        # Obtener todos los registros desde el API
        registros = self.api_service.obtener_todos_los_registros()
        self.tabla.mostrar_registros(registros)

    def buscar_registro(self):
        # Solicitar al usuario el ID del registro que quiere buscar
        id_buscar = simpledialog.askstring("Buscar Registro", "Ingrese el ID del registro:")

        if id_buscar:
            # Obtener todos los registros y buscar el registro con el ID especificado
            registros = self.api_service.obtener_todos_los_registros()
            registro_encontrado = next((registro for registro in registros if str(registro['id']) == id_buscar), None)

            if registro_encontrado:
                # Mostrar solo el registro encontrado en la tabla
                self.tabla.mostrar_registro(registro_encontrado)
            else:
                messagebox.showinfo("Registro no encontrado", f"No se encontró un registro con el ID {id_buscar}")
