"""
Módulo de Autenticación
Maneja la autenticación de usuarios para el sistema de gestión de inventario.
"""

import getpass
import logging

# Credenciales de administrador preconfiguradas
NOMBRE_ADMIN = "admin"
CONTRASEÑA_ADMIN = "admin123"

def autenticar():
    """
    Autentica al usuario con nombre de usuario y contraseña.
    Retorna True si la autenticación es exitosa, False en caso contrario.
    """
    print("\n===== INICIAR SESIÓN =====")
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        nombre_usuario = input("Usuario: ")
        contraseña = getpass.getpass("Contraseña: ")

        # Verificación de campos vacíos
        if not nombre_usuario.strip() or not contraseña.strip():
            print("❌ Todos los campos son obligatorios. No pueden estar vacíos.")
            logging.warning("Intento con campos vacíos.")
            intentos += 1
            continue

        if nombre_usuario != NOMBRE_ADMIN:
            print("❌ Usuario incorrecto.")
            logging.warning(f"Intento con nombre de usuario inválido: '{nombre_usuario}'")
            intentos += 1
            continue

        if contraseña != CONTRASEÑA_ADMIN:
            print("❌ Contraseña incorrecta.")
            logging.warning("Contraseña incorrecta para el usuario admin.")
            intentos += 1
            continue

        print("\n✅ ¡Inicio de sesión exitoso! Bienvenido al Sistema de Gestión de Inventario.")
        logging.info("Inicio de sesión exitoso.")
        return True

    print("\n🚫 Número máximo de intentos de inicio de sesión excedido.")
    logging.error("Autenticación fallida: se excedió el número máximo de intentos.")
    return False