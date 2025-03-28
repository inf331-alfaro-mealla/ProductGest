"""
Módulo de Producto
Define la clase Producto y funciones de validación.
"""

class Producto:
    """Clase que representa un producto en el inventario."""
    
    def __init__(self, sku, nombre, descripcion, cantidad, precio, categoria):
        """
        Inicializa un nuevo Producto.
        
        Args:
            sku (str): Unidad de Mantenimiento de Stock única
            nombre (str): Nombre del producto
            descripcion (str): Descripción del producto
            cantidad (int): Cantidad disponible
            precio (float): Precio unitario
            categoria (str): Categoría del producto
        """
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria
    
    def a_diccionario(self):
        """Convierte el producto a diccionario para almacenamiento."""
        return {
            'sku': self.sku,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'cantidad': self.cantidad,
            'precio': self.precio,
            'categoria': self.categoria
        }
    
    @classmethod
    def desde_diccionario(cls, datos):
        """Crea una instancia de Producto desde datos de diccionario."""
        return cls(
            datos['sku'],
            datos['nombre'],
            datos['descripcion'],
            datos['cantidad'],
            datos['precio'],
            datos['categoria']
        )
    
    def __str__(self):
        """Representación en cadena del producto."""
        return f"{self.nombre} (SKU: {self.sku}) - ${self.precio:.2f} - {self.cantidad} en stock"


def validar_producto(sku, nombre, descripcion, cantidad, precio, categoria):
    """
    Valida los datos del producto antes de crear o actualizar.
    
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    # Verificar campos vacíos
    if not sku or not nombre or not descripcion or categoria is None:
        return False, "Todos los campos son obligatorios."
    
    # Validar cantidad
    if not isinstance(cantidad, int) or cantidad < 0:
        return False, "La cantidad debe ser un entero positivo."
    
    # Validar precio
    if not isinstance(precio, (int, float)) or precio <= 0:
        return False, "El precio debe ser un número positivo."
    
    return True, ""

