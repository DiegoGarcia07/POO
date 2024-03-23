import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Detalles del producto"
key = "__layout_gestionarProductos_verdetalles"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Column([[sg.Frame("Datos del producto", [[sg.Column([
            [sg.Text("ID del producto:")],
            [sg.Input(border_width=1, disabled=True, key="input_productos_verdetalles_id", size=(35,1))],
            [sg.Text("Tipo de producto:")],
            [sg.Radio("Película", "input_productos_verdetalles_tipo", default=True, disabled=True, key="input_productos_verdetalles_tipo_película"),
            sg.Radio("Serie", "input_productos_verdetalles_tipo", disabled=True, key="input_productos_verdetalles_tipo_serie")],
            [sg.Text("Nombre:")],
            [sg.Input(border_width=1, disabled=True, key="input_productos_verdetalles_nombre", size=(35,1))],
            [sg.Column([
                [sg.Text("Año:")],
                [sg.Input(border_width=1, disabled=True, key="input_productos_verdetalles_año", size=(7,1))]
            ]), sg.Column([
                [sg.Text("Género:")],
                [sg.Combo(["Acción", "Ficción", "Aventura", "Horror", "Infantil", "Romance", "Comedia", "Musical", "Documental", "Drama"], readonly=True, default_value="Acción", disabled=True, key="input_productos_verdetalles_género", size=(22,1))]
            ])],
            [sg.Text("Precio de venta:")],
            [sg.Text("$"), sg.Input(border_width=1, disabled=True, key="input_productos_verdetalles_precioDeVenta", size=(31,1))],
            [sg.Text("Precio de renta:")],
            [sg.Text("$"), sg.Input(border_width=1, disabled=True, key="input_productos_verdetalles_precioDeRenta", size=(31,1))],
            [sg.Text("Disponible:")],
            [sg.Radio("Sí", "input_productos_verdetalles_disponible", default=True, disabled=True, key="input_productos_verdetalles_disponible_si"),
            sg.Radio("No", "input_productos_verdetalles_disponible", disabled=True, key="input_productos_verdetalles_disponible_no")],
            [sg.Text("Director:", key="input_productos_verdetalles_datoextra_texto")],
            [sg.Input(border_width=1, disabled=True, key="input_productos_verdetalles_datoextra", size=(35,1))]
        ],size=(300,200), scrollable=True, vertical_scroll_only=True)]])]],pad=(0,0)),
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_productos_verdetalles_volver", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("🗑️ Eliminar", k="btn_productos_verdetalles_eliminar", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Button("✏️ Editar", k="btn_productos_verdetalles_editar", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def precarga(__ventana, GlobalTienda):
    infoProducto = GlobalTienda.listarProductos(__ventana.metadata)
    __ventana["input_productos_verdetalles_id"].update(value = __ventana.metadata)
    __ventana["input_productos_verdetalles_nombre"].update(value = infoProducto["nombre"])
    __ventana["input_productos_verdetalles_año"].update(value = infoProducto["año"])
    __ventana["input_productos_verdetalles_género"].update(value = infoProducto["género"])
    __ventana["input_productos_verdetalles_precioDeVenta"].update(value = infoProducto["precioDeVenta"])
    __ventana["input_productos_verdetalles_precioDeRenta"].update(value = infoProducto["precioDeRenta"])
    if infoProducto["tipo"] == "película":
        __ventana["input_productos_verdetalles_datoextra_texto"].update(value = "Director:")
        __ventana["input_productos_verdetalles_datoextra"].update(value = infoProducto["director"])
        __ventana["input_productos_verdetalles_tipo_película"].update(value = True)
    else:
        __ventana["input_productos_verdetalles_datoextra_texto"].update(value = "Temporada:")
        __ventana["input_productos_verdetalles_datoextra"].update(value = infoProducto["temporada"])
        __ventana["input_productos_verdetalles_tipo_serie"].update(value = True)
    if infoProducto["disponible"]:
        __ventana["input_productos_verdetalles_disponible_si"].update(value = True)
    else:
        __ventana["input_productos_verdetalles_disponible_no"].update(value = True)


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_productos_verdetalles_volver"):
        __ventana.metadata = None
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarProductos_listar")
    elif (event == "btn_productos_verdetalles_editar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarProductos_editar")
    elif (event == "btn_productos_verdetalles_eliminar"):
        __ventana_aviso_actual = Recursos.__ventana_avisos("neutral", "⚠️", "¿Eliminar producto?", "Sí", "No")
        eliminado = False
        while True:
            event, values = __ventana_aviso_actual.read(timeout=100)
            if event == "btn_aviso_ok":
                GlobalTienda._eliminarProducto(__ventana.metadata)
                eliminado = True
                __ventana.metadata = None
                break
            elif event == "btn_aviso_btn2" or event == sg.WIN_CLOSED:
                break
        __ventana_aviso_actual.close()
        del(__ventana_aviso_actual)

        if eliminado:
            __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Producto eliminado")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok":
                    __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarProductos_listar")
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)