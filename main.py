'''Crea un sistema básico de CRUD

Requisitos:

1. Base de datos: El sistema debe utilizar una base de datos para almacenar información sobre los libros, 
como título, autor, ISBN, género, etc. Se recomienda el uso de SQLite dada su simplicidad, aunque se permite el 
uso de alternativas como PostgreSQL o MySQL.

2. Interfaz de usuario: El sistema debe tener una interfaz de usuario simple que permite las operaciones 
típicas de un CRUD: Create, Read, Update, Delete. Opcional: se valorará positivamente el uso de alguna interfaz visual 
tipo PyQT5 y similares.

3. Funcionalidad adicional: El sistema debe permitir generar un listado. Se valora que se exporte a un formato legible 
como CSV.

4. Documentación: Debes proporcionar documentación clara y concisa que explique cómo funciona el sistema, 
cómo se ejecuta y cómo se pueden utilizar sus características.

5. Control de versiones y entorno virtual: Se debe utilizar un sistema de control de versiones, como Git, para realizar 
un seguimiento de las actualizaciones del código y colaborar en el desarrollo si se trabaja en grupo. 
Además deberá estar ubicado en un entorno virtual.

6. Presentación: Al final del proyecto, el alumnado debe presentar su aplicación y su funcionamiento ante el grupo y 
el profesor, destacando las características implementadas y los problemas superados.'''

import sqlite3
import csv
import os
videojuegos = []

def cargarDatosDeBaseDeDatos():
    if  not os.path.exists("baseDeDatos.db"):
        connect = sqlite3.connect("baseDeDatos.db")
        cursor = connect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS videojuegos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                plataforma TEXT NOT NULL,
                desarrollador TEXT NOT NULL,
                fecha_lanzamiento TEXT NOT NULL
            )''')
        connect.commit()
    else:
        connect = sqlite3.connect("baseDeDatos.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM videojuegos")
        videojuegos = cursor.fetchall()
        return videojuegos
    connect.close()

def anadirVideojuego(titulo, genero, plataforma, desarrollador, fechaLanzamiento):
    connect = sqlite3.connect("baseDeDatos.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO videojuegos (titulo, genero, plataforma, desarrollador, fecha_lanzamiento) VALUES (?, ?, ?, ?, ?)", (titulo, genero, plataforma, desarrollador, fechaLanzamiento))
    connect.commit()
    connect.close()
    cargarDatosDeBaseDeDatos()

def actualizarVideojuego(id, titulo, genero, plataforma, desarrollador, fechaLanzamiento):
    connect = sqlite3.connect("baseDeDatos.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE videojuegos SET titulo = ?, genero = ?, plataforma = ?, desarrollador = ?, fecha_lanzamiento = ? WHERE id = ?", (titulo, genero, plataforma, desarrollador, fechaLanzamiento, id))
    connect.commit()
    connect.close()
    cargarDatosDeBaseDeDatos()

def eliminarVideojuego(id):
    connect = sqlite3.connect("baseDeDatos.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM videojuegos WHERE id = ?", (id))
    connect.commit()
    connect.close()

def mostrarVideojuegos():
    videojuegos = cargarDatosDeBaseDeDatos()
    print("\nLista de Videojuegos")
    if videojuegos:
        for juego in videojuegos:
            print(f"ID: {juego[0]}, Título: {juego[1]}, Género: {juego[2]}, Plataforma: {juego[3]}, Desarrollador: {juego[4]}, Fecha de Lanzamiento: {juego[5]}")
    else:
        print("No hay videojuegos en la base de datos.")

def exportarACSV():
    videojuegos = cargarDatosDeBaseDeDatos()
    with open("videojuegos.csv", "w", encoding="UTF-8", newline="") as archivoCSV:
        escritor = csv.writer(archivoCSV)
        escritor.writerow(["ID", "Título", "Género", "Plataforma", "Desarrollador", "Fecha de Lanzamiento"])
        for juego in videojuegos:
            escritor.writerow(juego)
    print("Exportado a videojuegos.csv exitosamente.")

def imprimirMenu():
    print("\nInterfaz de Videojuegos")
    print("1. Ver videojuegos")
    print("2. Añadir videojuego")
    print("3. Actualizar videojuego")
    print("4. Eliminar videojuego")
    print("5. Exportar a CSV")
    print("6. Salir")

def main():
    while True:
        
        imprimirMenu()
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case '1':
                mostrarVideojuegos()
            
            case '2':
                titulo = input("Ingresa el título: ")
                genero = input("Ingresa el género: ")
                plataforma = input("Ingresa la plataforma: ")
                desarrollador = input("Ingresa el desarrollador: ")
                fecha_lanzamiento = input("Ingresa la fecha de lanzamiento (en formato dd-mm-aaaa): ")
                anadirVideojuego(titulo, genero, plataforma, desarrollador, fecha_lanzamiento)
            
            case '3':
                id = input("Ingresa el ID del videojuego a actualizar: ")
                titulo = input("Ingresa el nuevo título: ")
                genero = input("Ingresa el nuevo género: ")
                plataforma = input("Ingresa la nueva plataforma: ")
                desarrollador = input("Ingresa el nuevo desarrollador: ")
                fecha_lanzamiento = input("Ingresa la nueva fecha de lanzamiento (en formato dd-mm-aaaa): ")
                actualizarVideojuego(id, titulo, genero, plataforma, desarrollador, fecha_lanzamiento)
            
            case '4':
                id = input("Ingresa el ID del videojuego a eliminar: ")
                eliminarVideojuego(id)
            
            case '5':
                exportarACSV()
            
            case '6':
                print("saliendo de este programa tan estupendo")
                break
            
            case _:
                print("La opción introducida no es válida")

main()