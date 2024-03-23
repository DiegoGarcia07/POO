from datetime import datetime
import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Detalles del socio"
key = "__layout_gestionarSocios_verdetalles"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Column([[sg.Frame("Datos del socio", [[sg.Column([
            [sg.Text("ID del usuario:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_socios_verdetalles_id", size=(35,1))],
            [sg.Text("Nombre completo:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_socios_verdetalles_nombre", size=(35,1))],
            [sg.Text("Correo electrónico:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_socios_verdetalles_correo", size=(35,1))],
            [sg.Text("Número de teléfono:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_socios_verdetalles_teléfono", size=(35,1))],
            [sg.Text("Edad:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_socios_verdetalles_edad", size=(29,1)), sg.Text("años")],
            [sg.Text("VIP:")],
            [sg.Radio("Sí", "input_usuarios_socios_verdetalles_vip", disabled = True, key="input_usuarios_socios_verdetalles_vip_si"),
            sg.Radio("No", "input_usuarios_socios_verdetalles_vip", disabled = True, key="input_usuarios_socios_verdetalles_vip_no")]
        ],size=(300,200), scrollable=True, vertical_scroll_only=True)]])]],pad=(0,0)),
        sg.Column([[sg.Frame("Historial de compras:", [[sg.Column([[sg.Listbox([],
            key="input_usuarios_socios_verdetalles_historialcompras", size=(45,5)),]],size=(380,100))]])],
            [sg.Frame("Historial de rentas:", [[sg.Column([[sg.Listbox([],
            key="input_usuarios_socios_verdetalles_historialrentas", size=(45,5)),]],size=(380,100))]])]],pad=(0,0))
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_usuarios_socios_verdetalles_volver", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("🗑️ Eliminar", k="btn_usuarios_socios_verdetalles_eliminar", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Button("✏️ Editar", k="btn_usuarios_socios_verdetalles_editar", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def precarga(__ventana, GlobalTienda):
    infoUsuario = GlobalTienda.listarUsuarios("socio", __ventana.metadata)
    __ventana["input_usuarios_socios_verdetalles_id"].update(value = __ventana.metadata)
    __ventana["input_usuarios_socios_verdetalles_nombre"].update(value = infoUsuario["nombre"])
    __ventana["input_usuarios_socios_verdetalles_correo"].update(value = infoUsuario["correo"])
    __ventana["input_usuarios_socios_verdetalles_teléfono"].update(value = infoUsuario["teléfono"])
    __ventana["input_usuarios_socios_verdetalles_edad"].update(value = infoUsuario["edad"])
    if infoUsuario["VIP"]:
        __ventana["input_usuarios_socios_verdetalles_vip_si"].update(value = True)
    else:
        __ventana["input_usuarios_socios_verdetalles_vip_no"].update(value = True)

    def buscarOperaciones(tipo):
        operaciones_f = []
        operaciones = GlobalTienda.listarOperaciones(tipo)
        for operación in operaciones:
            if (operaciones[operación].get("fecha") is not None):
                if (str(operaciones[operación].get("idDelSocio")) == str(__ventana.metadata)):
                    productoVendido = GlobalTienda.listarProductos(operaciones[operación]["idDelProducto"])
                    nombre = productoVendido.get("nombre") if productoVendido.get("nombre") is not None else "Producto eliminado"
                    año = productoVendido.get("año") if productoVendido.get("año") is not None else "????"
                    fecha = datetime.fromtimestamp(operaciones[operación]["fecha"]).strftime('%Y-%m-%d %H:%M:%S')
                    operaciones_f.append(f"ID: {operación} - {fecha} - {nombre} ({año})")
        return operaciones_f

    __ventana["input_usuarios_socios_verdetalles_historialcompras"].update(values = buscarOperaciones("venta"))
    __ventana["input_usuarios_socios_verdetalles_historialrentas"].update(values = buscarOperaciones("renta"))


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_usuarios_socios_verdetalles_volver"):
        __ventana.metadata = None
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarSocios_listar")
    elif (event == "btn_usuarios_socios_verdetalles_editar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarSocios_editar")
    elif (event == "btn_usuarios_socios_verdetalles_eliminar"):
        __ventana_aviso_actual = Recursos.__ventana_avisos("neutral", "⚠️", "¿Eliminar socio?", "Sí", "No")
        eliminado = False
        while True:
            event, values = __ventana_aviso_actual.read(timeout=100)
            if event == "btn_aviso_ok":
                GlobalTienda._eliminarUsuario("socio", __ventana.metadata)
                eliminado = True
                __ventana.metadata = None
                break
            elif event == "btn_aviso_btn2" or event == sg.WIN_CLOSED:
                break
        __ventana_aviso_actual.close()
        del(__ventana_aviso_actual)

        if eliminado:
            __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Socio eliminado")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok":
                    __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarSocios_listar")
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)