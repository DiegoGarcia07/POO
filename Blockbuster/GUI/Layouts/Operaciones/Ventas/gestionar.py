import PySimpleGUI as sg
import GUI.recursos as Recursos

titulo = "Gestionar ventas"
key = "__layout_gestionarVentas"

layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[sg.Button("📥 Registrar", k="btn_operaciones_ventas_registrar", p=(10,10), font=Recursos.btnFont),
    sg.Button("📝 Listar", k="btn_operaciones_ventas_listar", p=(10,10), font=Recursos.btnFont),
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_operaciones_ventas_volver", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))

def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_operaciones_ventas_registrar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarVentas_registrar")
    elif (event == "btn_operaciones_ventas_listar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarVentas_listar")
    elif (event == "btn_operaciones_ventas_volver"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarOperaciones")