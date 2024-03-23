from datetime import datetime
import PySimpleGUI as sg
import GUI.recursos as Recursos

titulo = "Historial de rentas"
key = "__layout_gestionarRentas_listar"

layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Listbox([],
            key="input_operaciones_rentas_listar", size=(35,10))
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("⬅️ Volver", k="btn_operaciones_rentas_listar_volver", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("🔍 Ver detalles", k="btn_operaciones_rentas_listar_verdetalles", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))

def precarga(__ventana, GlobalTienda):
    rentas = GlobalTienda.listarOperaciones("renta")
    rentas_f = []
    for renta in rentas:
        if (rentas[renta].get("fecha") is not None):
            productoVendido = GlobalTienda.listarProductos(rentas[renta]["idDelProducto"])
            nombre = productoVendido.get("nombre") if productoVendido.get("nombre") is not None else "Producto eliminado"
            fecha = datetime.fromtimestamp(rentas[renta]["fecha"]).strftime('%Y-%m-%d %H:%M:%S')
            rentas_f.append(f"ID: {renta} - {fecha} - {nombre}")

    __ventana["input_operaciones_rentas_listar"].update(values = rentas_f)

def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_operaciones_rentas_listar_volver"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarRentas")
    elif (event == "btn_operaciones_rentas_listar_verdetalles"):
        if (not values["input_operaciones_rentas_listar"]):
            __ventana_aviso_actual = Recursos.__ventana_avisos("error", "❓", "No seleccionaste ninguna renta", "Reintentar")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok" or event == sg.WIN_CLOSED:
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)
        else:
            id = [int(s) for s in values["input_operaciones_rentas_listar"][0].split() if s.isdigit()]
            __ventana.metadata = id[0]
            __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarRentas_verdetalles")