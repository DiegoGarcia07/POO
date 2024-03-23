import PySimpleGUI as sg
import GUI.recursos as Recursos

titulo = "Gestionar usuarios"
key = "__layout_gestionarUsuarios"

layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[sg.Button("💼 Empleados", k="btn_usuarios_empleados", p=(10,10), font=Recursos.btnFont),
    sg.Button("🎖️ Socios", k="btn_usuarios_socios", p=(10,10), font=Recursos.btnFont)]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_usuarios_menu_volver", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))

def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_usuarios_empleados"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarEmpleados")
    if (event == "btn_usuarios_socios"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarSocios")
    elif (event == "btn_usuarios_menu_volver"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_menuPrincipal")