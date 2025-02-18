import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("tienda.db")
cursor = conn.cursor()

# Crear la tabla de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefono TEXT
)
''')

# Crear la tabla de productos
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')

# Crear la tabla de compras
cursor.execute('''
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    total REAL NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
)
''')

# Insertar datos de ejemplo en clientes
cursor.executemany('''
INSERT INTO clientes (nombre, email, telefono) VALUES (?, ?, ?)
''', [
    ("Juan Pérez", "juan.perez@email.com", "123456789"),
    ("María López", "maria.lopez@email.com", "987654321"),
    ("Carlos Gómez", "carlos.gomez@email.com", "456123789")
])

# Insertar datos de ejemplo en productos
cursor.executemany('''
INSERT INTO productos (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)
''', [
    ("Laptop", "Electrónica", 1200.99, 10),
    ("Mouse", "Accesorios", 25.50, 50),
    ("Teclado", "Accesorios", 45.75, 30),
    ("Monitor", "Electrónica", 250.00, 15)
])

# Insertar datos de ejemplo en compras
cursor.executemany('''
INSERT INTO compras (cliente_id, producto_id, cantidad, fecha, total) VALUES (?, ?, ?, ?, ?)
''', [
    (1, 1, 1, "2024-03-10", 1200.99),
    (2, 2, 2, "2024-03-11", 51.00),
    (3, 3, 1, "2024-03-12", 45.75),
    (1, 4, 1, "2024-03-13", 250.00)
])

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
