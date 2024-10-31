from tkinter import ttk

# Clase para la tabla (Treeview)
class ExamenTabla:
    def __init__(self, ventana):
        # Configurar la tabla para mostrar los datos
        self.tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Seleccion", "Equipo", "Minutos", "Goles"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Seleccion", text="Seleccion")
        self.tabla.heading("Equipo", text="Equipo")
        self.tabla.heading("Minutos", text="Minutos Jugados")
        self.tabla.heading("Goles", text="Anoto esta jornada")
        self.tabla.pack(pady=20, fill="x")

    def mostrar_registros(self, registros):
        # Limpiar la tabla antes de insertar nuevos datos
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Insertar cada registro en la tabla
        for registro in registros:
            self.tabla.insert("", "end", values=(registro['id'], registro['nombre'], registro['seleccion'], registro['equipo'], registro['minutos'], registro['goles']))

    def mostrar_registro(self, registro):
        # Limpiar la tabla y mostrar solo un registro
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Insertar el registro en la tabla
        self.tabla.insert("", "end", values=(registro['id'], registro['nombre'], registro['seleccion'], registro['equipo'], registro['minutos'], registro['goles']))
