import PySimpleGUI as sg
import GUI.recursos as Recursos


titulo = "Bienvenido"
key = "__layout_primerArranque"


layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[sg.Text("Esta es la configuración inicial. Configura los datos de la tienda.", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Column([[sg.Frame("Datos de la tienda", [[sg.Column([
            [sg.Text("ID de la sucursal:")],
            [sg.Input(key="input_primerarranque_idsucursal", enable_events=True, size=(35,1))],
            [sg.Text("Ubicación de la sucursal:")],
            [sg.Multiline(key="input_primerarranque_ubicación", enable_events=True, size=(35,3))]
        ],size=(300,200))]])]],pad=(0,0)),
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Push(), sg.Button("✅ Guardar", k="btn_primerarranque_guardar", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))


def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_primerarranque_guardar"):
        error = False
        campos = ["input_primerarranque_idsucursal", "input_primerarranque_ubicación"]
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
            GlobalTienda.ID = __ventana["input_primerarranque_idsucursal"].get()
            GlobalTienda.ubicación = __ventana["input_primerarranque_ubicación"].get()
            __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Datos guardados")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok" or event == sg.WIN_CLOSED:
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)
            __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_menuPrincipal")

        
    if event == "input_primerarranque_idsucursal" and values["input_primerarranque_idsucursal"] and values["input_primerarranque_idsucursal"][-1] not in ("0123456789"):
        __ventana["input_primerarranque_idsucursal"].update(values["input_primerarranque_idsucursal"][:-1])