import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Añadir producto"
key = "__layout_gestionarProductos_añadir"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Column([[sg.Frame("Datos del producto", [[sg.Column([
            [sg.Text("Tipo de producto:")],
            [sg.Radio("Película", "input_productos_añadir_tipo", default=True, enable_events=True, key="input_productos_añadir_tipo_película"),
            sg.Radio("Serie", "input_productos_añadir_tipo", enable_events=True, key="input_productos_añadir_tipo_serie")],
            [sg.Text("Nombre:")],
            [sg.Input(border_width=1, key="input_productos_añadir_nombre", enable_events=True, size=(35,1))],
            [sg.Column([
                [sg.Text("Año:")],
                [sg.Input(border_width=1, key="input_productos_añadir_año", enable_events=True, size=(7,1))]
            ]), sg.Column([
                [sg.Text("Género:")],
                [sg.Combo(["Acción", "Ficción", "Aventura", "Horror", "Infantil", "Romance", "Comedia", "Musical", "Documental", "Drama"], readonly=True, default_value="Acción", key="input_productos_añadir_género", size=(22,1))]
            ])],
            [sg.Text("Precio de venta:")],
            [sg.Text("$"), sg.Input(border_width=1, key="input_productos_añadir_precioDeVenta", enable_events=True, size=(31,1))],
            [sg.Text("Precio de renta:")],
            [sg.Text("$"), sg.Input(border_width=1, key="input_productos_añadir_precioDeRenta", enable_events=True, size=(31,1))],
            [sg.Text("Disponible:")],
            [sg.Radio("Sí", "input_productos_añadir_disponible", default=True, key="input_productos_añadir_disponible_si"),
            sg.Radio("No", "input_productos_añadir_disponible", key="input_productos_añadir_disponible_no")],
            [sg.Text("Director:", key="input_productos_añadir_datoextra_texto")],
            [sg.Input(border_width=1, key="input_productos_añadir_datoextra", enable_events=True, size=(35,1))]
        ],size=(300,200), scrollable=True, vertical_scroll_only=True)]])]],pad=(0,0)),
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("❌ Cancelar", k="btn_productos_añadir_cancelar", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("✅ Guardar", k="btn_productos_añadir_guardar", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_productos_añadir_cancelar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarProductos")
    elif (event == "btn_productos_añadir_guardar"):
        error = False
        campos = ["input_productos_añadir_nombre", "input_productos_añadir_año", "input_productos_añadir_precioDeVenta", "input_productos_añadir_precioDeRenta", "input_productos_añadir_datoextra"]
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
            tipoProducto = ("película" if __ventana["input_productos_añadir_tipo_película"].get() else "serie")
            GlobalTienda._registrarProducto(tipoProducto,
                __ventana["input_productos_añadir_nombre"].get(), __ventana["input_productos_añadir_año"].get(),
                __ventana["input_productos_añadir_género"].get(), float(__ventana["input_productos_añadir_precioDeVenta"].get()), 
                float(__ventana["input_productos_añadir_precioDeRenta"].get()), __ventana["input_productos_añadir_disponible_si"].get(),
                director = (__ventana["input_productos_añadir_datoextra"].get() if tipoProducto == "película" else None),
                temporada = (int(__ventana["input_productos_añadir_datoextra"].get()) if tipoProducto == "serie" else None),
            )
            __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Producto registrado")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok" or event == sg.WIN_CLOSED:
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)
            __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarProductos")

    if event == "input_productos_añadir_tipo_película" and __ventana["input_productos_añadir_tipo_película"].get():
        __ventana["input_productos_añadir_datoextra_texto"].update(value = "Director:")
    elif event == "input_productos_añadir_tipo_serie" and __ventana["input_productos_añadir_tipo_serie"].get():
        __ventana["input_productos_añadir_datoextra_texto"].update(value = "Temporada:")
        
    if event == "input_productos_añadir_año" and values["input_productos_añadir_año"] and values["input_productos_añadir_año"][-1] not in ("0123456789"):
        __ventana["input_productos_añadir_año"].update(values["input_productos_añadir_año"][:-1])

    elif event == "input_productos_añadir_precioDeVenta" and values["input_productos_añadir_precioDeVenta"] and values["input_productos_añadir_precioDeVenta"][-1] not in ("0123456789."):
        __ventana["input_productos_añadir_precioDeVenta"].update(values["input_productos_añadir_precioDeVenta"][:-1])
        
    elif event == "input_productos_añadir_precioDeRenta" and values["input_productos_añadir_precioDeRenta"] and values["input_productos_añadir_precioDeRenta"][-1] not in ("0123456789."):
        __ventana["input_productos_añadir_precioDeRenta"].update(values["input_productos_añadir_precioDeRenta"][:-1])
        
    elif event == "input_productos_añadir_temporada" and values["input_productos_añadir_temporada"] and values["input_productos_añadir_temporada"][-1] not in ("0123456789"):
        __ventana["input_productos_añadir_temporada"].update(values["input_productos_añadir_temporada"][:-1])