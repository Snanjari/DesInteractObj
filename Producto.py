# producto.py
class Producto:
    """
    Clase que representa un producto en una tienda.
    """

    def __init__(self, nombre: str, precio: int, stock: int = 0):
        """
        Inicializa un producto con su nombre, precio y stock.

        Args:
            nombre (str): Nombre del producto.
            precio (int): Precio del producto.
            stock (int, opcional): Stock del producto. Por defecto es 0.
        """
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self) -> str:
        """str: Nombre del producto."""
        return self.__nombre

    @property
    def precio(self) -> int:
        """int: Precio del producto."""
        return self.__precio

    @property
    def stock(self) -> int:
        """int: Stock del producto."""
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock: int):
        """
        Setter para actualizar el stock del producto.

        Args:
            nuevo_stock (int): Nuevo valor de stock del producto.
        """
        self.__stock = max(0, nuevo_stock)
