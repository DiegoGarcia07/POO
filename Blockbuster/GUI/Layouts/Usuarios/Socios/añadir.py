import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Añadir socio"
key = "__layout_gestionarSocios_añadir"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Column([[sg.Frame("Datos del socio", [[sg.Column([
            [sg.Text("Nombre completo:")],
            [sg.Input(border_width=1, key="input_usuarios_socios_añadir_nombre", enable_events=True, size=(35,1))],
            [sg.Text("Correo electrónico:")],
            [sg.Input(border_width=1, key="input_usuarios_socios_añadir_correo", enable_events=True, size=(35,1))],
            [sg.Text("Número de teléfono:")],
            [sg.Input(border_width=1, key="input_usuarios_socios_añadir_teléfono", enable_events=True, size=(35,1))],
            [sg.Text("Edad:")],
            [sg.Input(border_width=1, key="input_usuarios_socios_añadir_edad", enable_events=True, size=(29,1)), sg.Text("años")],
            [sg.Text("VIP:")],
            [sg.Radio("Sí", "input_usuarios_socios_añadir_vip", key="input_usuarios_socios_añadir_vip_si"),
            sg.Radio("No", "input_usuarios_socios_añadir_vip", default=True, key="input_usuarios_socios_añadir_vip_no")]
        ],size=(300,200), scrollable=True, vertical_scroll_only=True)]])]],pad=(0,0)),
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("❌ Cancelar", k="btn_usuarios_socios_añadir_cancelar", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("✅ Guardar", k="btn_usuarios_socios_añadir_guardar", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_usuarios_socios_añadir_cancelar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarSocios")
    elif (event == "btn_usuarios_socios_añadir_guardar"):
        error = False
        campos = ["input_usuarios_socios_añadir_nombre", "input_usuarios_socios_añadir_correo", "input_usuarios_socios_añadir_teléfono", "input_usuarios_socios_añadir_edad"]
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
            GlobalTienda._registrarUsuario("socio", 
                __ventana["input_usuarios_socios_añadir_nombre"].get(), __ventana["input_usuarios_socios_añadir_correo"].get(), 
                __ventana["input_usuarios_socios_añadir_teléfono"].get(), int(__ventana["input_usuarios_socios_añadir_edad"].get()), 
                VIP = __ventana["input_usuarios_socios_añadir_vip_si"].get(), 
            )
            __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Socio registrado")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok" or event == sg.WIN_CLOSED:
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)
            __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarSocios")

    if event == "input_usuarios_socios_añadir_teléfono" and values["input_usuarios_socios_añadir_teléfono"] and values["input_usuarios_socios_añadir_teléfono"][-1] not in ("0123456789"):
        __ventana["input_usuarios_socios_añadir_teléfono"].update(values["input_usuarios_socios_añadir_teléfono"][:-1])

    elif event == "input_usuarios_socios_añadir_edad" and values["input_usuarios_socios_añadir_edad"] and values["input_usuarios_socios_añadir_edad"][-1] not in ("0123456789"):
        __ventana["input_usuarios_socios_añadir_edad"].update(values["input_usuarios_socios_añadir_edad"][:-1])
        
    elif event == "input_usuarios_socios_añadir_sueldo" and values["input_usuarios_socios_añadir_sueldo"] and values["input_usuarios_socios_añadir_sueldo"][-1] not in ("0123456789."):
        __ventana["input_usuarios_socios_añadir_sueldo"].update(values["input_usuarios_socios_añadir_sueldo"][:-1])