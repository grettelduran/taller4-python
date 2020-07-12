from controller.controller import Controller
from model.modelo import Jugador
from flask import Flask, jsonify, request, make_response
import json

controller = Controller()
app = Flask(__name__)
app.config["SECRET_KEY"] = "mykey"
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False


@app.route("/")
def index():
    return "Sistema de Jugadores"


@app.route("/jugadores", methods=["POST"])
def insertar_jugador():
    if (
        not request.json
        or not "usuario" in request.json
        or not "contrasena" in request.json
        or not "nombre" in request.json
        or not "apellido" in request.json
        or not "correo" in request.json
    ):
        abort(400)
    jugador = controller.nuevo_jugador(
        request.json.get("usuario"),
        request.json.get("contrasena"),
        request.json.get("nombre"),
        request.json.get("apellido"),
        request.json.get("correo"),
    )
    return jsonify({"jugador": jugador.toJSON()}), 201


@app.route("/jugadores", methods=["GET"])
def obtener_jugadores():
    jugadores = controller.obtener_jugadores()
    jugadoresJSON = []
    for jugador in jugadores:
        jugadoresJSON.append(jugador.toJSON())
    return jsonify({"jugadores": jugadoresJSON}), 201


@app.route("/login", methods=["POST"])
def login():
    if (
        not request.json
        or not "usuario" in request.json
        or not "contrasena" in request.json
    ):
        abort(400)
    jugador = controller.login(
        request.json.get("usuario"), request.json.get("contrasena")
    )
    if jugador != None:
        return jsonify({"jugador": jugador.toJSON()}), 201
    return jsonify({"jugador": None}), 404
@app.route("/jugadores/<string:id_jugador>", methods=["GET"])
def get_jugador(id_jugador):
    jugador = controller.obtener_jugador(id_jugador)
    if jugador != None:
        return jsonify({"jugador": jugador.toJSON()}), 201
    return jsonify({"jugador": None}), 404
if __name__ == "__main__":
    app.run(debug=True)

