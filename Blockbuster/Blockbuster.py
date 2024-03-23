from datetime import datetime               # Clase para manejar fechas
import os                                   # Clase para manejar archivos
import json                                 # Clase para manejar archivos JSON
from Operación.Venta import Venta           # Importar clases extendidas del proyecto
from Operación.Renta import Renta
from Producto.Producto import Producto
from Usuario.Empleado import Empleado
from Usuario.Socio import Socio


ubicaciónArchivoJSON = os.getcwd()+"\DatosTienda.json"      # Cambiar esto a la ubicación correcta

class Blockbuster:
    # Función para obtener diccionarios de otras clases
    def __alt_dict__(self, objeto):
        if (callable(objeto.__dict__)): return objeto.__dict__()
        else: return objeto.__dict__

    # Definimos el constructor de la mega clase, extrae la información del archivo .json
    def __init__(self):
        try:
            datos = json.load(open(ubicaciónArchivoJSON))
        except:
            datos = {}

        self.primerArranque = datos == {}       # Si no encontró los datos de la tienda, se ejecuta el primer arranque

        self.ID = datos.get("ID") or 1
        self.ubicación = datos.get("ubicación") or "Lugar feliz"
        self.usuarios = datos.get("usuarios") or {
            "socio": {}, "empleado": {}
        }
        self.productos = datos.get("productos") or {}
        self.operaciones = datos.get("operaciones") or {
            "venta": {}, "renta": {}
        }

    # Definimos el diccionario
    def __dict__(self):
        return {
            "ID": self.ID,
            "ubicación": self.ubicación,
            "usuarios": self.usuarios,
            "productos": self.productos,
            "operaciones": self.operaciones
        }

    # Función para almacenar los datos en el archivo .json
    def almacenarDatos(self):
        datos = open(ubicaciónArchivoJSON, "w")
        datos_json = json.dumps(self.__alt_dict__(self), indent=4)
        datos.write(datos_json)


    # Productos: registrar
    def _registrarProducto(self, tipo, nombre, año, género, precioDeVenta, precioDeRenta, disponible, director = None, temporada = None, registrar = True):
        productoPorRegistrar = Producto(tipo, nombre, año, género, precioDeVenta, precioDeRenta, disponible, director, temporada)
        if registrar: self.productos[str(len(self.productos))] = self.__alt_dict__(productoPorRegistrar)
        return productoPorRegistrar

    # Productos: listar
    def listarProductos(self, ID = None):
        if (ID == None):
            return self.productos
        else:
            ID = str(ID)
            return self.productos.get(ID)

    # Productos: editar
    def _editarProducto(self, ID, datos):
        ID = str(ID)
        if self.productos.get(ID):
            self.productos[ID] = datos

    # Productos: eliminar
    def _eliminarProducto(self, ID):
        ID = str(ID)
        if self.productos.get(ID): self.productos[ID] = {}


    # Usuarios: registrar
    def _registrarUsuario(self, tipo, nombre, correo, teléfono, edad, sueldo = None, VIP = None, registrar = True):
        if (tipo == "empleado"):
            usuarioPorRegistrar = Empleado(nombre, correo, teléfono, edad, datetime.now(), sueldo)
        elif (tipo == "socio"):
            usuarioPorRegistrar = Socio(nombre, correo, teléfono, edad, datetime.now(), VIP)
        
        if registrar: self.usuarios[tipo][str(len(self.usuarios[tipo]))] = self.__alt_dict__(usuarioPorRegistrar)
        return usuarioPorRegistrar

    # Usuarios: listar
    def listarUsuarios(self, tipo, ID = None):
        if (ID == None):
            return self.usuarios[tipo]
        else:
            ID = str(ID)
            return self.usuarios[tipo].get(ID)

    # Usuarios: editar
    def _editarUsuario(self, tipo, ID, datos):
        ID = str(ID)
        if self.usuarios[tipo].get(ID):
            self.usuarios[tipo][ID] = datos

    # Usuarios: eliminar
    def _eliminarUsuario(self, tipo, ID):
        ID = str(ID)
        if self.usuarios[tipo].get(ID): self.usuarios[tipo][ID] = {}

    
    # Operaciones: registrar
    def _registrarOperación(self, tipo, fecha, idDelProducto, idDelEmpleado, idDelSocio, precioFinal, cantidad = None, registrar = True):
        if (tipo == "venta"):
            operaciónPorRegistrar = Venta(fecha, idDelProducto, idDelEmpleado, idDelSocio, precioFinal, cantidad)
        elif (tipo == "renta"):
            operaciónPorRegistrar = Renta(fecha, idDelProducto, idDelEmpleado, idDelSocio, precioFinal, False)

        if registrar: self.operaciones[tipo][str(len(self.operaciones[tipo]))] = self.__alt_dict__(operaciónPorRegistrar)
        return operaciónPorRegistrar

    # Operaciones: listar
    def listarOperaciones(self, tipo, ID = None):
        if (ID == None):
            return self.operaciones[tipo]
        else:
            ID = str(ID)
            return self.operaciones[tipo].get(ID)

    # Operaciones: cancelar (eliminar)
    def _cancelarOperación(self, tipo, ID):
        ID = str(ID)
        if self.operaciones[tipo].get(ID): self.operaciones[tipo][ID] = {}

    # Rentas: concluir
    def _concluirRenta(self, ID):
        ID = str(ID)
        rentaPorConcluir = self.operaciones["renta"].get(ID)
        if (rentaPorConcluir.get("fechaDeDevolución") is not None):
            rentaPorConcluir = self.operaciones["renta"][ID]
            rentaPorConcluir["fechaDeDevolución"] = datetime.timestamp(datetime.now()) if (type(rentaPorConcluir["fechaDeDevolución"]) == type(True)) else rentaPorConcluir["fechaDeDevolución"]