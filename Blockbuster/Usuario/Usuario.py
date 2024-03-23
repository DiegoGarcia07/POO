class Usuario:
    def __init__(self, nombre, correo, teléfono, edad, fechaDeIngreso):
        self.nombre = nombre
        self._correo = correo
        self._teléfono = teléfono
        self._edad = edad
        self._fechaDeIngreso = fechaDeIngreso