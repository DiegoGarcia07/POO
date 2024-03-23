from datetime import datetime
from Usuario.Usuario import Usuario

class Socio(Usuario):
    def __init__(self, nombre, correo, teléfono, edad, fechaDeIngreso, VIP):
        Usuario.__init__(self, nombre, correo, teléfono, edad, fechaDeIngreso)
        self.VIP = VIP

    def __dict__(self):
        return {
            "nombre": self.nombre,
            "correo": self._correo,
            "teléfono": self._teléfono,
            "edad": self._edad,
            "fechaDeIngreso": datetime.timestamp(self._fechaDeIngreso),
            "VIP": self.VIP
        }

    def alterarVIP():
        pass

    def mostrarCompras():
        pass

    def mostrarrentas(vencidas):
        pass