import json

class Jugador:
    def __init__(self, id, usuario, contrasena, nombre, apellido, correo):
        self.id = id
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)