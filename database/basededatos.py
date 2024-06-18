
#*Modulo de base de datos
import sqlite3

#*Conexion a la base de datos
conexion = sqlite3.connect('database_vine.db')

#*Cursor(Permite la ejecucion de comandos en SQL)
cursor = conexion.cursor()

#*Tabla para almacenar datos
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Vinos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    año INTERGER NOT NULL,
    edad INTEGER NOT NULL,
    linea TEXT NOT NULL,
    volumen REAL NOT NULL,
    stock INTEGER NOT NULL,
    precio REAL NOT NULL )''')


#//Funciones para gestionar la base de datos
#*F.Agregar Vino
def agregar_vino(nombre,tipo, año, edad, linea, volumen, stock, precio):
    with sqlite3.connect('database_vine.db') as conn:
        cursor.conn.cursor()
        cursor.execute(''' 
        INSERT INTO Vinos (
        nombre, 
        tipo, 
        año, 
        edad, 
        linea, 
        volumen, 
        stock, 
        precio)
        VALUES(?,?,?,?,?,?,?,?)''', (nombre, tipo, año, edad, linea, volumen, stock, precio))
        conn.commit()


#*F.Modificar Vinos
def modificar_vino(id, nombre = None, tipo = None, año = None, edad = None, linea = None, volumen = None, stock = None,precio = None):
    with sqlite3.connect('database_vine.db') as conn:
        cursor = conn.cursor()
        if nombre:
            cursor.execute('UPDATE Vinos SET nombre = ? WHERE id = ?',(nombre,id))
        if tipo:
            cursor.execute('UPDATE Vinos SET tipo = ? WHERE id = ?',(tipo,id))
        if año:
            cursor.execute('UPDATE Vinos SET año = ? WHERE id = ?',(año,id))
        if edad:
            cursor.execute('UPDATE Vinos SET edad = ? WHERE id = ?',(edad,id))
        if linea:
            cursor.execute('UPDATE Vinos SET linea = ? WHERE id = ?',(linea,id))
        if volumen:
            cursor.execute('UPDATE Vinos SET volumen = ? WHERE id = ?',(volumen,id))
        if stock:
            cursor.execute('UPDATE Vinos SET stock = ? WHERE id = ?',(stock,id))
        if precio:
            cursor.execute('UPDATE Vinos SET precio = ? WHERE id = ?',(precio,id))

#*F.Eliminar Vinos
def eliminar_vino(id):
    with sqlite3.connect('database_vine.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Vinos WHERE id = ?', (id))
        conn.commit()

#*f.Mostrar ultimos 3 vinos modificados
def mostrar_ultimos_3_vinos_modificados():
    with sqlite3.connect('database_vine.db') as conn:
        cursor = conn.cursor()
        cursor.execute(''' 
    SELEC * FROM Vinos
    ORDER BY id DESC
    LIMIT 3 ''')
    return cursor.fetchall()

#*F.Buscar vinos 
def buscar_vino(nombre):
    with sqlite3.connect('database_vine.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Vinos WHERE nombre LIKE ?',('%'+ nombre + '%'))
    return cursor.fetchall()

#*F.Mostrar lista de vinos
def mostrar_lista_de_vinos():
    with sqlite3.connect('database_vine.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Vinos')
        return cursor.fetchall()

#//F.Optimizacion (Funcion premiun)