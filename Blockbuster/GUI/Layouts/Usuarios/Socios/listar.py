from ast import Global
import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Lista de socios"
key = "__layout_gestionarSocios_listar"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Listbox([],
            key="input_usuarios_socios_listar", size=(35,10))
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_usuarios_socios_listar_volver", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("🔍 Ver detalles", k="btn_usuarios_socios_listar_detalles", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def precarga(__ventana, GlobalTienda):
    socios = GlobalTienda.listarUsuarios("socio")
    socios_f = []
    for socio in socios:
        if (socios[socio].get("nombre") is not None):
            nombre = socios[socio]["nombre"]
            socios_f.append(f"ID: {socio} - {nombre}")

    __ventana["input_usuarios_socios_listar"].update(values = socios_f)


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_usuarios_socios_listar_volver"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarSocios")
    elif (event == "btn_usuarios_socios_listar_detalles"):
        if (not values["input_usuarios_socios_listar"]):
            __ventana_aviso_actual = Recursos.__ventana_avisos("error", "❓", "No seleccionaste ningún socio", "Reintentar")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok" or event == sg.WIN_CLOSED:
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)
        else:
            id = [int(s) for s in values["input_usuarios_socios_listar"][0].split() if s.isdigit()]
            __ventana.metadata = id[0]
            __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarSocios_verdetalles")