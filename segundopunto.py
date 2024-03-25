def agregar_fruta():
    id_fruta = input("Ingrese el ID de la fruta: ")
    nombre_fruta = input("Ingrese el nombre de la fruta: ")
    precio_unitario = float(input("Ingrese el precio unitario de la fruta: "))
    cantidad = int(input("Ingrese la cantidad de esta fruta: "))
    return {'id': id_fruta, 'nombre': nombre_fruta, 'precio_unitario': precio_unitario, 'cantidad': cantidad}

def costo_total_salpicon(frutas):
    total = sum(fruta['precio_unitario'] * fruta['cantidad'] for fruta in frutas)
    print("El costo total del salpicón es:", total)

def mostrar_frutas_ordenadas(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda x: x['precio_unitario'], reverse=True)
    print("Frutas ordenadas de mayor a menor costo:")
    for fruta in frutas_ordenadas:
        print(f"ID: {fruta['id']}, Nombre: {fruta['nombre']}, Precio Unitario: {fruta['precio_unitario']}, Cantidad: {fruta['cantidad']}")

def fruta_mas_barata(frutas):
    fruta_barata = min(frutas, key=lambda x: x['precio_unitario'])
    print("La fruta más barata es:")
    print(f"ID: {fruta_barata['id']}, Nombre: {fruta_barata['nombre']}, Precio Unitario: {fruta_barata['precio_unitario']}, Cantidad: {fruta_barata['cantidad']}")

def main():
    N = int(input("Ingrese la cantidad de frutas para el salpicón: "))
    frutas = []
    for i in range(N):
        print(f"Ingrese los detalles de la fruta {i+1}:")
        fruta = agregar_fruta()
        frutas.append(fruta)

    costo_total_salpicon(frutas)
    mostrar_frutas_ordenadas(frutas)
    fruta_mas_barata(frutas)

if __name__ == "__main__":
    main()