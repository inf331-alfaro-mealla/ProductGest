"""
Módulo de Inventario
Maneja operaciones CRUD para el sistema de gestión de inventario.
"""

import json
import os
import logging
from producto import Producto, validar_producto

class GestorInventario:
    """Clase para gestionar el inventario de productos."""
    
    def __init__(self, archivo_datos="datos_inventario.json"):
        self.archivo_datos = archivo_datos
        self.productos = []
        self.categorias = [
            "Electronica", 
            "Perifericos", 
            "Accesorios", 
            "Telefonos",
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
                logging.info("Datos del inventario cargados correctamente.")
            except (json.JSONDecodeError, KeyError) as e:
                logging.error(f"Error al cargar datos del inventario: {e}")
                self.productos = []
        else:
            logging.warning(f"Archivo de datos '{self.archivo_datos}' no encontrado. Se iniciará con inventario vacío.")
            self.productos = []
    
    def guardar_datos(self):
        """Guarda datos de productos en el archivo JSON."""
        try:
            datos = [producto.a_diccionario() for producto in self.productos]
            with open(self.archivo_datos, 'w') as archivo:
                json.dump(datos, archivo, indent=4)
            logging.info("Datos del inventario guardados exitosamente.")
        except Exception as e:
            logging.error(f"Error al guardar datos del inventario: {e}")
    
    def obtener_categorias(self):
        return self.categorias
    
    def obtener_todos_productos(self):
        return self.productos
    
    def obtener_producto_por_sku(self, sku):
        for producto in self.productos:
            if producto.sku.lower() == sku.lower():
                return producto
        return None
    
    def agregar_producto(self, sku, nombre, descripcion, cantidad, precio, categoria):
        if self.obtener_producto_por_sku(sku):
            mensaje = f"Error: Ya existe un producto con SKU '{sku}'."
            logging.warning(mensaje)
            return mensaje
        
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower() and producto.categoria == categoria:
                mensaje = f"Error: Ya existe un producto '{nombre}' en la categoría '{categoria}'."
                logging.warning(mensaje)
                return mensaje
        
        es_valido, mensaje_error = validar_producto(sku, nombre, descripcion, cantidad, precio, categoria)
        if not es_valido:
            mensaje = f"Error: {mensaje_error}"
            logging.warning(mensaje)
            return mensaje
        
        nuevo_producto = Producto(sku, nombre, descripcion, cantidad, precio, categoria)
        self.productos.append(nuevo_producto)
        self.guardar_datos()
        mensaje = f"Producto '{nombre}' agregado exitosamente."
        logging.info(mensaje)
        return mensaje
    
    def actualizar_producto(self, sku, nombre, descripcion, cantidad, precio, categoria):
        producto = self.obtener_producto_por_sku(sku)
        if not producto:
            mensaje = f"Error: No se encontró ningún producto con SKU '{sku}'."
            logging.warning(mensaje)
            return mensaje
        
        for p in self.productos:
            if p.sku != sku and p.nombre.lower() == nombre.lower() and p.categoria == categoria:
                mensaje = f"Error: Ya existe otro producto con nombre '{nombre}' en la categoría '{categoria}'."
                logging.warning(mensaje)
                return mensaje
        
        es_valido, mensaje_error = validar_producto(sku, nombre, descripcion, cantidad, precio, categoria)
        if not es_valido:
            mensaje = f"Error: {mensaje_error}"
            logging.warning(mensaje)
            return mensaje
        
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.cantidad = cantidad
        producto.precio = precio
        producto.categoria = categoria
        self.guardar_datos()
        mensaje = f"Producto '{nombre}' actualizado exitosamente."
        logging.info(mensaje)
        return mensaje
    
    def eliminar_producto(self, sku):
        producto = self.obtener_producto_por_sku(sku)
        if not producto:
            mensaje = f"Error: No se encontró ningún producto con SKU '{sku}'."
            logging.warning(mensaje)
            return mensaje
        
        self.productos = [p for p in self.productos if p.sku.lower() != sku.lower()]
        self.guardar_datos()
        mensaje = f"Producto '{producto.nombre}' eliminado exitosamente."
        logging.info(mensaje)
        return mensaje
    
    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]
    
    def buscar_por_categoria(self, categoria):
        return [p for p in self.productos if p.categoria == categoria]
    
    def buscar_por_precio(self, precio_maximo):
        return [p for p in self.productos if p.precio <= precio_maximo]
