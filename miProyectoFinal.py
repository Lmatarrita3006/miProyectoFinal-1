from datetime import datetime, timedelta

print("Gracias por visitar al restaurante STEAM CENTER")
rol = int(input("Digite 1 si desea ingresar a la plataforma de cliente y un 2 si desea ingresar a la plataforma de cocina "))

if rol == 1:
    print("Bienvenido, estimado cliente!")

    platillos = {
        "Entradas": [("Ensalada César", 3500), ("Aros de cebolla", 4500)],
        "Platos fuertes": [("Filete mignon", 9600), ("Pollo al horno", 8500)],
        "Postres": [("Pastel de chocolate", 3000), ("Helado de vainilla", 2600)],
        "Bebidas": [("Coca Cola", 1800), ("Té Frío", 1500)]
    }

    # Registro del cliente
with open("RegistroClientes.txt", "w") as file:
    archivo_clientes = "RegistroClientes.txt"
    cliente_encontrado = False
    while not cliente_encontrado:
        correo_electronico = input("Por favor, ingrese su correo electrónico: ")
        with open(archivo_clientes, "r") as file:
            for linea in file:
                if correo_electronico in linea:
                    cliente_encontrado = True
                    print("El cliente está registrado.")
                    break
        if not cliente_encontrado:
            nombre_completo = input("Por favor, ingrese su nombre completo: ")
            fecha_nacimiento = input("Por favor, ingrese su fecha de nacimiento (formato dd/mm/yyyy): ")
            tarjeta_credito = input("Por favor, ingrese su información de tarjeta de crédito: ")
            fecha_vencimiento = input("Por favor, ingrese la fecha de vencimiento de su tarjeta (formato mm/aaaa): ")
            codigo_seguridad = input("Por favor, ingrese el código de seguridad de su tarjeta: ")
            with open(archivo_clientes, "a") as file:
                file.write(f"{correo_electronico},{nombre_completo},{fecha_nacimiento},{tarjeta_credito},{fecha_vencimiento},{codigo_seguridad}\n")
            print("El cliente ha sido registrado exitosamente.")

    # Solicitud de pedidos
    pedido = {}
    while True:
        nombre = input("\n¿Qué platillo te gustaría ordenar? ")
        if nombre not in [platillo[0] for opciones in platillos.values() for platillo in opciones]:
            print("Lo siento, el platillo ingresado no está en el menú.")
            continue
        cantidad = int(input("¿Cuántos deseas ordenar? "))
        pedido[nombre] = cantidad
        finalizar_pedido = input("Si desea finalizar el pedido escriba 'terminar': ")
        if finalizar_pedido.lower() == "terminar":
            break

    # Calcular el total
    total = 0
    print("\nTu pedido:")
    for nombre, cantidad in pedido.items():
        for categoria, opciones in platillos.items():
            for platillo in opciones:
                if platillo[0] == nombre:
                    precio = platillo[1]
                    subtotal = precio * cantidad
                    total += subtotal
                    print(f"{nombre} x {cantidad} = {subtotal} colones")

    print(f"\nTotal a pagar: {total} colones")
    # Generar factura
print("\nFactura:")
fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha: {fecha_actual}")
print("Cliente:")
print(f"Correo electrónico: {correo_electronico}")
print(f"Nombre completo: {nombre_completo}")
print(f"Fecha de nacimiento: {fecha_nacimiento}")
subtotal = total
iva = round(subtotal * 0.13, 2)
descuento_cumpleanos = 0
fecha_nacimiento_cliente = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
if fecha_nacimiento_cliente.day == datetime.now().day and fecha_nacimiento_cliente.month == datetime.now().month:
    descuento_cumpleanos = round(subtotal * 0.10, 2)
total_pagar = round(subtotal + iva - descuento_cumpleanos, 2)
print(f"\nSubtotal: {subtotal} colones")
print(f"IVA (13%): {iva} colones")
if descuento_cumpleanos > 0:
    print(f"Descuento de cumpleaños (10%): -{descuento_cumpleanos} colones")
print(f"Total a pagar: {total_pagar} colones")


