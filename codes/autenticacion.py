"""
Módulo de Autenticación
Maneja la autenticación de usuarios para el sistema de gestión de inventario.
"""
import getpass

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
            return True
        else:
            intentos += 1
            restantes = max_intentos - intentos
            if restantes > 0:
                print(f"Credenciales inválidas. {restantes} intentos restantes.")
            else:
                print("Número máximo de intentos de inicio de sesión excedido.")
                return False
    
    return False

