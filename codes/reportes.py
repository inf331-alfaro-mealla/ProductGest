"""
Módulo de Reportes
Genera reportes para el sistema de gestión de inventario.
"""

import logging

def generar_reportes(inventario):
    """
    Genera y muestra reportes de inventario.

    Args:
        inventario (GestorInventario): La instancia del gestor de inventario
    """
    try:
        productos = inventario.obtener_todos_productos()

        total_productos = len(productos)
        valor_total = sum(p.cantidad * p.precio for p in productos)

        productos_disponibles = [p for p in productos if p.cantidad > 0]
        agotados = [p for p in productos if p.cantidad == 0]

        print("\n===== REPORTE RESUMEN DE INVENTARIO =====")
        print(f"Total de Productos: {total_productos}")
        print(f"Valor Total del Inventario: ${valor_total:.2f}")
        print(f"Productos Disponibles: {len(productos_disponibles)}")
        print(f"Productos Agotados: {len(agotados)}")

        if agotados:
            print("\n===== PRODUCTOS AGOTADOS =====")
            for producto in agotados:
                print(f"- {producto.nombre} (SKU: {producto.sku})")

        print("\n===== PRODUCTOS POR CATEGORÍA =====")
        categorias = inventario.obtener_categorias()
        for categoria in categorias:
            productos_categoria = [p for p in productos if p.categoria == categoria]
            if productos_categoria:
                valor_categoria = sum(p.cantidad * p.precio for p in productos_categoria)
                print(f"\n{categoria}: {len(productos_categoria)} productos")
                print(f"Valor de Categoría: ${valor_categoria:.2f}")

        if productos:
            print("\n===== TOP 5 PRODUCTOS MÁS VALIOSOS =====")
            ordenados_por_valor = sorted(productos, key=lambda p: p.cantidad * p.precio, reverse=True)
            for i, producto in enumerate(ordenados_por_valor[:5], 1):
                valor = producto.cantidad * producto.precio
                print(f"{i}. {producto.nombre} - ${valor:.2f} (${producto.precio:.2f} × {producto.cantidad})")

        logging.info("Reporte de inventario generado correctamente.")
    except Exception as e:
        logging.error(f"Error al generar reporte de inventario: {e}")
        print("Ocurrió un error al generar el reporte.")
