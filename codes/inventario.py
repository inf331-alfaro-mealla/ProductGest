"""
Módulo de Inventario
Maneja operaciones CRUD para el sistema de gestión de inventario.
"""
import json
import os
from producto import Producto, validar_producto

class GestorInventario:
    """Clase para gestionar el inventario de productos."""
    
    def __init__(self, archivo_datos="datos_inventario.json"):
        """
        Inicializa el gestor de inventario.
        
        Args:
            archivo_datos (str): Ruta al archivo JSON para almacenamiento de datos
        """
        self.archivo_datos = archivo_datos
        self.productos = []
        self.categorias = [
            "Electrónica", 
            "Ropa", 
            "Alimentos", 
            "Libros", 
            "Hogar y Cocina",
            "Deportes y Aire Libre",
            "Juguetes y Juegos",
            "Salud y Belleza",
            "Artículos de Oficina"
        ]
        self.cargar_datos()
    
    def cargar_datos(self):
        """Carga datos de productos desde el archivo JSON."""
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r') as archivo:
                    datos = json.load(archivo)
                    self.productos = [Producto.desde_diccionario(item) for item in datos]
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error al cargar datos: {e}")
                self.productos = []
        else:
            self.productos = []
    
    def guardar_datos(self):
        """Guarda datos de productos en el archivo JSON."""
        datos = [producto.a_diccionario() for producto in self.productos]
        with open(self.archivo_datos, 'w') as archivo:
            json.dump(datos, archivo, indent=4)
    
    def obtener_categorias(self):
        """Obtiene la lista de categorías predefinidas."""
        return self.categorias
    
    def obtener_todos_productos(self):
        """Obtiene todos los productos en el inventario."""
        return self.productos
    
    def obtener_producto_por_sku(self, sku):
        """
        Obtiene un producto por su SKU.
        
        Args:
            sku (str): El SKU a buscar
            
        Returns:
            Producto o None: El producto si se encuentra, None en caso contrario
        """
        for producto in self.productos:
            if producto.sku.lower() == sku.lower():
                return producto
        return None
    
    def agregar_producto(self, sku, nombre, descripcion, cantidad, precio, categoria):
        """
        Agrega un nuevo producto al inventario.
        
        Args:
            sku (str): Unidad de Mantenimiento de Stock única
            nombre (str): Nombre del producto
            descripcion (str): Descripción del producto
            cantidad (int): Cantidad disponible
            precio (float): Precio unitario
            categoria (str): Categoría del producto
            
        Returns:
            str: Mensaje de resultado
        """
        # Verificar si el SKU ya existe
        if self.obtener_producto_por_sku(sku):
            return f"Error: Ya existe un producto con SKU '{sku}'."
        
        # Verificar si el nombre del producto ya existe
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower() and producto.categoria == categoria:
                return f"Error: Ya existe un producto '{nombre}' en la categoría '{categoria}'."
        
        # Validar datos del producto
        es_valido, mensaje_error = validar_producto(sku, nombre, descripcion, cantidad, precio, categoria)
        if not es_valido:
            return f"Error: {mensaje_error}"
        
        # Crear y agregar el nuevo producto
        nuevo_producto = Producto(sku, nombre, descripcion, cantidad, precio, categoria)
        self.productos.append(nuevo_producto)
        self.guardar_datos()
        
        return f"Producto '{nombre}' agregado exitosamente."
    
    def actualizar_producto(self, sku, nombre, descripcion, cantidad, precio, categoria):
        """
        Actualiza un producto existente.
        
        Args:
            sku (str): SKU del producto a actualizar
            nombre (str): Nuevo nombre del producto
            descripcion (str): Nueva descripción del producto
            cantidad (int): Nueva cantidad
            precio (float): Nuevo precio
            categoria (str): Nueva categoría
            
        Returns:
            str: Mensaje de resultado
        """
        producto = self.obtener_producto_por_sku(sku)
        if not producto:
            return f"Error: No se encontró ningún producto con SKU '{sku}'."
        
        # Verificar duplicado de nombre en la misma categoría (excluyendo este producto)
        for p in self.productos:
            if p.sku != sku and p.nombre.lower() == nombre.lower() and p.categoria == categoria:
                return f"Error: Ya existe otro producto con nombre '{nombre}' en la categoría '{categoria}'."
        
        # Validar datos del producto
        es_valido, mensaje_error = validar_producto(sku, nombre, descripcion, cantidad, precio, categoria)
        if not es_valido:
            return f"Error: {mensaje_error}"
        
        # Actualizar el producto
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.cantidad = cantidad
        producto.precio = precio
        producto.categoria = categoria
        
        self.guardar_datos()
        return f"Producto '{nombre}' actualizado exitosamente."
    
    def eliminar_producto(self, sku):
        """
        Elimina un producto del inventario.
        
        Args:
            sku (str): SKU del producto a eliminar
            
        Returns:
            str: Mensaje de resultado
        """
        producto = self.obtener_producto_por_sku(sku)
        if not producto:
            return f"Error: No se encontró ningún producto con SKU '{sku}'."
        
        self.productos = [p for p in self.productos if p.sku.lower() != sku.lower()]
        self.guardar_datos()
        
        return f"Producto '{producto.nombre}' eliminado exitosamente."
    
    def buscar_por_nombre(self, nombre):
        """
        Busca productos por nombre (coincidencia parcial).
        
        Args:
            nombre (str): Nombre a buscar
            
        Returns:
            list: Lista de productos coincidentes
        """
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]
    
    def buscar_por_categoria(self, categoria):
        """
        Busca productos por categoría.
        
        Args:
            categoria (str): Categoría a buscar
            
        Returns:
            list: Lista de productos coincidentes
        """
        return [p for p in self.productos if p.categoria == categoria]
    
    def buscar_por_precio(self, precio_maximo):
        """
        Busca productos por precio máximo.
        
        Args:
            precio_maximo (float): Precio máximo a buscar
            
        Returns:
            list: Lista de productos coincidentes
        """
        return [p for p in self.productos if p.precio <= precio_maximo]

