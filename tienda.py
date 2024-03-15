# tienda.py
from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    """
    Clase que representa una tienda genérica.
    """
    def __init__(self, nombre: str, delivery: int):
        """
        Inicializa una tienda con su nombre y costo de delivery.

        Args:
            nombre (str): Nombre de la tienda.
            delivery (int): Costo de delivery de la tienda.
        """
        self.__nombre = nombre
        self.__delivery = delivery
        self.__productos = []

    @abstractmethod
    def ingresar_producto(self, nombre: str, precio: int, stock: int):
        """Método para ingresar un producto a la tienda."""
        pass

    @abstractmethod
    def listar_productos(self) -> str:
        """Método  para listar los productos de la tienda."""
        pass

    @abstractmethod
    def realizar_venta(self, nombre: str, cantidad: int):
        """Método abstracto para realizar una venta en la tienda."""
        pass

    @property
    def nombre(self) -> str:
        """str: Nombre de la tienda."""
        return self.__nombre

    @property
    def delivery(self) -> int:
        """int: Costo de delivery de la tienda."""
        return self.__delivery

    @property
    def productos(self) -> list:
        """list: Lista de productos de la tienda."""
        return self.__productos

class Restaurante(Tienda):
    """Clase que representa un restaurante."""

    def ingresar_producto(self, nombre: str, precio: int, stock: int = 0):
        """
        Ingresa un producto al restaurante.

        Args:
            nombre (str): Nombre del producto.
            precio (int): Precio del producto.
            stock (int, opcional): Stock del producto. Por defecto es 0.
        """
        # Los productos de restaurantes siempre tienen stock 0
        p = Producto(nombre, precio, 0)
        if p not in self.productos:
            self.productos.append(p)

    def listar_productos(self) -> str:
        """Lista los productos del restaurante."""
        productos_str = ""
        for item in self.productos:
            productos_str += f"Nombre: {item.nombre.capitalize()} // Precio: ${item.precio}\n"
        return productos_str

    def realizar_venta(self, nombre: str, cantidad: int):
        """Realiza una venta en el restaurante."""
        pass

class Supermercado(Tienda):
    """Clase que representa un supermercado."""

    def ingresar_producto(self, nombre: str, precio: int, stock: int):
        """
        Ingresa un producto al supermercado.

        Args:
            nombre (str): Nombre del producto.
            precio (int): Precio del producto.
            stock (int): Stock del producto.
        """
        p = Producto(nombre, precio, stock)
        if p in self.productos:
            indice = self.productos.index(p)
            self.productos[indice].stock += stock
        else:
            self.productos.append(p)

    def listar_productos(self) -> str:
        """Lista los productos del supermercado."""
        productos_str = ""
        for item in self.productos:
            if item.stock < 10:
                productos_str += f"Nombre: {item.nombre.capitalize()} // Precio: ${item.precio} // Stock: {item.stock}. 'Pocos productos disponibles'\n"
            else:
                productos_str += f"Nombre: {item.nombre.capitalize()} // Precio: ${item.precio} // Stock: {item.stock}\n"
        return productos_str

    def realizar_venta(self, nombre: str, cantidad: int):
        """Realiza una venta en el supermercado."""
        venta = Producto(nombre, 5000, cantidad)
        if venta in self.productos:
            indice = self.productos.index(venta)
            if cantidad > self.productos[indice].stock:
                self.productos[indice].stock = 0
            else:
                self.productos[indice].stock -= cantidad

class Farmacia(Tienda):
    """Clase que representa una farmacia."""

    def ingresar_producto(self, nombre: str, precio: int, stock: int):
        """
        Ingresa un producto a la farmacia.

        Args:
            nombre (str): Nombre del producto.
            precio (int): Precio del producto.
            stock (int): Stock del producto.
        """
        p = Producto(nombre, precio, stock)
        if p in self.productos:
            indice = self.productos.index(p)
            self.productos[indice].stock += stock
        else:
            self.productos.append(p)

    def listar_productos(self) -> str:
        """Lista los productos de la farmacia."""
        productos_str = ""
        for item in self.productos:
            if item.precio > 15000:
                productos_str += f"Nombre: {item.nombre.capitalize()} // Precio: ${item.precio}. 'Envío gratis al solicitar este producto'\n"
            else:
                productos_str += f"Nombre: {item.nombre.capitalize()} // Precio: ${item.precio}\n"
        return productos_str

def realizar_venta(self, nombre: str, cantidad: int):
    """Realiza una venta en la farmacia."""
    if cantidad <= 3:
        venta = Producto(nombre, 5000, cantidad)
        if venta in self.productos:
            if cantidad > self.productos[self.productos.index(venta)].stock:
                self.productos[self.productos.index(venta)].stock = 0
            else:
                self.productos[self.productos.index(venta)] -= venta
