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

- [Ir a la planififcacion previa a la integracion de Slack](https://docs.google.com/document/d/1MN-v2jxa6xgaRS1v-h1mIPGq8FWgicJxMVjVdhSfOEg/edit?usp=sharing)

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

- `main`: rama principal donde se integró tanto la **primera versión funcional v1.0** como **la version V1.1 para el ciclo 2 de pruebas cruzadas** del programa, desarrollada por Giovanni.
- `develop`: rama secundaria utilizada para trabajar colaborativamente el `README.md` y registrar evidencias como validación, verificación, pruebas y documentación.

Más adelante, se crearon **pull requests** desde `develop` hacia `main` para consolidar toda la documentación y los avances en un solo lugar.

### Protección y buenas prácticas

- Aunque **no se activó protección estricta de ramas** en GitHub, aplicamos buenas prácticas manuales:
  - La primera fase de documentación se trabajó en `develop`.
  - La ultima fase (despues de terminar ambos ciclo de pruebas) se trabajo en la rama `main`
  - Se hizo un **pull request con revisión manual** para integrar los cambios a `main`.
  - Los commits se firmaron y acompañaron con mensajes claros.

### Herramientas usadas

- **Slack**: Coordinación diaria y objetivos de trabajo compartidos.
- **Google Docs**: Planificación diaria y evidencia escrita de objetivos.
- **GitHub**: Control de versiones, ramas y documentación del código.
- **GreenTest.ai** *(pendiente)*: Para subir pruebas y obtener puntos adicionales.

Este flujo de trabajo, aunque simple, fue efectivo para la magnitud del proyecto y permitió mantener una trazabilidad clara de cada avance.

---

### 🧩 5. Capturas

### GitHub y Slack

A continuación, dejamos evidencia visual del trabajo realizado a lo largo del proyecto, incluyendo commits, pull requests, merges y planificación diaria en Slack.

- [Ver imagen de actividad de commits](./evidencias/commits.png)
- [Ver imagen del Pull Request de integración a main](./evidencias/pull-request.png)
- [Ver imagen del Merge exitoso](./evidencias/merge.png)
- [Ver imagen del canal Slack con organización diaria](./evidencias/slack.png)
- [Ver imagen de pruebas ciclo 1 Giovanni Mealla](./evidencias/ciclo1giovanni.png)
- [Ver imagen de pruebas ciclo 1 Ignacio Alfaro](./evidencias/ciclo1ignacio.png)
- [Ver imagen de la planificacion previa al slack en google docs](./evidencias/google-doc-plan.png)

### Pruebas cruzadas (Ciclo 2)

Ambos integrantes del equipo ejecutaron el conjunto de pruebas diseñadas por su compañero, con el objetivo de verificar el sistema desde otra perspectiva.

- Giovanni ejecutó las pruebas creadas por Ignacio (TC-06 a TC-17 del ciclo 1).
- Ignacio ejecutó las pruebas creadas por Giovanni (TS-01 a TS-05 del ciclo 1).

Los resultados fueron documentados en el Excel consolidado (`nombre_archivo_excel`), disponible en la carpeta `/tests`.

#### 📁 Evidencia visual de pruebas cruzadas (Giovanni ejecutando pruebas TS)

Todas las capturas de las pruebas realizadas por Giovanni en el ciclo 2 se encuentran en la carpeta `/evidencias/prueba-cruzada-de-giovanni-C2/`:

| ID de prueba | Enlace a evidencia |
|--------------|--------------------|
| TS-01 | [TS-01.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-01.png) |
| TS-02 | [TS-02.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-02.png) |
| TS-03 | [TS-03.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-03.png) |
| TS-04 | [TS-04.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-04.png) |
| TS-05 | [TS-05.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-05.png) |
| TS-06 | [TS-06.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-06.png) |
| TS-07 | [TS-07.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-07.png) |
| TS-08 | [TS-08.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-08.png) |
| TS-09 | [TS-09.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-09.png) |
| TS-10 | [TS-10.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-10.png) |
| TS-11 | [TS-11.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-11.png) |
| TS-12 | [TS-12.png](./evidencias/prueba-cruzada-de-giovanni-C2/TS-12.png) |

---

### 🧩 6. Problemas encontrados y cómo se solucionaron

Durante el desarrollo del proyecto, enfrentamos los siguientes desafíos:

- **Integración con Slack:** Al principio no podíamos integrar Slack con GitHub usando nuestras cuentas @usm.cl. La solución fue crear una organización en Slack utilizando una cuenta @sansano.usm.cl, lo que nos permitió finalmente realizar la integración sin problemas.

- **Disponibilidad de tiempo desigual:** Al tener diferencias en la disponibilidad horaria de cada integrante, se llegó a un acuerdo para que Giovanni se encargara del desarrollo inicial completo del sistema (y las pruebas del Ciclo 1), mientras Ignacio se encargó de la integración con GitHub, creación de ramas, documentación y la ejecución de su propio ciclo de pruebas. Mantuvimos comunicación constante para evitar trabajar sobre lo mismo.

- **Problemas menores con validaciones:** En una primera versión del sistema, al intentar agregar productos con cantidad negativa o SKU repetido, el sistema no respondía como se esperaba. Se añadieron validaciones estrictas y mensajes de error claros para reforzar la robustez del sistema.

- **Errores en el manejo de logs:** En algunos módulos no se registraban correctamente los eventos. Se solucionó asegurando el uso uniforme del módulo `logging` en todos los archivos del sistema (`main.py`, `inventario.py`, etc.).

---


## Licencia

ProductGest está licenciado bajo la Apache License, Version 2.0. Para más información, consulta el archivo de [licencia](https://www.apache.org/licenses/LICENSE-2.0).
