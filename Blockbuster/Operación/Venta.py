from datetime import datetime
from Operación.Operación import Operación

class Venta(Operación):
    def __init__(self, fecha, idDelProducto, idDelEmpleado, idDelSocio, precioFinal, cantidad):
        Operación.__init__(self, fecha, idDelProducto, idDelEmpleado, idDelSocio, precioFinal)
        self.cantidad = cantidad

    def __dict__(self):
        return {
            "fecha": datetime.timestamp(self.fecha),
            "idDelProducto": self._idDelProducto,
            "idDelEmpleado": self._idDelEmpleado,
            "idDelSocio": self._idDelSocio,
            "precioFinal": self.precioFinal,
            "cantidad": self.cantidad
        }