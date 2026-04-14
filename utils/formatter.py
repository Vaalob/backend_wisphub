def formatear_cliente(data_cliente, data_facturas):
    nombre = f"{data_cliente.get('name', '')}"

    facturas = []
    pendientes = False

    for f in data_facturas:
        if f["status"] != "paid":
            pendientes = True

        facturas.append({
            "descripcion": f["description"],
            "monto": f["total"],
            "estado": f["status"]
        })

    return {
        "nombre": nombre,
        "status_servicio": data_cliente.get("status"),
        "facturas": facturas,
        "tiene_pendientes": pendientes
    }