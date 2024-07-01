import sqlite3

#* Conectar a la base de datos (Se creará si no existe)
conn = sqlite3.connect('DATA_BASE_WINE.db')

#* Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

#// Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS vinos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    bodega TEXT NOT NULL,
    tipo TEXT NOT NULL,
    precio INTEGER NOT NULL,
    stock INTEGER NOT NULL
)
''')

#*Guardar cambios y cerrar la conexión
conn.commit()
conn.close()

#//Función para agregar datos
def agregar_datos():
    # Solicitar datos
    nombre = input("Nombre del vino: ")
    bodega = input("Bodega: ")
    tipo = input("Tipo: ")
    precio = int(input("Precio: "))
    stock = int(input("Stock: "))

    #*Conectar a la base de datos
    conn = sqlite3.connect('DATA_BASE_WINE.db')
    cursor = conn.cursor()

    #*Insertar datos en la tabla
    cursor.execute('''
    INSERT INTO vinos (nombre, bodega, tipo, precio, stock)
    VALUES (?, ?, ?, ?, ?)
    ''', (nombre, bodega, tipo, precio, stock))

    #*Guardar cambios y cerrar conexión
    conn.commit()
    conn.close()
    print("Datos almacenados con éxito")

#//Funcion para modificar datos
def modificar_datos():
    #*Conectar a la base de datos:
    conn = sqlite3.connect('DATA_BASE_WINE.db')
    cursor = conn.cursor()

    #*Solicitar el ID del registro a modificar
    id_vino = int(input("Ingrese el ID del vino que desea modificar: "))

    #*Solicitar nuevos datos
    nombre = input("Nuevo nombre del vino (Deje en blanco para no modificar): ") 
    bodega = input("Bodega (Deje en blanco para no modificar): ") 
    tipo = input("Tipo (Deje en blanco para no modificar): ") 
    precio = int(input("Precio(Deje en blanco para no modificar): ")) 
    stock = int(input("Stock (Deje en blanco para no modificar): ")) 
    #*crear una lista para almacenar los campos modificados
    campos_a_modificar = []
    valores = []
    #*Verificar y añadir los campos a modificar
    if nombre:
        campos_a_modificar.append("nombre = ?")
        valores.append(nombre)
    if bodega:
        campos_a_modificar.append("bodega = ?")
        valores.append(bodega)
    if tipo:
        campos_a_modificar.append("precio = ?")
        valores.append(tipo)
    if precio:
        campos_a_modificar.append("precio = ?")
        valores.append(int(precio))
    if stock:
        campos_a_modificar.append("stock = ?")
        valores.append(int(stock))
    #*Añadir el ID al final de la lista de valores
    valores.append(id_vino)
    #*construir la consulta SQL
    if campos_a_modificar:
        sql = f"UPDATE vinos SET {', '.join(campos_a_modificar)} WHERE id = ?"
        cursor.execute(sql, valores)
        conn.commit()
        print("Datos modificados con exito!")
    else:
        print("No se realizaron modificaciones")
    #*Cerrar la conexion
    conn.close()

modificar_datos()
