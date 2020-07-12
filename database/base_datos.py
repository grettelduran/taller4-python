import sqlite3 as dba_object
from sqlite3 import Error
from model.modelo import Jugador
from os import system, name


class BaseDatos:
    def sqlite_create_database(self):
        try:
            conexion = dba_object.connect("taller4.db", check_same_thread=False)
            return conexion
        except Error as err:
            print(err)

    def create_table_jugador(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS jugador(_id INTEGER PRIMARY KEY, usuario TEXT NOT NULL UNIQUE, contrasena TEXT NOT NULL, nombre TEXT NOT NULL, apellido TEXT NOT NULL, correo TEXT NOT NULL UNIQUE)"
            )
            connection.commit()
        except Error as err:
            print(Error, "Debio ser en el query!", err)

    def registrar_jugador(self, objJugador):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute(
                "INSERT INTO jugador (usuario,contrasena,nombre,apellido, correo) VALUES(?,?,?,?,?);",
                [
                    objJugador.usuario,
                    objJugador.contrasena,
                    objJugador.nombre,
                    objJugador.apellido,
                    objJugador.correo,
                ],
            )
            self.objeto_conexion.commit()
            objJugador.id = cursor.lastrowid
            return objJugador
        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)
            return None

    def __init__(self):
        self.objeto_conexion = self.sqlite_create_database()
        self.create_table_jugador(self.objeto_conexion)

    def get_all_rows_jugador(self):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("SELECT * FROM jugador")
            objeto_resultado = cursor.fetchall()
            self.objeto_conexion.commit()
            jugadores = []
            for numero in range(0, len(objeto_resultado)):
                jugador = Jugador(
                    objeto_resultado[numero][0],
                    objeto_resultado[numero][1],
                    objeto_resultado[numero][2],
                    objeto_resultado[numero][3],
                    objeto_resultado[numero][4],
                    objeto_resultado[numero][5],
                )
                jugadores.append(jugador)
            return jugadores

        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)

    def get_jugador_por_id(self, jugador_id):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("SELECT * FROM jugador WHERE _id = ?", [jugador_id])
            objeto_resultado = cursor.fetchall()
            self.objeto_conexion.commit()
            if len(objeto_resultado) > 0:
                jugador = Jugador(
                    objeto_resultado[0][0],
                    objeto_resultado[0][1],
                    objeto_resultado[0][2],
                    objeto_resultado[0][3],
                    objeto_resultado[0][4],
                    objeto_resultado[0][5],
                )
                return jugador
            return None

        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)

    def login(self, usuario, contrasena):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute(
                "SELECT * FROM jugador WHERE usuario = ? and contrasena= ?",
                [usuario, contrasena],
            )
            objeto_resultado = cursor.fetchall()
            self.objeto_conexion.commit()
            if len(objeto_resultado) > 0:
                jugador = Jugador(
                    objeto_resultado[0][0],
                    objeto_resultado[0][1],
                    objeto_resultado[0][2],
                    objeto_resultado[0][3],
                    objeto_resultado[0][4],
                    objeto_resultado[0][5],
                )
                return jugador
            return None

        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)
