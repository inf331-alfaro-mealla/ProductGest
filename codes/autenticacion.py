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

        if nombre_usuario == NOMBRE_ADMIN and contraseña == CONTRASEÑA_ADMIN:
            print("\n¡Inicio de sesión exitoso! Bienvenido al Sistema de Gestión de Inventario.")
            logging.info("Inicio de sesión exitoso.")
            return True
        else:
            intentos += 1
            restantes = max_intentos - intentos
            if restantes > 0:
                print(f"Credenciales inválidas. {restantes} intentos restantes.")
                logging.warning(f"Intento de autenticación fallido. Intentos restantes: {restantes}")
            else:
                print("Número máximo de intentos de inicio de sesión excedido.")
                logging.error("Autenticación fallida: se excedió el número máximo de intentos.")
                return False

    return False
