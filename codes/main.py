"""
Sistema de Gestión de Inventario - Módulo Principal
Este es el punto de entrada para la aplicación de gestión de inventario.
"""

import os
import logging
from autenticacion import autenticar
from inventario import GestorInventario
from reportes import generar_reportes
from utilidades import limpiar_pantalla

def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE INVENTARIO =====")
    print("1. Agregar Producto")
    print("2. Ver Todos los Productos")
    print("3. Buscar Productos")
    print("4. Actualizar Producto")
    print("5. Eliminar Producto")
    print("6. Generar Reportes")
    print("0. Salir")
    print("=======================================")

def menu_busqueda(inventario):
    limpiar_pantalla()
    print("\n===== BUSCAR PRODUCTOS =====")
    print("1. Buscar por Nombre")
    print("2. Buscar por Categoría")
    print("3. Buscar por Precio")
    print("4. Volver al Menú Principal")
    
    opcion = input("\nIngrese su opción (1-4): ")
    
    if opcion == '1':
        nombre = input("Ingrese el nombre del producto a buscar: ")
        resultados = inventario.buscar_por_nombre(nombre)
        mostrar_productos(resultados)
    elif opcion == '2':
        print("\nCategorías Disponibles:")
        for idx, categoria in enumerate(inventario.obtener_categorias(), 1):
            print(f"{idx}. {categoria}")
        try:
            indice_categoria = int(input("\nSeleccione el número de categoría: ")) - 1
            if 0 <= indice_categoria < len(inventario.obtener_categorias()):
                categoria = inventario.obtener_categorias()[indice_categoria]
                resultados = inventario.buscar_por_categoria(categoria)
                mostrar_productos(resultados)
            else:
                print("Selección de categoría inválida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif opcion == '3':
        try:
            precio = float(input("Ingrese el precio máximo para buscar: "))
            resultados = inventario.buscar_por_precio(precio)
            mostrar_productos(resultados)
        except ValueError:
            print("Por favor, ingrese un precio válido.")
    elif opcion == '4':
        return
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
    
    input("\nPresione Enter para continuar...")

def mostrar_productos(productos):
    if not productos:
        print("\nNo se encontraron productos.")
        return
    
    print("\n" + "=" * 80)
    print(f"{'SKU':<10} {'Nombre':<20} {'Categoría':<15} {'Precio':<10} {'Stock':<10}")
    print("-" * 80)
    for producto in productos:
        print(f"{producto.sku:<10} {producto.nombre[:18]:<20} {producto.categoria:<15} "
              f"${producto.precio:<9.2f} {producto.cantidad:<10}")
    print("=" * 80)
    print(f"Total de Productos: {len(productos)}")

def main():
    inventario = GestorInventario()

    if not autenticar():
        logging.warning("Autenticación fallida.")
        print("Autenticación fallida. Saliendo del programa.")
        return
    else:
        logging.info("Inicio de sesión exitoso.")

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("\nIngrese su opción (0-6): ")

        try:
            if opcion == '1':
                limpiar_pantalla()
                print("\n===== AGREGAR NUEVO PRODUCTO =====")
                sku = input("Ingrese SKU (código único): ")
                nombre = input("Ingrese nombre del producto: ")
                descripcion = input("Ingrese descripción del producto: ")

                try:
                    cantidad = int(input("Ingrese cantidad disponible: "))
                    if cantidad <= 0:
                        raise ValueError("Cantidad debe ser mayor que 0.")
                except ValueError as e:
                    print("Cantidad inválida.")
                    logging.warning(f"Error de cantidad: {e}")
                    input("\nPresione Enter para continuar...")
                    continue

                try:
                    precio = float(input("Ingrese precio unitario: $"))
                    if precio <= 0:
                        raise ValueError("Precio debe ser mayor que 0.")
                except ValueError as e:
                    print("Precio inválido.")
                    logging.warning(f"Error de precio: {e}")
                    input("\nPresione Enter para continuar...")
                    continue

                print("\nSeleccione categoría del producto:")
                categorias = inventario.obtener_categorias()
                for idx, categoria in enumerate(categorias, 1):
                    print(f"{idx}. {categoria}")
                try:
                    indice_categoria = int(input("\nIngrese número de categoría: ")) - 1
                    if 0 <= indice_categoria < len(categorias):
                        categoria = categorias[indice_categoria]
                    else:
                        raise ValueError("Categoría inválida.")
                except ValueError as e:
                    print("Selección de categoría inválida.")
                    logging.warning(f"Selección inválida de categoría: {e}")
                    input("\nPresione Enter para continuar...")
                    continue

                resultado = inventario.agregar_producto(sku, nombre, descripcion, cantidad, precio, categoria)
                print(resultado)
                input("\nPresione Enter para continuar...")

            elif opcion == '2':
                limpiar_pantalla()
                print("\n===== TODOS LOS PRODUCTOS =====")
                productos = inventario.obtener_todos_productos()
                mostrar_productos(productos)
                input("\nPresione Enter para continuar...")

            elif opcion == '3':
                menu_busqueda(inventario)

            elif opcion == '4':
                limpiar_pantalla()
                print("\n===== ACTUALIZAR PRODUCTO =====")
                sku = input("Ingrese SKU del producto a actualizar: ")
                producto = inventario.obtener_producto_por_sku(sku)

                if producto:
                    print(f"\nDetalles actuales del producto '{producto.nombre}':")
                    print(f"SKU: {producto.sku}")
                    print(f"Descripción: {producto.descripcion}")
                    print(f"Categoría: {producto.categoria}")
                    print(f"Cantidad: {producto.cantidad}")
                    print(f"Precio: ${producto.precio:.2f}")

                    nombre = input(f"Nombre [{producto.nombre}]: ") or producto.nombre
                    descripcion = input(f"Descripción [{producto.descripcion}]: ") or producto.descripcion

                    cantidad_input = input(f"Cantidad [{producto.cantidad}]: ")
                    if cantidad_input:
                        try:
                            cantidad = int(cantidad_input)
                            if cantidad <= 0:
                                raise ValueError("Cantidad no válida.")
                        except ValueError as e:
                            print("Cantidad inválida. Manteniendo valor actual.")
                            logging.warning(f"Error al actualizar cantidad: {e}")
                            cantidad = producto.cantidad
                    else:
                        cantidad = producto.cantidad

                    precio_input = input(f"Precio [${producto.precio:.2f}]: ")
                    if precio_input:
                        try:
                            precio = float(precio_input)
                            if precio <= 0:
                                raise ValueError("Precio no válido.")
                        except ValueError as e:
                            print("Precio inválido. Manteniendo valor actual.")
                            logging.warning(f"Error al actualizar precio: {e}")
                            precio = producto.precio
                    else:
                        precio = producto.precio

                    print("\nSeleccione categoría del producto:")
                    categorias = inventario.obtener_categorias()
                    for idx, cat in enumerate(categorias, 1):
                        print(f"{idx}. {cat}")
                    print(f"Actual: {producto.categoria}")
                    categoria_input = input("\nIngrese número de categoría (Enter para mantener actual): ")
                    if categoria_input:
                        try:
                            indice_categoria = int(categoria_input) - 1
                            if 0 <= indice_categoria < len(categorias):
                                categoria = categorias[indice_categoria]
                            else:
                                raise ValueError("Categoría inválida.")
                        except ValueError as e:
                            print("Selección inválida. Manteniendo categoría actual.")
                            logging.warning(f"Error al seleccionar nueva categoría: {e}")
                            categoria = producto.categoria
                    else:
                        categoria = producto.categoria

                    resultado = inventario.actualizar_producto(sku, nombre, descripcion, cantidad, precio, categoria)
                    print(resultado)
                else:
                    mensaje = f"No se encontró ningún producto con SKU: {sku}"
                    print(mensaje)
                    logging.warning(mensaje)

                input("\nPresione Enter para continuar...")

            elif opcion == '5':
                limpiar_pantalla()
                print("\n===== ELIMINAR PRODUCTO =====")
                sku = input("Ingrese SKU del producto a eliminar: ")
                producto = inventario.obtener_producto_por_sku(sku)

                if producto:
                    confirmar = input(f"¿Está seguro que desea eliminar '{producto.nombre}'? (s/n): ")
                    if confirmar.lower() == 's':
                        resultado = inventario.eliminar_producto(sku)
                        print(resultado)
                    else:
                        print("Eliminación cancelada.")
                        logging.info(f"Eliminación cancelada para SKU: {sku}")
                else:
                    mensaje = f"No se encontró ningún producto con SKU: {sku}"
                    print(mensaje)
                    logging.warning(mensaje)

                input("\nPresione Enter para continuar...")

            elif opcion == '6':
                limpiar_pantalla()
                print("\n===== REPORTES DE INVENTARIO =====")
                generar_reportes(inventario)
                logging.info("Reporte de inventario generado.")
                input("\nPresione Enter para continuar...")

            elif opcion == '0':
                print("\nGracias por usar el Sistema de Gestión de Inventario. ¡Adiós!")
                logging.info("El programa se cerró correctamente.")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
                logging.warning(f"Opción inválida ingresada: {opcion}")
                input("\nPresione Enter para continuar...")

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            logging.error(f"Excepción inesperada en el menú principal: {e}")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
