import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Detalles de la venta"
key = "__layout_gestionarVentas_verdetalles"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Column([[sg.Frame("Datos de la venta", [[sg.Column([
            [sg.Text("ID de la venta:")],
            [sg.Input(border_width=1, disabled=True, key="input_operaciones_ventas_verdetalles_id", size=(35,1))],
            [sg.Text("Producto vendido:")],
            [sg.Input(border_width=1, disabled=True, key="input_operaciones_ventas_verdetalles_producto", size=(35,1))],
            [sg.Text("Empleado que hizo la venta:")],
            [sg.Input(border_width=1, disabled=True, key="input_operaciones_ventas_verdetalles_empleado", size=(35,1))],
            [sg.Text("Socio:")],
            [sg.Input(border_width=1, disabled=True, key="input_operaciones_ventas_verdetalles_socio", size=(35,1))],
            [sg.Text("Cantidad:")],
            [sg.Input(border_width=1, disabled=True, key="input_operaciones_ventas_verdetalles_cantidad", size=(35,1))],
            [sg.Text("Precio final:")],
            [sg.Text("$"), sg.Input(border_width=1, disabled=True, key="input_operaciones_ventas_verdetalles_precio", size=(31,1))],
        ],size=(300,200), scrollable=True, vertical_scroll_only=True)]])]],pad=(0,0)),
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_operaciones_ventas_verdetalles_volver", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("❌ Cancelar venta", k="btn_operaciones_ventas_verdetalles_cancelar", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def precarga(__ventana, GlobalTienda):
    infoVenta = GlobalTienda.listarOperaciones("venta", __ventana.metadata)
    __ventana["input_operaciones_ventas_verdetalles_id"].update(value = __ventana.metadata)
    
    idDelEmpleado = infoVenta["idDelEmpleado"]
    empleadoVenta = GlobalTienda.listarUsuarios("empleado", infoVenta["idDelEmpleado"])
    nombreDelEmpleado = empleadoVenta.get("nombre") if empleadoVenta.get("nombre") is not None else "Empleado eliminado"

    idDelSocio = infoVenta["idDelSocio"]
    socioVenta = GlobalTienda.listarUsuarios("socio", infoVenta["idDelSocio"])
    nombreDelSocio = socioVenta.get("nombre") if socioVenta.get("nombre") is not None else "Socio eliminado"

    idDelProducto = infoVenta["idDelProducto"]
    productoVenta = GlobalTienda.listarProductos(infoVenta["idDelProducto"])
    nombreDelProducto = productoVenta.get("nombre") if productoVenta.get("nombre") is not None else "Producto eliminado"
    añoDelProducto = productoVenta.get("año") if productoVenta.get("año") is not None else "????"

    __ventana["input_operaciones_ventas_verdetalles_producto"].update(value = f"ID: {idDelProducto} - {nombreDelProducto} ({añoDelProducto})")
    __ventana["input_operaciones_ventas_verdetalles_empleado"].update(value = f"ID: {idDelEmpleado} - {nombreDelEmpleado}")
    __ventana["input_operaciones_ventas_verdetalles_socio"].update(value = f"ID: {idDelSocio} - {nombreDelSocio}")
    __ventana["input_operaciones_ventas_verdetalles_cantidad"].update(value = infoVenta["cantidad"])
    __ventana["input_operaciones_ventas_verdetalles_precio"].update(value = infoVenta["precioFinal"])


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_operaciones_ventas_verdetalles_volver"):
        __ventana.metadata = None
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarVentas_listar")
    elif (event == "btn_operaciones_ventas_verdetalles_cancelar"):
        __ventana_aviso_actual = Recursos.__ventana_avisos("neutral", "⚠️", "¿Cancelar venta?", "Sí", "No")
        eliminado = False
        while True:
            event, values = __ventana_aviso_actual.read(timeout=100)
            if event == "btn_aviso_ok":
                GlobalTienda._cancelarOperación("venta", __ventana.metadata)
                eliminado = True
                __ventana.metadata = None
                break
            elif event == "btn_aviso_btn2" or event == sg.WIN_CLOSED:
                break
        __ventana_aviso_actual.close()
        del(__ventana_aviso_actual)

        if eliminado:
            __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Venta cancelada")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok":
                    __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarVentas_listar")
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)