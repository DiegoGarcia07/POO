from datetime import datetime
import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Detalles del empleado"
key = "__layout_gestionarEmpleados_verdetalles"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Column([[sg.Frame("Datos del empleado", [[sg.Column([
            [sg.Text("ID del usuario:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_empleados_verdetalles_id", size=(35,1))],
            [sg.Text("Nombre completo:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_empleados_verdetalles_nombre", size=(35,1))],
            [sg.Text("Correo electrónico:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_empleados_verdetalles_correo", size=(35,1))],
            [sg.Text("Número de teléfono:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_empleados_verdetalles_teléfono", size=(35,1))],
            [sg.Text("Edad:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_empleados_verdetalles_edad", size=(29,1)), sg.Text("años")],
            [sg.Text("Sueldo:")],
            [sg.Text("$"), sg.Input(border_width=1, disabled=True, key="input_usuarios_empleados_verdetalles_sueldo", size=(31,1))],
        ],size=(300,200), scrollable=True, vertical_scroll_only=True)]])]],pad=(0,0)),
        sg.Column([[sg.Frame("Productos vendidos:", [[sg.Column([[sg.Listbox([],
            key="input_usuarios_empleados_verdetalles_productosvendidos", size=(45,10)),]],size=(380,200))]])]],pad=(0,0))
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_usuarios_empleados_verdetalles_volver", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("🗑️ Eliminar", k="btn_usuarios_empleados_verdetalles_eliminar", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Button("✏️ Editar", k="btn_usuarios_empleados_verdetalles_editar", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def precarga(__ventana, GlobalTienda):
    infoUsuario = GlobalTienda.listarUsuarios("empleado", __ventana.metadata)
    __ventana["input_usuarios_empleados_verdetalles_id"].update(value = __ventana.metadata)
    __ventana["input_usuarios_empleados_verdetalles_nombre"].update(value = infoUsuario["nombre"])
    __ventana["input_usuarios_empleados_verdetalles_correo"].update(value = infoUsuario["correo"])
    __ventana["input_usuarios_empleados_verdetalles_teléfono"].update(value = infoUsuario["teléfono"])
    __ventana["input_usuarios_empleados_verdetalles_edad"].update(value = infoUsuario["edad"])
    __ventana["input_usuarios_empleados_verdetalles_sueldo"].update(value = infoUsuario["sueldo"])
    
    ventas = GlobalTienda.listarOperaciones("venta")
    ventas_f = []
    for venta in ventas:
        if (ventas[venta].get("fecha") is not None):
            if (str(ventas[venta].get("idDelEmpleado")) == str(__ventana.metadata)):
                productoVendido = GlobalTienda.listarProductos(ventas[venta]["idDelProducto"])
                nombre = productoVendido.get("nombre") if productoVendido.get("nombre") is not None else "Producto eliminado"
                año = productoVendido.get("año") if productoVendido.get("año") is not None else "????"
                fecha = datetime.fromtimestamp(ventas[venta]["fecha"]).strftime('%Y-%m-%d %H:%M:%S')
                ventas_f.append(f"ID: {venta} - {fecha} - {nombre} ({año})")

    __ventana["input_usuarios_empleados_verdetalles_productosvendidos"].update(values = ventas_f)


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_usuarios_empleados_verdetalles_volver"):
        __ventana.metadata = None
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarEmpleados_listar")
    elif (event == "btn_usuarios_empleados_verdetalles_editar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarEmpleados_editar")
    elif (event == "btn_usuarios_empleados_verdetalles_eliminar"):
        __ventana_aviso_actual = Recursos.__ventana_avisos("neutral", "⚠️", "¿Eliminar empleado?", "Sí", "No")
        eliminado = False
        while True:
            event, values = __ventana_aviso_actual.read(timeout=100)
            if event == "btn_aviso_ok":
                GlobalTienda._eliminarUsuario("empleado", __ventana.metadata)
                eliminado = True
                __ventana.metadata = None
                break
            elif event == "btn_aviso_btn2" or event == sg.WIN_CLOSED:
                break
        __ventana_aviso_actual.close()
        del(__ventana_aviso_actual)

        if eliminado:
            __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Empleado eliminado")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok":
                    __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarEmpleados_listar")
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)