import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import random
from examen2 import getRecord

class App:
    def __init__(self, ventana):
        # Configuración de la ventana principal
        self.ventana = ventana
        self.ventana.title("Registros de Deportistas")
        self.ventana.geometry("1000x320")
        self.ventana.resizable(False, False)

        # Crear un objeto de la clase APIService
        self.api_service = getRecord("https://671be4242c842d92c381a59c.mockapi.io/Test")

        # Crear la tabla (Treeview) para mostrar los datos
        self.tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Seleccion", "Equipo", "Posicion"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Seleccion", text="Seleccion")
        self.tabla.heading("Equipo", text="Equipo")
        self.tabla.heading("Posicion", text="Posicion")
        self.tabla.pack(pady=20, fill="x")

        # Botón para actualizar los datos
        self.boton_actualizar = tk.Button(ventana, text="Actualizar", command=self.mostrar_registros)
        self.boton_actualizar.pack(side="left", padx=10, pady=10)

        # Botón para mostrar un registro aleatorio
        self.boton_aleatorio = tk.Button(ventana, text="Registro Aleatorio", command=self.mostrar_registro_aleatorio)
        self.boton_aleatorio.pack(side="left", padx=10, pady=10)

        # Botón para buscar un registro específico
        self.boton_buscar = tk.Button(ventana, text="Buscar Registro", command=self.buscar_registro)
        self.boton_buscar.pack(side="left", padx=10, pady=10)

        # Mostrar los registros al iniciar la aplicación
        self.mostrar_registros()

    def mostrar_registros(self):
        # Obtener todos los registros desde el APIService
        self.registros = self.api_service.obtener_todos_los_registros()

        # Limpiar la tabla antes de insertar nuevos datos
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Insertar cada registro en la tabla
        for registro in self.registros:
            self.tabla.insert("", "end", values=(registro['id'], registro['nombre'], registro['seleccion'], registro['equipo'], registro['posicion']))

    def mostrar_registro_aleatorio(self):
        # Seleccionar un registro aleatorio si hay registros disponibles
        if self.registros:
            registro_aleatorio = random.choice(self.registros)

            # Limpiar la tabla y mostrar solo el registro aleatorio
            for row in self.tabla.get_children():
                self.tabla.delete(row)

            # Insertar el registro aleatorio en la tabla
            self.tabla.insert("", "end", values=(registro_aleatorio['id'], registro_aleatorio['nombre'], registro_aleatorio['seleccion'], registro_aleatorio['equipo'], registro_aleatorio['posicion']))
        else:
            print("No hay registros para mostrar.")

    def buscar_registro(self):
        # Solicitar al usuario el ID del registro que quiere buscar
        id_buscar = simpledialog.askstring("Buscar Registro", "Ingrese el ID del registro:")

        if id_buscar:
            # Buscar el registro con el ID especificado
            registro_encontrado = next((registro for registro in self.registros if str(registro['id']) == id_buscar), None)

            if registro_encontrado:
                # Limpiar la tabla y mostrar solo el registro encontrado
                for row in self.tabla.get_children():
                    self.tabla.delete(row)

                # Insertar el registro encontrado en la tabla
                self.tabla.insert("", "end", values=(registro_encontrado['id'], registro_encontrado['nombre'], registro_encontrado['seleccion'], registro_encontrado['equipo'], registro_encontrado['posicion']))
            else:
                messagebox.showinfo("Registro no encontrado", f"No se encontró un registro con el ID {id_buscar}")

# Crear la ventana principal
if __name__ == "__main__":
    ventana = tk.Tk()
    app = App(ventana)
    ventana.mainloop()
