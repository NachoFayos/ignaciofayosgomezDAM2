import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

# Colores personalizados
BG_COLOR = "#f8f9fa"  # Fondo claro
FRAME_COLOR = "#ffffff"  # Contenedores blancos
ACCENT_COLOR = "#007bff"  # Azul moderno para botones
HOVER_COLOR = "#0056b3"  # Azul oscuro al pasar el cursor
TEXT_COLOR = "#333333"  # Texto oscuro

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Base de Datos y Monitorización")
root.geometry("1000x700")
root.configure(bg=BG_COLOR)

# Aplicar estilos personalizados
style = ttk.Style()
style.theme_use("clam")

# Estilos para widgets
style.configure("TLabel", font=("Segoe UI", 11), background=BG_COLOR, foreground=TEXT_COLOR)
style.configure("TFrame", background=BG_COLOR)
style.configure("TButton", font=("Segoe UI", 10, "bold"), background=ACCENT_COLOR, foreground="white", padding=8)
style.configure("TCombobox", font=("Segoe UI", 10), padding=5)
style.configure("TNotebook", background=BG_COLOR, borderwidth=0)

# Crear Notebook (Pestañas en la interfaz)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# PESTAÑA 1: Base de Datos
db_frame = ttk.Frame(notebook, style="TFrame")
notebook.add(db_frame, text="Base de Datos")

# Sección de conexión a MySQL
frame_conexion = ttk.LabelFrame(db_frame, text="Conexión a MySQL", padding=10)
frame_conexion.pack(fill="x", padx=10, pady=10)

ttk.Label(frame_conexion, text="Host:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
host_entry = ttk.Entry(frame_conexion)
host_entry.grid(row=0, column=1, padx=5, pady=5)
host_entry.insert(0, "localhost")

ttk.Label(frame_conexion, text="Usuario:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
user_entry = ttk.Entry(frame_conexion)
user_entry.grid(row=1, column=1, padx=5, pady=5)
user_entry.insert(0, "root")

ttk.Label(frame_conexion, text="Contraseña:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
password_entry = ttk.Entry(frame_conexion, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)

# Conectar a MySQL
def conectar_mysql():
    try:
        global conn
        conn = mysql.connector.connect(
            host=host_entry.get(),
            user=user_entry.get(),
            password=password_entry.get()
        )
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in cursor.fetchall()]
        db_combobox["values"] = databases
        messagebox.showinfo("Conexión", "Conectado a MySQL con éxito")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error de conexión: {e}")

ttk.Button(frame_conexion, text="Conectar", command=conectar_mysql).grid(row=3, column=1, padx=5, pady=10)

# SELECCIÓN DE BASE DE DATOS, TABLAS Y COLUMNAS
frame_bd = ttk.LabelFrame(db_frame, text="Selección de Base de Datos y Tablas", padding=10)
frame_bd.pack(fill="x", padx=10, pady=5)

ttk.Label(frame_bd, text="Base de Datos:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
db_combobox = ttk.Combobox(frame_bd, state="readonly")
db_combobox.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_bd, text="Tabla:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
table_combobox = ttk.Combobox(frame_bd, state="readonly")
table_combobox.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_bd, text="Columna:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
column_combobox = ttk.Combobox(frame_bd, state="readonly")
column_combobox.grid(row=2, column=1, padx=5, pady=5)

# FUNCIONES PARA CARGAR TABLAS Y COLUMNAS
def cargar_tablas():
    try:
        conn.database = db_combobox.get()
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [tbl[0] for tbl in cursor.fetchall()]
        table_combobox["values"] = tables
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudieron cargar las tablas: {e}")

def cargar_columnas():
    try:
        cursor = conn.cursor()
        cursor.execute(f"SHOW COLUMNS FROM `{table_combobox.get()}`")
        columns = [col[0] for col in cursor.fetchall()]
        column_combobox["values"] = columns
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudieron cargar las columnas: {e}")

ttk.Button(frame_bd, text="Cargar Tablas", command=cargar_tablas).grid(row=0, column=2, padx=5, pady=5)
ttk.Button(frame_bd, text="Cargar Columnas", command=cargar_columnas).grid(row=1, column=2, padx=5, pady=5)

# SELECCIÓN DE GRÁFICOS
frame_columna = ttk.LabelFrame(db_frame, text="Opciones de Gráfico", padding=10)
frame_columna.pack(fill="x", padx=10, pady=5)

chart_types = ["Barras", "Anillo (Porcentajes)"]
chart_combobox = ttk.Combobox(frame_columna, values=chart_types, state="readonly")
chart_combobox.grid(row=0, column=1, padx=5, pady=5)
chart_combobox.set("Barras")

# GENERAR GRÁFICO
graph_frame = ttk.Frame(db_frame)
graph_frame.pack(fill="both", expand=True, padx=10, pady=10)

def generar_grafico():
    selected_table = table_combobox.get()
    selected_column = column_combobox.get()
    chart_type = chart_combobox.get()

    cursor = conn.cursor()
    cursor.execute(f"SELECT `{selected_column}` FROM `{selected_table}`")
    data = [row[0] for row in cursor.fetchall()]

    df = pd.DataFrame(data, columns=[selected_column])
    value_counts = df[selected_column].value_counts()

    fig, ax = plt.subplots(figsize=(8, 6))
    if chart_type == "Barras":
        value_counts.plot(kind="bar", ax=ax)
    elif chart_type == "Anillo (Porcentajes)":
        ax.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)

    ax.set_title(f"{chart_type} de {selected_column}")

    for widget in graph_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

ttk.Button(frame_columna, text="Generar Gráfico", command=generar_grafico).grid(row=0, column=2, padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()
