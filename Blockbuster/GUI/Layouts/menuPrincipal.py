import PySimpleGUI as sg
import GUI.recursos as Recursos

titulo = "Menú principal"
key = "__layout_menuPrincipal"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Button("📦 Gestionar productos", k="btn_productos_menu", p=(10,10), font=Recursos.btnFont),
    sg.Button("🛒 Gestionar operaciones", k="btn_operaciones_menu", p=(10,10), font=Recursos.btnFont),
    sg.Button("👤 Gestionar usuarios", k="btn_usuarios_menu", p=(10,10), font=Recursos.btnFont)],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Push(), sg.Button("❌ Salir", k="btn_salir", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key))


def precarga(__ventana, GlobalTienda):
    __ventana["texto_encabezado"].update(value=f"Sucursal: {GlobalTienda.ID}\tUbicación: {GlobalTienda.ubicación}")


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_productos_menu"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarProductos")
    elif (event == "btn_operaciones_menu"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarOperaciones")
    elif (event == "btn_usuarios_menu"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarUsuarios")