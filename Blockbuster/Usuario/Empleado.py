from datetime import datetime
from Usuario.Usuario import Usuario

class Empleado(Usuario):
    def __init__(self, nombre, correo, teléfono, edad, fechaDeIngreso, sueldo):
        Usuario.__init__(self, nombre, correo, teléfono, edad, fechaDeIngreso)
        self.sueldo = sueldo

    def __dict__(self):
        return {
            "nombre": self.nombre,
            "correo": self._correo,
            "teléfono": self._teléfono,
            "edad": self._edad,
            "fechaDeIngreso": datetime.timestamp(self._fechaDeIngreso),
            "sueldo": self.sueldo
        }

    def mostrarVentas():
        pass

    def mostarRentas(vencidas):
        pass