# features/steps/steps.py

from behave import given, when, then

# Feature 1: Receptar y gestionar solicitudes de proveedores
@given('un proveedor envía una solicitud')
def step_impl(context):
    context.solicitud = {"proveedor": "Proveedor A", "documentacion": "incompleta"}

@when('el sistema recibe la solicitud')
def step_impl(context):
    context.solicitud_recibida = True

@then('la solicitud debe ser registrada en el sistema')
def step_impl(context):
    assert context.solicitud_recibida

@given('una solicitud de proveedor registrada')
def step_impl(context):
    context.solicitud = {"proveedor": "Proveedor A", "estado": "registrada"}

@when('el sistema consulta el estado de la solicitud')
def step_impl(context):
    context.estado_consultado = True

@then('se debe mostrar el estado actual de la solicitud')
def step_impl(context):
    assert context.estado_consultado

# Feature 2: Revisar y validar documentación
@given('una solicitud con documentación completa')
def step_impl(context):
    context.solicitud = {"proveedor": "Proveedor A", "documentacion": "completa"}

@when('el sistema revisa la documentación preliminar')
def step_impl(context):
    context.documentacion_revisada = True

@then('se debe verificar que la documentación esté completa')
def step_impl(context):
    assert context.solicitud["documentacion"] == "completa"

@given('una solicitud con documentación incompleta')
def step_impl(context):
    context.solicitud = {"proveedor": "Proveedor A", "documentacion": "incompleta"}

@when('el sistema identifica la documentación faltante')
def step_impl(context):
    context.documentacion_faltante = True

@then('se debe solicitar la documentación faltante al proveedor')
def step_impl(context):
    assert context.documentacion_faltante

# Feature 3: Validar cumplimiento legal
@given('una solicitud con incumplimiento legal')
def step_impl(context):
    context.solicitud = {"proveedor": "Proveedor A", "cumplimiento_legal": False}

@when('el sistema valida el cumplimiento legal')
def step_impl(context):
    context.cumplimiento_legal = context.solicitud["cumplimiento_legal"]

@then('se debe verificar que el proveedor cumple con las normativas legales')
def step_impl(context):
    assert context.cumplimiento_legal

@then('la solicitud debe ser rechazada')
def step_impl(context):
    assert not context.cumplimiento_legal

# Feature 4: Evaluar portafolio y capacidad operativa
@given('una solicitud de proveedor con portafolio')
def step_impl(context):
    context.solicitud = {"proveedor": "Proveedor A", "portafolio": "aceptable"}

@when('el sistema evalúa el portafolio del proveedor')
def step_impl(context):
    context.portafolio_evaluado = True

@then('se debe verificar que el portafolio cumple con los requisitos')
def step_impl(context):
    assert context.portafolio_evaluado

@given('una solicitud de proveedor con capacidad operativa')
def step_impl(context):
    context.solicitud = {"proveedor": "Proveedor A", "capacidad_operativa": "suficiente"}

@when('el sistema revisa la capacidad operativa del proveedor')
def step_impl(context):
    context.capacidad_operativa_revisada = True

@then('se debe verificar que el proveedor tiene la capacidad necesaria')
def step_impl(context):
    assert context.capacidad_operativa_revisada

# Feature 5: Probar calidad y formalizar contratos
@given('una solicitud de proveedor con productos o servicios')
def step_impl(context):
    context.solicitud = {"proveedor": "Proveedor A", "calidad": "alta"}

@when('el sistema prueba la calidad de los productos o servicios')
def step_impl(context):
    context.calidad_probada = True

@then('se debe verificar que la calidad cumple con los estándares')
def step_impl(context):
    assert context.calidad_probada

@given('una solicitud de proveedor aprobada')
def step_impl(context):
    context.solicitud = {"proveedor": "Proveedor A", "aprobada": True}

@when('el sistema formaliza los términos y condiciones')
def step_impl(context):
    context.terminos_formalizados = True

@then('se debe generar un acuerdo con los términos y condiciones')
def step_impl(context):
    assert context.terminos_formalizados

@given('un acuerdo con términos y condiciones')
def step_impl(context):
    context.acuerdo = {"terminos": "aceptados", "contrato": "pendiente"}

@when('el sistema revisa y ajusta el contrato')
def step_impl(context):
    context.contrato_ajustado = True

@then('se debe formalizar el contrato con el proveedor')
def step_impl(context):
    assert context.contrato_ajustado

# Feature 6: Analizar el estado financiero del proveedor
@given('una solicitud de proveedor con estado financiero')
def step_impl(context):
    context.solicitud = {"proveedor": "Proveedor A", "estado_financiero": "estable"}

@when('el sistema analiza el estado financiero del proveedor')
def step_impl(context):
    context.estado_financiero_analizado = True

@then('se debe verificar que el proveedor es financieramente estable')
def step_impl(context):
    assert context.estado_financiero_analizado


# features/steps/steps.py

from behave import given, when, then

# Simulación de una base de datos en memoria
proveedores_db = {}
clientes_db = {}
productos_db = {}
compras_db = {}

# CRUD de Proveedores
@given('un nuevo proveedor con nombre "{nombre}" y contacto "{contacto}"')
def step_impl(context, nombre, contacto):
    context.nuevo_proveedor = {"nombre": nombre, "contacto": contacto}

@when('el sistema registra el proveedor')
def step_impl(context):
    proveedor_id = len(proveedores_db) + 1
    proveedores_db[proveedor_id] = context.nuevo_proveedor
    context.proveedor_id = proveedor_id

@then('el proveedor debe ser guardado en la base de datos')
def step_impl(context):
    assert context.proveedor_id in proveedores_db

@given('un proveedor con ID {id:d} registrado en el sistema')
def step_impl(context, id):
    context.proveedor_id = id
    proveedores_db[id] = {"nombre": "Proveedor A", "contacto": "contacto@proveedora.com"}

@when('el sistema consulta la información del proveedor')
def step_impl(context):
    context.proveedor = proveedores_db.get(context.proveedor_id)

@then('se debe mostrar la información del proveedor')
def step_impl(context):
    assert context.proveedor is not None

@when('el sistema actualiza el contacto del proveedor a "{nuevo_contacto}"')
def step_impl(context, nuevo_contacto):
    proveedores_db[context.proveedor_id]["contacto"] = nuevo_contacto

@then('la información del proveedor debe ser actualizada en la base de datos')
def step_impl(context):
    assert proveedores_db[context.proveedor_id]["contacto"] == "nuevo_contacto@proveedora.com"

@when('el sistema elimina el proveedor')
def step_impl(context):
    del proveedores_db[context.proveedor_id]

@then('el proveedor debe ser eliminado de la base de datos')
def step_impl(context):
    assert context.proveedor_id not in proveedores_db

# CRUD de Clientes
@given('un nuevo cliente con nombre "{nombre}" y correo "{correo}"')
def step_impl(context, nombre, correo):
    context.nuevo_cliente = {"nombre": nombre, "correo": correo}

@when('el sistema registra el cliente')
def step_impl(context):
    cliente_id = len(clientes_db) + 1
    clientes_db[cliente_id] = context.nuevo_cliente
    context.cliente_id = cliente_id

@then('el cliente debe ser guardado en la base de datos')
def step_impl(context):
    assert context.cliente_id in clientes_db

@given('un cliente con ID {id:d} registrado en el sistema')
def step_impl(context, id):
    context.cliente_id = id
    clientes_db[id] = {"nombre": "Cliente A", "correo": "cliente@example.com"}

@when('el sistema consulta la información del cliente')
def step_impl(context):
    context.cliente = clientes_db.get(context.cliente_id)

@then('se debe mostrar la información del cliente')
def step_impl(context):
    assert context.cliente is not None

@when('el sistema actualiza el correo del cliente a "{nuevo_correo}"')
def step_impl(context, nuevo_correo):
    clientes_db[context.cliente_id]["correo"] = nuevo_correo

@then('la información del cliente debe ser actualizada en la base de datos')
def step_impl(context):
    assert clientes_db[context.cliente_id]["correo"] == "nuevo_correo@example.com"

@when('el sistema elimina el cliente')
def step_impl(context):
    del clientes_db[context.cliente_id]

@then('el cliente debe ser eliminado de la base de datos')
def step_impl(context):
    assert context.cliente_id not in clientes_db

# CRUD de Productos
@given('un nuevo producto con nombre "{nombre}" y precio {precio:d}')
def step_impl(context, nombre, precio):
    context.nuevo_producto = {"nombre": nombre, "precio": precio}

@when('el sistema registra el producto')
def step_impl(context):
    producto_id = len(productos_db) + 1
    productos_db[producto_id] = context.nuevo_producto
    context.producto_id = producto_id

@then('el producto debe ser guardado en la base de datos')
def step_impl(context):
    assert context.producto_id in productos_db

@given('un producto con ID {id:d} registrado en el sistema')
def step_impl(context, id):
    context.producto_id = id
    productos_db[id] = {"nombre": "Producto A", "precio": 100}

@when('el sistema consulta la información del producto')
def step_impl(context):
    context.producto = productos_db.get(context.producto_id)

@then('se debe mostrar la información del producto')
def step_impl(context):
    assert context.producto is not None

@when('el sistema actualiza el precio del producto a {nuevo_precio:d}')
def step_impl(context, nuevo_precio):
    productos_db[context.producto_id]["precio"] = nuevo_precio

@then('la información del producto debe ser actualizada en la base de datos')
def step_impl(context):
    assert productos_db[context.producto_id]["precio"] == 150

@when('el sistema elimina el producto')
def step_impl(context):
    del productos_db[context.producto_id]

@then('el producto debe ser eliminado de la base de datos')
def step_impl(context):
    assert context.producto_id not in productos_db

# CRUD de Compras
@given('una nueva compra con proveedor ID {proveedor_id:d}, producto ID {producto_id:d} y cantidad {cantidad:d}')
def step_impl(context, proveedor_id, producto_id, cantidad):
    context.nueva_compra = {"proveedor_id": proveedor_id, "producto_id": producto_id, "cantidad": cantidad}

@when('el sistema registra la compra')
def step_impl(context):
    compra_id = len(compras_db) + 1
    compras_db[compra_id] = context.nueva_compra
    context.compra_id = compra_id

@then('la compra debe ser guardada en la base de datos')
def step_impl(context):
    assert context.compra_id in compras_db

@given('una compra con ID {id:d} registrada en el sistema')
def step_impl(context, id):
    context.compra_id = id
    compras_db[id] = {"proveedor_id": 1, "producto_id": 1, "cantidad": 10}

@when('el sistema consulta la información de la compra')
def step_impl(context):
    context.compra = compras_db.get(context.compra_id)

@then('se debe mostrar la información de la compra')
def step_impl(context):
    assert context.compra is not None

@when('el sistema actualiza la cantidad de la compra a {nueva_cantidad:d}')
def step_impl(context, nueva_cantidad):
    compras_db[context.compra_id]["cantidad"] = nueva_cantidad

@then('la información de la compra debe ser actualizada en la base de datos')
def step_impl(context):
    assert compras_db[context.compra_id]["cantidad"] == 15

@when('el sistema elimina la compra')
def step_impl(context):
    del compras_db[context.compra_id]

@then('la compra debe ser eliminada de la base de datos')
def step_impl(context):
    assert context.compra_id not in compras_db