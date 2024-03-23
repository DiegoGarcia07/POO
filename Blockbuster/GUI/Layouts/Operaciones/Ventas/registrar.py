from datetime import datetime
import PySimpleGUI as sg
import GUI.recursos as Recursos

titulo = "Registrar venta"
key = "__layout_gestionarVentas_registrar"

layout = sg.pin(sg.Column([
    [sg.Column([[sg.Text(titulo, font="Arial 24", k=key+"_titulo")]], justification="center")],
    [sg.Column([[
        sg.Column([[sg.Frame("Datos generales:", [[sg.Column([
            [sg.Text("Empleado vendedor:")],
            [sg.Combo([], key="input_operaciones_ventas_registrar_idempleado", size=(21,1))],
            [sg.Text("Socio comprador:")],
            [sg.Combo([], key="input_operaciones_ventas_registrar_idsocio", size=(21,1))],
            [sg.Text("Cantidad vendida:")],
            [sg.Input(border_width=1, key="input_operaciones_ventas_registrar_cantidad", enable_events=True, size=(21,1))],
            [sg.Text("Precio total:")],
            [sg.Text("$"), sg.Input(border_width=1, key="input_operaciones_ventas_registrar_precio", enable_events=True, size=(19,1))],
        ],size=(200,200), scrollable=True, vertical_scroll_only=True)]])]],pad=(0,0)),
        sg.Column([[sg.Frame("Producto vendido:", [[sg.Column([[sg.Listbox([],
            key="input_operaciones_ventas_registrar_producto",size=(35,10)),]],size=(300,200))]])]],pad=(0,0))
    ]], justification="center")],
    [sg.HorizontalSeparator(color="#021129", p=(0, 10))],
    [sg.Button("❌ Cancelar", k="btn_operaciones_ventas_registrar_cancelar", font=Recursos.btnFont, button_color=Recursos.btnColor),
    sg.Push(), sg.Button("✅ Guardar", k="btn_operaciones_ventas_registrar_guardar", font=Recursos.btnFont, button_color=Recursos.btnColor)]
], k=key, visible=False))

def precarga(__ventana, GlobalTienda):
    empleados = GlobalTienda.listarUsuarios("empleado")
    empleados_f = []
    for empleado in empleados:
        if (empleados[empleado].get("nombre") is not None):
            nombre = empleados[empleado]["nombre"]
            empleados_f.append(f"ID: {empleado} - {nombre}")

    __ventana["input_operaciones_ventas_registrar_idempleado"].update(values = empleados_f)

    socios = GlobalTienda.listarUsuarios("socio")
    socios_f = []
    for socio in socios:
        if (socios[socio].get("nombre") is not None):
            nombre = socios[socio]["nombre"]
            socios_f.append(f"ID: {socio} - {nombre}")

    __ventana["input_operaciones_ventas_registrar_idsocio"].update(values = socios_f)

    productos = GlobalTienda.listarProductos()
    productos_f = []
    for producto in productos:
        if (productos[producto].get("nombre") is not None):
            nombre = productos[producto]["nombre"]
            tipo = productos[producto]["tipo"].capitalize()
            año = productos[producto]["año"]
            productos_f.append(f"ID: {producto} - Tipo: {tipo} - {nombre} ({año})")

    __ventana["input_operaciones_ventas_registrar_producto"].update(values = productos_f)

def eventos(GlobalTienda, __ventana, event, values):
    if (event == "btn_operaciones_ventas_registrar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarVentas_registrar")
    elif (event == "btn_operaciones_ventas_registrar_cancelar"):
        __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarVentas")
    elif (event == "btn_operaciones_ventas_registrar_guardar"):
        error = False
        campos = ["input_operaciones_ventas_registrar_idempleado", "input_operaciones_ventas_registrar_idsocio", "input_operaciones_ventas_registrar_cantidad", "input_operaciones_ventas_registrar_precio", "input_operaciones_ventas_registrar_producto"]
        for campo in campos:
            campo = __ventana[campo].get()
            if (campo == []): campo = ""
            if (campo == ""):
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
            idDelProducto = [int(s) for s in values["input_operaciones_ventas_registrar_producto"][0].split() if s.isdigit()][0]
            idDelEmpleado = [int(s) for s in values["input_operaciones_ventas_registrar_idempleado"].split() if s.isdigit()][0]
            idDelSocio = [int(s) for s in values["input_operaciones_ventas_registrar_idsocio"].split() if s.isdigit()][0]
            GlobalTienda._registrarOperación("venta", datetime.now(),
                idDelProducto, idDelEmpleado, idDelSocio,
                float(__ventana["input_operaciones_ventas_registrar_precio"].get()), 
                cantidad = int(__ventana["input_operaciones_ventas_registrar_cantidad"].get()), 
            )
            __ventana_aviso_actual = Recursos.__ventana_avisos("éxito", "✅", "Venta registrada")
            while True:
                event, values = __ventana_aviso_actual.read(timeout=100)
                if event == "btn_aviso_ok" or event == sg.WIN_CLOSED:
                    break
            __ventana_aviso_actual.close()
            del(__ventana_aviso_actual)
            __ventana.__cambiarVentanas(GlobalTienda, __ventana, "__layout_gestionarVentas")

    if event == "input_operaciones_ventas_registrar_cantidad" and values["input_operaciones_ventas_registrar_cantidad"] and values["input_operaciones_ventas_registrar_cantidad"][-1] not in ("123456789"):
        __ventana["input_operaciones_ventas_registrar_cantidad"].update(values["input_operaciones_ventas_registrar_cantidad"][:-1])
    elif event == "input_operaciones_ventas_registrar_precio" and values["input_operaciones_ventas_registrar_precio"] and values["input_operaciones_ventas_registrar_precio"][-1] not in ("0123456789."):
        __ventana["input_operaciones_ventas_registrar_precio"].update(values["input_operaciones_ventas_registrar_precio"][:-1])