# README - Sistema de Gestión de Productos "The Save Point"

## 📋 Descripción del Proyecto

Este proyecto es una solución práctica desarrollada como parte del **Módulo #3: Aprendizaje Basado en Problemas (ABP)**. Se trata de un **Sistema de Gestión de Inventario de Videojuegos** implementado en Python, diseñado para resolver la problemática de control y administración de existencias en una tienda de videojuegos.

---

## 🎯 Problema Identificado

**"The Save Point"** requería una solución de software para:
- ✅ Registrar nuevos productos (videojuegos) con datos completos
- ✅ Modificar información de productos existentes
- ✅ Eliminar productos del inventario de forma segura
- ✅ Visualizar y buscar existencias de forma rápida
- ✅ Implementar un sistema de acceso seguro con credenciales

---

## 💡 Solución Propuesta

Desarrollé un **Sistema de Gestión Modular en Python** que integra:

### Arquitectura del Sistema

```
Sistema de Gestión (main.py)
    ├── Módulo de Autenticación (menu.py - login_sistema)
    ├── Módulo de Captura de Datos (menu.py - capturar_datos)
    ├── Módulo de Modificación (menu.py - modificar_videojuego)
    ├── Módulo de Eliminación (menu.py - eliminar_videojuego)
    ├── Módulo de Visualización (menu.py - menu_visualizacion)
    ├── Módulo de Validaciones (validaciones.py)
    ├── Módulo de Funciones Útiles (funciones_utiles.py)
    └── Módulo de Gestión de Datos (gestion_datos.py)
```

---

## 📁 Estructura de Archivos y Explicación

### 1️⃣ **main.py** - Punto de Entrada Principal

**Propósito**: Orquestar el flujo completo del sistema.

**Funcionalidades implementadas**:
- Solicita autenticación del usuario
- Despliega un menú interactivo
- Maneja operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
- Gestiona excepciones con `KeyboardInterrupt`

```python
# Flujo principal:
# 1. Login
# 2. Si acceso concedido → Mostrar menú
# 3. Procesar opción seleccionada
# 4. Manejo seguro de interrupciones (Ctrl+C)
```

---

### 2️⃣ **menu.py** - Módulo de Interfaz y Lógica

**Propósito**: Implementar todas las funciones de interacción con el usuario.

#### Funciones Clave:

**A) `login_sistema()`**
- Valida credenciales de usuario
- Permite 3 intentos
- Retorna tuple: `(bool, str)` → `(acceso_permitido, nombre_usuario)`
- Maneja `KeyboardInterrupt`

**B) `capturar_datos()`**
- Solicita información completa del videojuego:
  - Título
  - Año
  - Plataforma
  - Editor
  - Formato (Físico/Digital)
  - Género
  - Precio (validado)
  - Stock (validado)
- Crea diccionario del producto
- Agrega a inventario
- Muestra confirmación

**C) `modificar_videojuego(lista)`**
- Busca producto por nombre
- Permite modificar:
  - Precio
  - Stock
- Valida entrada numérica
- Actualiza inventario en tiempo real

**D) `eliminar_videojuego(lista)`**
- Busca producto por nombre
- **Solicita confirmación** antes de eliminar
- Elimina solo si usuario confirma (S/N)
- Muestra mensajes de estado

**E) `menu_visualizacion(lista)`**
- Submenú que integra:
  - Mostrar inventario completo
  - Buscar por nombre
  - Volver al menú principal

**F) Funciones de Visualización**
- `mostrar_inventario()`: Tabla formateada de todos los productos
- `buscar_videojuego()`: Búsqueda por término (insensible a mayúsculas)

---

### 3️⃣ **gestion_datos.py** - Gestión Centralizada de Datos

**Propósito**: Almacenar datos y configuraciones globales.

**Contenido**:
```python
GENEROS = ["Acción", "RPG", "Estrategia", "Deportes", "Puzzle", ...]
USUARIOS_SISTEMA = {"usuario": "contraseña", ...}
videojuegos_inventario = []  # Lista dinámica de productos
```

**Ventaja**: Datos centralizados y fáciles de modificar.

---

### 4️⃣ **validaciones.py** - Módulo de Validación de Datos

**Propósito**: Garantizar integridad de datos numéricos.

**Funciones**:
- `validar_entero(mensaje)`: Valida entrada como número entero
- `validar_float(mensaje)`: Valida entrada como número decimal
- `verificar_credenciales(usuario, clave)`: Valida login

**Implementación**:
- Uso de `try/except ValueError`
- Bucles hasta obtener dato válido
- Mensajes de error al usuario

---

### 5️⃣ **funciones_utiles.py** - Funciones Auxiliares

**Propósito**: Operaciones comunes reutilizables.

**Funciones**:
- `formatear_pesos(valor)`: Convierte números a formato moneda
- `limpiar_pantalla()`: Limpia consola (Windows/Linux compatible)

**Beneficio**: Código DRY (Don't Repeat Yourself)

---

## 🔒 Características de Seguridad Implementadas

| Característica | Implementación |
|---|---|
| **Autenticación** | Login con credenciales y 3 intentos |
| **Confirmación de Eliminación** | Solicitud S/N antes de borrar |
| **Validación de Entrada** | Funciones específicas para tipo de dato |
| **Manejo de Excepciones** | Try/except para KeyboardInterrupt |
| **Datos Centralizados** | Importación de módulo único |

---

## 🛠️ Tecnologías y Conceptos Utilizados

### Conceptos de Programación:
✅ **Modularidad**: Código organizado en módulos separados  
✅ **Funciones**: Reutilización de código  
✅ **Estructuras de Datos**: Listas y diccionarios  
✅ **Manejo de Excepciones**: Try/except  
✅ **Validación de Datos**: Entrada y salida controladas  
✅ **Control de Flujo**: If/elif/else, while loops  
✅ **Importaciones**: Modularidad y referencias cruzadas  

### Mejores Prácticas:
✅ Nombres de variables descriptivos  
✅ Documentación con comentarios  
✅ Separación de responsabilidades  
✅ Interfaz amigable con emojis  
✅ Mensajes de error/éxito claros  

---

## 📊 Flujo de Ejecución

```
INICIO
  ↓
LOGIN (3 intentos)
  ├─ Éxito → MENÚ PRINCIPAL
  │           ├─ Opción 1: CAPTURAR DATOS
  │           ├─ Opción 2: MODIFICAR DATOS
  │           ├─ Opción 3: ELIMINAR (con confirmación)
  │           ├─ Opción 4: VISUALIZAR/BUSCAR
  │           └─ Opción 5: SALIR
  │
  └─ Falso → ACCESO DENEGADO
              ↓
              FIN
```

---

## 📈 Datos Capturados por Producto

Cada videojuego almacena:

```python
{
    "Titulo": str,          # Nombre del juego
    "Genero": str,          # Categoría
    "Precio": float,        # Valor en pesos
    "Stock": int,           # Cantidad disponible
    "Anio": str,            # Año de lanzamiento
    "Plataforma": str,      # PS5, Xbox, PC, etc.
    "Editor": str,          # Desarrollador/Distribuidor
    "Formato": str          # Físico o Digital
}
```

---

## 🎓 Competencias Desarrolladas (ABP)

### Según el Módulo #3:

| Competencia | Demostración en el Proyecto |
|---|---|
| **Pensamiento Crítico** | Análisis del problema → Solución modular |
| **Resolución de Problemas** | Implementación de validaciones y confirmaciones |
| **Programación Estructurada** | Modularidad y reutilización de código |
| **Gestión de Datos** | CRUD completo y validación |
| **Trabajo Colaborativo** | Código limpio y documentado para otros |
| **Comunicación Técnica** | Mensajes claros al usuario |

---

## ✨ Mejoras Implementadas Progresivamente

### Iteración 1: Funcionalidad Básica
- ✅ Captura de datos
- ✅ Visualización simple

### Iteración 2: Validación y Seguridad
- ✅ Sistema de login
- ✅ Validación de entrada numérica
- ✅ Manejo de excepciones

### Iteración 3: Funcionalidad Completa
- ✅ Modificación de productos
- ✅ Eliminación con confirmación
- ✅ Búsqueda avanzada

### Iteración 4: Refinamiento
- ✅ Mejor formato de salida
- ✅ Mensajes descriptivos
- ✅ Manejo de KeyboardInterrupt
- ✅ Interfaz intuitiva

---

## 🚀 Cómo Ejecutar el Sistema

```bash
# 1. Navegar a la carpeta del proyecto
cd "curso python\FUNDAMENTOS DE PROGRAMACIÓN EN PYTHON\Sistema de gestión de productos-The Save Point"

# 2. Ejecutar el programa
python main.py

# 3. Ingresar credenciales (ej: usuario/contraseña)
# 4. Interactuar con el menú
# 5. Presionar Ctrl+C para salir seguramente
```

---

## 📝 Reflexión Final (Perspectiva del Alumno)

Este proyecto me permitió:

1. **Entender la importancia de la modularidad** en proyectos grandes
2. **Aplicar validación de datos** para garantizar integridad
3. **Implementar seguridad básica** con autenticación
4. **Usar estructuras de datos** (listas y diccionarios) efectivamente
5. **Manejar excepciones** de forma profesional
6. **Documentar código** para facilitar mantenimiento
7. **Resolver problemas reales** con programación Python

---

## 📚 Referencias y Recursos Utilizados

- Documentación oficial de Python 3.x
- Conceptos de ABP (Aprendizaje Basado en Problemas)
- Mejores prácticas de programación modular
- Validación y seguridad en entrada de datos

---

## 📌 Conclusión

El **Sistema de Gestión de Productos "The Save Point"** es una solución completa que demuestra la aplicación práctica de conceptos de programación en Python para resolver un problema real. La modularidad, validación y seguridad implementadas garantizan un sistema robusto y mantenible.

---

**Alumna**: Constanza Fernanda Saa Mercado
**Módulo**: #3 - Aprendizaje Basado en Problemas  
**Fecha**: Febrero 2026  
**Versión del Proyecto**: 1.0  
**Estado**: ✅ Completado