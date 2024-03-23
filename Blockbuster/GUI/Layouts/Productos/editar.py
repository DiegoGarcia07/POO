import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Detalles del producto"
key = "__layout_gestionarProductos_editar"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Column([[sg.Frame("Datos del producto", [[sg.Column([
            [sg.Text("ID del producto:")],
            [sg.Input(border_width=1, disabled=True, key="input_productos_editar_id", size=(35,1))],
            [sg.Text("Tipo de producto:")],
            [sg.Radio("Película", "input_productos_editar_tipo", default=True, disabled=True, key="input_productos_editar_tipo_película"),
            sg.Radio("Serie", "input_productos_editar_tipo", disabled=True, key="input_productos_editar_tipo_serie")],
            [sg.Text("Nombre:")],
            [sg.Input(border_width=1, disabled=True, key="input_productos_editar_nombre", size=(35,1))],
            [sg.Column([
                [sg.Text("Año:")],
                [sg.Input(border_width=1, disabled=True, key="input_productos_editar_año", size=(7,1))]
            ]), sg.Column([
                [sg.Text("Género:")],
                [sg.Combo(["Acción", "Ficción", "Aventura", "Horror", "Infantil", "Romance", "Comedia", "Musical", "Documental", "Drama"], readonly=True, default_value="Acción", disabled=True, key="input_productos_editar_género", size=(22,1))]
            ])],
            [sg.Text("Precio de venta:")],
            [sg.Text("$"), sg.Input(border_width=1, key="input_productos_editar_precioDeVenta", size=(31,1))],
            [sg.Text("Precio de renta:")],
            [sg.Text("$"), sg.Input(border_width=1, key="input_productos_editar_precioDeRenta", size=(31,1))],
            [sg.Text("Disponible:")],
            [sg.Radio("Sí", "input_productos_editar_disponible", default=True, key="input_productos_editar_disponible_si"),
            sg.Radio("No", "input_productos_editar_disponible", key="input_productos_editar_disponible_no")],
            [sg.Text("Director:", key="input_productos_editar_datoextra_texto")],
            [sg.Input(border_width=1, disabled=True, key="input_productos_editar_datoextra", size=(35,1))]
        ],size=(300,200), scrollable=True, vertical_scroll_only=True)]])]],pad=(0,0)),
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("❌ Cancelar", k="btn_productos_editar_cancelar", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("✅ Guardar", k="btn_productos_editar_guardar", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def precarga(__ventana, GlobalTienda):
    infoProducto = GlobalTienda.listarProductos(__ventana.metadata)
    __ventana["input_productos_editar_id"].update(value = __ventana.metadata)
    __ventana["input_productos_editar_nombre"].update(value = infoProducto["nombre"])
    __ventana["input_productos_editar_año"].update(value = infoProducto["año"])
    __ventana["input_productos_editar_género"].update(value = infoProducto["género"])
    __ventana["input_productos_editar_precioDeVenta"].update(value = infoProducto["precioDeVenta"])
    __ventana["input_productos_editar_precioDeRenta"].update(value = infoProducto["precioDeRenta"])
    if infoProducto["tipo"] == "película":
        __ventana["input_productos_editar_datoextra_texto"].update(value = "Director:")
        __ventana["input_productos_editar_datoextra"].update(value = infoProducto["director"])
        __ventana["input_productos_editar_tipo_película"].update(value = True)
    else:
        __ventana["input_productos_editar_datoextra_texto"].update(value = "Temporada:")
        __ventana["input_productos_editar_datoextra"].update(value = infoProducto["temporada"])
        __ventana["input_productos_editar_tipo_serie"].update(value = True)
    if infoProducto["disponible"]:
        __ventana["input_productos_editar_disponible_si"].update(value = True)
    else:
        __ventana["input_productos_editar_disponible_no"].update(value = True)

def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_productos_editar_cancelar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarProductos_verdetalles")
    elif (event == "btn_productos_editar_guardar"):
        error = False
        campos = ["input_productos_editar_nombre", "input_productos_editar_año", "input_productos_editar_precioDeVenta", "input_productos_editar_precioDeRenta", "input_productos_editar_datoextra"]
        for campo in campos:
            if (__ventana[campo].get() == ""):
                error = True
                __ventana_aviso_actual = Recursos.__ventana_avisos("error", "⚠️", "Todos los campos son requeridos")
                while True:
                    event, values = __ventana_aviso_actual.read(timeout=100)
                    if event == "btn_aviso_ok" or event == sg.WIN_CLOSED:
                        break
                __ventana_aviso_actual.close()
                del(__ventana_aviso_actual)
                break
        if (not error):
            tipoProducto = ("película" if __ventana["input_productos_editar_tipo_película"].get() else "serie")
            datos = GlobalTienda.__alt_dict__(GlobalTienda._registrarProducto(tipoProducto,
                __ventana["input_productos_editar_nombre"].get(), __ventana["input_productos_editar_año"].get(),
                __ventana["input_productos_editar_género"].get(), float(__ventana["input_productos_editar_precioDeVenta"].get()), 
                float(__ventana["input_productos_editar_precioDeRenta"].get()), __ventana["input_productos_editar_disponible_si"].get(),
                director = (__ventana["input_productos_editar_datoextra"].get() if tipoProducto == "película" else None),
                temporada = (int(__ventana["input_productos_editar_datoextra"].get()) if tipoProducto == "serie" else None),
                registrar = False
            ))
            __ventana_aviso_actual = Recursos.__ventana_avisos("neutral", "⚠️", "¿Guardar cambios del producto?", "Sí", "No")
            guardado = False
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok":
                    guardado = True
                    break
                elif event == "btn_aviso_btn2" or event == sg.WIN_CLOSED:
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)

            if guardado:
                GlobalTienda._editarProducto(__ventana.metadata, datos)
                __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Cambios guardados")
                while True:
                    event, values = __ventana_aviso_actual.read(timeout=100)
                    if event == "btn_aviso_ok":
                        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarProductos_verdetalles")
                        break
                __ventana_aviso_actual.close()
                del(__ventana_aviso_actual)