import PySimpleGUI as sg
import GUI.recursos as Recursos

titulo = "Gestionar empleados"
key = "__layout_gestionarEmpleados"

layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[sg.Button("➕ Añadir", k="btn_usuarios_empleados_añadir", p=(10,10), font=Recursos.btnFont),
    sg.Button("📝 Listar", k="btn_usuarios_empleados_listar", p=(10,10), font=Recursos.btnFont)]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_usuarios_empleados_menu_volver", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))

def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_usuarios_empleados_añadir"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarEmpleados_añadir")
    elif (event == "btn_usuarios_empleados_listar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarEmpleados_listar")
    elif (event == "btn_usuarios_empleados_menu_volver"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarUsuarios")