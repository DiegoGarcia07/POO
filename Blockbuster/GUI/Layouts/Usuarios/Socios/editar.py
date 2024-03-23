import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Editar socio"
key = "__layout_gestionarSocios_editar"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Column([[sg.Frame("Datos del socio", [[sg.Column([
            [sg.Text("ID del usuario:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_socios_editar_id", size=(35,1))],
            [sg.Text("Nombre completo:")],
            [sg.Input(border_width=1, disabled=True, key="input_usuarios_socios_editar_nombre", size=(35,1))],
            [sg.Text("Correo electrónico:")],
            [sg.Input(border_width=1, key="input_usuarios_socios_editar_correo", enable_events=True, size=(35,1))],
            [sg.Text("Número de teléfono:")],
            [sg.Input(border_width=1, key="input_usuarios_socios_editar_teléfono", enable_events=True, size=(35,1))],
            [sg.Text("Edad:")],
            [sg.Input(border_width=1, key="input_usuarios_socios_editar_edad", enable_events=True, size=(29,1)), sg.Text("años")],
            [sg.Text("VIP:")],
            [sg.Radio("Sí", "input_usuarios_socios_editar_vip", key="input_usuarios_socios_editar_vip_si"),
            sg.Radio("No", "input_usuarios_socios_editar_vip", key="input_usuarios_socios_editar_vip_no")]
        ],size=(300,200), scrollable=True, vertical_scroll_only=True)]])]],pad=(0,0)),
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("❌ Cancelar", k="btn_usuarios_socios_editar_cancelar", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("✅ Guardar", k="btn_usuarios_socios_editar_guardar", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def precarga(__ventana, GlobalTienda):
    infoUsuario = GlobalTienda.listarUsuarios("socio", __ventana.metadata)
    __ventana["input_usuarios_socios_editar_id"].update(value = __ventana.metadata)
    __ventana["input_usuarios_socios_editar_nombre"].update(value = infoUsuario["nombre"])
    __ventana["input_usuarios_socios_editar_correo"].update(value = infoUsuario["correo"])
    __ventana["input_usuarios_socios_editar_teléfono"].update(value = infoUsuario["teléfono"])
    __ventana["input_usuarios_socios_editar_edad"].update(value = infoUsuario["edad"])
    __ventana["input_usuarios_socios_editar_edad"].update(value = infoUsuario["edad"])
    if infoUsuario["VIP"]:
        __ventana["input_usuarios_socios_editar_vip_si"].update(value = True)
    else:
        __ventana["input_usuarios_socios_editar_vip_no"].update(value = True)


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_usuarios_socios_editar_cancelar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarSocios_verdetalles")
    elif (event == "btn_usuarios_socios_editar_guardar"):
        error = False
        campos = ["input_usuarios_socios_editar_nombre", "input_usuarios_socios_editar_correo", "input_usuarios_socios_editar_teléfono", "input_usuarios_socios_editar_edad"]
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
            datos = GlobalTienda.__alt_dict__(GlobalTienda._registrarUsuario("socio", 
                __ventana["input_usuarios_socios_editar_nombre"].get(), __ventana["input_usuarios_socios_editar_correo"].get(), 
                __ventana["input_usuarios_socios_editar_teléfono"].get(), int(__ventana["input_usuarios_socios_editar_edad"].get()), 
                VIP = __ventana["input_usuarios_socios_editar_vip_si"].get(), 
                registrar = False 
            ))
            __ventana_aviso_actual = Recursos.__ventana_avisos("neutral", "⚠️", "¿Guardar cambios de socio?", "Sí", "No")
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
                GlobalTienda._editarUsuario("socio", __ventana.metadata, datos)
                __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Cambios guardados")
                while True:
                    event, values = __ventana_aviso_actual.read(timeout=100)
                    if event == "btn_aviso_ok":
                        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarSocios_verdetalles")
                        break
                __ventana_aviso_actual.close()
                del(__ventana_aviso_actual)
        
    if event == "input_usuarios_socios_editar_teléfono" and values["input_usuarios_socios_editar_teléfono"] and values["input_usuarios_socios_editar_teléfono"][-1] not in ("0123456789"):
        __ventana["input_usuarios_socios_editar_teléfono"].update(values["input_usuarios_socios_editar_teléfono"][:-1])

    elif event == "input_usuarios_socios_editar_edad" and values["input_usuarios_socios_editar_edad"] and values["input_usuarios_socios_editar_edad"][-1] not in ("0123456789"):
        __ventana["input_usuarios_socios_editar_edad"].update(values["input_usuarios_socios_editar_edad"][:-1])
        
    elif event == "input_usuarios_socios_editar_sueldo" and values["input_usuarios_socios_editar_sueldo"] and values["input_usuarios_socios_editar_sueldo"][-1] not in ("0123456789."):
        __ventana["input_usuarios_socios_editar_sueldo"].update(values["input_usuarios_socios_editar_sueldo"][:-1])