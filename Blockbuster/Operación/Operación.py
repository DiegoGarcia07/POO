class Operación:
    def __init__(self, fecha, idDelProducto, idDelEmpleado, idDelSocio, precioFinal):
        self.fecha = fecha
        self._idDelProducto = idDelProducto
        self._idDelEmpleado = idDelEmpleado
        self._idDelSocio = idDelSocio
        self.precioFinal = precioFinal