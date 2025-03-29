"""
Módulo de Producto
Define la clase Producto y funciones de validación.
"""

import logging

class Producto:
    """Clase que representa un producto en el inventario."""

    def __init__(self, sku, nombre, descripcion, cantidad, precio, categoria):
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
        return f"{self.nombre} (SKU: {self.sku}) - ${self.precio:.2f} - {self.cantidad} en stock"

def validar_producto(sku, nombre, descripcion, cantidad, precio, categoria):
    """
    Valida los datos del producto antes de crear o actualizar.

    Returns:
        tuple: (es_valido, mensaje_error)
    """
    if not sku or not nombre or not descripcion or categoria is None:
        mensaje = "Todos los campos son obligatorios."
        logging.warning(f"Validación fallida: {mensaje}")
        return False, mensaje

    if not isinstance(cantidad, int) or cantidad < 0:
        mensaje = "La cantidad debe ser un entero positivo."
        logging.warning(f"Validación fallida: {mensaje}")
        return False, mensaje

    if not isinstance(precio, (int, float)) or precio <= 0:
        mensaje = "El precio debe ser un número positivo."
        logging.warning(f"Validación fallida: {mensaje}")
        return False, mensaje

    return True, ""
