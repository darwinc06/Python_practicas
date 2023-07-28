import sqlite3

# Conexion a la base de datos
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute(
    """
                CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    email TEXT
               )
                """
)

conn.commit()

# Crear Registro -> C
def crear_usuario(nombre: str, email) -> str:
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES(?, ?)", (nombre, email))
    conn.commit()
    return "Usuario Agregado"


# Obtener registros -> R
def obtener_registros() -> list:
    cursor.execute("SELECT id, nombre, email FROM usuarios")
    usuarios = cursor.fetchall()

    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append(usuario)
    
    return lista_usuarios


# Actualizar Usuario por id -> U
def actualizar_usuario(id: int, nombre: str, email: str) -> str:
    cursor.execute(
        "UPDATE usuarios SET nombre=?, email=?) WHERE id = ?", (nombre, email, id)
    )
    conn.commit()
    return "Usuario actualizado"


# Eliminar Usuario
def eliminar_usuario(id) -> str:
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    return "Usuario eliminado"


# Leer registro por su id
def obtener_usuario(id: int) -> list:
    cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()

    if usuario:
        return usuario
    return "Usuario no encontrado"


# # Crear usuario
# crear_usuario("Juan", "juan@gmail.com")
# crear_usuario("Marcos", "marcos@gmail.com")
# crear_usuario("Darwin", "darwin@gmail.com")