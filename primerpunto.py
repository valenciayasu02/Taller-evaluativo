def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    unidades = int(input("Ingrese la cantidad de unidades del producto: "))
    producto = {'nombre': nombre, 'precio': precio, 'unidades': unidades}
    inventario.append(producto)
    print("Producto agregado exitosamente.")

def mostrar_productos_bodega(inventario):
    print("Productos en bodega:")
    for i, producto in enumerate(inventario):
        print(f"Producto {i+1}:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Unidades: {producto['unidades']}")
        print()

def buscar_producto_por_nombre(inventario, nombre):
    for producto in inventario:
        if producto['nombre'] == nombre:
            print("Producto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print(f"Unidades: {producto['unidades']}")
            return
    print("Producto no encontrado.")

def modificar_unidades_compradas(inventario, nombre, nuevas_unidades):
    for producto in inventario:
        if producto['nombre'] == nombre:
            producto['unidades'] = nuevas_unidades
            print("Unidades modificadas exitosamente.")
            return
    print("Producto no encontrado.")

def eliminar_producto(inventario, nombre):
    for producto in inventario:
        if producto['nombre'] == nombre:
            inventario.remove(producto)
            print("Producto eliminado exitosamente.")
            return
    print("Producto no encontrado.")

# Lista para almacenar los productos en el inventario
inventario = []

# Menú de opciones
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar producto")
    print("2. Mostrar productos en bodega")
    print("3. Buscar producto por nombre")
    print("4. Modificar número de unidades compradas")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_producto(inventario)

    elif opcion == '2':
        mostrar_productos_bodega(inventario)

    elif opcion == '3':
        nombre = input("Ingrese el nombre del producto a buscar: ")
        buscar_producto_por_nombre(inventario, nombre)

    elif opcion == '4':
        nombre = input("Ingrese el nombre del producto: ")
        nuevas_unidades = int(input("Ingrese el nuevo número de unidades compradas: "))
        modificar_unidades_compradas(inventario, nombre, nuevas_unidades)

    elif opcion == '5':
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(inventario, nombre)

    elif opcion == '6':
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")