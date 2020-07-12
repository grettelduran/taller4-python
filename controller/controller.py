from database.base_datos import BaseDatos
from model.modelo import Jugador
from os import system, name


class Controller:
    def __init__(self):
        self.bd = BaseDatos()
        self.inicio()

    def inicio(self):
        print("Api Jugador:")

    def nuevo_jugador(self, usuario, contrasena, nombre, apellido, correo):
        jugador = Jugador(None, usuario, contrasena, nombre, apellido, correo)
        self.bd.registrar_jugador(jugador)
        return jugador

    def obtener_jugadores(self):
        return self.bd.get_all_rows_jugador()

    def login(self, usuario, contrasena):
        return self.bd.login(usuario, contrasena)
    def obtener_jugador(self, jugador_id):
        return self.bd.get_jugador_por_id(jugador_id)
