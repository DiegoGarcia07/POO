from datetime import datetime
from Operación.Operación import Operación

class Renta(Operación):
    def __init__(self, fecha, idDelProducto, idDelEmpleado, idDelSocio, precioFinal, fechaDeDevolución):
        Operación.__init__(self, fecha, idDelProducto, idDelEmpleado, idDelSocio, precioFinal)
        self.fechaDeDevolución = fechaDeDevolución

    def __dict__(self):
        return {
            "fecha": datetime.timestamp(self.fecha),
            "idDelProducto": self._idDelProducto,
            "idDelEmpleado": self._idDelEmpleado,
            "idDelSocio": self._idDelSocio,
            "precioFinal": self.precioFinal,
            "fechaDeDevolución": self.fechaDeDevolución if (type(self.fechaDeDevolución) == type(True)) else datetime.timestamp(self.fechaDeDevolución)
        }