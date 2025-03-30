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

## ✅ Validación y Verificación

### 1. ¿Cómo especificamos mejor el requerimiento? (Validación)

La **validación** consiste en asegurarnos de que el sistema que estamos construyendo **realmente resuelve el problema correcto**. Es decir, que los requisitos que definimos estén alineados con lo que el cliente necesita.

Nos hicimos la siguiente pregunta clave:  
> _¿Estamos resolviendo el problema correcto?_

Para responderla, analizamos cuidadosamente el enunciado de la tarea y levantamos dudas que registramos como **indefiniciones**. A partir de esas preguntas, definimos acuerdos explícitos (en un Excel compartido) sobre cada punto. Esto nos permitió acotar el alcance y **establecer un requerimiento claro, completo y realista**, ajustado al contexto de un emprendedor que necesita una herramienta funcional y simple.

#### 📌 Requerimiento Validado

- **Interfaz:** Solo por consola, sin interfaz web ni móvil.
- **Usuarios:** Acceso exclusivo mediante un usuario administrador preconfigurado (sin registro ni roles).
- **CRUD de Productos:** Cada producto debe tener `SKU` único, `nombre`, `descripción`, `cantidad`, `precio` y `categoría`. No se permiten duplicados por nombre/categoría.
- **Categorías:** Son predefinidas por el sistema.
- **Stock:** Solo puede modificarse desde las operaciones CRUD. No se pueden registrar productos con stock ≤ 0.
- **Búsqueda:** Solo por nombre, categoría y precio máximo. No se permiten filtros avanzados.
- **Reportes:** Bajo demanda, mostrados en consola. Incluyen total de productos, valor total del inventario, productos agotados, y resumen por categoría.

Validamos estos requisitos **contrastando lo que se pedía con la realidad del problema a resolver**, asegurándonos de que el sistema tenga sentido desde el punto de vista del cliente.

---

### 2. ¿Cómo nos aseguramos de que el programa cumple el requerimiento? (Verificación)

La **verificación** se enfoca en comprobar que el sistema se está desarrollando **de acuerdo a lo que se dijo que se iba a hacer**. En otras palabras, contrastamos el código real con los requerimientos especificados.

Nos hicimos esta pregunta clave:  
> _¿Estamos resolviendo correctamente el problema?_

#### 🧪 Estrategias de Verificación Aplicadas

**a) Diseño alineado con los acuerdos**  
Modularizamos el código en archivos separados (`main.py`, `inventario.py`, `autenticacion.py`, etc.) para facilitar el control sobre cada parte del sistema. Esto nos permitió verificar funcionalidad por funcionalidad, sin ambigüedades.

**b) Validaciones estrictas en código**  
- Se verifica que los campos no estén vacíos ni tengan tipos inválidos.
- El `SKU` debe seguir un formato alfanumérico válido y no repetirse.
- El precio y la cantidad deben ser mayores a cero.

**c) Manejo de errores y logs**  
Manejamos errores mediante `try-except`, y usamos `logging` para registrar todos los eventos relevantes. Esto incluye inicios de sesión, intentos fallidos, errores de validación y operaciones exitosas.

**d) Pruebas funcionales en consola**  
Cada funcionalidad fue probada con entradas válidas e inválidas. Verificamos login, CRUD, búsquedas y generación de reportes. Nos aseguramos de que los mensajes de error sean claros y que el programa no se caiga ante entradas incorrectas.

**e) Registro estructurado de pruebas (Ciclo 1)**  
Realizamos un ciclo de pruebas individuales. Aquí un resumen de las pruebas ejecutadas por Giovanni Mealla:

| ID      | Entrada                                              | Resultado esperado                                   | Resultado obtenido                                    | Éxito/Fallo |
|---------|------------------------------------------------------|-----------------------------------------------------|-------------------------------------------------------|-------------|
| TC-01   | Ingreso usuario admin y clave admin123               | Acceso exitoso al sistema                           | Mensaje de bienvenida mostrado, acceso permitido      | ✔️ Éxito    |
| TC-02   | Ingresar admin con contraseña incorrecta 3 veces     | Bloqueo tras 3 intentos, salida del sistema         | Se bloqueó correctamente y se cerró el sistema        | ✔️ Éxito    |
| TC-03   | Intentar agregar producto con SKU ya existente       | Mensaje de error por SKU duplicado                  | Error: "ya existe producto con SKU"                   | ✔️ Éxito    |
| TC-04   | Agregar producto con cantidad -5                     | Error por cantidad inválida                         | Mensaje: "cantidad debe ser mayor a 0"                | ✔️ Éxito    |
| TC-05   | Seleccionar “Generar Reportes” desde el menú         | Mostrar resumen con total, valor y agotados         | Reporte mostrado correctamente en consola             | ✔️ Éxito    |

Las pruebas fueron registradas en el Excel entregado por la asignatura (`SimpleTestCaseSuite_S2_2025_rev1.0.xlsx`), especificando: ID, entrada, resultado esperado, resultado obtenido, éxito/fallo y comentarios.

**f) Verificación cruzada (Ciclo 2)**  
Cuando ambos miembros del equipo tengamos nuestras pruebas individuales listas, realizaremos pruebas cruzadas con un set unificado. Esto nos permitirá confirmar el cumplimiento desde diferentes enfoques.

**g) Validación externa (Greentest.ai)**  
Planeamos registrar nuestras pruebas en [Greentest.ai](https://app.greentest.ai) para obtener retroalimentación automatizada y optar a puntos extra.

---

Este enfoque de **validación + verificación** nos permitió construir un sistema ajustado al problema real y técnicamente correcto, con respaldo en pruebas y trazabilidad de decisiones.

## 🧩 3. Organización del equipo y flujo de trabajo

Desde el inicio del proyecto, organizamos nuestras tareas utilizando un documento colaborativo en Google Docs, donde planificamos día a día las actividades a realizar. Esta planificación comenzó el **domingo 23 de marzo** y se extendió hasta el sábado 29 de marzo, donde registramos tanto los objetivos generales como los acuerdos de equipo.

Para las comunicaciones, usamos **WhatsApp** durante la primera semana, y desde el **30 de marzo** migramos a un canal en **Slack** llamado `#productgest`, el cual fue vinculado con GitHub para recibir notificaciones de commits, pull requests y merges.

### División del trabajo

- **Giovanni Mealla** se encargó de:
  - Implementar la **primera versión funcional** del sistema completo en consola (versión 1.0).
  - Hacer todos los **commits de desarrollo en la rama `main`**.
  - Documentar diariamente los avances y **registrar los objetivos** en el documento de Google Docs.
  - Ejecutar el **ciclo 1 de pruebas** sobre su propia versión funcional.
  - Redactar las secciones de **validación, verificación y pruebas** del `README.md`.

- **Ignacio Alfaro** se encargó de:
  - Crear la **organización en GitHub**, la estructura inicial del repositorio y la rama `develop`.
  - Integrar el repositorio con **Slack**.
  - Trabajar en la edición del `README.md` en paralelo mientras Giovanni desarrollaba.
  - Ejecutar su propio conjunto de **pruebas del ciclo 1** y coordinar la ejecución futura de pruebas cruzadas.
  - Subir avances al repositorio y colaborar en los últimos ajustes del proyecto.

La planificación diaria fue clave para mantenernos coordinados, y al estar organizada por fechas, permitió que ambos pudieran avanzar incluso en horarios distintos. Además, usamos mensajes fijados en Slack para establecer tareas prioritarias y mantener claridad sobre los pendientes diarios.

---

## 🧩 4. Flujo de trabajo y administración del código

### Paradigma de ramas utilizado

Utilizamos un **flujo simple basado en `main` y `develop`**:

- `main`: rama principal donde se integró la **primera versión funcional** del programa, desarrollada por Giovanni.
- `develop`: rama secundaria utilizada para trabajar colaborativamente el `README.md` y registrar evidencias como validación, verificación, pruebas y documentación.

Más adelante, se creó un **pull request** desde `develop` hacia `main` para consolidar toda la documentación y los avances en un solo lugar.

### Protección y buenas prácticas

- Aunque **no se activó protección estricta de ramas** en GitHub, aplicamos buenas prácticas manuales:
  - Toda la fase de documentación se trabajó en `develop`.
  - Se hizo un **pull request con revisión manual** para integrar los cambios a `main`.
  - Los commits se firmaron y acompañaron con mensajes claros.

### Herramientas usadas

- **Slack**: Coordinación diaria y objetivos de trabajo compartidos.
- **Google Docs**: Planificación diaria y evidencia escrita de objetivos.
- **GitHub**: Control de versiones, ramas y documentación del código.
- **GreenTest.ai** *(pendiente)*: Para subir pruebas y obtener puntos adicionales.

Este flujo de trabajo, aunque simple, fue efectivo para la magnitud del proyecto y permitió mantener una trazabilidad clara de cada avance.



## Licencia

ProductGest está licenciado bajo la Apache License, Version 2.0. Para más información, consulta el archivo de [licencia](https://www.apache.org/licenses/LICENSE-2.0).
