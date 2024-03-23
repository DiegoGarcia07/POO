from datetime import datetime
import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Detalles de la renta"
key = "__layout_gestionarRentas_verdetalles"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Column([[sg.Frame("Datos de la renta", [[sg.Column([
            [sg.Text("ID de la renta:")],
            [sg.Input(border_width=1, disabled=True, key="input_operaciones_rentas_verdetalles_id", size=(35,1))],
            [sg.Text("Producto rentado:")],
            [sg.Input(border_width=1, disabled=True, key="input_operaciones_rentas_verdetalles_producto", size=(35,1))],
            [sg.Text("Empleado que registró la renta:")],
            [sg.Input(border_width=1, disabled=True, key="input_operaciones_rentas_verdetalles_empleado", size=(35,1))],
            [sg.Text("Socio:")],
            [sg.Input(border_width=1, disabled=True, key="input_operaciones_rentas_verdetalles_socio", size=(35,1))],
            [sg.Text("Fecha de devolución:")],
            [sg.Input(border_width=1, disabled=True, key="input_operaciones_rentas_verdetalles_devolución", size=(35,1))],
            [sg.Text("Precio final:")],
            [sg.Text("$"), sg.Input(border_width=1, disabled=True, key="input_operaciones_rentas_verdetalles_precio", size=(31,1))],
        ],size=(300,200), scrollable=True, vertical_scroll_only=True)]])]],pad=(0,0)),
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_operaciones_rentas_verdetalles_volver", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("📤 Concluir renta", k="btn_operaciones_rentas_verdetalles_concluida", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Button("❌ Cancelar renta", k="btn_operaciones_rentas_verdetalles_cancelar", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def precarga(__ventana, GlobalTienda):
    infoRenta = GlobalTienda.listarOperaciones("renta", __ventana.metadata)
    __ventana["input_operaciones_rentas_verdetalles_id"].update(value = __ventana.metadata)
    
    idDelEmpleado = infoRenta["idDelEmpleado"]
    empleadoRenta = GlobalTienda.listarUsuarios("empleado", infoRenta["idDelEmpleado"])
    nombreDelEmpleado = empleadoRenta.get("nombre") if empleadoRenta.get("nombre") is not None else "Empleado eliminado"

    idDelSocio = infoRenta["idDelSocio"]
    socioRenta = GlobalTienda.listarUsuarios("socio", infoRenta["idDelSocio"])
    nombreDelSocio = socioRenta.get("nombre") if socioRenta.get("nombre") is not None else "Socio eliminado"

    idDelProducto = infoRenta["idDelProducto"]
    productoRenta = GlobalTienda.listarProductos(infoRenta["idDelProducto"])
    nombreDelProducto = productoRenta.get("nombre") if productoRenta.get("nombre") is not None else "Producto eliminado"
    añoDelProducto = productoRenta.get("año") if productoRenta.get("año") is not None else "????"

    __ventana["input_operaciones_rentas_verdetalles_producto"].update(value = f"ID: {idDelProducto} - {nombreDelProducto} ({añoDelProducto})")
    __ventana["input_operaciones_rentas_verdetalles_empleado"].update(value = f"ID: {idDelEmpleado} - {nombreDelEmpleado}")
    __ventana["input_operaciones_rentas_verdetalles_socio"].update(value = f"ID: {idDelSocio} - {nombreDelSocio}")
    __ventana["input_operaciones_rentas_verdetalles_devolución"].update(value = infoRenta["fechaDeDevolución"])
    __ventana["input_operaciones_rentas_verdetalles_precio"].update(value = infoRenta["precioFinal"])

    if (type(infoRenta["fechaDeDevolución"]) is not type(True)):
        __ventana["btn_operaciones_rentas_verdetalles_concluida"].update(visible = False)
        __ventana["input_operaciones_rentas_verdetalles_devolución"].update(value = datetime.fromtimestamp(infoRenta["fechaDeDevolución"]).strftime('%Y-%m-%d %H:%M:%S'))
    else:
        __ventana["btn_operaciones_rentas_verdetalles_concluida"].update(visible = True)
        __ventana["input_operaciones_rentas_verdetalles_devolución"].update(value = "No ha sido devuelto")


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_operaciones_rentas_verdetalles_volver"):
        __ventana.metadata = None
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarRentas_listar")
    elif (event == "btn_operaciones_rentas_verdetalles_concluida"):
        __ventana_aviso_actual = Recursos.__ventana_avisos("neutral", "⚠️", "¿Marcar la renta como concluida?", "Sí", "No")
        concluido = False
        while True:
            event, values = __ventana_aviso_actual.read(timeout=100)
            if event == "btn_aviso_ok":
                GlobalTienda._concluirRenta(__ventana.metadata)
                concluido = True
                break
            elif event == "btn_aviso_btn2" or event == sg.WIN_CLOSED:
                break
        __ventana_aviso_actual.close()
        del(__ventana_aviso_actual)

        if concluido:
            __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Renta concluida")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok":
                    __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarRentas_verdetalles")
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)
    elif (event == "btn_operaciones_rentas_verdetalles_cancelar"):
        __ventana_aviso_actual = Recursos.__ventana_avisos("neutral", "⚠️", "¿Cancelar renta?", "Sí", "No")
        eliminado = False
        while True:
            event, values = __ventana_aviso_actual.read(timeout=100)
            if event == "btn_aviso_ok":
                GlobalTienda._cancelarOperación("renta", __ventana.metadata)
                eliminado = True
                __ventana.metadata = None
                break
            elif event == "btn_aviso_btn2" or event == sg.WIN_CLOSED:
                break
        __ventana_aviso_actual.close()
        del(__ventana_aviso_actual)

        if eliminado:
            __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Renta cancelada")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok":
                    __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarRentas_listar")
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)