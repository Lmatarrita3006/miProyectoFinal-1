from datetime import datetime, timedelta

print("Gracias por visitar al restaurante STEAM CENTER")
rol = int(input("Digite 1 si desea ingresar a la plataforma de cliente y un 2 si desea ingresar a la plataforma de cocina "))
if rol == 2:
    print("Bienvenido, encargado de cocina!")
    with open("Pedidos.txt", "r") as file:
        pedidos = []
        for linea in file:
            hora_actual, hora_estimada = linea.strip().split(",")
            pedidos.append({"hora_actual": datetime.strptime(hora_actual, "%d/%m/%Y %H:%M:%S"), "hora_estimada": datetime.strptime(hora_estimada, "%d/%m/%Y %H:%M:%S")})

    # Mostrar la lista de pedidos pendientes
    if len(pedidos) == 0:
        print("No hay pedidos pendientes.")
    else:
        print("Pedidos pendientes:")
        for i, pedido in enumerate(pedidos):
            print(f"{i + 1}. {pedido['hora_actual'].strftime('%d/%m/%Y %H:%M:%S')}")

        # Procesar los pedidos
        while True:
            opcion = input("\n¿Desea procesar un pedido? (s/n): ")
            if opcion.lower() == "n":
                break

            # Obtener el número del pedido a procesar
            numero_pedido = int(input("Por favor, ingrese el número del pedido: "))
            if numero_pedido < 1 or numero_pedido > len(pedidos):
                print("Número de pedido inválido.")
                continue
            pedido = pedidos[numero_pedido - 1]

            # Verificar si el pedido ya está listo
            if datetime.now() < pedido["hora_estimada"]:
                print("El pedido aún no está listo.")
            else:
                # Actualizar el archivo de pedidos
                with open("Pedidos.txt", "w") as file:
                    for i, p in enumerate(pedidos):
                        if i != numero_pedido - 1:
                            file.write(f"{p['hora_actual'].strftime('%d/%m/%Y %H:%M:%S')},{p['hora_estimada'].strftime('%d/%m/%Y %H:%M:%S')}\n")

                print("El pedido está listo. Hora de entrega:", datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

    print("Gracias por utilizar la plataforma de cocina.")

elif rol == 1:
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

        # Presentación del menú
        print("\n-------------------------------")
        print("{:<20}{}".format("MENÚ", ""))
        print("-------------------------------")
        for categoria, platillos_en_categoria in platillos.items():
            print(categoria + ":")
            for i, platillo in enumerate(platillos_en_categoria):
                nombre, precio = platillo
                print("{:<2d}. {:<20}₡{}".format(i + 1, nombre, precio))
        print("-------------------------------")

        # Solicitud de pedidos
        pedido = {}
        while True:
            nombre = input("\n¿Qué platillo te gustaría ordenar? ")
            if nombre not in [platillo[0] for opciones in platillos.values() for platillo in opciones]:
                print("Lo siento, el platillo ingresado no está en el menú.")
                continue
            cantidad = int(input("¿Cuántos deseas ordenar? "))
            pedido[nombre] = cantidad
            finalizar_pedido = int(input("Si desea finalizar el pedido, digite 1, de lo contrario digite 2: "))
            if finalizar_pedido == 1:
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
                        print(f"{nombre} x {cantidad} = ₡{subtotal}")
    hora_actual = datetime.now()
    tiempo_preparacion = timedelta(minutes=len(pedido) * 15)
    hora_estimada = hora_actual + tiempo_preparacion

    print(f"\nTotal a pagar: {total} colones")
    print(f"La orden estará lista aproximadamente a las {hora_estimada.strftime('%I:%M%p')}, ¡Que disfrutes!")

    # Guardar la hora actual y la hora estimada en un archivo de texto
    with open("Pedidos.txt", "a") as file:
        file.write(f"{hora_actual.strftime('%d/%m/%Y %H:%M:%S')},{hora_estimada.strftime('%d/%m/%Y %H:%M:%S')}\n")

        print(f"\nTotal a pagar: {total} colones")
        # Generar factura
    print("\n-------------------------------")
    print("Factura:")
    print("-------------------------------")
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
    print(f"\nSubtotal: ₡{subtotal}")
    print(f"IVA (13%): ₡{iva}")
    if descuento_cumpleanos > 0:
        print(f"Descuento de cumpleaños (10%): ₡{descuento_cumpleanos}")
    print(f"Total a pagar: ₡{total_pagar}")
    print("-------------------------------")










