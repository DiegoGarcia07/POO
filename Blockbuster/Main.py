from Blockbuster import Blockbuster    # Importando la mega clase
import PySimpleGUI as sg    # Librería para interfaces gráficas de usuario
import GUI.recursos as Recursos     # Módulo para los elementos que son utilizados constantemente en este programa


sg.theme_add_new("Blockbuster", Recursos.tema_Blockbuster)   # Importamos el tema (definido en Recursos)
sg.theme("Blockbuster")     # Seleccionamos el tema

GlobalTienda = Blockbuster()    # Creamos la tienda, y automáticamente obtiene la información desde el archivo .json


# Diseño: menú principal y primer arranque
import GUI.Layouts.menuPrincipal as __layout_menuPrincipal
import GUI.Layouts.primerArranque as __layout_primerArranque

# Diseño: gestionar operaciones
import GUI.Layouts.Operaciones.gestionar as __layout_gestionarOperaciones
import GUI.Layouts.Operaciones.Ventas.gestionar as __layout_gestionarVentas
import GUI.Layouts.Operaciones.Ventas.registrar as __layout_gestionarVentas_registrar
import GUI.Layouts.Operaciones.Ventas.listar as __layout_gestionarVentas_listar
import GUI.Layouts.Operaciones.Ventas.verdetalles as __layout_gestionarVentas_verdetalles
import GUI.Layouts.Operaciones.Rentas.gestionar as __layout_gestionarRentas
import GUI.Layouts.Operaciones.Rentas.registrar as __layout_gestionarRentas_registrar
import GUI.Layouts.Operaciones.Rentas.listar as __layout_gestionarRentas_listar
import GUI.Layouts.Operaciones.Rentas.verdetalles as __layout_gestionarRentas_verdetalles

# Diseño: gestionar usuarios
import GUI.Layouts.Usuarios.gestionar as __layout_gestionarUsuarios
import GUI.Layouts.Usuarios.Empleados.gestionar as __layout_gestionarEmpleados
import GUI.Layouts.Usuarios.Empleados.añadir as __layout_gestionarEmpleados_añadir
import GUI.Layouts.Usuarios.Empleados.listar as __layout_gestionarEmpleados_listar
import GUI.Layouts.Usuarios.Empleados.verdetalles as __layout_gestionarEmpleados_verdetalles
import GUI.Layouts.Usuarios.Empleados.editar as __layout_gestionarEmpleados_editar
import GUI.Layouts.Usuarios.Socios.gestionar as __layout_gestionarSocios
import GUI.Layouts.Usuarios.Socios.añadir as __layout_gestionarSocios_añadir
import GUI.Layouts.Usuarios.Socios.listar as __layout_gestionarSocios_listar
import GUI.Layouts.Usuarios.Socios.verdetalles as __layout_gestionarSocios_verdetalles
import GUI.Layouts.Usuarios.Socios.editar as __layout_gestionarSocios_editar

# Diseño: gestionar productos
import GUI.Layouts.Productos.gestionar as __layout_gestionarProductos
import GUI.Layouts.Productos.añadir as __layout_gestionarProductos_añadir
import GUI.Layouts.Productos.listar as __layout_gestionarProductos_listar
import GUI.Layouts.Productos.verdetalles as __layout_gestionarProductos_verdetalles
import GUI.Layouts.Productos.editar as __layout_gestionarProductos_editar


# Diseño general
setattr(sg.Window, "__globales", globals())     # Añadimos a la clase las variables globales (GlobalTienda, y todos los diseños)
setattr(sg.Window, "__cambiarVentanas", Recursos.__cambiarVentanas)     # Añadimos a la clase la función para cambiar entre diseños
__ventana = sg.Window("Blockbuster: Menú principal", [
        Recursos.__layout_encabezado(GlobalTienda),
        [__layout_menuPrincipal.layout, __layout_primerArranque.layout, __layout_gestionarOperaciones.layout,
        __layout_gestionarVentas.layout, __layout_gestionarVentas_registrar.layout, __layout_gestionarVentas_listar.layout, __layout_gestionarVentas_verdetalles.layout,
        __layout_gestionarRentas.layout, __layout_gestionarRentas_registrar.layout, __layout_gestionarRentas_listar.layout, __layout_gestionarRentas_verdetalles.layout,
        __layout_gestionarUsuarios.layout,
        __layout_gestionarEmpleados.layout, __layout_gestionarEmpleados_añadir.layout, __layout_gestionarEmpleados_listar.layout, __layout_gestionarEmpleados_verdetalles.layout, __layout_gestionarEmpleados_editar.layout,
        __layout_gestionarSocios.layout, __layout_gestionarSocios_añadir.layout, __layout_gestionarSocios_listar.layout, __layout_gestionarSocios_verdetalles.layout, __layout_gestionarSocios_editar.layout,
        __layout_gestionarProductos.layout, __layout_gestionarProductos_añadir.layout,  __layout_gestionarProductos_listar.layout, __layout_gestionarProductos_verdetalles.layout, __layout_gestionarProductos_editar.layout
        ]
    ], finalize=True, keep_on_top=True)


# Detectar si es el primer arranque, y mostrar la pantalla
if GlobalTienda.primerArranque: __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_primerArranque")
else: __layout_menuPrincipal.precarga(__ventana, GlobalTienda)

# Programa
while True:
    event, values = __ventana.read(timeout=100)     # Abre la ventana del programa, y escucha por acciones cada 100ms
    if event == "btn_salir" or event == sg.WIN_CLOSED: break    # Romper el bucle si el usuario sale

    # Cada vez que se escuche un evento, llamar a las funciones de eventos de cada pantalla
    __layout_menuPrincipal.eventos(GlobalTienda, __ventana, event, values)
    __layout_primerArranque.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarOperaciones.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarVentas.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarVentas_registrar.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarVentas_listar.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarVentas_verdetalles.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarRentas.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarRentas_registrar.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarRentas_listar.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarRentas_verdetalles.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarUsuarios.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarEmpleados.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarEmpleados_añadir.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarEmpleados_listar.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarEmpleados_verdetalles.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarEmpleados_editar.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarSocios.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarSocios_añadir.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarSocios_listar.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarSocios_verdetalles.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarSocios_editar.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarProductos.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarProductos_añadir.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarProductos_listar.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarProductos_verdetalles.eventos(GlobalTienda, __ventana, event, values)
    __layout_gestionarProductos_editar.eventos(GlobalTienda, __ventana, event, values)

    __ventana.move_to_center()      # Constantemente mantener la ventana en el centro de la pantalla

__ventana.close()   # Roto el bucle, cerramos la ventana del programa
GlobalTienda.almacenarDatos()       # Guardamos todos los cambios realizados en el archivo .json

