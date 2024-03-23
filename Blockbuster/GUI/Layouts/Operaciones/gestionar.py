import PySimpleGUI as sg
import GUI.recursos as Recursos

titulo = "Gestionar operaciones"
key = "__layout_gestionarOperaciones"

layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[sg.Button("💲 Ventas", k="btn_operaciones_ventas", p=(10,10), font=Recursos.btnFont),
    sg.Button("📮 Rentas", k="btn_operaciones_rentas", p=(10,10), font=Recursos.btnFont)]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_operaciones_menu_volver", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))

def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_operaciones_ventas"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarVentas")
    elif (event == "btn_operaciones_rentas"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarRentas")
    elif (event == "btn_operaciones_menu_volver"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_menuPrincipal")