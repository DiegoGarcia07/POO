from ast import Global
import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Lista de empleados"
key = "__layout_gestionarEmpleados_listar"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Listbox([],
            key="input_usuarios_empleados_listar", size=(35,10))
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_usuarios_empleados_listar_volver", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("🔍 Ver detalles", k="btn_usuarios_empleados_listar_detalles", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def precarga(__ventana, GlobalTienda):
    empleados = GlobalTienda.listarUsuarios("empleado")
    empleados_f = []
    for empleado in empleados:
        if (empleados[empleado].get("nombre") is not None):
            nombre = empleados[empleado]["nombre"]
            empleados_f.append(f"ID: {empleado} - {nombre}")

    __ventana["input_usuarios_empleados_listar"].update(values = empleados_f)


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_usuarios_empleados_listar_volver"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarEmpleados")
    elif (event == "btn_usuarios_empleados_listar_detalles"):
        if (not values["input_usuarios_empleados_listar"]):
            __ventana_aviso_actual = Recursos.__ventana_avisos("error", "❓", "No seleccionaste ningún empleado", "Reintentar")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok" or event == sg.WIN_CLOSED:
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)
        else:
            id = [int(s) for s in values["input_usuarios_empleados_listar"][0].split() if s.isdigit()]
            __ventana.metadata = id[0]
            __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarEmpleados_verdetalles")