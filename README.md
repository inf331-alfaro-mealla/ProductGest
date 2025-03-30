# ProductGest

## Descripción

ProductGest es una aplicación sencilla para la gestión de inventarios, diseñada para ayudar a los emprendedores a administrar eficientemente los productos en sus bodegas. Permite realizar acciones básicas de CRUD (Crear, Leer, Actualizar y Eliminar) de productos, gestionar el stock, generar reportes de inventario, y asegurar el acceso mediante un sistema de autenticación.

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/productgest.git
   ```
2. Navega al directorio del proyecto:
   ```
   cd productgest
   ```
3. Instala las dependencias requeridas (Python o Java, según el caso). Para Python, usa:
   ```
   pip install -r requirements.txt
   ```

## Cómo usar

1. Inicia la aplicación:
   - Para Python:
     ```
     python main.py
     ```
2. Inicia sesión utilizando tu nombre de usuario (admin) y contraseña (admin123) registrados.
3. Accede al panel de control para gestionar productos, buscar, filtrar, y generar reportes de inventario.

## Cómo contribuir

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request en el repositorio principal.

## Requisitos

- Python 3.9 o superior
- No se requieren librerías externas adicionales. El sistema funciona con módulos estándar de Python.

## Validación y Verificación

### 1. ¿Cómo especificamos mejor el requerimiento? (Validación)

Desde el enfoque de **validación**, buscamos asegurar que el sistema responde realmente a las necesidades del cliente: un emprendedor que desea una solución **sencilla, funcional y práctica** para gestionar el inventario de su bodega.

Para lograrlo:

- **Levantamos dudas y ambigüedades** del enunciado original.
- **Registramos acuerdos explícitos** en una tabla de validación (archivo Excel).
- **Tomamos decisiones de diseño simples y consistentes** con las respuestas del profesor y los objetivos del proyecto.

#### Requerimiento Validado

- **Interfaz:** Sistema de consola, sin interfaz gráfica ni acceso web.
- **Autenticación:** Solo login con un usuario administrador preconfigurado. No se implementa registro ni roles diferenciados.
- **CRUD de Productos:** Cada producto tiene `SKU`, `nombre`, `descripción`, `cantidad`, `precio` y `categoría`. El `SKU` es único, y no se permiten duplicados por nombre en la misma categoría.
- **Categorías:** Son predefinidas por el sistema y no se pueden modificar dinámicamente.
- **Stock:** No se pueden registrar productos con stock 0. El stock se actualiza únicamente desde el CRUD.
- **Filtrado y Búsqueda:** Solo se permite búsqueda simple por `nombre`, `categoría` y `precio máximo`.
- **Reportes:** Generados bajo demanda desde un menú. Se muestran por consola e incluyen: total de productos, valor total del inventario, productos agotados, productos por categoría y los 5 más valiosos.
- **Validación de datos:** Se validan todos los campos antes de guardar. No se permiten campos vacíos, precios negativos ni cantidades inválidas.

Esta validación nos permitió **acotar correctamente el alcance**, definir reglas de negocio claras, y asegurar que la aplicación cumpla su propósito sin funcionalidades innecesarias o mal definidas.

---

### 2. ¿Cómo nos aseguramos de que el programa cumple el requerimiento? (Verificación)

Desde el enfoque de **verificación**, nos centramos en comprobar que el sistema se desarrolló tal como lo especificamos durante la validación. Es decir, que cada funcionalidad cumple con lo definido y que el comportamiento del programa es el esperado ante distintos escenarios.

#### Estrategias de Verificación Aplicadas

**a) Diseño alineado con los acuerdos**  
Estructuramos el sistema de forma modular y clara, según los acuerdos tomados como equipo. Cada funcionalidad (autenticación, CRUD, reportes, búsquedas) está contenida en un módulo propio, lo que facilita su verificación por separado.

**b) Validaciones estrictas en código**  
El sistema valida cada dato ingresado antes de ser guardado:

- No se permiten campos vacíos ni datos con formato incorrecto.
- El `SKU` debe ser único y seguir un formato alfanumérico.
- El precio y la cantidad deben ser positivos.

**c) Manejo de errores y logs**  
Usamos `try-except` para manejar excepciones en tiempo de ejecución y evitar caídas del programa.  
Todos los eventos importantes se registran en el archivo `registro.log`, con distintos niveles (`INFO`, `WARNING`, `ERROR`), lo que permite realizar trazabilidad en caso de fallos.

**d) Pruebas funcionales en consola**  
Verificamos manualmente cada funcionalidad usando distintos tipos de entradas, tanto válidas como inválidas. Entre los casos probados se incluyen:

- Inicio de sesión con credenciales correctas e incorrectas.
- Intentos de agregar productos duplicados o con datos inválidos.
- Actualización, eliminación y visualización de productos.
- Búsquedas simples por nombre, categoría y precio.
- Generación de reportes en diferentes escenarios.

**e) Registro estructurado de pruebas (Ciclo 1)**  
Durante el primer ciclo de pruebas, cada integrante del equipo ejecutó casos de prueba individualmente. A continuación, se resumen algunos de los casos ejecutados por Giovanni Mealla el día **28-03-2025**, entre las 20:00 y las 20:30:

| ID    | Entrada                                          | Resultado esperado                          | Resultado obtenido                               | Éxito/Fallo |
| ----- | ------------------------------------------------ | ------------------------------------------- | ------------------------------------------------ | ----------- |
| TC-01 | Ingreso usuario admin y clave admin123           | Acceso exitoso al sistema                   | Mensaje de bienvenida mostrado, acceso permitido | ✔️ Éxito    |
| TC-02 | Ingresar admin con contraseña incorrecta 3 veces | Bloqueo tras 3 intentos, salida del sistema | Se bloqueó correctamente y se cerró el sistema   | ✔️ Éxito    |
| TC-03 | Intentar agregar producto con SKU ya existente   | Mensaje de error por SKU duplicado          | Error: "ya existe producto con SKU"              | ✔️ Éxito    |
| TC-04 | Agregar producto con cantidad -5                 | Error por cantidad inválida                 | Mensaje: "cantidad debe ser mayor a 0"           | ✔️ Éxito    |
| TC-05 | Seleccionar “Generar Reportes” desde el menú     | Mostrar resumen con total, valor y agotados | Reporte mostrado correctamente en consola        | ✔️ Éxito    |

Todos los casos fueron documentados en el archivo `SimpleTestCaseSuite_S2_2025_rev1.0.xlsx`, según el formato entregado por la asignatura.

**f) Verificación cruzada (Ciclo 2)**  
Una vez finalizado el ciclo individual de pruebas por cada integrante, consolidaremos un set único de pruebas para ejecutarlas de forma cruzada. Esto nos permitirá confirmar que el sistema funciona correctamente también desde la perspectiva del otro miembro del equipo.

**g) Plataforma Greentest.ai**  
Planeamos también cargar los casos de prueba consolidados en [Greentest.ai](https://app.greentest.ai) para obtener retroalimentación adicional, asegurar la trazabilidad de los casos y optar a los puntos adicionales que ofrece la tarea por usar esta plataforma.

## Licencia

ProductGest está licenciado bajo la Apache License, Version 2.0. Para más información, consulta el archivo de [licencia](https://www.apache.org/licenses/LICENSE-2.0).
