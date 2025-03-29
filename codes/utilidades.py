"""
Módulo de Utilidades
Funciones de utilidad para el sistema de gestión de inventario.
"""

import os
import re
import logging

# Configuración global de logging
logging.basicConfig(
    filename='registro.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def es_sku_valido(sku):
    """
    Valida el formato de SKU (alfanumérico, sin espacios).

    Args:
        sku (str): El SKU a validar

    Returns:
        bool: True si es válido, False en caso contrario
    """
    patron = r'^[a-zA-Z0-9-]+$'
    return bool(re.match(patron, sku))

def formatear_moneda(cantidad):
    """
    Formatea un número como moneda.

    Args:
        cantidad (float): La cantidad a formatear

    Returns:
        str: Cadena de moneda formateada
    """
    return f"${cantidad:.2f}"

def truncar_cadena(texto, longitud_maxima=30):
    """
    Trunca una cadena a una longitud máxima y agrega puntos suspensivos.

    Args:
        texto (str): El texto a truncar
        longitud_maxima (int): Longitud máxima

    Returns:
        str: Cadena truncada
    """
    if len(texto) <= longitud_maxima:
        return texto
    return texto[:longitud_maxima - 3] + "..."
