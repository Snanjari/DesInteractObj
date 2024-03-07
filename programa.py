from tienda import Restaurante, Farmacia, Supermercado

def ingresar_datos_tienda():
    """
    Solicita al usuario ingresar el nombre y el costo de delivery de una tienda.
    
    Returns:
        str: Nombre de la tienda.
        int: Costo de delivery de la tienda.
    """
    nombre = input("\nIngrese el nombre de la tienda: ")
    delivery = int(input("Ingrese el costo de delivery: "))
    return nombre, delivery

def ingresar_producto(tienda):
    """
    Solicita al usuario ingresar los datos de un producto y lo agrega a la tienda.
    
    Args:
        tienda (Tienda): Instancia de la tienda a la que se agregará el producto.
    """
    nombre = input("\nIngrese nombre del producto: ")
    precio = int(input("Ingrese precio del producto: "))
    stock = int(input("Ingrese stock del producto: "))
    tienda.ingresar_producto(nombre, precio, stock)

def listar_productos(tienda):
    """
    Muestra los productos existentes en la tienda.
    
    Args:
        tienda (Tienda): Instancia de la tienda cuyos productos se listarán.
    """
    print("\nProductos en la tienda:")
    print(tienda.listar_productos())

def realizar_venta(tienda):
    """
    Solicita al usuario realizar una venta de un producto en la tienda.
    
    Args:
        tienda (Tienda): Instancia de la tienda donde se realizará la venta.
    """
    nombre_producto = input("\nIngrese nombre del producto a vender: ")
    cantidad = int(input("Ingrese cantidad a vender: "))
    tienda.realizar_venta(nombre_producto, cantidad)

def main():
    """
    Función principal del programa.
    """
    print("Bienvenido al sistema de gestión de tiendas")

    while True:
        print("\n¿Qué tipo de tienda desea administrar?")
        print("1. Restaurante")
        print("2. Farmacia")
        print("3. Supermercado")
        print("4. Salir")

        opcion_tienda = int(input("> "))

        if opcion_tienda == 4:
            print("Hasta luego.")
            break

        nombre, delivery = ingresar_datos_tienda()

        if opcion_tienda == 1:
            tienda = Restaurante(nombre, delivery)
        elif opcion_tienda == 2:
            tienda = Farmacia(nombre, delivery)
        elif opcion_tienda == 3:
            tienda = Supermercado(nombre, delivery)
        else:
            print("Opción inválida. Por favor, elija una opción válida.")
            continue

        while True:
            print("\n¿Qué desea hacer?")
            print("1. Ingresar un producto")
            print("2. Listar productos")
            print("3. Realizar una venta")
            print("4. Volver al menú principal")

            opcion_accion = int(input("> "))

            if opcion_accion == 1:
                ingresar_producto(tienda)
            elif opcion_accion == 2:
                listar_productos(tienda)
            elif opcion_accion == 3:
                realizar_venta(tienda)
            elif opcion_accion == 4:
                break
            else:
                print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
